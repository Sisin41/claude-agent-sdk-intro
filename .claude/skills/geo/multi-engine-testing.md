# GEO Multi-Engine Testing

## Purpose
Execute generated prompts across multiple AI engines (ChatGPT, Perplexity, Gemini) in parallel to measure brand visibility and extract citations.

---

## Prerequisites
**Required Input**: Generated prompts from `prompt-generation.md`
**Input File**: `/data/geo/prompts-{company}-{mode}.json`

**Required MCP Tool**: `mcp__MarketingTools__run_multi_engine_test`
(If unavailable, use manual fallback with WebSearch)

---

## Execution Modes

### LIGHT Mode
**Prompts**: 10-20
**Engines**: 2 (ChatGPT + Perplexity recommended)
**Total Tests**: 20-40
**Expected Time**: 30-60 seconds (with MCP) / 10-15 minutes (manual)

### DEEP Mode
**Prompts**: 80-100
**Engines**: 3 (ChatGPT + Perplexity + Gemini)
**Total Tests**: 240-300
**Expected Time**: 30-90 seconds (with MCP) / 40-60 minutes (manual)

---

## MCP Tool Specification

### Tool: `run_multi_engine_test`

**Purpose**: Execute prompts across multiple AI engines in parallel

**Input Schema**:
```typescript
interface RunMultiEngineTestInput {
  prompts: PromptTest[];
  engines: EngineConfig[];
  max_concurrent?: number;  // Default: 50
  retry_failed?: boolean;   // Default: true
  timeout_ms?: number;      // Default: 10000 (10 seconds)
}

interface PromptTest {
  prompt_id: string;
  text: string;
  metadata?: {
    question_family?: string;
    user_type?: string;
    funnel_stage?: string;
    expected_visibility?: string;
  };
}

interface EngineConfig {
  name: 'chatgpt' | 'perplexity' | 'gemini';
  model?: string;  // Optional specific model
  api_key?: string;  // Usually from env vars
}
```

**Output Schema**:
```typescript
interface TestResult {
  prompt_id: string;
  engine: string;
  success: boolean;
  response: string | null;
  citations: Citation[];
  brand_mentioned: boolean;
  brand_position?: number;  // Position if mentioned (1st, 2nd, etc.)
  timestamp: string;
  latency_ms: number;
  error?: string;
}

interface Citation {
  position: number;  // Order in response (1, 2, 3...)
  url: string;
  title: string;
  snippet: string;
  context: string;  // How it was cited in response
}
```

**Expected Behavior**:
1. Takes list of prompts + list of engines
2. Creates all combinations (prompts × engines)
3. Executes in parallel with configurable concurrency (default 50)
4. Handles rate limits gracefully (exponential backoff)
5. Retries failed requests (up to 3 times)
6. Extracts citations from each response
7. Detects brand mentions
8. Returns structured results array

**Performance Requirements**:
- 300 tests should complete in < 90 seconds
- Must handle rate limiting without crashing
- Must work with different API keys per engine

---

## Workflow Steps

### Step 1: Load Prompts

```
Read: /data/geo/prompts-{company}-{mode}.json
Extract: prompts array
Validate: All prompts have required fields (prompt_id, text)
```

---

### Step 2: Configure Engines

**LIGHT Mode**:
```json
{
  "engines": [
    {
      "name": "chatgpt",
      "model": "gpt-4-turbo",
      "api_key": "${OPENAI_API_KEY}"
    },
    {
      "name": "perplexity",
      "api_key": "${PERPLEXITY_API_KEY}"
    }
  ]
}
```

**DEEP Mode**:
```json
{
  "engines": [
    {
      "name": "chatgpt",
      "model": "gpt-4-turbo",
      "api_key": "${OPENAI_API_KEY}"
    },
    {
      "name": "perplexity",
      "api_key": "${PERPLEXITY_API_KEY}"
    },
    {
      "name": "gemini",
      "model": "gemini-pro",
      "api_key": "${GOOGLE_API_KEY}"
    }
  ]
}
```

**API Key Check**:
- Verify all required API keys are set in environment
- If missing, warn user and skip that engine
- Cannot proceed if ALL engines are missing API keys

---

### Step 3: Execute Tests (MCP Tool Available)

**Using MCP Tool** (Preferred):

```python
# Pseudo-code for agent
results = await mcp__MarketingTools__run_multi_engine_test({
    "prompts": loaded_prompts,
    "engines": configured_engines,
    "max_concurrent": 50,
    "retry_failed": true,
    "timeout_ms": 10000
})
```

**Progress Tracking**:
```
Show real-time progress:
[████████████████░░░░] 70% (210/300)

By engine:
ChatGPT:    [████████████████████] 100/100 ✓ (42s)
Perplexity: [████████████████████] 100/100 ✓ (38s)
Gemini:     [██████░░░░░░░░░░░░░░] 10/100 ⏳ (in progress)
```

**Expected Output**:
```json
{
  "results": [
    {
      "prompt_id": "prompt_001",
      "engine": "chatgpt",
      "success": true,
      "response": "The best AI customer support tools for SaaS companies include...",
      "citations": [
        {
          "position": 1,
          "url": "https://zendesk.com/ai-support",
          "title": "Zendesk AI Features",
          "snippet": "AI-powered automation...",
          "context": "Mentioned as leading solution"
        },
        {
          "position": 2,
          "url": "https://acmecorp.com/features",
          "title": "Acme AI Support Platform",
          "snippet": "Reduce ticket volume by 60%",
          "context": "Cited for efficiency gains"
        }
      ],
      "brand_mentioned": true,
      "brand_position": 2,
      "timestamp": "2024-01-15T11:15:23Z",
      "latency_ms": 2834
    }
  ],
  "summary": {
    "total_tests": 300,
    "successful": 295,
    "failed": 5,
    "average_latency_ms": 2650,
    "total_time_seconds": 45,
    "brand_mentions": {
      "chatgpt": 12,
      "perplexity": 28,
      "gemini": 8,
      "total": 48
    }
  }
}
```

**Error Handling**:
- If rate limited: Exponential backoff, retry
- If API key invalid: Skip that engine, log error
- If timeout: Mark as failed, continue with others
- If network error: Retry up to 3 times

**Time**: 30-90 seconds for 300 tests (DEEP mode)

---

### Step 4: Execute Tests (MCP Tool NOT Available - Manual Fallback)

**Fallback Strategy**: Use WebSearch to simulate AI engine queries

**⚠️ Limitations**:
- Cannot directly query ChatGPT, Perplexity, Gemini APIs
- Can only search web for "what would AI say about this?"
- Results are approximations, not real AI engine responses
- Much slower (sequential, not parallel)
- Less accurate

**Fallback Steps**:

1. **For each prompt**:
   ```
   WebSearch: "[prompt text] site:perplexity.ai"
   or
   WebSearch: "[prompt text] chatgpt response"
   ```

2. **Extract information from search results**:
   - Look for blog posts comparing tools
   - Check industry review sites (G2, Capterra)
   - Search for "[topic] 2024" to get current sources

3. **Manual citation extraction**:
   - Parse top 10 search results
   - Look for brand mentions
   - Create synthetic "citation" data

**Example Manual Execution**:
```
For prompt: "Best AI customer support tools for SaaS"

1. WebSearch: "Best AI customer support tools for SaaS 2024"
2. WebFetch top 5 results:
   - g2.com/categories/ai-customer-support
   - capterra.com/customer-service-software
   - blog.hubspot.com/best-support-tools
3. Parse each page for brand mentions
4. Rank brands by mention frequency
5. Create test result entry
```

**Fallback Output** (simplified):
```json
{
  "results": [
    {
      "prompt_id": "prompt_001",
      "engine": "web_search_proxy",
      "success": true,
      "response": "[Approximated from search results]",
      "citations": [
        {
          "position": 1,
          "url": "https://g2.com/categories/ai-support",
          "title": "Top AI Support Tools - G2",
          "snippet": "...",
          "context": "Mentioned in category listing"
        }
      ],
      "brand_mentioned": false,
      "timestamp": "2024-01-15T11:15:23Z",
      "latency_ms": 5000,
      "note": "Fallback method - web search proxy, not real AI engine"
    }
  ]
}
```

**Time**: 10-15 minutes for LIGHT (20 prompts) / 40-60 minutes for DEEP (100 prompts)

**⚠️ Recommendation**: Strongly recommend building MCP tool for production use

---

### Step 5: Brand Mention Detection

**Logic for detecting if brand is mentioned**:

```python
def detect_brand_mention(response: str, brand_name: str, brand_domain: str) -> dict:
    """
    Detect if brand is mentioned in AI response

    Returns:
    {
        "mentioned": bool,
        "position": int or None,  # 1st, 2nd, 3rd mention
        "context": str  # How it was mentioned
    }
    """
    brand_variations = [
        brand_name,
        brand_name.lower(),
        brand_domain.replace(".com", ""),
        # Add common variations
    ]

    for variation in brand_variations:
        if variation in response.lower():
            # Find position (how early in response)
            position = calculate_mention_position(response, variation)
            context = extract_mention_context(response, variation)
            return {
                "mentioned": True,
                "position": position,
                "context": context
            }

    return {"mentioned": False, "position": None, "context": None}
```

**Mention Position Calculation**:
- 1 = Mentioned in first paragraph/section
- 2 = Mentioned in second paragraph/section
- 3+ = Mentioned later
- Higher position = more prominent

---

### Step 6: Citation Extraction

**Per Engine Citation Format**:

**ChatGPT**:
```
Look for [1], [2], [3] inline citations
Extract from response footer or inline references
```

**Perplexity**:
```
Look for numbered citations at end
Format: "1. source.com - Title"
Extract URL, title, snippet
```

**Gemini**:
```
Look for source attributions
Format varies - may be inline or at bottom
Extract URL and context
```

**Generic Citation Parser**:
```python
def extract_citations(response: str, engine: str) -> list[Citation]:
    """
    Extract citations from AI engine response
    Engine-specific parsing logic
    """
    if engine == "chatgpt":
        return parse_chatgpt_citations(response)
    elif engine == "perplexity":
        return parse_perplexity_citations(response)
    elif engine == "gemini":
        return parse_gemini_citations(response)
    else:
        return []
```

---

### Step 7: Results Aggregation

**Aggregate results by**:

1. **By Engine**:
```json
{
  "by_engine": {
    "chatgpt": {
      "total_tests": 100,
      "brand_mentions": 12,
      "visibility_rate": "12.0%",
      "avg_latency_ms": 2834,
      "success_rate": "98%"
    },
    "perplexity": {
      "total_tests": 100,
      "brand_mentions": 28,
      "visibility_rate": "28.0%",
      "avg_latency_ms": 2456,
      "success_rate": "100%"
    },
    "gemini": {
      "total_tests": 100,
      "brand_mentions": 8,
      "visibility_rate": "8.0%",
      "avg_latency_ms": 3102,
      "success_rate": "95%"
    }
  }
}
```

2. **By Question Type**:
```json
{
  "by_question_family": {
    "comparison": {
      "total_tests": 75,
      "brand_mentions": 22,
      "visibility_rate": "29.3%"
    },
    "problem-solution": {
      "total_tests": 60,
      "brand_mentions": 3,
      "visibility_rate": "5.0%"
    }
  }
}
```

3. **By Funnel Stage**:
```json
{
  "by_funnel_stage": {
    "awareness": {
      "total_tests": 95,
      "brand_mentions": 9,
      "visibility_rate": "9.5%"
    },
    "decision": {
      "total_tests": 71,
      "brand_mentions": 18,
      "visibility_rate": "25.4%"
    }
  }
}
```

4. **Overall Summary**:
```json
{
  "overall": {
    "total_tests": 300,
    "successful_tests": 295,
    "failed_tests": 5,
    "total_brand_mentions": 48,
    "overall_visibility_rate": "16.8%",
    "total_citations_extracted": 847,
    "total_time_seconds": 45,
    "average_latency_ms": 2797
  }
}
```

---

### Step 8: Save Results

**Output File**: `/data/geo/test-results-{company}-{mode}.json`

```json
{
  "metadata": {
    "mode": "DEEP",
    "company": "Acme Corp",
    "executed_at": "2024-01-15T11:15:00Z",
    "execution_time_seconds": 45,
    "mcp_tool_used": true
  },
  "test_configuration": {
    "total_prompts": 100,
    "engines": ["chatgpt", "perplexity", "gemini"],
    "total_tests": 300,
    "concurrency": 50
  },
  "results": [
    { ... },  // 300 test result objects
  ],
  "aggregations": {
    "by_engine": { ... },
    "by_question_family": { ... },
    "by_funnel_stage": { ... },
    "overall": { ... }
  },
  "failures": [
    {
      "prompt_id": "prompt_045",
      "engine": "gemini",
      "error": "Rate limit exceeded",
      "retry_count": 3
    }
  ]
}
```

---

## Performance Benchmarks

### With MCP Tool (Parallel Execution)
```
LIGHT Mode (20 prompts × 2 engines = 40 tests):
- Time: 15-30 seconds
- Throughput: ~2 tests/second

DEEP Mode (100 prompts × 3 engines = 300 tests):
- Time: 30-90 seconds
- Throughput: ~3-10 tests/second

Bottleneck: API rate limits, not our system
```

### Without MCP Tool (Manual Fallback)
```
LIGHT Mode (20 prompts):
- Time: 10-15 minutes
- Throughput: ~2 tests/minute

DEEP Mode (100 prompts):
- Time: 40-60 minutes
- Throughput: ~2 tests/minute

Bottleneck: Sequential WebSearch calls
```

**Speedup with MCP Tool**: **15-20x faster**

---

## Error Handling & Edge Cases

**Rate Limiting**:
```
If 429 error:
- Exponential backoff (2s, 4s, 8s, 16s)
- Retry up to 3 times
- If still fails, mark as failed and continue
```

**Invalid API Key**:
```
If 401 error:
- Log clear error message
- Skip that engine entirely
- Continue with other engines
- Warn user in final report
```

**Network Errors**:
```
If connection timeout or network error:
- Retry immediately (network may be flaky)
- If fails again, mark as failed
- Continue with other tests
```

**Malformed Responses**:
```
If response doesn't parse correctly:
- Log response for debugging
- Extract what data is possible
- Mark citations as "unable to parse"
- Continue with test
```

---

## Validation Checks

Before saving results:

1. **Completeness**: At least 90% of tests should succeed
2. **Citation Quality**: At least 50% of successful tests should have citations
3. **Timing**: DEEP mode should complete in < 2 minutes (with MCP tool)
4. **Data Integrity**: All required fields present in results

If validation fails, log warnings but still save results

---

## Usage Example

**Agent Workflow**:
```
1. Read this skill file
2. Load prompts from previous step
3. Check if MCP tool available:
   - If yes: Use parallel execution (fast!)
   - If no: Warn user, use fallback (slow)
4. Configure engines (check API keys)
5. Execute tests with progress tracking
6. Aggregate results by dimensions
7. Validate output
8. Save JSON to /data/geo/
9. Show summary to user:
   "✅ Tested 300 prompts across 3 engines in 45 seconds
    Brand mentioned 48 times (16.8% visibility)
    Top engine: Perplexity (28.0%)
    Full results: /data/geo/test-results-acme-deep.json"
10. Pass data to next skill (citation-analysis.md)
```

---

## Next Skill
Once complete, test results feed into:
→ **`citation-analysis.md`** for deep LLM-powered analysis

---

## MCP Tools Required

### **CRITICAL**: `mcp__MarketingTools__run_multi_engine_test`

**Priority**: **P0 - Must Have**

**Rationale**:
- Makes 3-4 day manual process into 15-minute automated workflow
- 15-20x performance improvement
- Core value proposition of the system
- Without this, DEEP mode is impractical

**Implementation Requirements**:
- Support ChatGPT, Perplexity, Gemini APIs
- Parallel execution with configurable concurrency
- Intelligent rate limit handling
- Citation extraction per engine
- Brand mention detection

**See**: `/mcp-servers/marketing-tools/src/geo/multi-engine-runner.ts` (to be built)

---

## Future Enhancements

**Additional Engines**:
- Claude (Anthropic)
- Bing Chat
- Bard (if API becomes available)

**Advanced Features**:
- A/B testing (run same prompt with different phrasing)
- Temporal tracking (run same tests weekly, track changes)
- Competitive benchmarking (how do competitors rank?)
