# GEO Citation Analysis - Detailed Reference

This file contains the full programmatic analysis code, LLM prompt templates, extended output schemas, and aggregation logic referenced by the main SKILL.md.

## Full Programmatic Analysis Code

```python
import json
from collections import Counter, defaultdict
from urllib.parse import urlparse

# Load test results from multi-engine testing
test_results = [...]  # From /data/geo/test-results-{company}-deep.json

brand_name = "Acme Corp"
brand_domain = "acmecorp.com"
competitors = ["Zendesk", "Intercom", "Freshdesk"]

# ============================================================================
# STEP 1: Extract and Deduplicate Citations
# ============================================================================

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
            'response_context': result['response'][:300]
        })

        citation_contexts[url].append({
            'engine': result['engine'],
            'prompt_id': result['prompt_id'],
            'brand_mentioned_in_response': result.get('brand_mentioned', False)
        })

unique_urls = list(set(c['url'] for c in all_citations))
print(f"Total citations: {len(all_citations)}")
print(f"Unique URLs: {len(unique_urls)}")

# ============================================================================
# STEP 2: Analyze Citations Programmatically
# ============================================================================

analyzed_citations = []

for url in unique_urls:
    url_citations = [c for c in all_citations if c['url'] == url]
    first_citation = url_citations[0]
    domain = urlparse(url).netloc

    brand_mentioned = (
        brand_domain.lower() in url.lower() or
        brand_name.lower() in first_citation['snippet'].lower()
    )

    competitors_mentioned = []
    for competitor in competitors:
        if competitor.lower() in url.lower() or competitor.lower() in first_citation['snippet'].lower():
            competitors_mentioned.append(competitor)

    # Content type from URL patterns
    if any(domain in url for domain in ['g2.com', 'capterra.com', 'trustpilot.com']):
        content_type = 'review'
    elif '/blog/' in url or '/article/' in url:
        content_type = 'blog'
    elif '/product' in url or '/features' in url or '/pricing' in url:
        content_type = 'product_page'
    elif '/docs/' in url or '/documentation/' in url:
        content_type = 'documentation'
    elif '/case-stud' in url or '/customer' in url:
        content_type = 'case_study'
    elif '/vs/' in url or 'comparison' in url:
        content_type = 'comparison'
    else:
        content_type = 'other'

    # Basic sentiment analysis
    snippet_lower = first_citation['snippet'].lower()
    positive_words = ['best', 'top', 'leading', 'excellent', 'recommended', 'great', 'superior', 'outstanding']
    negative_words = ['worst', 'avoid', 'poor', 'issues', 'problems', 'terrible', 'disappointing']

    positive_count = sum(1 for word in positive_words if word in snippet_lower)
    negative_count = sum(1 for word in negative_words if word in snippet_lower)

    if positive_count > negative_count:
        sentiment = 'positive'
    elif negative_count > positive_count:
        sentiment = 'negative'
    else:
        sentiment = 'neutral'

    times_cited = len(url_citations)
    engines_cited_by = list(set(c['engine'] for c in url_citations))

    contexts = citation_contexts[url]
    brand_mentioned_in_contexts = sum(1 for ctx in contexts if ctx.get('brand_mentioned_in_response', False))

    analyzed_citations.append({
        'url': url,
        'domain': domain,
        'title': first_citation['title'],
        'brand_mentioned': brand_mentioned,
        'sentiment': sentiment,
        'competitors_mentioned': competitors_mentioned,
        'content_type': content_type,
        'times_cited': times_cited,
        'engines_cited_by': engines_cited_by,
        'brand_mentioned_in_contexts': brand_mentioned_in_contexts
    })

# ============================================================================
# STEP 3: Aggregate Insights
# ============================================================================

brand_citations = [c for c in analyzed_citations if c['brand_mentioned']]

competitor_citation_counts = defaultdict(int)
for c in analyzed_citations:
    for comp in c['competitors_mentioned']:
        competitor_citation_counts[comp] += 1

content_type_counts = Counter(c['content_type'] for c in analyzed_citations)
sentiment_counts = Counter(c['sentiment'] for c in brand_citations)
domain_citation_counts = Counter(c['domain'] for c in analyzed_citations)
top_domains = domain_citation_counts.most_common(20)

top_brand_content = sorted(
    brand_citations,
    key=lambda x: x['times_cited'],
    reverse=True
)[:10]

engine_coverage = defaultdict(int)
for c in analyzed_citations:
    for engine in c['engines_cited_by']:
        engine_coverage[engine] += 1

# Citation gaps (competitors cited but we are not)
citation_gaps = []
for c in analyzed_citations:
    if c['competitors_mentioned'] and not c['brand_mentioned']:
        citation_gaps.append({
            'url': c['url'],
            'domain': c['domain'],
            'competitors': c['competitors_mentioned'],
            'times_cited': c['times_cited'],
            'content_type': c['content_type']
        })

citation_gaps = sorted(citation_gaps, key=lambda x: x['times_cited'], reverse=True)[:20]

# ============================================================================
# STEP 4: Return ONLY Aggregated Insights
# ============================================================================

result = {
    "analysis_summary": {
        "total_citations": len(all_citations),
        "unique_urls": len(unique_urls),
        "brand_citations": len(brand_citations),
        "brand_citation_rate": f"{(len(brand_citations) / len(unique_urls) * 100):.1f}%"
    },

    "competitor_analysis": {
        comp: {
            "citation_count": count,
            "vs_our_brand": f"+{count - len(brand_citations)}" if count > len(brand_citations) else f"{count - len(brand_citations)}"
        }
        for comp, count in sorted(competitor_citation_counts.items(), key=lambda x: x[1], reverse=True)
    },

    "content_type_breakdown": dict(content_type_counts),

    "sentiment_analysis": {
        "positive": sentiment_counts.get('positive', 0),
        "neutral": sentiment_counts.get('neutral', 0),
        "negative": sentiment_counts.get('negative', 0),
        "positive_rate": f"{(sentiment_counts.get('positive', 0) / len(brand_citations) * 100):.1f}%" if brand_citations else "0%"
    },

    "top_cited_domains": [
        {"domain": domain, "citations": count}
        for domain, count in top_domains
    ],

    "top_performing_content": [
        {
            "url": c['url'],
            "domain": c['domain'],
            "times_cited": c['times_cited'],
            "engines": c['engines_cited_by'],
            "sentiment": c['sentiment']
        }
        for c in top_brand_content
    ],

    "engine_coverage": dict(engine_coverage),

    "citation_gaps": [
        {
            "url": gap['url'],
            "domain": gap['domain'],
            "competitors_mentioned": gap['competitors'],
            "times_cited": gap['times_cited'],
            "content_type": gap['content_type'],
            "opportunity": f"High-value opportunity: cited {gap['times_cited']}x mentioning {', '.join(gap['competitors'])} but not us"
        }
        for gap in citation_gaps
    ],

    "key_insights": [
        f"Brand cited in {len(brand_citations)} of {len(unique_urls)} unique URLs ({(len(brand_citations) / len(unique_urls) * 100):.1f}%)",
        f"Top competitor: {max(competitor_citation_counts.items(), key=lambda x: x[1])[0]} with {max(competitor_citation_counts.items(), key=lambda x: x[1])[1]} citations" if competitor_citation_counts else "No competitor citations found",
        f"Sentiment when mentioned: {sentiment_counts.get('positive', 0)} positive, {sentiment_counts.get('neutral', 0)} neutral, {sentiment_counts.get('negative', 0)} negative",
        f"Top performing content type: {content_type_counts.most_common(1)[0][0]} ({content_type_counts.most_common(1)[0][1]} citations)",
        f"Found {len(citation_gaps)} high-value citation opportunities (competitors mentioned but we are not)"
    ]
}

print(json.dumps(result, indent=2))
```

## LLM-Powered Analysis (Alternative to Programmatic)

For cases where deeper semantic analysis is needed, use LLM calls per citation.

### LLM Prompt Template (per citation)

```
Analyze this citation from an AI engine response:

**Citation Info:**
URL: {citation.url}
Title: {citation.title}
Snippet: {citation.snippet}
Context in response: {citation.context}

**Brand Info:**
Our brand: {brand_name}
Domain: {brand_domain}
Competitors: {competitors}

**Analysis Required:**

1. **Relevance Score** (0-100): How relevant is this citation to the query?
2. **Sentiment** (positive/neutral/negative): How is our brand portrayed?
3. **Brand Context**: How is our brand mentioned (if at all)?
4. **Competitor Mentions**: Which competitors are mentioned?
5. **Key Points**: 2-3 key takeaways from this citation
6. **Authority Score** (0-100): How authoritative is this source?
7. **Content Type**: blog, product_page, review, news, documentation, case_study, comparison, other

**DEEP Mode Only:**
8. **Detailed Analysis**: Any additional insights worth noting?
9. **Recommendations**: How could we improve to be cited here?

**Output as JSON:**
{
  "relevance_score": 85,
  "sentiment": "positive",
  "brand_context": "Mentioned as leading AI-powered solution with specific ROI data",
  "competitor_mentions": ["Zendesk", "Intercom"],
  "key_points": [
    "AI automation reduces ticket volume by 40-60%",
    "ROI typically achieved in 3-6 months"
  ],
  "authority_score": 75,
  "content_type": "blog",
  "detailed_analysis": "Comprehensive comparison article on G2.com...",
  "recommendations": [
    "Strengthen thought leadership content",
    "Get more customer reviews on G2"
  ]
}
```

### LLM Analysis Output Schema

```typescript
interface CitationAnalysis {
  citation_id: string;
  url: string;
  title: string;
  relevance_score: number;       // 0-100
  sentiment: 'positive' | 'neutral' | 'negative';
  brand_context: string;
  competitor_mentions: string[];
  key_points: string[];
  authority_score: number;        // 0-100
  content_type: string;
  times_cited: number;
  cited_by_engines: string[];
  detailed_analysis?: string;     // DEEP mode only
  recommendations?: string[];     // DEEP mode only
}
```

## Extended Aggregation Schemas

### Top Performing Content

```json
{
  "top_cited_content": [
    {
      "url": "https://acmecorp.com/blog/reduce-ticket-volume",
      "title": "How to Reduce Ticket Volume by 60%",
      "citations_count": 12,
      "engines_citing": ["chatgpt", "perplexity", "gemini"],
      "avg_relevance": 94,
      "sentiment": "positive",
      "why_it_works": "Data-driven, specific metrics, solves clear pain point"
    }
  ]
}
```

### Citation Gaps

```json
{
  "citation_gaps": [
    {
      "query_category": "AI customer support",
      "tests_run": 15,
      "brand_citations": 0,
      "competitor_citations": {
        "Zendesk": 12,
        "Intercom": 8
      },
      "opportunity": "HIGH",
      "reasoning": "High-volume query category where we are not appearing but competitors dominate"
    }
  ]
}
```

### Competitive Landscape

```json
{
  "competitive_landscape": {
    "visibility_comparison": {
      "Zendesk": {
        "total_mentions": 89,
        "visibility_rate": "31.3%",
        "avg_position": 1.8,
        "sentiment": "positive (78%), neutral (20%), negative (2%)"
      },
      "Intercom": {
        "total_mentions": 67,
        "visibility_rate": "23.6%",
        "avg_position": 2.3,
        "sentiment": "positive (71%), neutral (25%), negative (4%)"
      },
      "Our Brand": {
        "total_mentions": 48,
        "visibility_rate": "16.8%",
        "avg_position": 2.8,
        "sentiment": "positive (81%), neutral (17%), negative (2%)"
      }
    },
    "competitive_gaps": [
      "Zendesk dominates enterprise queries - we need enterprise case studies",
      "Intercom wins on easy to use positioning - emphasize our UX",
      "We have better ROI metrics but fewer overall citations - need more content volume"
    ]
  }
}
```

### Content Quality Assessment

```json
{
  "content_assessment": {
    "high_authority_citations": 32,
    "medium_authority": 45,
    "low_authority": 11,
    "content_types": {
      "blog": 28,
      "product_page": 12,
      "review_site": 5,
      "case_study": 3
    },
    "insights": [
      "Blog content performs best (58% of citations)",
      "Product pages underperform - need optimization",
      "Only 3 case study citations - opportunity to create more"
    ]
  }
}
```

## Full Output File Schema

```json
{
  "metadata": {
    "mode": "DEEP",
    "total_citations_analyzed": 847,
    "unique_urls": 600,
    "analysis_approach": "programmatic",
    "analysis_time_seconds": 138,
    "generated_at": "2024-01-15T11:30:00Z"
  },
  "brand_performance": {
    "total_brand_citations": 48,
    "visibility_rate": "16.8%",
    "avg_relevance_score": 87,
    "sentiment_breakdown": {
      "positive": 39,
      "neutral": 8,
      "negative": 1
    },
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

## Token Savings Comparison

### Traditional LLM Approach (600 citations)
```
Each citation analysis: ~75 tokens
Total: 600 x 75 = 45,000 tokens
Plus prompt overhead: ~3,000 tokens
Total: ~48,000 tokens
```

### Programmatic Approach
```
Citations processed in code (not loaded to context): 0 tokens
Final aggregated insights: ~800 tokens
Code overhead: ~1,200 tokens
Total: ~2,000 tokens

Savings: 48,000 -> 2,000 = 96% reduction
```
