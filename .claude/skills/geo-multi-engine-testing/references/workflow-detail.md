# GEO Multi-Engine Testing - Detailed Reference

This file contains detailed aggregation schemas, test result formats, fallback strategies, and extended examples referenced by the main SKILL.md.

## Test Result Object Schema

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

## Full Aggregation Schemas

### By Engine

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

### By Question Type

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

### By Funnel Stage

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

### Overall Summary

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

## Full Output File Schema

```json
{
  "metadata": {
    "mode": "DEEP",
    "company": "Acme Corp",
    "executed_at": "2024-01-15T11:15:00Z",
    "execution_time_seconds": 45,
    "api_scripts_used": true
  },
  "test_configuration": {
    "total_prompts": 100,
    "engines": ["chatgpt", "perplexity", "gemini"],
    "total_tests": 300,
    "concurrency": 50
  },
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
  "aggregations": {
    "by_engine": {},
    "by_question_family": {},
    "by_funnel_stage": {},
    "overall": {}
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

## Manual Fallback Strategy (No API Keys Available)

If API scripts cannot be used, fall back to WebSearch to simulate AI engine queries.

**Limitations**:
- Cannot directly query ChatGPT, Perplexity, Gemini APIs
- Results are approximations, not real AI engine responses
- Much slower (sequential, not parallel)
- Less accurate

**Fallback Steps**:

1. For each prompt:
   ```
   WebSearch: "[prompt text] site:perplexity.ai"
   or
   WebSearch: "[prompt text] chatgpt response"
   ```

2. Extract information from search results:
   - Look for blog posts comparing tools
   - Check industry review sites (G2, Capterra)
   - Search for "[topic] 2024" to get current sources

3. Manual citation extraction:
   - Parse top 10 search results
   - Look for brand mentions
   - Create synthetic "citation" data

**Fallback Timing**:
- LIGHT (20 prompts): 10-15 minutes
- DEEP (100 prompts): 40-60 minutes

## Citation Parser Details

### ChatGPT Citation Parsing
```
Look for [1], [2], [3] inline citations
Extract from response footer or inline references
```

### Perplexity Citation Parsing
```
Look for numbered citations at end
Format: "1. source.com - Title"
Extract URL, title, snippet
```

### Gemini Citation Parsing
```
Look for source attributions
Format varies - may be inline or at bottom
Extract URL and context
```

### Generic Citation Parser

```python
def extract_citations(response: str, engine: str) -> list:
    if engine == "chatgpt":
        return parse_chatgpt_citations(response)
    elif engine == "perplexity":
        return parse_perplexity_citations(response)
    elif engine == "gemini":
        return parse_gemini_citations(response)
    else:
        return []
```

## When to Use Each Approach

| Scenario | Approach | Why |
|----------|----------|-----|
| Quick test (10-20 prompts) | API Scripts Direct | Simple, fast, results fit in context |
| Deep analysis (50-100 prompts) | Programmatic | Massive token savings, enables scale |
| Real-time feedback needed | API Scripts Direct | See each response as it comes |
| Batch processing | Programmatic | Process hundreds efficiently |
| No API keys | Manual Fallback | WebSearch approximation |
