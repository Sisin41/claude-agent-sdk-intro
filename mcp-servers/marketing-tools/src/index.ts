#!/usr/bin/env node

/**
 * Marketing Tools MCP Server
 *
 * Provides high-performance marketing analysis tools via MCP protocol.
 * Currently includes:
 * - GEO-001: Multi-Engine Testing
 * - GEO-002: Citation Analysis
 */

import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import {
  CallToolRequestSchema,
  ListToolsRequestSchema,
} from '@modelcontextprotocol/sdk/types.js';

import { runMultiEngineTest, MultiEngineTestInputSchema } from './tools/geo/multiEngineTest.js';
import { analyzeCitations, AnalyzeCitationsInputSchema } from './tools/geo/analyzeCitations.js';
import { logger } from './utils/logger.js';

/**
 * MCP Server for Marketing Tools
 */
class MarketingToolsServer {
  private server: Server;

  constructor() {
    this.server = new Server(
      {
        name: 'marketing-tools',
        version: '1.0.0',
      },
      {
        capabilities: {
          tools: {},
        },
      }
    );

    this.setupToolHandlers();
    this.setupErrorHandling();
  }

  private setupToolHandlers() {
    // List available tools
    this.server.setRequestHandler(ListToolsRequestSchema, async () => {
      return {
        tools: [
          {
            name: 'run_multi_engine_test',
            description: 'Execute prompts across multiple AI engines (ChatGPT, Perplexity, Gemini) in parallel to measure brand visibility and extract citations. Supports 50+ concurrent tests with automatic retry logic.',
            inputSchema: {
              type: 'object',
              properties: {
                prompts: {
                  type: 'array',
                  description: 'Array of test prompts to execute',
                  items: {
                    type: 'object',
                    properties: {
                      prompt_id: { type: 'string' },
                      text: { type: 'string' },
                      category: { type: 'string' },
                      user_type: { type: 'string' },
                      funnel_stage: { type: 'string' },
                    },
                    required: ['prompt_id', 'text'],
                  },
                },
                engines: {
                  type: 'array',
                  description: 'AI engines to test against',
                  items: {
                    type: 'string',
                    enum: ['chatgpt', 'perplexity', 'gemini'],
                  },
                },
                max_concurrent: {
                  type: 'number',
                  description: 'Maximum concurrent requests (default: 50)',
                  default: 50,
                },
                retry_failed: {
                  type: 'boolean',
                  description: 'Retry failed requests (default: true)',
                  default: true,
                },
                max_retries: {
                  type: 'number',
                  description: 'Maximum retry attempts (default: 3)',
                  default: 3,
                },
                timeout_ms: {
                  type: 'number',
                  description: 'Timeout per request in milliseconds (default: 10000)',
                  default: 10000,
                },
                target_brand: {
                  type: 'string',
                  description: 'Brand name to track mentions for',
                },
              },
              required: ['prompts', 'engines'],
            },
          },
          {
            name: 'analyze_citations',
            description: 'Analyze citations from multi-engine test results using LLM-powered analysis. Performs sentiment analysis, relevance scoring, competitive positioning, and generates actionable recommendations.',
            inputSchema: {
              type: 'object',
              properties: {
                results: {
                  type: 'array',
                  description: 'Test results from run_multi_engine_test',
                  items: {
                    type: 'object',
                  },
                },
                target_brand: {
                  type: 'string',
                  description: 'Brand name to analyze',
                },
                competitors: {
                  type: 'array',
                  description: 'Competitor brand names',
                  items: { type: 'string' },
                },
                analysis_depth: {
                  type: 'string',
                  description: 'Analysis depth: light or deep',
                  enum: ['light', 'deep'],
                  default: 'light',
                },
                include_sentiment: {
                  type: 'boolean',
                  description: 'Include sentiment analysis (default: true)',
                  default: true,
                },
                include_relevance: {
                  type: 'boolean',
                  description: 'Include relevance scoring (default: true)',
                  default: true,
                },
                max_concurrent: {
                  type: 'number',
                  description: 'Maximum concurrent LLM calls (default: 10)',
                  default: 10,
                },
              },
              required: ['results', 'target_brand'],
            },
          },
        ],
      };
    });

    // Handle tool calls
    this.server.setRequestHandler(CallToolRequestSchema, async (request) => {
      const { name, arguments: args } = request.params;

      try {
        logger.info(`Tool call: ${name}`);

        if (name === 'run_multi_engine_test') {
          const result = await runMultiEngineTest(args);
          return {
            content: [
              {
                type: 'text',
                text: JSON.stringify(result, null, 2),
              },
            ],
          };
        }

        if (name === 'analyze_citations') {
          const result = await analyzeCitations(args);
          return {
            content: [
              {
                type: 'text',
                text: JSON.stringify(result, null, 2),
              },
            ],
          };
        }

        throw new Error(`Unknown tool: ${name}`);
      } catch (error) {
        logger.error(`Tool call failed: ${name}`, { error });
        return {
          content: [
            {
              type: 'text',
              text: JSON.stringify({
                success: false,
                error: error instanceof Error ? error.message : 'Unknown error',
              }),
            },
          ],
          isError: true,
        };
      }
    });
  }

  private setupErrorHandling() {
    this.server.onerror = (error) => {
      logger.error('Server error', { error });
    };

    process.on('SIGINT', async () => {
      logger.info('Shutting down server...');
      await this.server.close();
      process.exit(0);
    });
  }

  async run() {
    const transport = new StdioServerTransport();
    await this.server.connect(transport);
    logger.info('Marketing Tools MCP Server running');
  }
}

// Start server
const server = new MarketingToolsServer();
server.run().catch((error) => {
  logger.error('Failed to start server', { error });
  process.exit(1);
});
