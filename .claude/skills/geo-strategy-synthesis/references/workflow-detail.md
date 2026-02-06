# GEO Strategy Synthesis - Detailed Reference

This file contains full metric schemas, report templates, and extended examples referenced by the main SKILL.md.

## Full Key Metrics Schemas

### Overall Performance Metrics

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
    "problem-solution": "5.0%",
    "exploratory": "0%"
  },
  "by_funnel_stage": {
    "decision": "25.4%",
    "consideration": "22.1%",
    "awareness": "9.5%",
    "retention": "0%"
  }
}
```

### Competitive Position

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

### Content Performance

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

## High-Value Opportunities Schema

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

## LIGHT Mode Report Template

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
- **Tests Run**: 40 (20 prompts x 2 engines)
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
   - Perplexity: 28.0% (showing it is possible)
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

## DEEP Mode Report Template

**File**: `/docs/marketing/geo-analysis-{company}-deep.md`

```markdown
# Comprehensive GEO Analysis - {Company Name}

**Report Date**: {date}
**Execution Mode**: DEEP
**Analysis Coverage**: 95 prompts, 3 engines, 847 citations analyzed

---

## Table of Contents
1. Executive Summary
2. Current Performance Analysis
3. Competitive Benchmarking
4. Content Performance
5. Critical Gaps & Opportunities
6. Strategic Recommendations
7. Implementation Roadmap
8. Success Metrics
9. Appendix

---

## 1. Executive Summary

### Key Findings

**Current GEO Performance**:
- Overall visibility: **16.8%** (vs 25-35% industry benchmark)
- Total tests: 285 across 3 AI engines
- Brand citations: 48 (17% of tests)
- Competitive rank: **3rd place** (behind Zendesk & Intercom)

**Strengths**:
- Strong Perplexity performance (29.5% - above benchmark)
- High sentiment quality (81% positive when mentioned)
- Effective data-driven content (top blog has 12 citations)

**Critical Gaps**:
- Weak ChatGPT presence (12.6% vs 29.5% on Perplexity)
- Gemini severely underperforming (8.4% vs 20%+ benchmark)
- Missing awareness-stage visibility (9.5% vs 25% target)
- No presence in problem-solution queries (5% vs 25% target)

**Top 3 Strategic Opportunities**:
1. "AI Customer Support" Content Gap (+8-10% visibility)
2. Problem-Solution Content (+5-7% visibility)
3. Gemini Optimization (+10-15% on Gemini)

**Projected Impact**:
- Timeline: 12 weeks
- Visibility Improvement: +15-20%
- Investment: 100-120 hours, $5-8K
- Expected Result: Move from 16.8% to 32-37% visibility

---

## 2. Current Performance Analysis

### 2.1 Overall Metrics

| Metric | Value | Benchmark | Status |
|--------|-------|-----------|--------|
| Overall Visibility | 16.8% | 25-35% | Below |
| Total Tests | 285 | N/A | Comprehensive |
| Brand Mentions | 48 | N/A | - |
| Average Citation Position | 2.8 | < 2.0 target | Low |
| Sentiment (when mentioned) | 81% positive | > 75% | Good |

### 2.2 Performance by Engine

| Engine | Visibility | vs Benchmark | Rank | Assessment |
|--------|-----------|--------------|------|------------|
| Perplexity | 29.5% | +4.5% | 2nd | Strength |
| ChatGPT | 12.6% | -12.4% | 3rd | Critical Gap |
| Gemini | 8.4% | -21.6% | 4th | Severe Gap |

**Insight**: Perplexity success proves we CAN compete. Need to replicate on ChatGPT and Gemini.

### 2.3 Performance by Question Type

| Question Family | Tests | Mentions | Visibility | Target | Gap |
|----------------|-------|----------|-----------|--------|-----|
| Comparison | 75 | 22 | 29.3% | 25-30% | On Target |
| Recommendation | 60 | 15 | 25.0% | 25-30% | On Target |
| Informational | 60 | 8 | 13.3% | 20-25% | Below |
| Problem-Solution | 60 | 3 | 5.0% | 25-30% | Critical |
| Exploratory | 30 | 0 | 0% | 15-20% | Missing |

**Insight**: Strong in bottom-funnel (comparison/recommendation), weak in top-funnel (problem-solution/exploratory).

---

## 6. Strategic Recommendations

### Priority 1: Close Critical Gaps (Weeks 1-4)

#### 6.1 Target "AI Customer Support" Keyword Family

**Gap Analysis**:
- Current visibility: 0 citations
- Competitor visibility: Zendesk (25), Intercom (18)
- Search intent: Awareness + Consideration
- Opportunity: HIGH

**Strategy**: Create comprehensive pillar page + supporting cluster

**Action Plan**:
1. Week 1: Research + Create Pillar Page (3500-word guide with definitions, use cases, ROI calculator, buyer's guide, structured data)
2. Week 2-3: Create 5 Cluster Articles
3. Week 4: Promotion (social media, email, outreach)

**Resources**: Content writer (60h), SEO specialist (8h), Designer (6h), Budget $3-4K

**Success Metrics**:
- Cited by 2/3 engines within 30 days
- +5-8% visibility on awareness queries
- 5,000+ organic pageviews in first 60 days

**Expected Impact**: +8-10% overall visibility

---

## 7. Implementation Roadmap

### 12-Week GEO Optimization Roadmap

#### Phase 1: Quick Wins (Weeks 1-2)
- Week 1: Create "AI Customer Support" pillar page (Research 8h, Draft 16h, Review 8h, Publish 4h)
- Week 2: Optimize top 3 existing pages (FAQ sections 6h, Structured data 4h, Internal linking 2h)
- Expected Impact: +3-5% visibility

#### Phase 2: Content Sprint (Weeks 3-6)
- Week 3: Create 3 problem-solution articles
- Week 4: Create 2 awareness-stage guides
- Week 5-6: Promote + monitor
- Expected Impact: +5-7% visibility

#### Phase 3: Technical Optimization (Weeks 7-8)
- Schema.org across all content
- Topic cluster architecture
- Internal linking structure
- "Key Takeaways" sections
- Expected Impact: +2-4% visibility

#### Phase 4: Authority Building (Weeks 9-12)
- Authoritative backlinks outreach
- Original research/survey
- Guest posts on high-authority sites
- Speaking engagements/webinars
- Expected Impact: +3-5% visibility

**Total Projected Impact**: +13-21% visibility improvement
**Total Investment**: 100-120 hours, $5-8K budget

---

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

---

## 9. Appendix

### A. Full Prompt List
Link to /data/geo/prompts-{company}-deep.json

### B. Raw Test Results
Link to /data/geo/test-results-{company}-deep.json

### C. Citation Analysis
Link to /data/geo/citation-analysis-{company}-deep.json

### D. Competitor Deep-Dive
Detailed section on each competitor

### E. Technical Implementation Guide
Step-by-step instructions for Schema.org, topic clusters, etc.

---

**Report Generated**: {timestamp}
**Total Analysis Time**: ~20 minutes
**Next Recommended Action**: Review recommendations, approve Phase 1 Quick Wins
```
