# GEO Strategy Synthesis

## Purpose
Synthesize all GEO analysis data (company value, prompts, test results, citations) into a comprehensive strategic report with prioritized, actionable recommendations.

---

## Prerequisites
**Required Inputs**:
1. Company value data: `/data/geo/company-value-{company}-{mode}.json`
2. Generated prompts: `/data/geo/prompts-{company}-{mode}.json`
3. Test results: `/data/geo/test-results-{company}-{mode}.json`
4. Citation analysis: `/data/geo/citation-analysis-{company}-{mode}.json`

**No MCP Tools Required** - Uses Read, Write, Edit

---

## Execution Modes

### LIGHT Mode
**Report Length**: 2-3 pages
**Content**: High-level findings + top 3 recommendations
**Expected Time**: 2-3 minutes

### DEEP Mode
**Report Length**: 15-20 pages
**Content**: Comprehensive analysis + detailed 12-week roadmap
**Expected Time**: 5-8 minutes

---

## Workflow Steps

### Step 1: Load All Data Sources

```
Read and parse:
1. /data/geo/company-value-{company}-{mode}.json
2. /data/geo/prompts-{company}-{mode}.json
3. /data/geo/test-results-{company}-{mode}.json
4. /data/geo/citation-analysis-{company}-{mode}.json

Validate all files exist and are parseable
```

---

### Step 2: Calculate Key Metrics

**Overall Performance Metrics**:
```json
{
  "current_performance": {
    "overall_visibility_rate": "16.8%",
    "industry_benchmark": "25-35%",
    "gap_to_benchmark": "-8.2 to -18.2 percentage points",
    "total_tests_run": 300,
    "total_brand_mentions": 48,
    "total_citations_analyzed": 847
  },
  "by_engine": {
    "chatgpt": {
      "visibility": "12.6%",
      "vs_benchmark": "-12.4%",
      "rank_vs_competitors": "3rd"
    },
    "perplexity": {
      "visibility": "29.5%",
      "vs_benchmark": "+4.5%",
      "rank_vs_competitors": "2nd"
    },
    "gemini": {
      "visibility": "8.4%",
      "vs_benchmark": "-21.6%",
      "rank_vs_competitors": "4th"
    }
  },
  "by_question_type": {
    "comparison": "29.3%",
    "recommendation": "25.0%",
    "informational": "13.3%",
    "problem-solution": "5.0%",  // ⚠️ Critical gap
    "exploratory": "0%"  // ⚠️ Missing entirely
  },
  "by_funnel_stage": {
    "decision": "25.4%",
    "consideration": "22.1%",
    "awareness": "9.5%",  // ⚠️ Weak
    "retention": "0%"  // ⚠️ Missing
  }
}
```

**Competitive Position**:
```json
{
  "competitive_position": {
    "rank": "3rd",
    "visibility_vs_competitors": {
      "zendesk": {"visibility": "31.3%", "gap": "-14.5%"},
      "intercom": {"visibility": "23.6%", "gap": "-6.8%"},
      "your_brand": {"visibility": "16.8%"},
      "freshdesk": {"visibility": "12.0%", "gap": "+4.8%"}
    }
  }
}
```

**Content Performance**:
```json
{
  "content_performance": {
    "top_performers": [
      {
        "url": "/blog/reduce-ticket-volume",
        "citations": 12,
        "why_it_works": "Data-driven with specific ROI metrics"
      }
    ],
    "underperformers": [
      {
        "url": "/pricing",
        "citations": 0,
        "traffic": "high",
        "issue": "Good SEO traffic but no AI citations"
      }
    ]
  }
}
```

---

### Step 3: Identify Opportunities & Gaps

**Critical Gaps** (must address):
```json
{
  "critical_gaps": [
    {
      "gap": "Problem-Solution queries",
      "current_visibility": "5.0%",
      "target": "25%+",
      "impact": "HIGH",
      "queries_tested": 60,
      "competitor_visibility": "Zendesk 35%, Intercom 28%",
      "opportunity_value": "+15-20% overall visibility if fixed"
    },
    {
      "gap": "Awareness-stage content",
      "current_visibility": "9.5%",
      "target": "25%+",
      "impact": "HIGH",
      "reasoning": "Missing top-of-funnel visibility"
    },
    {
      "gap": "Gemini engine",
      "current_visibility": "8.4%",
      "target": "20%+",
      "impact": "MEDIUM",
      "reasoning": "21% below benchmark, competitors performing better"
    }
  ]
}
```

**High-Value Opportunities**:
```json
{
  "opportunities": [
    {
      "opportunity": "AI customer support keyword family",
      "current_citations": 0,
      "competitor_citations": {"Zendesk": 25, "Intercom": 18},
      "search_volume": "HIGH",
      "difficulty": "MEDIUM",
      "estimated_impact": "+8-10% visibility",
      "effort": "Create 1 pillar page + 5 cluster articles (60-80 hours)"
    }
  ]
}
```

---

### Step 4: Develop Strategic Recommendations

**Prioritization Framework**:

```
Priority = (Impact × Feasibility) / Effort

Impact: HIGH = 3, MEDIUM = 2, LOW = 1
Feasibility: EASY = 3, MEDIUM = 2, HARD = 1
Effort: LOW = 3, MEDIUM = 2, HIGH = 1

Priority Score: 1-9 (higher = more priority)
```

**Recommendation Structure**:
```json
{
  "recommendation_id": "rec_001",
  "title": "Create 'AI Customer Support' Pillar Content",
  "priority": "P1",
  "priority_score": 8.0,
  "impact": "HIGH",
  "feasibility": "MEDIUM",
  "effort": "MEDIUM",
  "estimated_visibility_increase": "+8-10%",
  "timeline": "Weeks 1-4",
  "resources_required": {
    "content_writers": 1,
    "time_hours": 60,
    "budget_usd": 3000
  },
  "action_items": [
    "Research 'AI customer support' keyword family",
    "Create comprehensive pillar page (3000+ words)",
    "Write 5 supporting cluster articles",
    "Add structured data (Schema.org)",
    "Promote via social + email"
  ],
  "success_metrics": [
    "Cited by at least 2/3 engines within 30 days",
    "Appear in top 5 results for target queries",
    "+5% visibility on awareness-stage queries"
  ],
  "rationale": "Competitors getting 25+ citations for this keyword family while we have 0. High search volume, medium difficulty. Addresses both awareness gap and keyword gap."
}
```

---

### Step 5: Create Implementation Roadmap

**LIGHT Mode**: Simple task list

**DEEP Mode**: Detailed 12-week Gantt chart

```markdown
## 12-Week GEO Optimization Roadmap

### Phase 1: Quick Wins (Weeks 1-2)
- [ ] Week 1: Create "AI Customer Support" pillar page
  - Research + outline (8 hours)
  - First draft (16 hours)
  - Review + edit (8 hours)
  - Publish + promote (4 hours)

- [ ] Week 2: Optimize top 3 existing pages
  - Add FAQ sections (6 hours)
  - Implement structured data (4 hours)
  - Improve internal linking (2 hours)

**Expected Impact**: +3-5% visibility

### Phase 2: Content Sprint (Weeks 3-6)
- [ ] Week 3: Create 3 problem-solution articles
  - "How to reduce support costs by 50%"
  - "Eliminate support ticket backlog"
  - "Scale support without hiring"

- [ ] Week 4: Create 2 awareness-stage guides
  - "Complete guide to AI customer support"
  - "AI vs traditional support: What's the difference?"

- [ ] Week 5-6: Promote + monitor
  - Social media promotion
  - Email to subscriber list
  - Monitor AI engine citations

**Expected Impact**: +5-7% visibility

### Phase 3: Technical Optimization (Weeks 7-8)
- [ ] Implement Schema.org across all content
- [ ] Build topic cluster architecture
- [ ] Improve internal linking structure
- [ ] Add "Key Takeaways" sections to all articles

**Expected Impact**: +2-4% visibility

### Phase 4: Authority Building (Weeks 9-12)
- [ ] Outreach for authoritative backlinks
- [ ] Create original research/survey
- [ ] Guest posts on high-authority sites
- [ ] Speaking engagements/webinars

**Expected Impact**: +3-5% visibility

**Total Projected Impact**: +13-21% visibility improvement
**Total Investment**: 100-120 hours, $5-8K budget
```

---

### Step 6: LIGHT Mode Report Template

**File**: `/docs/marketing/geo-analysis-{company}-light.md`

```markdown
# GEO Analysis Report - {Company Name} (LIGHT)

**Date**: {date}
**Execution Mode**: LIGHT
**Analysis Coverage**: 20 prompts, 2 engines, basic analysis

---

## Executive Summary

### Current Performance
- **Overall Visibility**: 16.8% (vs 25-35% industry benchmark)
- **Tests Run**: 40 (20 prompts × 2 engines)
- **Brand Mentions**: 15 total
- **Best Engine**: Perplexity (28.0%)
- **Competitive Rank**: 3rd (behind Zendesk, Intercom)

### Top 3 Opportunities

1. **Target "AI customer support" queries** (+8-10% visibility potential)
   - Currently: 0 citations
   - Competitors: Zendesk (12), Intercom (8)
   - Action: Create pillar content

2. **Optimize for problem-solution queries** (+5-7% visibility)
   - Currently: 5% visibility
   - Should be: 25%+
   - Action: Create 3 "How to..." articles

3. **Improve ChatGPT presence** (+6-8% visibility)
   - Currently: 12.6%
   - Perplexity: 28.0% (showing it's possible)
   - Action: Long-form comprehensive content

---

## Quick Wins (Next 2-4 Weeks)

1. **Create "AI Customer Support" pillar page**
   - Time: 40 hours
   - Impact: HIGH
   - Timeline: Week 1-2

2. **Add FAQ sections to top 5 pages**
   - Time: 6 hours
   - Impact: MEDIUM
   - Timeline: Week 1

3. **Fix 3 underperforming pages**
   - Time: 12 hours
   - Impact: MEDIUM
   - Timeline: Week 2-3

---

## Expected Results

**Timeline**: 6-8 weeks
**Visibility Improvement**: +10-15%
**Investment**: 60-80 hours content work

---

## Next Steps

1. Review and approve this strategy
2. Assign content creation resources
3. Start with Quick Win #1
4. Monitor progress weekly
5. Re-run GEO analysis in 6 weeks

---

**Full Data**: See `/data/geo/` for detailed analysis files
```

**Time to Generate**: 2-3 minutes

---

### Step 7: DEEP Mode Report Template

**File**: `/docs/marketing/geo-analysis-{company}-deep.md`

```markdown
# Comprehensive GEO Analysis - {Company Name}

**Report Date**: {date}
**Execution Mode**: DEEP
**Analysis Coverage**: 95 prompts, 3 engines, 847 citations analyzed

---

## Table of Contents
1. [Executive Summary](#executive-summary)
2. [Current Performance Analysis](#current-performance-analysis)
3. [Competitive Benchmarking](#competitive-benchmarking)
4. [Content Performance](#content-performance)
5. [Critical Gaps & Opportunities](#critical-gaps--opportunities)
6. [Strategic Recommendations](#strategic-recommendations)
7. [Implementation Roadmap](#implementation-roadmap)
8. [Success Metrics](#success-metrics)
9. [Appendix](#appendix)

---

## 1. Executive Summary

### Key Findings

**Current GEO Performance**:
- Overall visibility: **16.8%** (vs 25-35% industry benchmark)
- Total tests: 285 across 3 AI engines
- Brand citations: 48 (17% of tests)
- Competitive rank: **3rd place** (behind Zendesk & Intercom)

**Strengths**:
✅ Strong Perplexity performance (29.5% - above benchmark)
✅ High sentiment quality (81% positive when mentioned)
✅ Effective data-driven content (top blog has 12 citations)

**Critical Gaps**:
⚠️ Weak ChatGPT presence (12.6% vs 29.5% on Perplexity)
⚠️ Gemini severely underperforming (8.4% vs 20%+ benchmark)
⚠️ Missing awareness-stage visibility (9.5% vs 25% target)
⚠️ No presence in problem-solution queries (5% vs 25% target)

**Top 3 Strategic Opportunities**:
1. **"AI Customer Support" Content Gap** (+8-10% visibility)
2. **Problem-Solution Content** (+5-7% visibility)
3. **Gemini Optimization** (+10-15% on Gemini)

**Projected Impact**:
- Timeline: 12 weeks
- Visibility Improvement: **+15-20%**
- Investment: 100-120 hours, $5-8K
- Expected Result: Move from 16.8% to 32-37% visibility

---

## 2. Current Performance Analysis

### 2.1 Overall Metrics

| Metric | Value | Benchmark | Status |
|--------|-------|-----------|--------|
| Overall Visibility | 16.8% | 25-35% | ⚠️ Below |
| Total Tests | 285 | N/A | ✓ Comprehensive |
| Brand Mentions | 48 | N/A | - |
| Average Citation Position | 2.8 | < 2.0 target | ⚠️ Low |
| Sentiment (when mentioned) | 81% positive | > 75% | ✅ Good |

### 2.2 Performance by Engine

| Engine | Visibility | vs Benchmark | Rank | Assessment |
|--------|-----------|--------------|------|------------|
| **Perplexity** | 29.5% | +4.5% | 2nd | ✅ **Strength** |
| **ChatGPT** | 12.6% | -12.4% | 3rd | ⚠️ **Critical Gap** |
| **Gemini** | 8.4% | -21.6% | 4th | 🔴 **Severe Gap** |

**Insight**: Perplexity success proves we CAN compete. Need to replicate this success on ChatGPT and Gemini.

### 2.3 Performance by Question Type

| Question Family | Tests | Mentions | Visibility | Target | Gap |
|----------------|-------|----------|-----------|--------|-----|
| Comparison | 75 | 22 | **29.3%** | 25-30% | ✅ On Target |
| Recommendation | 60 | 15 | **25.0%** | 25-30% | ✅ On Target |
| Informational | 60 | 8 | **13.3%** | 20-25% | ⚠️ Below |
| Problem-Solution | 60 | 3 | **5.0%** | 25-30% | 🔴 **Critical** |
| Exploratory | 30 | 0 | **0%** | 15-20% | 🔴 **Missing** |

**Insight**: Strong in bottom-funnel (comparison/recommendation), weak in top-funnel (problem-solution/exploratory).

[... Continue with detailed sections ...]

## 6. Strategic Recommendations

### Priority 1: Close Critical Gaps (Weeks 1-4)

#### 6.1 Target "AI Customer Support" Keyword Family

**Gap Analysis**:
- Current visibility: 0 citations
- Competitor visibility: Zendesk (25), Intercom (18)
- Search intent: Awareness + Consideration
- Opportunity: **HIGH**

**Strategy**:
Create comprehensive pillar page + supporting cluster

**Action Plan**:
1. **Week 1**: Research + Create Pillar Page
   - Keyword research: "AI customer support" family
   - Create 3500-word comprehensive guide
   - Include: Definitions, use cases, ROI calculator, buyer's guide
   - Add structured data (Schema.org Article + FAQPage)
   - Internal links to 5 related pages

2. **Week 2-3**: Create 5 Cluster Articles
   - "What is AI customer support?" (1500 words)
   - "How AI customer support works" (2000 words)
   - "AI customer support vs traditional" (1800 words)
   - "ROI of AI customer support" (1500 words)
   - "AI customer support implementation guide" (2500 words)

3. **Week 4**: Promotion
   - Social media campaign
   - Email to 10K subscriber list
   - Outreach to 5 industry publications
   - Reddit/Hacker News (if appropriate)

**Resources**:
- Content writer: 60 hours
- SEO specialist: 8 hours
- Designer (graphics): 6 hours
- Budget: $3,000-4,000

**Success Metrics**:
- Cited by 2/3 engines within 30 days
- +5-8% visibility on awareness queries
- 5,000+ organic pageviews in first 60 days

**Expected Impact**: **+8-10% overall visibility**

[... Continue with all recommendations ...]

## 7. Implementation Roadmap

[Include full 12-week Gantt chart from Step 5]

## 8. Success Metrics

### Leading Indicators (Monitor Weekly)
- New content indexed by AI engines
- Citation count on new content
- Improvement in target keyword families
- Social shares + backlinks

### Lagging Indicators (Monitor Monthly)
- Overall visibility % across engines
- Rank vs competitors
- Engine-specific performance
- Funnel-stage coverage

### Target Metrics (12 Weeks)

| Metric | Current | Target | Improvement |
|--------|---------|--------|-------------|
| Overall Visibility | 16.8% | 32-37% | +15-20% |
| ChatGPT | 12.6% | 25%+ | +12.4% |
| Gemini | 8.4% | 20%+ | +11.6% |
| Perplexity | 29.5% | 35%+ | +5.5% |
| Awareness Queries | 9.5% | 25%+ | +15.5% |
| Problem-Solution | 5.0% | 25%+ | +20% |

## 9. Appendix

### A. Full Prompt List
[Link to /data/geo/prompts-{company}-deep.json]

### B. Raw Test Results
[Link to /data/geo/test-results-{company}-deep.json]

### C. Citation Analysis
[Link to /data/geo/citation-analysis-{company}-deep.json]

### D. Competitor Deep-Dive
[Detailed section on each competitor]

### E. Technical Implementation Guide
[Step-by-step instructions for Schema.org, topic clusters, etc.]

---

**Report Generated**: {timestamp}
**Total Analysis Time**: ~20 minutes
**Next Recommended Action**: Review recommendations, approve Phase 1 Quick Wins
```

**Time to Generate**: 5-8 minutes

---

## Validation Checks

Before saving report:

1. **Data Completeness**: All input files successfully loaded
2. **Metrics Calculated**: All key performance metrics computed
3. **Recommendations Present**: At least 3 prioritized recommendations
4. **Roadmap Included**: Timeline with specific action items
5. **File Links Work**: All references to data files are valid

---

## Usage Example

**Agent Workflow**:
```
1. Read this approach file
2. Load all 4 data files from previous steps
3. Calculate key metrics
4. Identify gaps and opportunities
5. Generate prioritized recommendations
6. Create implementation roadmap
7. Write report (LIGHT or DEEP template)
8. Save markdown to /docs/marketing/
9. Provide summary to user:
   "✅ GEO strategy complete!

    Current visibility: 16.8% (vs 25-35% benchmark)
    Top opportunity: 'AI customer support' content (+8-10%)
    12-week roadmap created
    Expected improvement: +15-20% visibility

    📄 Full report: /docs/marketing/geo-analysis-acme-deep.md

    Ready to proceed with implementation?"
```

---

## Next Steps After Synthesis

1. **User Reviews Report**: Human reviews recommendations
2. **Approval Gate**: User approves strategy or requests changes
3. **Implementation Begins**: Content creation, optimization work
4. **Progress Tracking**: Weekly check-ins on roadmap
5. **Re-Analysis**: Run GEO analysis again in 4-8 weeks to measure progress

---

## MCP Tools Needed

**None** - This approach uses only built-in tools (Read, Write, Edit)

Strategy synthesis is primarily about data aggregation and narrative creation, which the agent can do natively without custom tools.

---

## Report Quality Guidelines

### Good Report Characteristics
✅ **Data-Driven**: Every recommendation backed by specific data
✅ **Actionable**: Clear action items with timelines
✅ **Prioritized**: Recommendations ranked by impact/effort
✅ **Realistic**: Honest about effort and timeline required
✅ **Measurable**: Specific success metrics defined

### Bad Report Examples
❌ Vague recommendations ("improve content")
❌ No prioritization (everything is "high priority")
❌ Unrealistic timelines ("increase visibility 50% in 1 week")
❌ No metrics ("make things better")
❌ Missing rationale (why these recommendations?)
