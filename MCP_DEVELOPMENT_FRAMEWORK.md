# MCP Development Framework & Standards

## Purpose

This document establishes the **standard framework** for developing, testing, and documenting Model Context Protocol (MCP) tools for the Ultimate Marketing Agent system.

**Use this framework for**: All 33 MCP tools identified in MCP_TOOLS_COMPREHENSIVE_PLAN.md

---

## Table of Contents

1. [Project Structure](#project-structure)
2. [Development Standards](#development-standards)
3. [Testing Framework](#testing-framework)
4. [Documentation Requirements](#documentation-requirements)
5. [Quality Gates](#quality-gates)
6. [Development Workflow](#development-workflow)
7. [Tool Specification Template](#tool-specification-template)

---

## Project Structure

### Directory Layout

```
/mcp-servers/
├── marketing-tools/                    # Single unified MCP server
│   ├── src/
│   │   ├── index.ts                   # Server entry point
│   │   ├── tools/
│   │   │   ├── geo/
│   │   │   │   ├── multiEngineTest.ts     # GEO-001
│   │   │   │   ├── analyzeCitations.ts    # GEO-002
│   │   │   │   └── competitorVisibility.ts # GEO-003
│   │   │   ├── seo/
│   │   │   │   ├── keywordResearch.ts
│   │   │   │   ├── technicalCrawl.ts
│   │   │   │   └── ...
│   │   │   ├── ads/
│   │   │   │   └── ...
│   │   │   └── shared/
│   │   │       ├── rateLimiter.ts
│   │   │       ├── cache.ts
│   │   │       └── types.ts
│   │   ├── clients/                   # API clients
│   │   │   ├── openai.ts
│   │   │   ├── perplexity.ts
│   │   │   ├── gemini.ts
│   │   │   └── ...
│   │   └── utils/
│   │       ├── logger.ts
│   │       ├── validation.ts
│   │       └── errors.ts
│   ├── tests/
│   │   ├── unit/
│   │   │   ├── tools/
│   │   │   │   ├── geo/
│   │   │   │   │   ├── multiEngineTest.test.ts
│   │   │   │   │   └── analyzeCitations.test.ts
│   │   │   │   └── ...
│   │   │   └── utils/
│   │   ├── integration/
│   │   │   ├── geo-workflow.test.ts
│   │   │   └── ...
│   │   ├── fixtures/                  # Test data
│   │   │   ├── prompts.json
│   │   │   ├── citations.json
│   │   │   └── ...
│   │   └── helpers/
│   │       ├── mockClients.ts
│   │       └── testUtils.ts
│   ├── docs/
│   │   ├── API.md                     # Auto-generated API reference
│   │   ├── USAGE.md                   # Usage examples
│   │   └── tools/
│   │       ├── GEO-001.md
│   │       ├── GEO-002.md
│   │       └── ...
│   ├── package.json
│   ├── tsconfig.json
│   ├── jest.config.js
│   ├── .env.example
│   └── README.md
└── README.md                          # Overview of all MCP servers
```

### Why Single Unified Server?

**Benefits**:
- ✅ Shared caching layer (Redis)
- ✅ Shared rate limiting
- ✅ Single deployment unit
- ✅ Easier dependency management
- ✅ Cross-tool optimizations (e.g., GEO + SEO data reuse)

---

## Development Standards

### Technology Stack

**Required**:
- **Runtime**: Node.js 18+
- **Language**: TypeScript 5.0+
- **MCP SDK**: `@modelcontextprotocol/sdk`
- **Testing**: Jest 29+
- **Linting**: ESLint + Prettier
- **HTTP Client**: Axios (with retry logic)
- **Caching**: ioredis (Redis client)

**Optional** (as needed):
- **Queue**: Bull (for background jobs)
- **Database**: Better-sqlite3 (for local persistence)

### Code Standards

#### 1. TypeScript Strict Mode

**tsconfig.json**:
```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "commonjs",
    "lib": ["ES2022"],
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "resolveJsonModule": true,
    "declaration": true,
    "outDir": "./dist",
    "rootDir": "./src"
  }
}
```

#### 2. Type Definitions

**Every tool must have**:
```typescript
// Input schema
interface ToolNameInput {
  // Required fields first
  requiredField: string;

  // Optional fields with defaults documented
  optionalField?: number; // Default: 50
}

// Output schema
interface ToolNameOutput {
  success: boolean;
  data: ToolSpecificData;
  metadata: {
    execution_time_ms: number;
    api_calls_made: number;
    cached: boolean;
  };
  errors?: ErrorDetail[];
}

// Error details
interface ErrorDetail {
  code: string;
  message: string;
  field?: string;
  context?: Record<string, unknown>;
}
```

#### 3. Input Validation

**Use Zod for runtime validation**:
```typescript
import { z } from 'zod';

const MultiEngineTestInputSchema = z.object({
  prompts: z.array(z.object({
    prompt_id: z.string(),
    text: z.string().min(1).max(500),
    category: z.string(),
  })).min(1).max(100),

  engines: z.array(z.enum(['chatgpt', 'perplexity', 'gemini'])).min(1),

  max_concurrent: z.number().int().min(1).max(50).default(50),

  retry_failed: z.boolean().default(true),

  timeout_ms: z.number().int().min(1000).max(30000).default(10000),
});

// Usage
function validateInput(input: unknown): MultiEngineTestInput {
  return MultiEngineTestInputSchema.parse(input);
}
```

#### 4. Error Handling

**Standard error hierarchy**:
```typescript
class MCPToolError extends Error {
  constructor(
    message: string,
    public code: string,
    public statusCode: number = 500,
    public context?: Record<string, unknown>
  ) {
    super(message);
    this.name = 'MCPToolError';
  }
}

class ValidationError extends MCPToolError {
  constructor(message: string, field?: string) {
    super(message, 'VALIDATION_ERROR', 400, { field });
  }
}

class RateLimitError extends MCPToolError {
  constructor(message: string, retryAfter: number) {
    super(message, 'RATE_LIMIT_EXCEEDED', 429, { retryAfter });
  }
}

class APIError extends MCPToolError {
  constructor(message: string, provider: string, statusCode?: number) {
    super(message, 'API_ERROR', statusCode || 502, { provider });
  }
}
```

#### 5. Logging Standards

**Use structured logging**:
```typescript
import winston from 'winston';

const logger = winston.createLogger({
  level: process.env.LOG_LEVEL || 'info',
  format: winston.format.json(),
  defaultMeta: { service: 'marketing-tools-mcp' },
  transports: [
    new winston.transports.File({ filename: 'error.log', level: 'error' }),
    new winston.transports.File({ filename: 'combined.log' }),
  ],
});

// Usage
logger.info('Multi-engine test started', {
  tool: 'GEO-001',
  prompt_count: 50,
  engines: ['chatgpt', 'perplexity'],
});

logger.error('API call failed', {
  tool: 'GEO-001',
  engine: 'perplexity',
  error: error.message,
  status_code: 429,
});
```

#### 6. Async/Await with Error Handling

**Pattern**:
```typescript
async function runMultiEngineTest(
  input: MultiEngineTestInput
): Promise<MultiEngineTestOutput> {
  const startTime = Date.now();
  const errors: ErrorDetail[] = [];

  try {
    // Validate input
    const validatedInput = validateInput(input);

    // Execute with error collection (don't throw on individual failures)
    const results = await Promise.allSettled(
      validatedInput.prompts.map(prompt =>
        executePrompt(prompt, validatedInput.engines)
      )
    );

    // Collect errors but continue
    const successful = results
      .filter((r): r is PromiseFulfilledResult<TestResult> => r.status === 'fulfilled')
      .map(r => r.value);

    const failed = results
      .filter((r): r is PromiseRejectedResult => r.status === 'rejected')
      .map(r => ({
        code: 'EXECUTION_FAILED',
        message: r.reason.message,
      }));

    errors.push(...failed);

    return {
      success: successful.length > 0,
      data: { results: successful },
      metadata: {
        execution_time_ms: Date.now() - startTime,
        api_calls_made: successful.length,
        cached: false,
      },
      errors: errors.length > 0 ? errors : undefined,
    };

  } catch (error) {
    logger.error('Tool execution failed', { error });
    throw new MCPToolError(
      'Failed to execute multi-engine test',
      'EXECUTION_ERROR',
      500,
      { original_error: error.message }
    );
  }
}
```

---

## Testing Framework

### Testing Philosophy

**Test Pyramid**:
```
        /\
       /  \  E2E (5%)
      /____\
     /      \  Integration (15%)
    /________\
   /          \  Unit (80%)
  /__________\
```

### Unit Testing Standards

**Every tool must have**:
- ✅ Input validation tests
- ✅ Success case tests (happy path)
- ✅ Error handling tests
- ✅ Edge case tests
- ✅ Mock all external dependencies

**Example: GEO-001 Unit Tests**

```typescript
// tests/unit/tools/geo/multiEngineTest.test.ts

import { runMultiEngineTest } from '../../../../src/tools/geo/multiEngineTest';
import * as clients from '../../../../src/clients';

// Mock all API clients
jest.mock('../../../../src/clients');

describe('GEO-001: Multi-Engine Test', () => {
  beforeEach(() => {
    jest.clearAllMocks();
  });

  describe('Input Validation', () => {
    it('should reject empty prompts array', async () => {
      await expect(
        runMultiEngineTest({
          prompts: [],
          engines: ['chatgpt'],
        })
      ).rejects.toThrow(ValidationError);
    });

    it('should reject prompts exceeding max count (100)', async () => {
      const prompts = Array(101).fill({ prompt_id: 'test', text: 'test' });

      await expect(
        runMultiEngineTest({ prompts, engines: ['chatgpt'] })
      ).rejects.toThrow('Maximum 100 prompts allowed');
    });

    it('should reject invalid engine names', async () => {
      await expect(
        runMultiEngineTest({
          prompts: [{ prompt_id: 'p1', text: 'test' }],
          engines: ['invalid-engine'],
        })
      ).rejects.toThrow(ValidationError);
    });

    it('should apply default max_concurrent (50)', async () => {
      const input = {
        prompts: [{ prompt_id: 'p1', text: 'test' }],
        engines: ['chatgpt'],
        // max_concurrent not specified
      };

      const validated = validateInput(input);
      expect(validated.max_concurrent).toBe(50);
    });
  });

  describe('Success Cases', () => {
    it('should execute single prompt on single engine', async () => {
      const mockResponse = {
        response: 'Test response',
        citations: [],
        latency_ms: 1200,
      };

      (clients.chatgpt.query as jest.Mock).mockResolvedValue(mockResponse);

      const result = await runMultiEngineTest({
        prompts: [{ prompt_id: 'p1', text: 'What is marketing?' }],
        engines: ['chatgpt'],
      });

      expect(result.success).toBe(true);
      expect(result.data.results).toHaveLength(1);
      expect(result.data.results[0]).toMatchObject({
        prompt_id: 'p1',
        engine: 'chatgpt',
        response: 'Test response',
      });
    });

    it('should execute multiple prompts in parallel', async () => {
      (clients.chatgpt.query as jest.Mock).mockResolvedValue({
        response: 'Response',
        citations: [],
        latency_ms: 1000,
      });

      const prompts = Array(10).fill(null).map((_, i) => ({
        prompt_id: `p${i}`,
        text: `Prompt ${i}`,
      }));

      const startTime = Date.now();
      const result = await runMultiEngineTest({
        prompts,
        engines: ['chatgpt'],
        max_concurrent: 5,
      });
      const duration = Date.now() - startTime;

      expect(result.success).toBe(true);
      expect(result.data.results).toHaveLength(10);

      // Should complete faster than sequential (10 * 1000ms)
      expect(duration).toBeLessThan(5000);
    });

    it('should execute on multiple engines', async () => {
      (clients.chatgpt.query as jest.Mock).mockResolvedValue({
        response: 'ChatGPT response',
        citations: [],
        latency_ms: 1000,
      });

      (clients.perplexity.query as jest.Mock).mockResolvedValue({
        response: 'Perplexity response',
        citations: [{ url: 'test.com' }],
        latency_ms: 1500,
      });

      const result = await runMultiEngineTest({
        prompts: [{ prompt_id: 'p1', text: 'Test' }],
        engines: ['chatgpt', 'perplexity'],
      });

      expect(result.data.results).toHaveLength(2);
      expect(result.data.results[0].engine).toBe('chatgpt');
      expect(result.data.results[1].engine).toBe('perplexity');
    });
  });

  describe('Error Handling', () => {
    it('should retry failed requests when retry_failed=true', async () => {
      let attempts = 0;
      (clients.chatgpt.query as jest.Mock).mockImplementation(() => {
        attempts++;
        if (attempts < 3) {
          throw new Error('Rate limit');
        }
        return Promise.resolve({ response: 'Success', citations: [], latency_ms: 1000 });
      });

      const result = await runMultiEngineTest({
        prompts: [{ prompt_id: 'p1', text: 'Test' }],
        engines: ['chatgpt'],
        retry_failed: true,
      });

      expect(result.success).toBe(true);
      expect(attempts).toBe(3);
    });

    it('should not retry when retry_failed=false', async () => {
      (clients.chatgpt.query as jest.Mock).mockRejectedValue(
        new Error('API Error')
      );

      const result = await runMultiEngineTest({
        prompts: [{ prompt_id: 'p1', text: 'Test' }],
        engines: ['chatgpt'],
        retry_failed: false,
      });

      expect(result.success).toBe(false);
      expect(result.errors).toHaveLength(1);
      expect(clients.chatgpt.query).toHaveBeenCalledTimes(1);
    });

    it('should collect errors but not throw when some prompts fail', async () => {
      (clients.chatgpt.query as jest.Mock)
        .mockResolvedValueOnce({ response: 'Success 1', citations: [], latency_ms: 1000 })
        .mockRejectedValueOnce(new Error('Failed'))
        .mockResolvedValueOnce({ response: 'Success 2', citations: [], latency_ms: 1000 });

      const result = await runMultiEngineTest({
        prompts: [
          { prompt_id: 'p1', text: 'Test 1' },
          { prompt_id: 'p2', text: 'Test 2' },
          { prompt_id: 'p3', text: 'Test 3' },
        ],
        engines: ['chatgpt'],
        retry_failed: false,
      });

      expect(result.success).toBe(true); // Some succeeded
      expect(result.data.results).toHaveLength(2);
      expect(result.errors).toHaveLength(1);
    });
  });

  describe('Edge Cases', () => {
    it('should handle very long prompts (max 500 chars)', async () => {
      const longPrompt = 'a'.repeat(500);

      (clients.chatgpt.query as jest.Mock).mockResolvedValue({
        response: 'Response',
        citations: [],
        latency_ms: 1000,
      });

      await expect(
        runMultiEngineTest({
          prompts: [{ prompt_id: 'p1', text: longPrompt }],
          engines: ['chatgpt'],
        })
      ).resolves.toBeDefined();
    });

    it('should reject prompts over 500 characters', async () => {
      const tooLong = 'a'.repeat(501);

      await expect(
        runMultiEngineTest({
          prompts: [{ prompt_id: 'p1', text: tooLong }],
          engines: ['chatgpt'],
        })
      ).rejects.toThrow(ValidationError);
    });

    it('should handle timeout correctly', async () => {
      (clients.chatgpt.query as jest.Mock).mockImplementation(
        () => new Promise(resolve => setTimeout(resolve, 15000))
      );

      await expect(
        runMultiEngineTest({
          prompts: [{ prompt_id: 'p1', text: 'Test' }],
          engines: ['chatgpt'],
          timeout_ms: 5000,
        })
      ).rejects.toThrow('Timeout');
    });
  });

  describe('Performance', () => {
    it('should respect max_concurrent limit', async () => {
      let concurrentCalls = 0;
      let maxConcurrent = 0;

      (clients.chatgpt.query as jest.Mock).mockImplementation(async () => {
        concurrentCalls++;
        maxConcurrent = Math.max(maxConcurrent, concurrentCalls);

        await new Promise(resolve => setTimeout(resolve, 100));

        concurrentCalls--;
        return { response: 'Test', citations: [], latency_ms: 100 };
      });

      const prompts = Array(20).fill(null).map((_, i) => ({
        prompt_id: `p${i}`,
        text: 'Test',
      }));

      await runMultiEngineTest({
        prompts,
        engines: ['chatgpt'],
        max_concurrent: 5,
      });

      expect(maxConcurrent).toBeLessThanOrEqual(5);
    });
  });
});
```

### Integration Testing

**Test real workflows across multiple tools**:

```typescript
// tests/integration/geo-workflow.test.ts

describe('GEO Workflow Integration', () => {
  it('should complete full GEO analysis workflow', async () => {
    // Step 1: Run multi-engine test
    const testResults = await runMultiEngineTest({
      prompts: fixtures.geoPrompts,
      engines: ['chatgpt', 'perplexity', 'gemini'],
    });

    expect(testResults.success).toBe(true);

    // Step 2: Analyze citations
    const citationAnalysis = await analyzeCitations({
      test_results: testResults.data.results,
      target_brand: 'Acme Corp',
      analysis_depth: 'DEEP',
    });

    expect(citationAnalysis.success).toBe(true);
    expect(citationAnalysis.data.brand_mention_rate).toBeGreaterThan(0);

    // Step 3: Verify data flow
    expect(citationAnalysis.data.total_responses).toBe(
      testResults.data.results.length
    );
  });
});
```

### Test Fixtures

**tests/fixtures/prompts.json**:
```json
{
  "geoPrompts": [
    {
      "prompt_id": "awareness-1",
      "text": "What are the best marketing analytics tools?",
      "category": "awareness",
      "user_type": "marketer",
      "funnel_stage": "awareness"
    },
    {
      "prompt_id": "comparison-1",
      "text": "Compare Acme Corp vs Competitor A for marketing analytics",
      "category": "comparison",
      "user_type": "decision-maker",
      "funnel_stage": "consideration"
    }
  ]
}
```

### Test Coverage Requirements

**Minimum coverage thresholds**:
- **Statements**: 80%
- **Branches**: 75%
- **Functions**: 80%
- **Lines**: 80%

**jest.config.js**:
```javascript
module.exports = {
  preset: 'ts-jest',
  testEnvironment: 'node',
  coverageThreshold: {
    global: {
      branches: 75,
      functions: 80,
      lines: 80,
      statements: 80,
    },
  },
  collectCoverageFrom: [
    'src/**/*.ts',
    '!src/**/*.d.ts',
    '!src/index.ts',
  ],
};
```

---

## Documentation Requirements

### 1. Tool Documentation (per tool)

**Template**: `docs/tools/{TOOL-ID}.md`

```markdown
# {TOOL-ID}: {Tool Name}

## Overview
Brief description of what this tool does.

## Priority
- **P0/P1/P2/P3**
- **Status**: ✅ Implemented / 🚧 In Progress / ⏳ Planned

## Input Schema

\`\`\`typescript
interface ToolNameInput {
  requiredParam: string;  // Description
  optionalParam?: number; // Description (Default: 50)
}
\`\`\`

## Output Schema

\`\`\`typescript
interface ToolNameOutput {
  success: boolean;
  data: {...};
  metadata: {...};
}
\`\`\`

## Usage Examples

### Example 1: Basic Usage
\`\`\`typescript
const result = await toolName({
  requiredParam: "value",
});
\`\`\`

### Example 2: Advanced Usage
\`\`\`typescript
const result = await toolName({
  requiredParam: "value",
  optionalParam: 100,
});
\`\`\`

## Error Codes

| Code | Description | Resolution |
|------|-------------|------------|
| VALIDATION_ERROR | Invalid input | Check input schema |
| RATE_LIMIT_EXCEEDED | Too many requests | Wait and retry |
| API_ERROR | External API failed | Check API status |

## Performance

- **Typical Latency**: 2-5 seconds for 100 prompts
- **Rate Limits**: 50 requests/second (configurable)
- **Caching**: Responses cached for 1 hour

## Dependencies

- OpenAI API
- Perplexity API
- Gemini API
- Redis (caching)

## Testing

See: `tests/unit/tools/geo/multiEngineTest.test.ts`

Run tests:
\`\`\`bash
npm test -- multiEngineTest
\`\`\`
```

### 2. API Reference (Auto-generated)

Use **TypeDoc** to generate API documentation from TypeScript comments:

```typescript
/**
 * Executes prompts across multiple AI engines in parallel
 *
 * @param input - Test configuration
 * @param input.prompts - Array of prompts to test (max 100)
 * @param input.engines - AI engines to test against
 * @param input.max_concurrent - Maximum concurrent requests (default: 50)
 *
 * @returns Test results with citations and metrics
 *
 * @throws {ValidationError} If input validation fails
 * @throws {RateLimitError} If rate limit exceeded
 *
 * @example
 * ```typescript
 * const results = await runMultiEngineTest({
 *   prompts: [{ prompt_id: 'p1', text: 'What is SEO?' }],
 *   engines: ['chatgpt', 'perplexity'],
 * });
 * ```
 */
export async function runMultiEngineTest(
  input: MultiEngineTestInput
): Promise<MultiEngineTestOutput> {
  // ...
}
```

### 3. README.md

**mcp-servers/marketing-tools/README.md**:
```markdown
# Marketing Tools MCP Server

Unified MCP server providing 33 marketing analysis tools.

## Quick Start

\`\`\`bash
npm install
npm run build
npm start
\`\`\`

## Configuration

Copy `.env.example` to `.env`:
\`\`\`bash
cp .env.example .env
\`\`\`

Required environment variables:
- `OPENAI_API_KEY`
- `PERPLEXITY_API_KEY`
- `GEMINI_API_KEY`
- `REDIS_URL` (optional, defaults to localhost)

## Available Tools

### GEO Tools (P0)
- **GEO-001**: Multi-Engine Test - Execute prompts across AI engines
- **GEO-002**: Analyze Citations - LLM-powered citation analysis

[See full tool list](./docs/API.md)

## Testing

\`\`\`bash
# Run all tests
npm test

# Run with coverage
npm run test:coverage

# Run specific test
npm test -- multiEngineTest
\`\`\`

## Development

\`\`\`bash
# Watch mode
npm run dev

# Lint
npm run lint

# Format
npm run format
\`\`\`
```

---

## Quality Gates

### Pre-Commit Checklist

**Before committing any tool implementation**:

- [ ] ✅ All unit tests pass
- [ ] ✅ Integration tests pass (if applicable)
- [ ] ✅ Code coverage meets thresholds (80%)
- [ ] ✅ TypeScript compiles with no errors
- [ ] ✅ ESLint passes with no warnings
- [ ] ✅ Input validation with Zod
- [ ] ✅ Error handling for all failure modes
- [ ] ✅ Logging for key operations
- [ ] ✅ Tool documentation created
- [ ] ✅ Usage examples provided
- [ ] ✅ Performance tested (if applicable)

### Code Review Checklist

- [ ] Input validation comprehensive?
- [ ] Error messages clear and actionable?
- [ ] Async operations properly handled?
- [ ] Rate limiting implemented?
- [ ] Caching implemented (where beneficial)?
- [ ] Tests cover edge cases?
- [ ] Documentation complete?
- [ ] Performance acceptable?

---

## Development Workflow

### Step-by-Step Process

**For each new tool (e.g., GEO-001)**:

#### **Phase 1: Planning (15 min)**
1. Read tool spec from `MCP_TOOLS_REQUIREMENTS.md`
2. Identify dependencies (APIs, libraries)
3. Design input/output types
4. List test scenarios

#### **Phase 2: Implementation (2-4 hours)**
1. Create type definitions in `src/tools/{category}/{toolName}.ts`
2. Implement validation with Zod
3. Implement core logic
4. Add error handling
5. Add logging
6. Write JSDoc comments

#### **Phase 3: Testing (1-2 hours)**
1. Create unit test file `tests/unit/tools/{category}/{toolName}.test.ts`
2. Write validation tests
3. Write success case tests
4. Write error handling tests
5. Write edge case tests
6. Write performance tests (if needed)
7. Run coverage: `npm run test:coverage`

#### **Phase 4: Documentation (30 min)**
1. Create `docs/tools/{TOOL-ID}.md`
2. Write usage examples
3. Document error codes
4. Document performance characteristics
5. Update main README.md

#### **Phase 5: Integration (30 min)**
1. Register tool in `src/index.ts`
2. Add to tool registry
3. Test with MCP client
4. Create integration test (if cross-tool dependencies)

#### **Phase 6: Review & Commit (15 min)**
1. Run full test suite: `npm test`
2. Run linter: `npm run lint`
3. Check coverage report
4. Review quality gates checklist
5. Commit with descriptive message

---

## Tool Specification Template

**For documenting new tools before implementation**:

```markdown
## Tool ID: {CATEGORY}-{NUMBER}

### Name
{Tool Name}

### Priority
P0 / P1 / P2 / P3

### Description
{1-2 sentence description}

### Input Schema
\`\`\`typescript
interface ToolInput {
  requiredParam: type;    // Description
  optionalParam?: type;   // Description (Default: value)
}
\`\`\`

### Output Schema
\`\`\`typescript
interface ToolOutput {
  success: boolean;
  data: {
    // Tool-specific output
  };
  metadata: {
    execution_time_ms: number;
    api_calls_made: number;
  };
}
\`\`\`

### Business Logic
1. Step 1
2. Step 2
3. Step 3

### External Dependencies
- API 1 (rate limit, cost)
- API 2 (rate limit, cost)

### Caching Strategy
- Cache key: {description}
- TTL: {duration}
- Invalidation: {conditions}

### Rate Limiting
- Limit: X requests per Y seconds
- Scope: per-user / global

### Error Scenarios
1. Error 1 → Code, Message, Resolution
2. Error 2 → Code, Message, Resolution

### Testing Scenarios
1. Success case 1
2. Success case 2
3. Error case 1
4. Edge case 1

### Estimated Complexity
- Implementation: X hours
- Testing: Y hours
- Total: Z hours
```

---

## Summary

### Key Principles

1. **Type Safety**: Strict TypeScript, Zod validation
2. **Error Resilience**: Graceful degradation, detailed errors
3. **Testability**: 80%+ coverage, mocked dependencies
4. **Documentation**: Every tool fully documented
5. **Performance**: Parallel execution, caching, rate limiting
6. **Observability**: Structured logging, metrics

### Checklist for Each Tool

✅ **Code**:
- Type definitions
- Zod validation
- Error handling
- Logging
- JSDoc comments

✅ **Tests**:
- Unit tests (80%+ coverage)
- Integration tests (if needed)
- Fixtures

✅ **Docs**:
- Tool documentation
- Usage examples
- Error reference

✅ **Quality**:
- All tests pass
- Linter passes
- Coverage thresholds met

---

**Next Steps**: Implement GEO-001 and GEO-002 following this framework.
