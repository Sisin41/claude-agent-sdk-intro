---
name: competitor-analysis
description: Analyze competitor strategies across all marketing channels (GEO, SEO, Paid Ads, Content, Social) to identify competitive advantages, gaps, opportunities, and threats. Use when benchmarking against competitors or building competitive intelligence reports.
metadata:
  author: castor
  version: "1.0"
  domain: shared
  execution-modes: light, deep
---

# Comprehensive Competitor Analysis

## Purpose

Analyze competitor strategies across all marketing channels (GEO, SEO, Paid Ads, Content, Social) to identify competitive advantages, gaps, opportunities, and threats.

## Execution Modes

### Light Mode (10-15 minutes)
**Goal**: Competitive snapshot with top 3 insights
**Scope**: 2-3 competitors, high-level overview
**Output**: Competitive positioning summary + quick wins

### Deep Mode (45-60 minutes)
**Goal**: Comprehensive competitive intelligence report
**Scope**: 4-6 competitors, detailed analysis across all channels
**Output**: Full competitive analysis with strategic recommendations

## Prerequisites

**Required Input**:
- List of competitors (2-6 companies)
- Your company information (for comparison)
- Industry/market (for context)

**Optional**:
- Specific areas of focus (SEO, Ads, Content, etc.)
- Budget range (to identify comparable competitors)
- Geographic market

## Step 1: Identify Competitors

**Types**:
- **Direct**: Same product/service, audience, price range
- **Indirect**: Different product, same problem solved
- **Aspirational**: Where you want to be (larger, established)
- **Emerging**: New entrants, growing fast, future threats

**Discovery Methods**:
1. **Search-Based**: Use WebSearch for "best {category} software", "alternatives to {product}", "{product} vs"
2. **Review Sites**: G2.com, Capterra category pages, Product Hunt collections
3. **Customer Research**: Ask customers what alternatives they considered
4. **Market Research**: Crunchbase, CB Insights, industry reports

**Output**: List of 4-6 competitors ranked by relevance

## Step 2: Analysis Framework (6 Dimensions)

### Dimension 1: Market Positioning
Analyze target audience, value proposition, pricing strategy, and brand positioning for each competitor. Extract data into structured format with fields for audience segment, industries, pricing tier, and positioning category (Challenger, Leader, Innovator, Specialist).

### Dimension 2: GEO (AI Search Engine Visibility)
Test 10-15 high-value prompts per competitor across AI engines. Track visibility percentage, citation quality, average position, and sentiment. Compare against your own GEO analysis results.

### Dimension 3: SEO Performance
Research domain authority, ranking keywords, estimated organic traffic, backlink profile, content strategy (frequency, types, depth), and technical SEO quality. Use WebSearch and WebFetch for data gathering.

### Dimension 4: Paid Advertising
Analyze Google Ads presence (brand bidding, non-brand, ad copy style), Meta Ads (via Facebook Ad Library - active ads count, formats, messaging themes, offers), LinkedIn Ads activity, and display/retargeting presence.

### Dimension 5: Content Marketing
Audit blog/resource center (post frequency, content types, depth), gated content/lead magnets, video content (YouTube), podcasts/webinars, and social media (followers, engagement, post frequency).

### Dimension 6: Product & Features
Compare core features, pricing tiers, integrations count, and customer reviews (G2 rating, review count, common praise/complaint themes).

See `references/workflow-detail.md` for detailed analysis templates and example JSON output for each dimension.

## Step 3: Competitive Positioning (SWOT)

Synthesize findings into a SWOT analysis:

```json
{
  "competitive_swot": {
    "strengths": [
      "Lower price point than Competitor A",
      "Unique features (real-time collaboration)",
      "Faster customer support response"
    ],
    "weaknesses": [
      "Lower organic traffic than Competitor A",
      "Weaker brand recognition",
      "Limited AI visibility",
      "Smaller content library"
    ],
    "opportunities": [
      "Competitors weak on video - your strength",
      "Gap in mid-market positioning",
      "Underserved international markets",
      "AI search engines (early mover advantage)"
    ],
    "threats": [
      "Competitor A expanding down-market",
      "Competitor C growing 200% YoY",
      "Market consolidation risk",
      "AI automation industry disruption"
    ]
  }
}
```

## Output Deliverables

### Light Mode Output

Save to `/data/competitor/competitive-analysis-{company}-quick.json`:

```json
{
  "metadata": {
    "mode": "QUICK",
    "company": "{company}",
    "competitors_analyzed": 3,
    "generated_at": "{timestamp}"
  },
  "executive_summary": {
    "competitive_position": "CHALLENGER - Strong product, weak brand awareness",
    "top_3_insights": ["..."],
    "biggest_threat": "...",
    "biggest_opportunity": "..."
  },
  "competitor_comparison": {
    "competitor_a": {
      "position": "Market Leader",
      "strengths": ["..."],
      "weaknesses": ["..."],
      "vs_you": "..."
    }
  },
  "quick_wins": [
    {
      "opportunity": "...",
      "action": "...",
      "impact": "...",
      "effort": "...",
      "timeline": "..."
    }
  ]
}
```

### Deep Mode Output

Save to `/data/competitor/competitive-analysis-{company}-deep.json` with comprehensive breakdown of all 6 dimensions, detailed data, SWOT analysis, and strategic recommendations.

## Validation Checks

```
- At least 2-3 competitors analyzed (Light), 4-6 (Deep)
- All major dimensions covered (GEO, SEO, Ads, Content, Product)
- Data sources cited for all claims
- SWOT analysis completed
- Actionable recommendations provided
- Competitive positioning clear
```

## Agent Workflow

```
1. Read this skill file
2. Identify 2-6 competitors (user-provided or discovered)
3. Determine mode (Light or Deep)
4. Track analysis with TodoWrite:
   [ ] Competitor identification
   [ ] Market positioning analysis
   [ ] GEO analysis
   [ ] SEO analysis
   [ ] Paid ads analysis
   [ ] Content marketing analysis
   [ ] Product comparison
   [ ] SWOT synthesis
   [ ] Recommendations
   [ ] Output generation
5. Execute research for each competitor using WebSearch and WebFetch
6. Compare and synthesize
7. Save JSON to /data/competitor/
8. Provide strategic summary
```

## Integration with Other Skills

**Uses data from**:
- All analysis skills (to compare your performance vs competitors)

**Feeds into**:
- `presentation-creation` skill for competitive slides
- `data-synthesis` skill for strategic insights
- All channel strategies (inform tactics based on competitive gaps)
