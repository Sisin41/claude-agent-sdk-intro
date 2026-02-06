---
name: seo-keyword-research
description: Identify high-value keyword opportunities through search volume, competition, and user intent analysis. Use when building content strategy, entering new markets, or auditing keyword gaps against competitors.
metadata:
  author: castor
  version: "1.0"
  domain: seo
  execution-modes: light, deep
---

# SEO Keyword Research

Identify high-value keyword opportunities through comprehensive research of search volume, competition, and user intent to guide content strategy and optimization efforts.

## Execution Modes

### Light Mode (15-20 keywords, 5-10 minutes)

- **Goal**: Fast identification of top keyword opportunities
- **Research Depth**: Basic search analysis
- **Output**: Prioritized list of 15-20 keywords

### Deep Mode (30-50 keywords, 20-30 minutes)

- **Goal**: Detailed keyword strategy with clusters and intent mapping
- **Research Depth**: Deep competitive analysis, long-tail exploration
- **Output**: Full keyword strategy with topic clusters

## Prerequisites

**Required Input**:
- Website/domain to optimize
- Industry/niche

**Optional Input**:
- Target audience (can research during execution)
- Competitors (can identify during execution)

## Workflow

### Step 1: Seed Keyword Identification

Identify 10-15 seed keywords that represent core business topics.

**Light Mode**:
1. `WebFetch` the target website homepage
2. Extract main topics/services from content
3. Identify 5-10 seed keywords from services
4. Add industry-standard terms

**Deep Mode**:
1. `WebFetch` homepage, services pages, product pages
2. Extract all major topics
3. `WebSearch` for "{industry} services" to find terminology
4. `WebSearch` for "site:{competitor.com}" to see their keywords
5. Compile 15-20 seed keywords

**Output**: List of seed keywords with notes on relevance.

### Step 2: Keyword Expansion

Expand seed keywords into 30-100+ variations using four techniques:

1. **Question-Based**: "how to {seed}", "what is {seed}", "{seed} guide"
2. **Comparison**: "best {seed}", "{seed} vs {alt}", "top {seed}"
3. **Problem-Solving**: "{problem} solution", "fix {problem}", "improve {metric}"
4. **Long-Tail**: "{seed} for {audience}", "{seed} for {industry}", "{seed} with {feature}"

Light Mode: top 5 seeds, 2-3 variations each (~15-20 total).
Deep Mode: all 15 seeds, 3-5 variations per technique (50-100+ total).

### Step 3: Search Volume Estimation

Estimate monthly search volume for each keyword using proxy methods (no direct Ahrefs/SEMrush access).

- **Google Autocomplete**: `WebSearch` the keyword -- autocomplete suggests HIGH (10K+), related results suggest MEDIUM (1K-10K), no suggestions suggest LOW (<1K)
- **Published Data**: `WebSearch` "[keyword] search volume" for blog posts with keyword data
- **Competitive Proxy**: `WebSearch` "site:{competitor.com} [keyword]" -- dedicated page = HIGH, blog mention = MEDIUM

Volume categories: HIGH (10K+), MEDIUM (1K-10K), LOW (100-1K), VERY LOW (<100).

### Step 4: Keyword Difficulty Assessment

Estimate ranking difficulty for each keyword.

For each keyword, `WebSearch` the term and check top 5 results:
- Majority major brands (Forbes, HubSpot, etc.) = HIGH difficulty
- Mix of brands and blogs = MEDIUM difficulty
- Mostly smaller sites = LOW difficulty

For Deep Mode, also `WebFetch` top 3 ranking pages to assess content quality, word count, and freshness.

Difficulty scale: 0-30 Easy, 31-60 Medium, 61-80 Hard, 81-100 Very Hard.

### Step 5: User Intent Classification

Categorize keywords by user intent:

| Intent | Examples | Content Type | Funnel Stage |
|--------|----------|-------------|--------------|
| Informational | "what is X", "how does X work" | Blog posts, guides | Awareness |
| Commercial | "best X tools", "X comparison" | Comparison articles, reviews | Consideration |
| Transactional | "X pricing", "buy X" | Product/pricing pages | Decision |
| Navigational | "[brand] support", "[product] login" | Brand pages | Retention |

### Step 6: Opportunity Scoring

Prioritize keywords using the opportunity formula:

```
Opportunity Score = (Volume Score x Intent Value) / (Difficulty + 1)

Volume Score: HIGH=3, MEDIUM=2, LOW=1
Intent Value: Transactional=3, Commercial=2, Informational=1
```

Priority tiers: P1 (>0.10), P2 (0.05-0.10), P3 (<0.05).

### Step 7: Competitive Gap Analysis

Identify keywords where competitors rank but you do not.

**Light Mode**: Top 2 competitors, `WebSearch` site:{competitor} with seed keywords.
**Deep Mode**: 3-5 competitors, full mapping of ranking pages per keyword category.

Gap categories: Critical (high-volume, competitor top 3), Opportunity (medium-volume, weak competitor content), Quick Win (low difficulty, easy to create).

### Step 8: Keyword Grouping & Clustering

Organize keywords into topic clusters for content planning.

1. **Identify Pillar Topics**: Broad, high-volume keywords for comprehensive guides (3000+ words)
2. **Group Supporting Keywords**: 5-10 related, specific keywords per pillar
3. **Map Internal Linking**: Each cluster article links to/from its pillar page

### Step 9: Content Recommendations

For each priority keyword, recommend content format, word count, structure, required elements, internal link targets, and target outcome. See [workflow-detail.md](references/workflow-detail.md) for full recommendation schema.

### Step 10: Output Generation

Save results to `/data/seo/keywords-{site}-{mode}.json`.

- Light Mode: keyword list with volume, difficulty, intent, opportunity score, and priority
- Deep Mode: full keyword data + topic clusters + competitive gaps + content recommendations

See [workflow-detail.md](references/workflow-detail.md) for complete output schemas.

## Error Handling

- **Website inaccessible**: Use `WebSearch` for cached versions; research industry keywords generically; flag limited data availability
- **Competitors unknown**: `WebSearch` "{industry} top companies" or "{main keyword} companies"; use industry leaders as proxies
- **No clear keywords found**: Use industry-standard terminology; research similar companies; start with broad seed keywords

## Validation Checks

Before saving output, verify:
- At least 10 keywords identified
- All keywords have search volume estimates
- All keywords have difficulty scores
- All keywords have intent classification
- At least 3 P1 (high priority) keywords identified

## Usage Example

```
1. Read this skill file
2. Determine mode (light or deep)
3. Use TodoWrite to track progress through Steps 1-10
4. Execute research steps using WebSearch and WebFetch
5. Save JSON output to /data/seo/
6. Provide summary:
   "Found 52 keyword opportunities
    - 12 high priority (P1)
    - 25 medium priority (P2)
    - 15 low priority (P3)

    Top opportunity: 'best AI customer support tools'
    - Volume: MEDIUM (2K-5K searches/month)
    - Difficulty: 45 (medium)
    - Opportunity score: 0.087

    Recommended: Create comparison article

    Full research: /data/seo/keywords-acme-comprehensive.json"
```

## Integration with Other Skills

This keyword data feeds into:
- **seo-content-optimization** for optimizing existing content against target keywords
- **seo-technical-audit** for site-wide optimization context
