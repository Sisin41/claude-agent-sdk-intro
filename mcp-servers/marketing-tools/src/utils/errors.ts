/**
 * Custom error classes for MCP tools
 */

/**
 * Base error class for all MCP tool errors
 */
export class MCPToolError extends Error {
  constructor(
    message: string,
    public code: string,
    public statusCode: number = 500,
    public context?: Record<string, unknown>
  ) {
    super(message);
    this.name = 'MCPToolError';
    Error.captureStackTrace(this, this.constructor);
  }

  toJSON(): Record<string, unknown> {
    return {
      name: this.name,
      code: this.code,
      message: this.message,
      statusCode: this.statusCode,
      context: this.context,
    };
  }
}

/**
 * Input validation error
 */
export class ValidationError extends MCPToolError {
  constructor(message: string, field?: string) {
    super(message, 'VALIDATION_ERROR', 400, { field });
    this.name = 'ValidationError';
  }
}

/**
 * Rate limit exceeded error
 */
export class RateLimitError extends MCPToolError {
  constructor(message: string, retryAfter: number) {
    super(message, 'RATE_LIMIT_EXCEEDED', 429, { retryAfter });
    this.name = 'RateLimitError';
  }
}

/**
 * External API error
 */
export class APIError extends MCPToolError {
  constructor(message: string, provider: string, originalStatus?: number) {
    super(message, 'API_ERROR', originalStatus || 502, { provider });
    this.name = 'APIError';
  }
}

/**
 * Timeout error
 */
export class TimeoutError extends MCPToolError {
  constructor(message: string, timeoutMs: number) {
    super(message, 'TIMEOUT_ERROR', 408, { timeoutMs });
    this.name = 'TimeoutError';
  }
}

/**
 * Caching error
 */
export class CacheError extends MCPToolError {
  constructor(message: string) {
    super(message, 'CACHE_ERROR', 500);
    this.name = 'CacheError';
  }
}

/**
 * Configuration error
 */
export class ConfigError extends MCPToolError {
  constructor(message: string, missingConfig?: string) {
    super(message, 'CONFIG_ERROR', 500, { missingConfig });
    this.name = 'ConfigError';
  }
}
