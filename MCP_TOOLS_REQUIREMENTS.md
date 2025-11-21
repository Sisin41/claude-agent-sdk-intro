# MCP Tools Requirements - Marketing Agent

**Project**: Ultimate Marketing Agent
**Component**: Custom MCP Server - Marketing Tools
**Status**: Requirements Defined - Ready for Implementation
**Last Updated**: 2025-11-20

---

## Executive Summary

This document specifies the requirements for **2 critical MCP tools** that enable the Marketing Agent's core functionality. These tools provide **20x performance improvements** over manual/sequential approaches.

**Tools**:
1. `run_multi_engine_test` - Parallel AI engine testing (P0 - Critical)
2. `analyze_citations` - Parallel LLM-powered citation analysis (P0 - Critical)

**Impact**: Transforms 3-4 day manual workflow into 20-minute automated process.

---

## Tool #1: Multi-Engine Test Runner

### Overview

**Tool Name**: `run_multi_engine_test`
**Priority**: **P0 (Must Have)**
**Purpose**: Execute test prompts across multiple AI engines (ChatGPT, Perplexity, Gemini) in parallel to measure brand visibility

**Defined In**: `.claude/skills/geo/multi-engine-testing.md`

### Business Value

**Without This Tool**:
- Sequential execution: 300 tests = 14 minutes
- Manual WebSearch fallback: 40-60 minutes
- Limited to 1-2 engines (time constraints)
- Poor data quality (manual extraction)

**With This Tool**:
- Parallel execution: 300 tests = 30-90 seconds
- **20x performance improvement**
- All 3 engines tested simultaneously
- High-quality structured data

**ROI**: Core value proposition of DEEP mode - makes it practical to run comprehensive GEO analysis.

---

### Functional Requirements

#### FR-1: Prompt Execution

**Requirement**: Execute list of prompts across multiple AI engines

**Input**:
```typescript
interface PromptTest {
  prompt_id: string;          // Unique identifier (e.g., "prompt_001")
  text: string;               // The actual prompt text
  metadata?: {                // Optional metadata for tracking
    question_family?: string;  // e.g., "comparison", "problem-solution"
    user_type?: string;        // e.g., "Head of Support"
    funnel_stage?: string;     // e.g., "consideration"
    expected_visibility?: string; // "HIGH", "MEDIUM", "LOW"
  };
}

interface EngineConfig {
  name: 'chatgpt' | 'perplexity' | 'gemini';
  model?: string;             // Optional specific model (e.g., "gpt-4-turbo")
  api_key?: string;           // API key (usually from env vars)
}

interface RunMultiEngineTestInput {
  prompts: PromptTest[];      // 10-100 prompts
  engines: EngineConfig[];    // 2-3 engine configurations
  max_concurrent?: number;    // Default: 50
  retry_failed?: boolean;     // Default: true
  timeout_ms?: number;        // Default: 10000 (10 seconds per request)
}
```

**Output**:
```typescript
interface TestResult {
  prompt_id: string;
  engine: string;             // "chatgpt", "perplexity", or "gemini"
  success: boolean;
  response: string | null;    // Full text response from engine
  citations: Citation[];      // Extracted citations
  brand_mentioned: boolean;   // Was brand mentioned?
  brand_position?: number;    // Position if mentioned (1=first, 2=second, etc.)
  timestamp: string;          // ISO 8601 timestamp
  latency_ms: number;         // Time taken for this request
  error?: string;             // Error message if failed
}

interface Citation {
  position: number;           // Order in response (1, 2, 3...)
  url: string;
  title: string;
  snippet: string;            // Excerpt from source
  context: string;            // How it was cited in AI response
}
```

**Acceptance Criteria**:
- [ ] Accepts 10-100 prompts
- [ ] Supports ChatGPT, Perplexity, Gemini engines
- [ ] Returns structured TestResult for each prompt×engine combination
- [ ] Response includes full AI engine output
- [ ] Citations extracted with URLs, titles, snippets

---

#### FR-2: Parallel Execution

**Requirement**: Execute requests in parallel with configurable concurrency

**Specifications**:
- Default concurrency: 50 concurrent requests
- Configurable via `max_concurrent` parameter
- Should handle 300 tests (100 prompts × 3 engines) in < 90 seconds

**Implementation Approach**:
```typescript
// Use p-map or similar for controlled concurrency
import pMap from 'p-map';

const allTests = prompts.flatMap(prompt =>
  engines.map(engine => ({ prompt, engine }))
);

const results = await pMap(
  allTests,
  async ({ prompt, engine }) => {
    return await executeTest(prompt, engine);
  },
  { concurrency: max_concurrent }
);
```

**Acceptance Criteria**:
- [ ] Can run 50+ concurrent requests without crashing
- [ ] Completes 300 tests in < 90 seconds
- [ ] Memory usage stays stable (no leaks)
- [ ] Progress can be tracked (see FR-7)

---

#### FR-3: Rate Limit Handling

**Requirement**: Gracefully handle API rate limits with intelligent retry logic

**Rate Limits**:
- **ChatGPT (OpenAI)**: 3,500 requests/minute (TPM varies)
- **Perplexity**: 50 requests/minute (standard tier)
- **Gemini**: 60 requests/minute (free tier)

**Retry Strategy**:
```
If 429 (rate limit) error:
1. First retry: Wait 2 seconds
2. Second retry: Wait 4 seconds
3. Third retry: Wait 8 seconds
4. After 3 retries: Mark as failed, continue with others
```

**Exponential Backoff Formula**:
```typescript
const delay = Math.min(1000 * Math.pow(2, retryCount), 16000);
```

**Acceptance Criteria**:
- [ ] Detects 429 status codes
- [ ] Implements exponential backoff (2s, 4s, 8s, max 16s)
- [ ] Retries up to 3 times per request
- [ ] Continues with other tests if one fails
- [ ] Logs rate limit events for debugging

---

#### FR-4: Citation Extraction

**Requirement**: Extract citations from AI engine responses (engine-specific parsing)

**ChatGPT Citation Format**:
```
Response may include:
- Inline citations: [1], [2], [3]
- Footer with sources
- Sometimes no explicit citations (just mentions)

Example:
"The best AI tools include Zendesk[1] and Acme[2]..."

Sources:
[1] https://zendesk.com/ai - Zendesk AI Features
[2] https://acmecorp.com/features - Acme AI Platform
```

**Perplexity Citation Format**:
```
Numbered citations at end:
1. zendesk.com/ai - Zendesk AI Features
2. acmecorp.com/features - Acme AI Platform
```

**Gemini Citation Format**:
```
Source attributions (format varies):
- May be inline
- May be at bottom
- May include URLs directly
```

**Extraction Requirements**:
- Parse engine-specific citation formats
- Extract: URL, title, snippet, position
- Handle missing/malformed citations gracefully
- Return empty array if no citations found

**Acceptance Criteria**:
- [ ] Extracts citations from ChatGPT responses
- [ ] Extracts citations from Perplexity responses
- [ ] Extracts citations from Gemini responses
- [ ] Returns structured Citation objects
- [ ] Handles responses with 0 citations
- [ ] Handles malformed citation formats

---

#### FR-5: Brand Mention Detection

**Requirement**: Detect if brand is mentioned in AI response

**Input**:
```typescript
interface BrandInfo {
  brand_name: string;        // e.g., "Acme Corp"
  domain: string;            // e.g., "acmecorp.com"
  variations?: string[];     // e.g., ["Acme", "acme", "acmecorp"]
}
```

**Detection Logic**:
```typescript
function detectBrandMention(response: string, brandInfo: BrandInfo): {
  mentioned: boolean;
  position: number | null;   // Which mention (1st, 2nd, 3rd in response)
  context: string | null;    // Surrounding text
} {
  const variations = [
    brandInfo.brand_name,
    brandInfo.brand_name.toLowerCase(),
    brandInfo.domain.replace('.com', ''),
    ...(brandInfo.variations || [])
  ];

  for (const variation of variations) {
    if (response.toLowerCase().includes(variation.toLowerCase())) {
      return {
        mentioned: true,
        position: calculateMentionPosition(response, variation),
        context: extractContext(response, variation)
      };
    }
  }

  return { mentioned: false, position: null, context: null };
}
```

**Position Calculation**:
- 1 = Mentioned in first paragraph/section
- 2 = Mentioned in second paragraph
- 3+ = Mentioned later

**Acceptance Criteria**:
- [ ] Detects exact brand name matches (case-insensitive)
- [ ] Detects domain name mentions
- [ ] Supports custom brand variations
- [ ] Returns position in response
- [ ] Extracts context (50 chars before/after)

---

#### FR-6: Error Handling

**Requirement**: Handle all error conditions gracefully

**Error Types**:

1. **Invalid API Key (401)**:
   - Log clear error: "Invalid API key for {engine}"
   - Skip that engine entirely
   - Continue with other engines
   - Include warning in summary

2. **Network Errors**:
   - Retry immediately (network may be flaky)
   - If fails again, mark as failed
   - Continue with other tests

3. **Timeout**:
   - Configurable timeout (default 10s)
   - Mark as failed after timeout
   - Continue with other tests

4. **Malformed Response**:
   - Log response for debugging
   - Extract what data is possible
   - Mark citations as "unable to parse"
   - Continue with test

5. **Engine-Specific Errors**:
   - Handle each engine's error format
   - Extract error messages
   - Log for debugging

**Acceptance Criteria**:
- [ ] Continues execution if one test fails
- [ ] Logs errors with context (prompt_id, engine, error type)
- [ ] Returns partial results (successful tests only)
- [ ] Includes error count in summary
- [ ] Never crashes entire batch due to single failure

---

#### FR-7: Progress Tracking

**Requirement**: Provide real-time progress updates

**Progress Data**:
```typescript
interface Progress {
  total_tests: number;
  completed_tests: number;
  failed_tests: number;
  by_engine: {
    [engine: string]: {
      total: number;
      completed: number;
      failed: number;
    };
  };
  elapsed_seconds: number;
  estimated_remaining_seconds: number;
}
```

**Update Frequency**: Every 10 completed tests or every 2 seconds

**Example Output**:
```
[████████████████░░░░] 70% (210/300)

By engine:
ChatGPT:    [████████████████████] 100/100 ✓ (42s)
Perplexity: [████████████████████] 100/100 ✓ (38s)
Gemini:     [██████░░░░░░░░░░░░░░] 10/100 ⏳ (est. 45s remaining)
```

**Acceptance Criteria**:
- [ ] Emits progress events during execution
- [ ] Shows percentage complete
- [ ] Shows breakdown by engine
- [ ] Shows elapsed time
- [ ] Shows estimated time remaining

---

#### FR-8: Result Aggregation

**Requirement**: Aggregate results with summary statistics

**Summary Output**:
```typescript
interface TestSummary {
  total_tests: number;
  successful_tests: number;
  failed_tests: number;
  success_rate: number;        // Percentage
  average_latency_ms: number;
  total_time_seconds: number;
  brand_mentions: {
    total: number;
    by_engine: {
      [engine: string]: number;
    };
    visibility_rate: number;    // Percentage
  };
  failures: Array<{
    prompt_id: string;
    engine: string;
    error: string;
    retry_count: number;
  }>;
}
```

**Acceptance Criteria**:
- [ ] Calculates total/successful/failed counts
- [ ] Calculates average latency
- [ ] Counts brand mentions per engine
- [ ] Calculates visibility rate (mentions / total tests)
- [ ] Lists all failures with details

---

### Non-Functional Requirements

#### NFR-1: Performance

- **Throughput**: 3-10 tests/second (with 50 concurrent)
- **Latency**: < 90 seconds for 300 tests
- **Memory**: < 512MB for 300 tests
- **CPU**: Should not peg CPU at 100% (concurrency limiting)

#### NFR-2: Reliability

- **Success Rate**: > 95% of tests should succeed (assuming valid API keys)
- **Stability**: No crashes or memory leaks
- **Idempotency**: Same inputs → same outputs (deterministic)

#### NFR-3: Security

- **API Keys**: Never log API keys
- **Secrets**: Load from environment variables
- **Input Validation**: Validate all inputs before execution
- **Output Sanitization**: Ensure no sensitive data in logs

#### NFR-4: Observability

- **Logging**: Structured logs (JSON format)
- **Error Tracking**: Clear error messages with context
- **Metrics**: Track success/failure rates, latencies
- **Debugging**: Ability to run in verbose mode

---

### API Specification

#### MCP Tool Declaration

```json
{
  "name": "run_multi_engine_test",
  "description": "Execute test prompts across multiple AI engines (ChatGPT, Perplexity, Gemini) in parallel to measure brand visibility and extract citations",
  "inputSchema": {
    "type": "object",
    "properties": {
      "prompts": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "prompt_id": { "type": "string" },
            "text": { "type": "string" },
            "metadata": { "type": "object" }
          },
          "required": ["prompt_id", "text"]
        }
      },
      "engines": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "name": { "type": "string", "enum": ["chatgpt", "perplexity", "gemini"] },
            "model": { "type": "string" },
            "api_key": { "type": "string" }
          },
          "required": ["name"]
        }
      },
      "max_concurrent": { "type": "number", "default": 50 },
      "retry_failed": { "type": "boolean", "default": true },
      "timeout_ms": { "type": "number", "default": 10000 }
    },
    "required": ["prompts", "engines"]
  }
}
```

---

### Implementation Guidance

#### Technology Stack

**Language**: TypeScript (Node.js)
**Key Libraries**:
- `p-map` - Controlled parallel execution
- `axios` or `fetch` - HTTP requests
- `openai` - OpenAI API client
- Custom clients for Perplexity and Gemini

**File Structure**:
```
mcp-servers/marketing-tools/src/geo/
├── multi-engine-runner.ts       # Main tool implementation
├── engines/
│   ├── chatgpt.ts               # ChatGPT API integration
│   ├── perplexity.ts            # Perplexity API integration
│   ├── gemini.ts                # Gemini API integration
│   └── base-engine.ts           # Shared engine interface
├── citation-extractor.ts        # Citation parsing logic
├── brand-detector.ts            # Brand mention detection
└── types.ts                     # TypeScript interfaces
```

#### Sample Implementation Outline

```typescript
// multi-engine-runner.ts

import pMap from 'p-map';
import { ChatGPTEngine } from './engines/chatgpt';
import { PerplexityEngine } from './engines/perplexity';
import { GeminiEngine } from './engines/gemini';

export async function runMultiEngineTest(input: RunMultiEngineTestInput): Promise<TestResult[]> {
  // 1. Initialize engines
  const engineInstances = input.engines.map(config => createEngine(config));

  // 2. Create all test combinations
  const allTests = input.prompts.flatMap(prompt =>
    engineInstances.map(engine => ({ prompt, engine }))
  );

  console.log(`Running ${allTests.length} tests across ${input.engines.length} engines...`);

  // 3. Execute in parallel with retry logic
  const results = await pMap(
    allTests,
    async ({ prompt, engine }) => {
      return await executeWithRetry(prompt, engine, input.retry_failed);
    },
    { concurrency: input.max_concurrent || 50 }
  );

  // 4. Aggregate and return
  return results.filter(r => r !== null);
}

async function executeWithRetry(
  prompt: PromptTest,
  engine: BaseEngine,
  retryEnabled: boolean
): Promise<TestResult | null> {
  let retryCount = 0;
  const maxRetries = retryEnabled ? 3 : 0;

  while (retryCount <= maxRetries) {
    try {
      const startTime = Date.now();
      const response = await engine.query(prompt.text);
      const citations = extractCitations(response, engine.name);
      const brandMention = detectBrandMention(response, BRAND_INFO);

      return {
        prompt_id: prompt.prompt_id,
        engine: engine.name,
        success: true,
        response: response,
        citations: citations,
        brand_mentioned: brandMention.mentioned,
        brand_position: brandMention.position,
        timestamp: new Date().toISOString(),
        latency_ms: Date.now() - startTime
      };
    } catch (error) {
      if (error.status === 429 && retryCount < maxRetries) {
        // Rate limit - wait and retry
        const delay = Math.min(1000 * Math.pow(2, retryCount), 16000);
        await sleep(delay);
        retryCount++;
        continue;
      } else {
        // Other error or max retries reached
        return {
          prompt_id: prompt.prompt_id,
          engine: engine.name,
          success: false,
          response: null,
          citations: [],
          brand_mentioned: false,
          timestamp: new Date().toISOString(),
          latency_ms: 0,
          error: error.message
        };
      }
    }
  }
}
```

---

### Testing Requirements

#### Unit Tests

- [ ] Test individual engine integrations (mock APIs)
- [ ] Test citation extraction per engine
- [ ] Test brand detection logic
- [ ] Test retry logic with simulated rate limits
- [ ] Test error handling for all error types

#### Integration Tests

- [ ] Test with real API keys (dev environment)
- [ ] Test 10 prompts × 2 engines (20 tests)
- [ ] Verify all citations extracted correctly
- [ ] Verify brand detection accuracy

#### Performance Tests

- [ ] Benchmark: 100 prompts × 3 engines (300 tests)
- [ ] Verify completion in < 90 seconds
- [ ] Verify memory usage < 512MB
- [ ] Verify no memory leaks over multiple runs

#### Edge Case Tests

- [ ] Empty prompt list
- [ ] Invalid API keys
- [ ] Network disconnection mid-execution
- [ ] All engines fail
- [ ] Malformed engine responses

---

### Deployment Checklist

- [ ] TypeScript compiled to JavaScript
- [ ] All dependencies listed in package.json
- [ ] Environment variables documented
- [ ] MCP tool registered in server index
- [ ] README with usage examples
- [ ] Error messages are user-friendly
- [ ] Logging configured properly
- [ ] Performance tested with 300+ tests

---

### Environment Variables Required

```bash
# .env file
OPENAI_API_KEY=sk-...           # For ChatGPT
PERPLEXITY_API_KEY=pplx-...     # For Perplexity
GOOGLE_API_KEY=AIza...          # For Gemini (Google)
```

---

### Success Criteria

This tool is **complete and ready** when:

1. ✅ Can execute 300 tests in < 90 seconds
2. ✅ Success rate > 95% (with valid API keys)
3. ✅ Extracts citations from all 3 engines correctly
4. ✅ Detects brand mentions accurately (> 95%)
5. ✅ Handles rate limits gracefully (no crashes)
6. ✅ All error conditions handled properly
7. ✅ Progress tracking works
8. ✅ Summary statistics accurate
9. ✅ Integration tests pass
10. ✅ Works with marketing agent (end-to-end test)

---

## Tool #2: Citation Analyzer

### Overview

**Tool Name**: `analyze_citations`
**Priority**: **P0 (Must Have)**
**Purpose**: Analyze citations using parallel LLM calls to extract deep insights (relevance, sentiment, recommendations)

**Defined In**: `.claude/skills/geo/citation-analysis.md`

### Business Value

**Without This Tool**:
- Manual analysis: 45 minutes for 900 citations
- Basic pattern matching only (no deep insights)
- Cannot scale to DEEP mode volumes
- Limited quality of insights

**With This Tool**:
- Parallel LLM analysis: 2-3 minutes for 900 citations
- **20x performance improvement**
- Deep insights using Claude Haiku
- High-quality structured analysis
- Cost: ~$0.11-0.25 per run (very affordable)

**ROI**: Enables DEEP mode analysis with actionable insights, not just data dumps.

---

### Functional Requirements

#### FR-1: Citation Processing

**Requirement**: Process list of citations with LLM-powered analysis

**Input**:
```typescript
interface AnalyzeCitationsInput {
  test_results: TestResult[];  // From multi-engine testing tool
  brand_info: {
    brand_name: string;
    domain: string;
    competitors?: string[];
  };
  analysis_mode: 'light' | 'deep';
  max_concurrent?: number;     // Default: 50
  llm_model?: string;          // Default: 'claude-haiku-3-5'
}
```

**Output**:
```typescript
interface CitationAnalysis {
  citation_id: string;
  url: string;
  title: string;

  // Analysis results
  relevance_score: number;          // 0-100
  sentiment: 'positive' | 'neutral' | 'negative';
  brand_context: string;            // How brand was mentioned
  competitor_mentions: string[];
  key_points: string[];
  authority_score: number;          // 0-100
  content_type: 'blog' | 'product_page' | 'review' | 'news' | 'documentation' | 'other';

  // Deep mode only
  detailed_analysis?: string;
  recommendations?: string[];

  // Metadata
  times_cited: number;              // Across all tests
  cited_by_engines: string[];       // Which engines cited it
}
```

**Acceptance Criteria**:
- [ ] Accepts test results from tool #1
- [ ] Extracts all unique citations
- [ ] Deduplicates by URL
- [ ] Tracks citation frequency
- [ ] Returns structured analysis per citation

---

#### FR-2: LLM-Powered Analysis

**Requirement**: Use LLM to analyze each citation in parallel

**LLM Configuration**:
- **Model**: Claude Haiku 3.5 (fast and cost-effective)
- **Max Tokens**: 500 (LIGHT) / 1500 (DEEP)
- **Temperature**: 0.3 (more deterministic)
- **Concurrency**: 50 parallel calls

**Prompt Template** (per citation):
```
Analyze this citation from an AI engine response:

**Citation Info:**
URL: {url}
Title: {title}
Snippet: {snippet}
Context in response: {context}

**Brand Info:**
Our brand: {brand_name}
Domain: {domain}
Competitors: {competitors}

**Analysis Required:**

1. **Relevance Score** (0-100): How relevant is this citation?
2. **Sentiment** (positive/neutral/negative): How is our brand portrayed?
3. **Brand Context**: How is our brand mentioned (quote exact phrase)?
4. **Competitor Mentions**: Which competitors mentioned?
5. **Key Points**: 2-3 main takeaways from citation
6. **Authority Score** (0-100): How authoritative is this source?
7. **Content Type**: blog/product_page/review/news/documentation/other

[DEEP mode only:]
8. **Detailed Analysis**: Additional insights
9. **Recommendations**: How to improve to be cited here?

Output as JSON:
{
  "relevance_score": 85,
  "sentiment": "positive",
  "brand_context": "...",
  ...
}
```

**Acceptance Criteria**:
- [ ] Builds correct prompt per citation
- [ ] Calls Claude Haiku API
- [ ] Parses LLM JSON response
- [ ] Handles malformed LLM responses
- [ ] Returns structured CitationAnalysis object

---

#### FR-3: Parallel Execution

**Requirement**: Execute LLM calls in parallel with concurrency control

**Implementation**:
```typescript
import pMap from 'p-map';

const analyses = await pMap(
  uniqueCitations,
  async (citation) => {
    const prompt = buildAnalysisPrompt(citation, brandInfo, mode);
    const response = await callLLM({
      model: 'claude-haiku-3-5',
      prompt: prompt,
      max_tokens: mode === 'light' ? 500 : 1500
    });
    return parseLLMResponse(response);
  },
  { concurrency: 50 }
);
```

**Performance Target**:
- 900 citations in < 3 minutes
- ~5 citations/second throughput

**Acceptance Criteria**:
- [ ] Executes 50 concurrent LLM calls
- [ ] Completes 900 citations in < 3 minutes
- [ ] Memory usage stable
- [ ] Progress tracking works

---

#### FR-4: Citation Deduplication

**Requirement**: Deduplicate citations by URL

**Logic**:
```typescript
function deduplicateCitations(citations: Citation[]): Citation[] {
  const urlMap = new Map<string, Citation>();

  for (const citation of citations) {
    const normalizedUrl = normalizeUrl(citation.url);

    if (!urlMap.has(normalizedUrl)) {
      urlMap.set(normalizedUrl, {
        ...citation,
        times_cited: 1,
        cited_by_engines: [citation.source_engine]
      });
    } else {
      const existing = urlMap.get(normalizedUrl);
      existing.times_cited++;
      if (!existing.cited_by_engines.includes(citation.source_engine)) {
        existing.cited_by_engines.push(citation.source_engine);
      }
    }
  }

  return Array.from(urlMap.values());
}

function normalizeUrl(url: string): string {
  // Remove trailing slashes, http/https differences, www prefix
  return url
    .toLowerCase()
    .replace(/^https?:\/\//, '')
    .replace(/^www\./, '')
    .replace(/\/$/, '');
}
```

**Acceptance Criteria**:
- [ ] Same URL counted once with `times_cited` counter
- [ ] Tracks which engines cited it
- [ ] Handles URL variations (http/https, www, trailing slash)
- [ ] Preserves first occurrence's metadata

---

#### FR-5: Result Aggregation

**Requirement**: Aggregate citation analyses with summary statistics

**Aggregations**:

1. **Brand Performance**:
```typescript
{
  total_brand_citations: number;
  avg_relevance_score: number;
  sentiment_breakdown: {
    positive: number;
    neutral: number;
    negative: number;
  };
}
```

2. **Top Content**:
```typescript
{
  top_cited_content: Array<{
    url: string;
    title: string;
    times_cited: number;
    engines_citing: string[];
    avg_relevance: number;
  }>;
}
```

3. **Competitor Visibility**:
```typescript
{
  competitor_citations: {
    [competitor: string]: {
      count: number;
      avg_relevance: number;
      sentiment: string;
    };
  };
}
```

**Acceptance Criteria**:
- [ ] Calculates all summary statistics
- [ ] Identifies top 10 cited content
- [ ] Tracks competitor mentions
- [ ] Groups by sentiment

---

#### FR-6: Error Handling

**Requirement**: Handle LLM failures gracefully

**Error Scenarios**:

1. **LLM API Error**:
   - Retry once with exponential backoff
   - If fails, fallback to basic pattern matching
   - Flag as "partial_analysis": true
   - Continue with other citations

2. **Malformed LLM Response**:
   - Attempt regex extraction of key fields
   - If extraction fails, mark as "analysis_failed"
   - Log for review
   - Continue with others

3. **Rate Limiting**:
   - Reduce concurrency from 50 to 25
   - Add 100ms delay between batches
   - Retry failed batch

**Acceptance Criteria**:
- [ ] Continues execution if one LLM call fails
- [ ] Logs failures with context
- [ ] Returns partial results
- [ ] Includes failure count in summary
- [ ] Fallback to basic analysis if LLM unavailable

---

#### FR-7: Cost Tracking

**Requirement**: Track and report API costs

**Cost Calculation**:
```typescript
interface CostEstimate {
  total_citations_analyzed: number;
  llm_model: string;
  total_tokens_used: number;
  estimated_cost_usd: number;
}

// Claude Haiku pricing: ~$0.25 per 1M input tokens, ~$1.25 per 1M output tokens
function calculateCost(citations: number, avgInputTokens: number, avgOutputTokens: number): number {
  const inputCost = (citations * avgInputTokens / 1_000_000) * 0.25;
  const outputCost = (citations * avgOutputTokens / 1_000_000) * 1.25;
  return inputCost + outputCost;
}
```

**Acceptance Criteria**:
- [ ] Tracks tokens per LLM call
- [ ] Calculates total cost
- [ ] Includes cost in summary
- [ ] Warns if cost exceeds threshold

---

### Non-Functional Requirements

#### NFR-1: Performance

- **Throughput**: 5 citations/second
- **Latency**: < 3 minutes for 900 citations
- **Memory**: < 256MB for 900 citations
- **LLM Latency**: < 2 seconds per call (Haiku is fast)

#### NFR-2: Cost Efficiency

- **Model Choice**: Claude Haiku (cheapest, fastest)
- **Token Optimization**: Concise prompts
- **Cost per DEEP run**: < $0.30
- **Cost per LIGHT run**: < $0.05

#### NFR-3: Quality

- **Accuracy**: > 90% correct sentiment classification
- **Consistency**: Same citation → same analysis (deterministic)
- **Completeness**: All required fields populated

---

### API Specification

#### MCP Tool Declaration

```json
{
  "name": "analyze_citations",
  "description": "Analyze citations from AI engine test results using parallel LLM calls to extract relevance, sentiment, and recommendations",
  "inputSchema": {
    "type": "object",
    "properties": {
      "test_results": {
        "type": "array",
        "items": { "type": "object" }
      },
      "brand_info": {
        "type": "object",
        "properties": {
          "brand_name": { "type": "string" },
          "domain": { "type": "string" },
          "competitors": {
            "type": "array",
            "items": { "type": "string" }
          }
        },
        "required": ["brand_name", "domain"]
      },
      "analysis_mode": {
        "type": "string",
        "enum": ["light", "deep"],
        "default": "deep"
      },
      "max_concurrent": { "type": "number", "default": 50 },
      "llm_model": { "type": "string", "default": "claude-haiku-3-5" }
    },
    "required": ["test_results", "brand_info"]
  }
}
```

---

### Implementation Guidance

#### File Structure

```
mcp-servers/marketing-tools/src/geo/
├── citation-analyzer.ts         # Main tool implementation
├── llm/
│   ├── claude-client.ts         # Anthropic API client
│   ├── prompt-builder.ts        # Build analysis prompts
│   └── response-parser.ts       # Parse LLM JSON responses
├── aggregators/
│   ├── brand-aggregator.ts      # Aggregate brand insights
│   ├── competitor-aggregator.ts # Aggregate competitor data
│   └── content-aggregator.ts    # Aggregate content performance
└── types.ts
```

#### Sample Implementation

```typescript
// citation-analyzer.ts

import pMap from 'p-map';
import { AnthropicClient } from './llm/claude-client';

export async function analyzeCitations(input: AnalyzeCitationsInput): Promise<CitationAnalysisResult> {
  // 1. Extract and deduplicate citations
  const allCitations = extractCitations(input.test_results);
  const uniqueCitations = deduplicateCitations(allCitations);

  console.log(`Analyzing ${uniqueCitations.length} unique citations...`);

  // 2. Analyze in parallel with LLM
  const analyses = await pMap(
    uniqueCitations,
    async (citation) => {
      const prompt = buildAnalysisPrompt(citation, input.brand_info, input.analysis_mode);

      try {
        const response = await llmClient.analyze(prompt, {
          model: input.llm_model || 'claude-haiku-3-5',
          max_tokens: input.analysis_mode === 'light' ? 500 : 1500
        });

        return parseLLMResponse(response, citation);
      } catch (error) {
        // Fallback to basic analysis
        return basicAnalysis(citation, input.brand_info);
      }
    },
    { concurrency: input.max_concurrent || 50 }
  );

  // 3. Aggregate results
  const summary = aggregateAnalyses(analyses, input.brand_info);

  return {
    citations: analyses,
    summary: summary,
    metadata: {
      total_citations: uniqueCitations.length,
      llm_powered: true,
      cost_estimate: calculateCost(uniqueCitations.length)
    }
  };
}
```

---

### Testing Requirements

#### Unit Tests

- [ ] Test citation extraction from test results
- [ ] Test deduplication logic
- [ ] Test prompt building
- [ ] Test LLM response parsing
- [ ] Test aggregation logic

#### Integration Tests

- [ ] Test with 50 real citations
- [ ] Verify LLM analysis quality
- [ ] Verify cost calculations
- [ ] Test fallback to basic analysis

#### Performance Tests

- [ ] Benchmark 900 citations
- [ ] Verify < 3 minutes completion
- [ ] Verify memory usage < 256MB
- [ ] Verify cost < $0.30

---

### Success Criteria

This tool is **complete and ready** when:

1. ✅ Can analyze 900 citations in < 3 minutes
2. ✅ Analysis accuracy > 90%
3. ✅ Cost per DEEP run < $0.30
4. ✅ Handles LLM failures gracefully
5. ✅ All aggregations calculated correctly
6. ✅ Integration tests pass
7. ✅ Works with marketing agent (end-to-end)

---

## Implementation Priority

### Phase 1: Tool #1 (Week 1)
Build `run_multi_engine_test` first:
- Most critical for core workflow
- Enables testing basic GEO analysis
- Can validate approach before tool #2

### Phase 2: Tool #2 (Week 2)
Build `analyze_citations` second:
- Depends on tool #1's output
- Enables DEEP mode analysis
- Completes the GEO workflow

### Phase 3: Testing & Optimization (Week 3)
- End-to-end integration tests
- Performance optimization
- Error handling refinement

---

## Acceptance Testing

**Test Scenario**: Run full DEEP GEO analysis for sample company

1. Agent loads skills
2. Executes company value identification (manual/built-in tools)
3. Generates 95 test prompts (manual/built-in tools)
4. **Calls Tool #1**: Executes 285 tests in < 90 seconds ✓
5. **Calls Tool #2**: Analyzes 900 citations in < 3 minutes ✓
6. Agent synthesizes strategy (manual/built-in tools)
7. Generates comprehensive report

**Success**: Complete DEEP analysis in < 20 minutes total

---

## Documentation Requirements

For each tool:
- [ ] README with usage examples
- [ ] API documentation
- [ ] Error code reference
- [ ] Cost estimation guide
- [ ] Troubleshooting guide

---

**Document Status**: ✅ Complete and Ready for Implementation
**Next Step**: Begin implementation of Tool #1 (`run_multi_engine_test`)
