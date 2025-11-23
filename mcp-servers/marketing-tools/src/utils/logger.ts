/**
 * Structured logging utility
 */

import winston from 'winston';

const logLevel = process.env.LOG_LEVEL || 'info';
const nodeEnv = process.env.NODE_ENV || 'development';

/**
 * Create Winston logger instance
 */
export const logger = winston.createLogger({
  level: logLevel,
  format: winston.format.combine(
    winston.format.timestamp({ format: 'YYYY-MM-DD HH:mm:ss' }),
    winston.format.errors({ stack: true }),
    winston.format.splat(),
    winston.format.json()
  ),
  defaultMeta: {
    service: 'marketing-tools-mcp',
    environment: nodeEnv,
  },
  transports: [
    // Write all logs to combined.log
    new winston.transports.File({ filename: 'logs/combined.log' }),

    // Write errors to error.log
    new winston.transports.File({ filename: 'logs/error.log', level: 'error' }),

    // Also log to console in development
    ...(nodeEnv === 'development'
      ? [
          new winston.transports.Console({
            format: winston.format.combine(
              winston.format.colorize(),
              winston.format.simple()
            ),
          }),
        ]
      : []),
  ],
});

/**
 * Log tool execution start
 */
export function logToolStart(toolId: string, params?: Record<string, unknown>): void {
  logger.info('Tool execution started', {
    tool_id: toolId,
    params,
  });
}

/**
 * Log tool execution success
 */
export function logToolSuccess(
  toolId: string,
  durationMs: number,
  metadata?: Record<string, unknown>
): void {
  logger.info('Tool execution completed', {
    tool_id: toolId,
    duration_ms: durationMs,
    ...metadata,
  });
}

/**
 * Log tool execution error
 */
export function logToolError(
  toolId: string,
  error: Error,
  context?: Record<string, unknown>
): void {
  logger.error('Tool execution failed', {
    tool_id: toolId,
    error: error.message,
    error_name: error.name,
    stack: error.stack,
    ...context,
  });
}

/**
 * Log API call
 */
export function logAPICall(
  provider: string,
  endpoint: string,
  durationMs: number,
  success: boolean
): void {
  const level = success ? 'info' : 'warn';
  logger.log(level, 'External API call', {
    provider,
    endpoint,
    duration_ms: durationMs,
    success,
  });
}

/**
 * Log cache hit/miss
 */
export function logCache(cacheKey: string, hit: boolean): void {
  logger.debug('Cache access', {
    cache_key: cacheKey,
    hit,
  });
}
