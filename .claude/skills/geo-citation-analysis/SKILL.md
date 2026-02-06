---
name: geo-citation-analysis
description: Analyze all citations from multi-engine test results to extract insights about brand mentions, competitor visibility, content quality, and citation gaps. Use after geo-multi-engine-testing to understand why the brand is or is not being cited.
metadata:
  author: castor
  version: "1.0"
  domain: geo
  execution-modes: light, deep
---

# GEO Citation Analysis

## Purpose

Analyze all citations from multi-engine test results using pattern matching (LIGHT) or LLM-powered parallel analysis (DEEP) to extract insights about brand mentions, competitor visibility, and content quality.

## Prerequisites

**Required Input**: Test results from `geo-multi-engine-testing` skill
**Input File**: `/data/geo/test-results-{company}-{mode}.json`

## Execution Modes

### LIGHT Mode
- **Input**: ~40 test results with ~120 citations
- **Analysis Depth**: Basic counting and categorization
- **LLM Analysis**: None (pattern matching only)
- **Expected Time**: 30-60 seconds

### DEEP Mode
- **Input**: ~300 test results with ~900 citations
- **Analysis Depth**: Comprehensive programmatic or LLM-powered analysis
- **Expected Time**: 2-3 minutes (programmatic) / 30-45 minutes (manual)

## Workflow Steps

### Step 1: Load and Prepare Data

```
Read: /data/geo/test-results-{company}-{mode}.json
Extract: All test results with citations
Count: Total citations
Deduplicate: Same URL may appear in multiple test results
```

**Citation Extraction**:
```python
all_citations = []
for result in test_results:
    for citation in result.citations:
        citation_with_context = {
            **citation,
            "source_prompt": result.prompt_id,
            "source_engine": result.engine,
            "brand_mentioned_in_result": result.brand_mentioned
        }
        all_citations.append(citation_with_context)

unique_citations = deduplicate_by_url(all_citations)
```

**Expected Counts**:
- LIGHT: ~120 total citations, ~80 unique URLs
- DEEP: ~900 total citations, ~600 unique URLs

### Step 2: LIGHT Mode Analysis (Pattern Matching)

No LLM calls -- just pattern matching and counting.

**For each citation**:

1. **Brand Mention Detection**:
   ```python
   brand_mentioned = brand_name.lower() in citation.snippet.lower()
   ```

2. **Sentiment (Basic)**:
   ```python
   positive_words = ["best", "top", "leading", "excellent", "recommended"]
   negative_words = ["worst", "avoid", "poor", "issues", "problems"]

   if any(word in citation.snippet.lower() for word in positive_words):
       sentiment = "positive"
   elif any(word in citation.snippet.lower() for word in negative_words):
       sentiment = "negative"
   else:
       sentiment = "neutral"
   ```

3. **Competitor Detection**:
   ```python
   competitors_mentioned = [c for c in known_competitors if c.lower() in citation.snippet.lower()]
   ```

4. **Citation Type**:
   ```python
   if "g2.com" in citation.url or "capterra.com" in citation.url:
       content_type = "review"
   elif "/blog/" in citation.url:
       content_type = "blog"
   elif "/features" in citation.url or "/product" in citation.url:
       content_type = "product_page"
   else:
       content_type = "other"
   ```

**LIGHT Output**:
```json
{
  "citations": [
    {
      "citation_id": "cit_001",
      "url": "https://acmecorp.com/blog/reduce-tickets",
      "title": "How to Reduce Ticket Volume by 60%",
      "brand_mentioned": true,
      "sentiment": "positive",
      "competitors_mentioned": ["Zendesk"],
      "content_type": "blog",
      "times_cited": 12
    }
  ],
  "summary": {
    "total_unique_citations": 80,
    "brand_citations": 15,
    "competitor_citations": {
      "Zendesk": 28,
      "Intercom": 19,
      "Freshdesk": 12
    }
  }
}
```

### Step 3: DEEP Mode Analysis (Programmatic Approach -- Recommended)

For large-scale citation analysis (150+ citations), use programmatic Python code execution for maximum token efficiency.

**Token Efficiency**:
- Direct approach: 600 citations x 75 tokens = 45,000 tokens
- Programmatic: Aggregated insights only = ~800 tokens
- Savings: 96% token reduction

```python
import json
from collections import Counter, defaultdict
from urllib.parse import urlparse

# Load test results
test_results = [...]  # From /data/geo/test-results-{company}-deep.json
brand_name = "Acme Corp"
brand_domain = "acmecorp.com"
competitors = ["Zendesk", "Intercom", "Freshdesk"]

# Extract and deduplicate citations
all_citations = []
citation_contexts = defaultdict(list)

for result in test_results:
    for citation in result.get('citations', []):
        url = citation['url']
        all_citations.append({
            'url': url,
            'title': citation.get('title', ''),
            'snippet': citation.get('snippet', ''),
            'engine': result['engine'],
            'prompt_id': result['prompt_id'],
        })
        citation_contexts[url].append({
            'engine': result['engine'],
            'prompt_id': result['prompt_id'],
            'brand_mentioned_in_response': result.get('brand_mentioned', False)
        })

unique_urls = list(set(c['url'] for c in all_citations))

# Analyze each unique citation
analyzed_citations = []
for url in unique_urls:
    url_citations = [c for c in all_citations if c['url'] == url]
    first_citation = url_citations[0]
    domain = urlparse(url).netloc

    brand_mentioned = (
        brand_domain.lower() in url.lower() or
        brand_name.lower() in first_citation['snippet'].lower()
    )

    competitors_mentioned = [c for c in competitors
        if c.lower() in url.lower() or c.lower() in first_citation['snippet'].lower()]

    # Content type detection
    if any(d in url for d in ['g2.com', 'capterra.com', 'trustpilot.com']):
        content_type = 'review'
    elif '/blog/' in url or '/article/' in url:
        content_type = 'blog'
    elif '/product' in url or '/features' in url:
        content_type = 'product_page'
    elif '/docs/' in url:
        content_type = 'documentation'
    elif '/case-stud' in url or '/customer' in url:
        content_type = 'case_study'
    elif '/vs/' in url or 'comparison' in url:
        content_type = 'comparison'
    else:
        content_type = 'other'

    # Basic sentiment
    snippet_lower = first_citation['snippet'].lower()
    positive_words = ['best', 'top', 'leading', 'excellent', 'recommended']
    negative_words = ['worst', 'avoid', 'poor', 'issues', 'problems']
    pos = sum(1 for w in positive_words if w in snippet_lower)
    neg = sum(1 for w in negative_words if w in snippet_lower)
    sentiment = 'positive' if pos > neg else ('negative' if neg > pos else 'neutral')

    analyzed_citations.append({
        'url': url, 'domain': domain, 'title': first_citation['title'],
        'brand_mentioned': brand_mentioned, 'sentiment': sentiment,
        'competitors_mentioned': competitors_mentioned,
        'content_type': content_type,
        'times_cited': len(url_citations),
        'engines_cited_by': list(set(c['engine'] for c in url_citations)),
    })

# Aggregate insights (return only summary, not raw data)
```

See `references/workflow-detail.md` for the full aggregation code and output schema.

### Step 4: Aggregate Insights

Generate the following aggregate views:

**Top Performing Content**: Ranked by citation count, with engines citing and sentiment.

**Citation Gaps**: URLs where competitors are cited but brand is not -- sorted by times_cited as high-value opportunities.

**Competitor Analysis**: Visibility comparison showing total mentions, visibility rate, average position, and sentiment for each competitor vs the brand.

**Content Quality Assessment**: Breakdown by content type (blog, product page, review, case study) with insights on what performs best.

### Step 5: Save Results

**Output File**: `/data/geo/citation-analysis-{company}-{mode}.json`

```json
{
  "metadata": {
    "mode": "DEEP",
    "total_citations_analyzed": 847,
    "unique_urls": 600,
    "analysis_approach": "programmatic",
    "analysis_time_seconds": 138,
    "generated_at": "ISO timestamp"
  },
  "brand_performance": {
    "total_brand_citations": 48,
    "visibility_rate": "16.8%",
    "sentiment_breakdown": {},
    "top_cited_content": [],
    "content_quality_assessment": {}
  },
  "competitive_analysis": {
    "competitors": [],
    "visibility_comparison": {},
    "competitive_gaps": []
  },
  "citation_gaps": [],
  "detailed_citations": [],
  "recommendations": {
    "content_creation": [],
    "content_optimization": [],
    "competitive_positioning": []
  }
}
```

## When to Use Each Approach

| Scenario | Citations | Approach | Why |
|----------|-----------|----------|-----|
| Quick test (10-20 prompts) | 30-60 | LIGHT (pattern matching) | Fast, simple, no LLM needed |
| Medium test (30-40 prompts) | 90-120 | LLM Direct | LLM insights useful, fits in context |
| Deep analysis (50-100 prompts) | 150-300 | Programmatic | Massive token savings |
| Custom analysis needs | Any | Programmatic | Full control over analysis logic |

## Error Handling

**LLM Failures** (if using LLM approach):
- Retry once with exponential backoff
- If still fails, use basic pattern matching fallback
- Log error, continue with other citations
- Flag in output: `"partial_analysis": true`

**Malformed Responses**:
- Attempt to extract key fields with regex
- If extraction fails, mark as "analysis_failed"
- Continue with other citations

**Rate Limiting**:
- Reduce concurrency from 50 to 25
- Add slight delay between batches
- Retry failed batch

## Validation Checks

1. **Coverage**: At least 95% of citations analyzed successfully
2. **Data Quality**: All required fields present in analysis objects
3. **Sentiment Distribution**: Sentiment values are valid (positive/neutral/negative)
4. **Score Ranges**: Relevance and authority scores are 0-100

## Agent Workflow

```
1. Load test results from previous step
2. Determine mode (LIGHT or DEEP)
3. Extract and deduplicate citations
4. For LIGHT mode: Run basic pattern matching
   For DEEP mode: Use programmatic approach (recommended)
5. Use TodoWrite to track progress
6. Save analysis to /data/geo/citation-analysis-{company}-{mode}.json
7. Provide summary:
   "Analyzed 600 unique citations
    Brand cited: 48 times (8% of citations)
    Top competitor: Zendesk (89 citations)
    Top performing content: /blog/reduce-ticket-volume (12 citations)
    Key insight: Competitors dominate problem-solution queries
    Recommendation: Create 'How to reduce...' content series"
8. Pass data to next skill (geo-strategy-synthesis)
```

## Next Skill

Once complete, citation analysis feeds into:
**geo-strategy-synthesis** to create actionable recommendations
