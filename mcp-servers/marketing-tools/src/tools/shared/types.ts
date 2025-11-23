/**
 * Shared type definitions used across all MCP tools
 */

/**
 * Standard metadata included in all tool responses
 */
export interface ToolMetadata {
  execution_time_ms: number;
  api_calls_made: number;
  cached: boolean;
  tool_version: string;
}

/**
 * Error detail structure for partial failures
 */
export interface ErrorDetail {
  code: string;
  message: string;
  field?: string;
  context?: Record<string, unknown>;
}

/**
 * Base tool output structure
 */
export interface BaseToolOutput<T> {
  success: boolean;
  data: T;
  metadata: ToolMetadata;
  errors?: ErrorDetail[];
}

/**
 * AI Engine types supported by GEO tools
 */
export type AIEngine = 'chatgpt' | 'perplexity' | 'gemini';

/**
 * Citation extracted from AI engine response
 */
export interface Citation {
  url: string;
  title?: string;
  snippet?: string;
  position: number; // Position in the response (1-indexed)
}

/**
 * Brand mention information
 */
export interface BrandMention {
  brand_name: string;
  context: string; // Surrounding text
  sentiment?: 'positive' | 'neutral' | 'negative';
  position: number; // Position in response (1-indexed)
  mentioned_with?: string[]; // Other brands mentioned nearby
}

/**
 * Test prompt structure
 */
export interface PromptTest {
  prompt_id: string;
  text: string;
  category?: string; // e.g., "awareness", "comparison", "solution"
  user_type?: string; // e.g., "marketer", "decision-maker"
  funnel_stage?: string; // e.g., "awareness", "consideration", "decision"
}

/**
 * Engine configuration for multi-engine tests
 */
export interface EngineConfig {
  engine: AIEngine;
  model?: string; // Optional override for engine model
  parameters?: Record<string, unknown>; // Engine-specific parameters
}

/**
 * Result from a single prompt test on one engine
 */
export interface TestResult {
  prompt_id: string;
  engine: AIEngine;
  response: string;
  citations: Citation[];
  brand_mentioned: boolean;
  brand_mentions: BrandMention[];
  brand_position?: number; // Highest position if mentioned
  latency_ms: number;
  error?: string;
}

/**
 * Cached response structure
 */
export interface CachedResponse {
  data: unknown;
  timestamp: number;
  ttl: number;
}

/**
 * Rate limit bucket information
 */
export interface RateLimitBucket {
  tokens: number;
  last_refill: number;
  capacity: number;
  refill_rate: number; // tokens per second
}
