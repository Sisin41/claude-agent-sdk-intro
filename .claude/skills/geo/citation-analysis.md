# GEO Citation Analysis

## Purpose
Analyze all citations from multi-engine test results using LLM-powered parallel analysis to extract insights about brand mentions, competitor visibility, and content quality.

---

## Prerequisites
**Required Input**: Test results from `multi-engine-testing.md`
**Input File**: `/data/geo/test-results-{company}-{mode}.json`

**Required MCP Tool**: `mcp__MarketingTools__analyze_citations`
(If unavailable, use manual analysis with basic pattern matching)

---

## Execution Modes

### LIGHT Mode
**Input**: ~40 test results with ~120 citations
**Analysis Depth**: Basic counting and categorization
**LLM Analysis**: None (pattern matching only)
**Expected Time**: 30-60 seconds

### DEEP Mode
**Input**: ~300 test results with ~900 citations
**Analysis Depth**: Comprehensive LLM-powered analysis of each citation
**LLM Analysis**: Yes (parallel Claude Haiku calls)
**Expected Time**: 2-3 minutes (with MCP) / 30-45 minutes (manual)

---

## MCP Tool Specification

### Tool: `analyze_citations`

**Purpose**: Analyze citations using parallel LLM calls for deep insights

**Input Schema**:
```typescript
interface AnalyzeCitationsInput {
  test_results: TestResult[];  // From multi-engine testing
  brand_info: {
    brand_name: string;
    domain: string;
    competitors?: string[];
  };
  analysis_mode: 'light' | 'deep';
  max_concurrent?: number;  // Default: 50
  llm_model?: string;  // Default: 'claude-haiku-3-5'
}
```

**Output Schema**:
```typescript
interface CitationAnalysis {
  citation_id: string;
  url: string;
  title: string;
  // Analysis results:
  relevance_score: number;  // 0-100
  sentiment: 'positive' | 'neutral' | 'negative';
  brand_context: string;  // How brand was mentioned
  competitor_mentions: string[];
  key_points: string[];
  authority_score: number;  // 0-100 (domain authority estimate)
  content_type: 'blog' | 'product_page' | 'review' | 'news' | 'documentation' | 'other';
  // Deep mode only:
  detailed_analysis?: string;
  recommendations?: string[];
}
```

**Expected Behavior**:
1. Extract all unique citations from test results
2. Deduplicate citations (same URL may appear multiple times)
3. For each citation, build analysis prompt
4. Execute LLM calls in parallel (50 concurrent)
5. Parse and structure LLM responses
6. Aggregate insights across all citations
7. Return structured analysis results

**Performance Requirements**:
- 900 citations should analyze in < 3 minutes
- Must use fast/cheap model (Haiku recommended)
- Must handle LLM failures gracefully

---

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
            ...citation,
            "source_prompt": result.prompt_id,
            "source_engine": result.engine,
            "brand_mentioned_in_result": result.brand_mentioned
        }
        all_citations.append(citation_with_context)

# Deduplicate by URL
unique_citations = deduplicate_by_url(all_citations)
```

**Expected Counts**:
- LIGHT: ~120 total citations → ~80 unique URLs
- DEEP: ~900 total citations → ~600 unique URLs

---

### Step 2: LIGHT Mode Analysis (Basic Pattern Matching)

**No LLM calls - just pattern matching and counting**

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
   competitors_mentioned = []
   for competitor in known_competitors:
       if competitor.lower() in citation.snippet.lower():
           competitors_mentioned.append(competitor)
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

**Output (LIGHT)**:
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
      "times_cited": 12  // Across all tests
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

**Time**: 30-60 seconds

---

### Step 3: DEEP Mode Analysis (LLM-Powered)

**Using MCP Tool** (Preferred):

```python
# Pseudo-code for agent
citation_analyses = await mcp__MarketingTools__analyze_citations({
    "test_results": loaded_test_results,
    "brand_info": {
        "brand_name": "Acme Corp",
        "domain": "acmecorp.com",
        "competitors": ["Zendesk", "Intercom", "Freshdesk"]
    },
    "analysis_mode": "deep",
    "max_concurrent": 50,
    "llm_model": "claude-haiku-3-5"
})
```

**LLM Prompt Template (per citation)**:

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
   - Consider: Topic match, authority, specificity
   - Output: Single number 0-100

2. **Sentiment** (positive/neutral/negative): How is our brand portrayed?
   - Positive: Recommended, praised, highlighted benefits
   - Neutral: Mentioned factually, listed among options
   - Negative: Criticized, issues mentioned, not recommended
   - If brand not mentioned, assess sentiment toward topic

3. **Brand Context**: How is our brand mentioned (if at all)?
   - Quote exact phrase
   - Describe positioning (leader, alternative, option, etc.)
   - If not mentioned, state "Not mentioned"

4. **Competitor Mentions**: Which competitors are mentioned?
   - List all competitor brands mentioned
   - Note their positioning relative to us

5. **Key Points**: What are the main points from this citation?
   - Extract 2-3 key takeaways
   - Focus on facts, data, recommendations

6. **Authority Score** (0-100): How authoritative is this source?
   - Consider: Domain reputation, content quality, recency
   - Output: Single number 0-100

7. **Content Type**: What type of content is this?
   - Options: blog, product_page, review, news, documentation, case_study, comparison, other

**DEEP Mode Only (optional):**
8. **Detailed Analysis**: Any additional insights worth noting?
9. **Recommendations**: How could we improve to be cited here?

**Output as JSON:**
```json
{
  "relevance_score": 85,
  "sentiment": "positive",
  "brand_context": "Mentioned as 'leading AI-powered solution' with specific ROI data",
  "competitor_mentions": ["Zendesk", "Intercom"],
  "key_points": [
    "AI automation reduces ticket volume by 40-60%",
    "ROI typically achieved in 3-6 months",
    "Integration with existing tools is critical"
  ],
  "authority_score": 75,
  "content_type": "blog",
  "detailed_analysis": "Comprehensive comparison article on G2.com. Our brand ranked #2 for 'ease of implementation' but #4 overall. Strong emphasis on our ROI metrics.",
  "recommendations": [
    "Strengthen thought leadership content",
    "Get more customer reviews on G2",
    "Create comparison content vs Zendesk"
  ]
}
```
```

**Parallel Execution**:
```python
# Execute 900 LLM calls in parallel (50 concurrent)
await pMap(
    unique_citations,
    async (citation) => {
        const prompt = buildAnalysisPrompt(citation, brand_info, 'deep');
        const response = await callLLM({
            model: 'claude-haiku-3-5',
            prompt: prompt,
            max_tokens: 1500
        });
        return parseLLMResponse(response);
    },
    { concurrency: 50 }
)
```

**Progress Tracking**:
```
Analyzing 847 citations with LLM...
[████████████████████] 100% (847/847) ✓

Model: Claude Haiku 3.5 (fast, cost-effective)
Concurrency: 50 parallel calls
Time: 2m 18s
```

**Output (DEEP)**:
```json
{
  "citations": [
    {
      "citation_id": "cit_001",
      "url": "https://acmecorp.com/blog/reduce-tickets",
      "title": "How to Reduce Support Ticket Volume by 60%",
      "relevance_score": 94,
      "sentiment": "positive",
      "brand_context": "Featured as case study with quantified results: '60% ticket reduction, $120K annual savings'",
      "competitor_mentions": [],
      "key_points": [
        "AI routing reduces ticket volume significantly",
        "Real customer data shows 60% improvement",
        "ROI achieved in 4 months for mid-size SaaS"
      ],
      "authority_score": 87,
      "content_type": "blog",
      "times_cited": 12,  // How many times cited across all tests
      "cited_by_engines": ["chatgpt", "perplexity", "gemini"],
      "detailed_analysis": "This is our highest-performing content. Cited by all 3 engines, particularly strong on Perplexity. Data-driven approach with specific metrics makes it highly authoritative.",
      "recommendations": [
        "Create more content with similar data-driven approach",
        "Update with 2024 data to maintain freshness",
        "Add video walkthrough to increase engagement"
      ]
    }
  ],
  "summary": {
    "total_unique_citations": 600,
    "brand_citations": 48,
    "average_relevance_score": 78,
    "sentiment_breakdown": {
      "positive": 39,
      "neutral": 8,
      "negative": 1
    },
    "competitor_citations": {
      "Zendesk": {
        "count": 89,
        "avg_relevance": 82,
        "sentiment": "mostly_positive"
      },
      "Intercom": {
        "count": 67,
        "avg_relevance": 79,
        "sentiment": "mostly_positive"
      }
    }
  }
}
```

**Time**: 2-3 minutes for 900 citations

---

### Step 4: Aggregate Insights

**Top Performing Content**:
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

**Citation Gaps**:
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
      "reasoning": "High-volume query category where we're not appearing but competitors dominate"
    }
  ]
}
```

**Competitor Analysis**:
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
      "Zendesk dominates 'enterprise' queries - we need enterprise case studies",
      "Intercom wins on 'easy to use' positioning - emphasize our UX",
      "We have better ROI metrics but fewer overall citations - need more content volume"
    ]
  }
}
```

**Content Quality Assessment**:
```json
{
  "content_assessment": {
    "high_authority_citations": 32,  // Authority score > 80
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

---

### Step 5: Save Results

**Output File**: `/data/geo/citation-analysis-{company}-{mode}.json`

```json
{
  "metadata": {
    "mode": "DEEP",
    "total_citations_analyzed": 847,
    "unique_urls": 600,
    "llm_powered": true,
    "llm_model": "claude-haiku-3-5",
    "analysis_time_seconds": 138,
    "generated_at": "2024-01-15T11:30:00Z"
  },
  "brand_performance": {
    "total_brand_citations": 48,
    "visibility_rate": "16.8%",
    "avg_relevance_score": 87,
    "sentiment_breakdown": {...},
    "top_cited_content": [...],
    "content_quality_assessment": {...}
  },
  "competitive_analysis": {
    "competitors": [...],
    "visibility_comparison": {...},
    "competitive_gaps": [...]
  },
  "citation_gaps": [...],
  "detailed_citations": [
    {...}  // 600 citation analysis objects
  ],
  "recommendations": {
    "content_creation": [...],
    "content_optimization": [...],
    "competitive_positioning": [...]
  }
}
```

---

## Error Handling

**LLM Failures**:
```
If LLM call fails:
- Retry once with exponential backoff
- If still fails, use basic pattern matching fallback
- Log error for debugging
- Continue with other citations
- Flag in output: "partial_analysis": true
```

**Malformed LLM Responses**:
```
If LLM response doesn't parse to JSON:
- Attempt to extract key fields with regex
- If extraction fails, mark as "analysis_failed"
- Continue with other citations
- Log for review
```

**Rate Limiting**:
```
If Anthropic rate limit hit:
- Reduce concurrency from 50 to 25
- Add slight delay between batches
- Retry failed batch
```

---

## Validation Checks

Before saving results:

1. **Coverage**: At least 95% of citations analyzed successfully
2. **Data Quality**: All required fields present in analysis objects
3. **Sentiment Distribution**: Sentiment values are valid (positive/neutral/negative)
4. **Score Ranges**: Relevance and authority scores are 0-100

If validation fails, log warnings but still save results

---

## Usage Example

**Agent Workflow**:
```
1. Read this skill file
2. Load test results from previous step
3. Extract and deduplicate citations
4. Determine analysis mode (LIGHT or DEEP)
5. If DEEP and MCP tool available:
   - Execute parallel LLM analysis
   - Show progress: "Analyzing 847 citations... 45% (380/847)"
6. If LIGHT or no MCP tool:
   - Use basic pattern matching
7. Aggregate insights
8. Save JSON to /data/geo/
9. Provide summary to user:
   "✅ Analyzed 847 citations in 2m 18s
    Your brand: 48 citations (16.8% visibility)
    Sentiment: 81% positive
    Top content: /blog/reduce-ticket-volume (12 citations)
    Biggest gap: 'AI customer support' queries (0 citations)
    Full analysis: /data/geo/citation-analysis-acme-deep.json"
10. Pass data to next skill (strategy-synthesis.md)
```

---

## Next Skill
Once complete, citation analysis feeds into:
→ **`strategy-synthesis.md`** to create actionable recommendations

---

## MCP Tools Required

### **CRITICAL**: `mcp__MarketingTools__analyze_citations`

**Priority**: **P0 - Must Have**

**Rationale**:
- Manual analysis of 900 citations is impossible at scale
- LLM-powered analysis provides 10x better insights than pattern matching
- Parallel execution makes 45-minute task into 2-3 minute task
- Core differentiator of DEEP mode

**Implementation Requirements**:
- Accept list of citations
- Build LLM prompts per citation
- Execute in parallel (50 concurrent Haiku calls)
- Parse and structure LLM responses
- Handle failures gracefully
- Return structured analysis

**Cost Estimate**:
- 900 citations × ~500 tokens/analysis = ~450K tokens
- Claude Haiku pricing: ~$0.25 per 1M input tokens
- **Cost per DEEP run**: ~$0.11-0.25

**See**: `/mcp-servers/marketing-tools/src/geo/citation-analyzer.ts` (to be built)
