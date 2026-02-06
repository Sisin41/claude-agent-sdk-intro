---
name: geo-multi-engine-testing
description: Execute generated prompts across multiple AI engines (ChatGPT, Perplexity, Gemini) to measure brand visibility and extract citations. Use after geo-prompt-generation to run the actual AI engine tests.
metadata:
  author: castor
  version: "1.0"
  domain: geo
  execution-modes: light, deep
---

# GEO Multi-Engine Testing

## Purpose

Execute generated prompts across multiple AI engines (ChatGPT, Perplexity, Gemini) in parallel to measure brand visibility and extract citations.

## Prerequisites

**Required Input**: Generated prompts from `geo-prompt-generation` skill
**Input File**: `/data/geo/prompts-{company}-{mode}.json`

**Required Scripts**: API query scripts in `scripts/api/`:
- `scripts/api/query-chatgpt.sh` - Query ChatGPT API via curl
- `scripts/api/query-perplexity.sh` - Query Perplexity API via curl
- `scripts/api/query-gemini.sh` - Query Gemini API via curl

**Required Environment Variables**:
- `OPENAI_API_KEY` - For ChatGPT queries
- `PERPLEXITY_API_KEY` - For Perplexity queries
- `GOOGLE_API_KEY` - For Gemini queries

## Execution Modes

### LIGHT Mode (Standard Approach)
- **Prompts**: 10-20
- **Engines**: 2 (ChatGPT + Perplexity recommended)
- **Total Tests**: 20-40
- **Expected Time**: 30-60 seconds (with scripts) / 10-15 minutes (manual)
- **Token Usage**: ~8,000 tokens
- **Approach**: Use API scripts directly

### DEEP Mode (Programmatic Approach)
- **Prompts**: 50-100
- **Engines**: 3 (ChatGPT + Perplexity + Gemini)
- **Total Tests**: 150-300
- **Expected Time**: 2-5 minutes
- **Token Usage**: ~1,500 tokens (150x savings)
- **Approach**: Use programmatic tool calling (code execution)

## Workflow Steps

### Step 1: Load Prompts

```
Read: /data/geo/prompts-{company}-{mode}.json
Extract: prompts array
Validate: All prompts have required fields (prompt_id, text)
```

### Step 2: Configure Engines

**LIGHT Mode**:
```json
{
  "engines": [
    {"name": "chatgpt", "model": "gpt-4-turbo", "script": "scripts/api/query-chatgpt.sh"},
    {"name": "perplexity", "script": "scripts/api/query-perplexity.sh"}
  ]
}
```

**DEEP Mode**:
```json
{
  "engines": [
    {"name": "chatgpt", "model": "gpt-4-turbo", "script": "scripts/api/query-chatgpt.sh"},
    {"name": "perplexity", "script": "scripts/api/query-perplexity.sh"},
    {"name": "gemini", "model": "gemini-pro", "script": "scripts/api/query-gemini.sh"}
  ]
}
```

**API Key Check**: Verify all required API keys are set in environment. If missing, warn user and skip that engine. Cannot proceed if ALL engines are missing API keys.

### Step 3: Execute Tests via API Scripts

For each prompt, call the corresponding engine script:

```bash
# ChatGPT - returns plain text response
bash scripts/api/query-chatgpt.sh "What is the best customer support software?"

# Perplexity - returns JSON with {response, citations, web_results}
bash scripts/api/query-perplexity.sh "What is the best customer support software?"

# Gemini - returns JSON with {response, grounding_metadata, citations}
bash scripts/api/query-gemini.sh "What is the best customer support software?"
```

**Engine Response Formats**:
- **ChatGPT**: Returns string (search-enabled ChatGPT Plus, model: gpt-4o)
- **Perplexity**: Returns JSON with `{response, citations, web_results}` (model: sonar-pro)
- **Gemini**: Returns JSON with `{response, grounding_metadata, citations}` (model: gemini-2.0-flash-exp)

### Step 4: Programmatic Approach (DEEP Mode)

For large-scale testing (50+ prompts), use programmatic tool calling to run hundreds of queries efficiently, process responses in code (not in context), and return only aggregated insights.

```python
import json

test_prompts = [...]  # Load from prompts file
brand_name = "company.io"
competitors = ["zendesk", "intercom", "freshdesk"]

results = []

for prompt in test_prompts:
    # Call API scripts for each engine
    chatgpt_resp = run_script("scripts/api/query-chatgpt.sh", prompt)
    perplexity_resp = run_script("scripts/api/query-perplexity.sh", prompt)
    gemini_resp = run_script("scripts/api/query-gemini.sh", prompt)

    # Parse JSON responses
    perplexity_data = json.loads(perplexity_resp)
    gemini_data = json.loads(gemini_resp)

    # Extract text responses
    chatgpt_text = chatgpt_resp
    perplexity_text = perplexity_data["response"]
    gemini_text = gemini_data["response"]

    # Extract brand mentions IN CODE (not loaded into context)
    results.append({
        "prompt": prompt,
        "brand_cited": any([
            brand_name.lower() in chatgpt_text.lower(),
            brand_name.lower() in perplexity_text.lower(),
            brand_name.lower() in gemini_text.lower()
        ]),
        "engines_cited_in": [
            e for e, cited in [
                ("chatgpt", brand_name.lower() in chatgpt_text.lower()),
                ("perplexity", brand_name.lower() in perplexity_text.lower()),
                ("gemini", brand_name.lower() in gemini_text.lower())
            ] if cited
        ],
        "competitor_mentions": {
            "chatgpt": extract_competitors(chatgpt_text, competitors),
            "perplexity": extract_competitors(perplexity_text, competitors),
            "gemini": extract_competitors(gemini_text, competitors)
        },
        "citations": {
            "perplexity": perplexity_data.get("citations", []),
            "gemini": gemini_data.get("citations", [])
        }
    })

# Calculate visibility score
total_tests = len(results) * 3
brand_citations = sum(len(r["engines_cited_in"]) for r in results)
visibility_score = (brand_citations / total_tests) * 100

# Return ONLY aggregated insights
print(json.dumps({
    "visibility_score": round(visibility_score, 2),
    "total_prompts_tested": len(test_prompts),
    "brand_citations": brand_citations,
    "citation_breakdown": {
        "chatgpt": sum(1 for r in results if "chatgpt" in r["engines_cited_in"]),
        "perplexity": sum(1 for r in results if "perplexity" in r["engines_cited_in"]),
        "gemini": sum(1 for r in results if "gemini" in r["engines_cited_in"])
    },
    "top_competitor": find_most_mentioned_competitor(results),
    "citation_opportunities": identify_gaps(results)[:10]
}, indent=2))
```

### Helper Functions

```python
def extract_competitors(response: str, competitors: list) -> list:
    return [c for c in competitors if c.lower() in response.lower()]

def find_most_mentioned_competitor(results: list) -> str:
    from collections import Counter
    all_competitors = []
    for r in results:
        for engine_comps in r["competitor_mentions"].values():
            all_competitors.extend(engine_comps)
    if not all_competitors:
        return "None"
    return Counter(all_competitors).most_common(1)[0][0]

def identify_gaps(results: list) -> list:
    return [r["prompt"] for r in results if not r["brand_cited"]]
```

### Step 5: Brand Mention Detection

```python
def detect_brand_mention(response: str, brand_name: str, brand_domain: str) -> dict:
    brand_variations = [
        brand_name,
        brand_name.lower(),
        brand_domain.replace(".com", ""),
    ]
    for variation in brand_variations:
        if variation in response.lower():
            position = calculate_mention_position(response, variation)
            context = extract_mention_context(response, variation)
            return {"mentioned": True, "position": position, "context": context}
    return {"mentioned": False, "position": None, "context": None}
```

**Mention Position**: 1 = first paragraph, 2 = second paragraph, 3+ = later. Higher position = more prominent.

### Step 6: Citation Extraction

Per-engine citation parsing:
- **ChatGPT**: Look for [1], [2], [3] inline citations
- **Perplexity**: Numbered citations at end, format: "1. source.com - Title"
- **Gemini**: Source attributions, inline or at bottom

### Step 7: Results Aggregation

Aggregate results by engine, question type, funnel stage, and overall summary. See `references/workflow-detail.md` for full aggregation schemas.

### Step 8: Save Results

**Output File**: `/data/geo/test-results-{company}-{mode}.json`

```json
{
  "metadata": {
    "mode": "DEEP",
    "company": "Acme Corp",
    "executed_at": "ISO timestamp",
    "execution_time_seconds": 45,
    "api_scripts_used": true
  },
  "test_configuration": {
    "total_prompts": 100,
    "engines": ["chatgpt", "perplexity", "gemini"],
    "total_tests": 300,
    "concurrency": 50
  },
  "results": [],
  "aggregations": {
    "by_engine": {},
    "by_question_family": {},
    "by_funnel_stage": {},
    "overall": {}
  },
  "failures": []
}
```

## Token Savings (Programmatic vs Direct)

| Approach | Tokens | Savings |
|----------|--------|---------|
| Direct (150 responses in context) | ~80,000 | baseline |
| Programmatic (aggregated only) | ~1,500 | 98% reduction |

## Performance Benchmarks

| Mode | With API Scripts | Manual Fallback |
|------|-----------------|-----------------|
| LIGHT (40 tests) | 15-30 seconds | 10-15 minutes |
| DEEP (300 tests) | 30-90 seconds | 40-60 minutes |

## Error Handling

- **Rate Limiting (429)**: Exponential backoff (2s, 4s, 8s, 16s), retry up to 3 times
- **Invalid API Key (401)**: Log error, skip that engine, continue with others
- **Network Errors**: Retry immediately, if fails again mark as failed, continue
- **Malformed Responses**: Log for debugging, extract what data is possible, continue

## Validation Checks

1. **Completeness**: At least 90% of tests should succeed
2. **Citation Quality**: At least 50% of successful tests should have citations
3. **Timing**: DEEP mode should complete in < 2 minutes (with API scripts)
4. **Data Integrity**: All required fields present in results

## Agent Workflow

```
1. Load prompts from previous step
2. Determine execution approach:
   - LIGHT (10-20 prompts): Use API scripts directly
   - DEEP (50-100 prompts): Use programmatic approach
3. Use TodoWrite to track progress
4. Execute tests via scripts/api/ curl scripts
5. Save results to /data/geo/test-results-{company}-{mode}.json
6. Provide summary:
   "Tested 95 prompts across 3 engines (285 total tests)
    Brand mentioned: 48 times (16.8% visibility)
    ChatGPT: 12.6% | Perplexity: 29.5% | Gemini: 8.4%"
7. Pass data to next skill (geo-citation-analysis)
```

## Next Skill

Once complete, test results feed into:
**geo-citation-analysis** for deep analysis of why brand was/wasn't cited
