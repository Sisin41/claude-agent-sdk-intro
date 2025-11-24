/**
 * GEO-002: Analyze Citations Tool
 *
 * Performs LLM-powered parallel analysis of citations from multi-engine test results
 * to determine sentiment, relevance, and competitive positioning.
 */

import { z } from 'zod';
import pLimit from 'p-limit';
import { BaseToolOutput, TestResult, ErrorDetail } from '../shared/types';
import { ValidationError, APIError } from '../../utils/errors';
import { logger, logToolStart, logToolSuccess, logToolError } from '../../utils/logger';

// ============================================================================
// Input/Output Type Definitions
// ============================================================================

/**
 * Analysis depth options
 */
export type AnalysisDepth = 'LIGHT' | 'DEEP';

/**
 * Input schema for citation analysis
 */
export const AnalyzeCitationsInputSchema = z.object({
  test_results: z.array(
    z.object({
      prompt_id: z.string(),
      engine: z.enum(['chatgpt', 'perplexity', 'gemini']),
      response: z.string(),
      citations: z.array(z.any()),
      brand_mentioned: z.boolean(),
      brand_mentions: z.array(z.any()),
    })
  ).min(1, 'At least one test result is required'),

  target_brand: z.string().min(1, 'Target brand name is required'),

  competitors: z.array(z.string()).optional().default([]),

  analysis_depth: z.enum(['LIGHT', 'DEEP']).default('LIGHT'),

  max_concurrent: z.number().int().min(1).max(50).default(20),

  include_sentiment: z.boolean().default(true),

  include_relevance_score: z.boolean().default(true),
});

export type AnalyzeCitationsInput = z.infer<typeof AnalyzeCitationsInputSchema>;

/**
 * Citation analysis result
 */
export interface CitationAnalysis {
  prompt_id: string;
  engine: string;
  brand_mentioned: boolean;
  brand_position?: number; // Position in response (1-indexed)
  sentiment?: 'positive' | 'neutral' | 'negative';
  sentiment_score?: number; // -1 to 1
  relevance_score?: number; // 0 to 1
  key_themes: string[];
  competitors_mentioned: string[];
  competitive_positioning?: string; // How brand is positioned vs competitors
  citation_quality: 'high' | 'medium' | 'low';
  recommendations: string[];
}

/**
 * Aggregated insights
 */
export interface AggregatedInsights {
  overall_sentiment: 'positive' | 'neutral' | 'negative';
  avg_sentiment_score: number;
  avg_relevance_score: number;
  brand_mention_rate: number; // Percentage
  avg_brand_position?: number; // Average position when mentioned
  top_themes: Array<{ theme: string; frequency: number }>;
  competitive_landscape: Record<string, {
    mention_count: number;
    co_mention_with_brand: number;
    positioning: string;
  }>;
  recommendations: string[];
}

/**
 * Output data structure
 */
export interface AnalyzeCitationsData {
  analyses: CitationAnalysis[];
  insights: AggregatedInsights;
  total_responses: number;
  brand_mentions: number;
  avg_citations_per_response: number;
}

/**
 * Complete output type
 */
export type AnalyzeCitationsOutput = BaseToolOutput<AnalyzeCitationsData>;

// ============================================================================
// Helper Functions
// ============================================================================

/**
 * Mock LLM call for citation analysis
 * In production, this would call Claude Haiku or similar
 */
async function analyzeSingleCitation(
  result: TestResult,
  targetBrand: string,
  competitors: string[],
  depth: AnalysisDepth,
  includeSentiment: boolean,
  includeRelevance: boolean
): Promise<CitationAnalysis> {
  // Simulate LLM API call
  await new Promise((resolve) => setTimeout(resolve, 200 + Math.random() * 300));

  // Mock analysis (in production, use actual LLM)
  const brandMentioned = result.brand_mentioned;
  const brandPosition = result.brand_position;

  // Simplified sentiment analysis
  let sentiment: 'positive' | 'neutral' | 'negative' = 'neutral';
  let sentimentScore = 0;

  if (includeSentiment && brandMentioned) {
    const lowerResponse = result.response.toLowerCase();
    const positiveWords = ['best', 'excellent', 'great', 'leading', 'top'];
    const negativeWords = ['poor', 'bad', 'worst', 'lacking', 'limited'];

    const positiveCount = positiveWords.filter((w) => lowerResponse.includes(w)).length;
    const negativeCount = negativeWords.filter((w) => lowerResponse.includes(w)).length;

    if (positiveCount > negativeCount) {
      sentiment = 'positive';
      sentimentScore = 0.5 + Math.random() * 0.5; // 0.5 to 1.0
    } else if (negativeCount > positiveCount) {
      sentiment = 'negative';
      sentimentScore = -0.5 - Math.random() * 0.5; // -1.0 to -0.5
    } else {
      sentiment = 'neutral';
      sentimentScore = -0.2 + Math.random() * 0.4; // -0.2 to 0.2
    }
  }

  // Simplified relevance scoring
  const relevanceScore = includeRelevance
    ? 0.5 + Math.random() * 0.5 // Mock: 0.5 to 1.0
    : undefined;

  // Extract key themes (simplified)
  const themes = ['analytics', 'marketing', 'data', 'insights', 'automation'];
  const keyThemes = themes.filter(() => Math.random() > 0.6); // Randomly select themes

  // Check for competitor mentions
  const competitorsMentioned = competitors.filter((comp) =>
    result.response.toLowerCase().includes(comp.toLowerCase())
  );

  // Citation quality (mock)
  const citationQuality: 'high' | 'medium' | 'low' =
    result.citations.length >= 3 ? 'high' : result.citations.length >= 1 ? 'medium' : 'low';

  // Competitive positioning (if competitors mentioned)
  let competitivePositioning: string | undefined;
  if (competitorsMentioned.length > 0 && brandMentioned) {
    const positionings = [
      `${targetBrand} positioned as premium alternative to ${competitorsMentioned[0]}`,
      `${targetBrand} and ${competitorsMentioned[0]} mentioned as comparable solutions`,
      `${targetBrand} differentiated by ease of use compared to ${competitorsMentioned[0]}`,
    ];
    competitivePositioning = positionings[Math.floor(Math.random() * positionings.length)];
  }

  // Generate recommendations based on analysis
  const recommendations: string[] = [];

  if (!brandMentioned) {
    recommendations.push(
      `Optimize content to rank for "${result.prompt_id}" query type`
    );
  }

  if (sentiment === 'negative') {
    recommendations.push('Address negative sentiment in user-generated content');
  }

  if (citationQuality === 'low') {
    recommendations.push('Increase authoritative source citations mentioning the brand');
  }

  if (competitorsMentioned.length > 0 && !brandMentioned) {
    recommendations.push(
      `Competitor ${competitorsMentioned[0]} mentioned but not ${targetBrand} - create comparison content`
    );
  }

  return {
    prompt_id: result.prompt_id,
    engine: result.engine,
    brand_mentioned: brandMentioned,
    brand_position: brandPosition,
    sentiment: includeSentiment ? sentiment : undefined,
    sentiment_score: includeSentiment ? sentimentScore : undefined,
    relevance_score: relevanceScore,
    key_themes: keyThemes,
    competitors_mentioned: competitorsMentioned,
    competitive_positioning: competitivePositioning,
    citation_quality: citationQuality,
    recommendations,
  };
}

/**
 * Aggregate insights from all analyses
 */
function aggregateInsights(
  analyses: CitationAnalysis[],
  targetBrand: string,
  competitors: string[]
): AggregatedInsights {
  const totalAnalyses = analyses.length;

  // Overall sentiment
  const sentiments = analyses
    .filter((a) => a.sentiment)
    .map((a) => a.sentiment as 'positive' | 'neutral' | 'negative');

  const sentimentCounts = {
    positive: sentiments.filter((s) => s === 'positive').length,
    neutral: sentiments.filter((s) => s === 'neutral').length,
    negative: sentiments.filter((s) => s === 'negative').length,
  };

  const overallSentiment =
    sentimentCounts.positive > sentimentCounts.neutral &&
    sentimentCounts.positive > sentimentCounts.negative
      ? 'positive'
      : sentimentCounts.negative > sentimentCounts.neutral &&
        sentimentCounts.negative > sentimentCounts.positive
      ? 'negative'
      : 'neutral';

  // Average scores
  const avgSentimentScore =
    analyses.filter((a) => a.sentiment_score).reduce((sum, a) => sum + (a.sentiment_score || 0), 0) /
      analyses.filter((a) => a.sentiment_score).length || 0;

  const avgRelevanceScore =
    analyses.filter((a) => a.relevance_score).reduce((sum, a) => sum + (a.relevance_score || 0), 0) /
      analyses.filter((a) => a.relevance_score).length || 0;

  // Brand mention rate
  const brandMentions = analyses.filter((a) => a.brand_mentioned).length;
  const brandMentionRate = (brandMentions / totalAnalyses) * 100;

  // Average brand position (when mentioned)
  const positions = analyses.filter((a) => a.brand_position).map((a) => a.brand_position!);
  const avgBrandPosition = positions.length > 0
    ? positions.reduce((sum, p) => sum + p, 0) / positions.length
    : undefined;

  // Top themes
  const themeFrequency: Record<string, number> = {};
  analyses.forEach((a) => {
    a.key_themes.forEach((theme) => {
      themeFrequency[theme] = (themeFrequency[theme] || 0) + 1;
    });
  });

  const topThemes = Object.entries(themeFrequency)
    .map(([theme, frequency]) => ({ theme, frequency }))
    .sort((a, b) => b.frequency - a.frequency)
    .slice(0, 10);

  // Competitive landscape
  const competitiveLandscape: Record<string, {
    mention_count: number;
    co_mention_with_brand: number;
    positioning: string;
  }> = {};

  competitors.forEach((competitor) => {
    const mentionCount = analyses.filter((a) =>
      a.competitors_mentioned.includes(competitor)
    ).length;

    const coMentionCount = analyses.filter(
      (a) => a.brand_mentioned && a.competitors_mentioned.includes(competitor)
    ).length;

    const positionings = analyses
      .filter((a) => a.competitive_positioning)
      .map((a) => a.competitive_positioning!)
      .filter((p) => p.includes(competitor));

    const positioning = positionings.length > 0
      ? positionings[0]
      : `${competitor} mentioned ${mentionCount} times`;

    competitiveLandscape[competitor] = {
      mention_count: mentionCount,
      co_mention_with_brand: coMentionCount,
      positioning,
    };
  });

  // Aggregate recommendations
  const allRecommendations = analyses.flatMap((a) => a.recommendations);
  const recommendationFrequency: Record<string, number> = {};

  allRecommendations.forEach((rec) => {
    recommendationFrequency[rec] = (recommendationFrequency[rec] || 0) + 1;
  });

  const recommendations = Object.entries(recommendationFrequency)
    .sort((a, b) => b[1] - a[1])
    .slice(0, 10)
    .map(([rec]) => rec);

  return {
    overall_sentiment: overallSentiment,
    avg_sentiment_score: avgSentimentScore,
    avg_relevance_score: avgRelevanceScore,
    brand_mention_rate: brandMentionRate,
    avg_brand_position: avgBrandPosition,
    top_themes: topThemes,
    competitive_landscape: competitiveLandscape,
    recommendations,
  };
}

// ============================================================================
// Main Tool Function
// ============================================================================

/**
 * Analyze citations from multi-engine test results
 *
 * @param input - Analysis configuration
 * @returns Citation analysis with insights and recommendations
 *
 * @example
 * ```typescript
 * const analysis = await analyzeCitations({
 *   test_results: multiEngineTestResults.data.results,
 *   target_brand: 'Acme Corp',
 *   competitors: ['Competitor A', 'Competitor B'],
 *   analysis_depth: 'DEEP',
 * });
 * ```
 */
export async function analyzeCitations(
  input: AnalyzeCitationsInput
): Promise<AnalyzeCitationsOutput> {
  const startTime = Date.now();

  try {
    // Validate input
    const validatedInput = AnalyzeCitationsInputSchema.parse(input);

    logToolStart('GEO-002', {
      result_count: validatedInput.test_results.length,
      target_brand: validatedInput.target_brand,
      analysis_depth: validatedInput.analysis_depth,
    });

    // Analyze each result with concurrency limit
    const limit = pLimit(validatedInput.max_concurrent);
    const errors: ErrorDetail[] = [];

    const analysisPromises = validatedInput.test_results.map((result) =>
      limit(async (): Promise<CitationAnalysis | null> => {
        try {
          return await analyzeSingleCitation(
            result as TestResult,
            validatedInput.target_brand,
            validatedInput.competitors,
            validatedInput.analysis_depth,
            validatedInput.include_sentiment,
            validatedInput.include_relevance_score
          );
        } catch (error) {
          const err = error as Error;
          errors.push({
            code: 'ANALYSIS_FAILED',
            message: err.message,
            context: {
              prompt_id: result.prompt_id,
              engine: result.engine,
            },
          });
          return null;
        }
      })
    );

    const analysesWithNulls = await Promise.all(analysisPromises);
    const analyses = analysesWithNulls.filter((a): a is CitationAnalysis => a !== null);

    // Aggregate insights
    const insights = aggregateInsights(
      analyses,
      validatedInput.target_brand,
      validatedInput.competitors
    );

    // Calculate metrics
    const totalCitations = validatedInput.test_results.reduce(
      (sum, r) => sum + (r.citations?.length || 0),
      0
    );

    const avgCitations = totalCitations / validatedInput.test_results.length;

    const executionTime = Date.now() - startTime;

    logToolSuccess('GEO-002', executionTime, {
      analyses_completed: analyses.length,
      brand_mention_rate: insights.brand_mention_rate,
    });

    return {
      success: analyses.length > 0,
      data: {
        analyses,
        insights,
        total_responses: validatedInput.test_results.length,
        brand_mentions: insights.brand_mention_rate,
        avg_citations_per_response: avgCitations,
      },
      metadata: {
        execution_time_ms: executionTime,
        api_calls_made: analyses.length, // Each analysis = 1 LLM call
        cached: false,
        tool_version: '1.0.0',
      },
      errors: errors.length > 0 ? errors : undefined,
    };
  } catch (error) {
    const executionTime = Date.now() - startTime;
    logToolError('GEO-002', error as Error);

    if (error instanceof z.ZodError) {
      throw new ValidationError(
        `Input validation failed: ${error.errors.map((e) => e.message).join(', ')}`
      );
    }

    throw error;
  }
}
