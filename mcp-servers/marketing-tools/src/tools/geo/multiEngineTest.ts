/**
 * GEO-001: Multi-Engine Test Tool
 *
 * Executes test prompts across multiple AI engines (ChatGPT, Perplexity, Gemini)
 * in parallel to analyze brand visibility and citation patterns.
 */

import { z } from 'zod';
import pLimit from 'p-limit';
import {
  BaseToolOutput,
  PromptTest,
  AIEngine,
  TestResult,
  Citation,
  BrandMention,
  ErrorDetail,
} from '../shared/types';
import { ValidationError, TimeoutError, APIError } from '../../utils/errors';
import { logger, logToolStart, logToolSuccess, logToolError } from '../../utils/logger';

// ============================================================================
// Input/Output Type Definitions
// ============================================================================

/**
 * Input schema for multi-engine test
 */
export const MultiEngineTestInputSchema = z.object({
  prompts: z
    .array(
      z.object({
        prompt_id: z.string().min(1),
        text: z.string().min(1).max(500),
        category: z.string().optional(),
        user_type: z.string().optional(),
        funnel_stage: z.string().optional(),
      })
    )
    .min(1, 'At least one prompt is required')
    .max(100, 'Maximum 100 prompts allowed'),

  engines: z
    .array(z.enum(['chatgpt', 'perplexity', 'gemini']))
    .min(1, 'At least one engine is required')
    .max(3, 'Maximum 3 engines allowed'),

  target_brand: z.string().optional(), // Brand name to look for in responses

  max_concurrent: z.number().int().min(1).max(50).default(50),

  retry_failed: z.boolean().default(true),

  max_retries: z.number().int().min(0).max(5).default(3),

  timeout_ms: z.number().int().min(1000).max(30000).default(10000),
});

export type MultiEngineTestInput = z.infer<typeof MultiEngineTestInputSchema>;

/**
 * Output data structure
 */
export interface MultiEngineTestData {
  results: TestResult[];
  summary: {
    total_tests: number;
    successful_tests: number;
    failed_tests: number;
    total_citations: number;
    brand_mention_rate: number; // Percentage of responses mentioning brand
    avg_latency_ms: number;
    by_engine: Record<
      AIEngine,
      {
        total: number;
        successful: number;
        failed: number;
        avg_latency_ms: number;
        brand_mentions: number;
      }
    >;
  };
}

/**
 * Complete output type
 */
export type MultiEngineTestOutput = BaseToolOutput<MultiEngineTestData>;

// ============================================================================
// Helper Functions
// ============================================================================

/**
 * Extract citations from AI response
 * This is a simplified implementation - in production, use more sophisticated parsing
 */
function extractCitations(response: string): Citation[] {
  const citations: Citation[] = [];

  // Simple URL extraction (production would use engine-specific parsing)
  const urlRegex = /https?:\/\/[^\s<>"{}|\\^`\[\]]+/g;
  const matches = response.match(urlRegex);

  if (matches) {
    matches.forEach((url, index) => {
      citations.push({
        url,
        position: index + 1,
        title: undefined,
        snippet: undefined,
      });
    });
  }

  return citations;
}

/**
 * Detect brand mentions in response
 */
function detectBrandMentions(response: string, brandName?: string): BrandMention[] {
  if (!brandName) return [];

  const mentions: BrandMention[] = [];
  const lowerResponse = response.toLowerCase();
  const lowerBrand = brandName.toLowerCase();

  let position = 0;
  let index = lowerResponse.indexOf(lowerBrand, position);

  while (index !== -1) {
    // Extract context (50 chars before and after)
    const start = Math.max(0, index - 50);
    const end = Math.min(response.length, index + brandName.length + 50);
    const context = response.substring(start, end);

    mentions.push({
      brand_name: brandName,
      context,
      position: mentions.length + 1,
    });

    position = index + brandName.length;
    index = lowerResponse.indexOf(lowerBrand, position);
  }

  return mentions;
}

/**
 * Mock API call to AI engine
 * In production, this would call actual APIs
 */
async function callAIEngine(
  engine: AIEngine,
  prompt: string,
  timeoutMs: number
): Promise<{ response: string; latency_ms: number }> {
  const startTime = Date.now();

  // Simulate API call with timeout
  const apiCall = new Promise<{ response: string; latency_ms: number }>((resolve) => {
    const simulatedLatency = 1000 + Math.random() * 2000; // 1-3 seconds

    setTimeout(() => {
      // Mock response
      const response = `Mock response from ${engine} for prompt: "${prompt.substring(0, 50)}..."\n\nThis is a simulated response for testing. In production, this would call the actual ${engine} API.\n\nSources:\n- https://example.com/source1\n- https://example.com/source2`;

      resolve({
        response,
        latency_ms: Date.now() - startTime,
      });
    }, simulatedLatency);
  });

  const timeout = new Promise<never>((_, reject) => {
    setTimeout(() => {
      reject(new TimeoutError(`Request to ${engine} timed out after ${timeoutMs}ms`, timeoutMs));
    }, timeoutMs);
  });

  return Promise.race([apiCall, timeout]);
}

/**
 * Execute single prompt on single engine with retry logic
 */
async function executeSingleTest(
  prompt: PromptTest,
  engine: AIEngine,
  targetBrand: string | undefined,
  timeoutMs: number,
  retryFailed: boolean,
  maxRetries: number
): Promise<TestResult> {
  let lastError: Error | undefined;
  let attempt = 0;

  while (attempt <= maxRetries) {
    try {
      const { response, latency_ms } = await callAIEngine(engine, prompt.text, timeoutMs);

      const citations = extractCitations(response);
      const brandMentions = detectBrandMentions(response, targetBrand);
      const brandMentioned = brandMentions.length > 0;
      const brandPosition = brandMentioned ? brandMentions[0]?.position : undefined;

      return {
        prompt_id: prompt.prompt_id,
        engine,
        response,
        citations,
        brand_mentioned: brandMentioned,
        brand_mentions: brandMentions,
        brand_position: brandPosition,
        latency_ms,
      };
    } catch (error) {
      lastError = error as Error;
      attempt++;

      if (!retryFailed || attempt > maxRetries) {
        break;
      }

      // Exponential backoff
      const backoffMs = Math.min(1000 * Math.pow(2, attempt - 1), 10000);
      await new Promise((resolve) => setTimeout(resolve, backoffMs));

      logger.warn('Retrying failed test', {
        prompt_id: prompt.prompt_id,
        engine,
        attempt,
        max_retries: maxRetries,
      });
    }
  }

  // All retries failed
  throw new APIError(
    `Failed to execute test after ${attempt} attempts: ${lastError?.message}`,
    engine
  );
}

/**
 * Calculate summary statistics
 */
function calculateSummary(
  results: TestResult[],
  errors: ErrorDetail[],
  totalTests: number
): MultiEngineTestData['summary'] {
  const successful = results.length;
  const failed = errors.length;

  const totalCitations = results.reduce((sum, r) => sum + r.citations.length, 0);

  const brandMentions = results.filter((r) => r.brand_mentioned).length;
  const brandMentionRate = successful > 0 ? (brandMentions / successful) * 100 : 0;

  const avgLatency = successful > 0 ? results.reduce((sum, r) => sum + r.latency_ms, 0) / successful : 0;

  // Group by engine
  const byEngine: MultiEngineTestData['summary']['by_engine'] = {} as any;

  const engines = [...new Set(results.map((r) => r.engine))];

  engines.forEach((engine) => {
    const engineResults = results.filter((r) => r.engine === engine);
    const engineBrandMentions = engineResults.filter((r) => r.brand_mentioned).length;

    byEngine[engine] = {
      total: engineResults.length,
      successful: engineResults.length,
      failed: 0, // We don't track failed per engine in this implementation
      avg_latency_ms:
        engineResults.reduce((sum, r) => sum + r.latency_ms, 0) / engineResults.length || 0,
      brand_mentions: engineBrandMentions,
    };
  });

  return {
    total_tests: totalTests,
    successful_tests: successful,
    failed_tests: failed,
    total_citations: totalCitations,
    brand_mention_rate: brandMentionRate,
    avg_latency_ms: avgLatency,
    by_engine: byEngine,
  };
}

// ============================================================================
// Main Tool Function
// ============================================================================

/**
 * Execute prompts across multiple AI engines in parallel
 *
 * @param input - Test configuration
 * @returns Test results with citations and brand mentions
 *
 * @example
 * ```typescript
 * const results = await runMultiEngineTest({
 *   prompts: [
 *     { prompt_id: 'p1', text: 'What are the best marketing analytics tools?' }
 *   ],
 *   engines: ['chatgpt', 'perplexity'],
 *   target_brand: 'Acme Corp',
 * });
 * ```
 */
export async function runMultiEngineTest(
  input: MultiEngineTestInput
): Promise<MultiEngineTestOutput> {
  const startTime = Date.now();

  try {
    // Validate input
    const validatedInput = MultiEngineTestInputSchema.parse(input);

    logToolStart('GEO-001', {
      prompt_count: validatedInput.prompts.length,
      engines: validatedInput.engines,
      max_concurrent: validatedInput.maxConcurrent,
    });

    // Create all test combinations (prompts × engines)
    const allTests: Array<{
      prompt: PromptTest;
      engine: AIEngine;
    }> = [];

    validatedInput.prompts.forEach((prompt) => {
      validatedInput.engines.forEach((engine) => {
        allTests.push({ prompt, engine });
      });
    });

    const totalTests = allTests.length;

    // Execute tests with concurrency limit
    const limit = pLimit(validatedInput.max_concurrent);
    const errors: ErrorDetail[] = [];

    const testPromises = allTests.map(({ prompt, engine }) =>
      limit(async (): Promise<TestResult | null> => {
        try {
          return await executeSingleTest(
            prompt,
            engine,
            validatedInput.target_brand,
            validatedInput.timeout_ms,
            validatedInput.retry_failed,
            validatedInput.max_retries
          );
        } catch (error) {
          const err = error as Error;
          errors.push({
            code: 'EXECUTION_FAILED',
            message: err.message,
            context: {
              prompt_id: prompt.prompt_id,
              engine,
            },
          });
          return null;
        }
      })
    );

    const resultsWithNulls = await Promise.all(testPromises);
    const results = resultsWithNulls.filter((r): r is TestResult => r !== null);

    // Calculate summary
    const summary = calculateSummary(results, errors, totalTests);

    const executionTime = Date.now() - startTime;

    logToolSuccess('GEO-001', executionTime, {
      total_tests: totalTests,
      successful: results.length,
      failed: errors.length,
    });

    return {
      success: results.length > 0,
      data: {
        results,
        summary,
      },
      metadata: {
        execution_time_ms: executionTime,
        api_calls_made: results.length,
        cached: false,
        tool_version: '1.0.0',
      },
      errors: errors.length > 0 ? errors : undefined,
    };
  } catch (error) {
    const executionTime = Date.now() - startTime;
    logToolError('GEO-001', error as Error);

    if (error instanceof z.ZodError) {
      throw new ValidationError(
        `Input validation failed: ${error.errors.map((e) => e.message).join(', ')}`
      );
    }

    throw error;
  }
}
