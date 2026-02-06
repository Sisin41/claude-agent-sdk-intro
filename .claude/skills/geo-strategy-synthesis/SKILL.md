---
name: geo-strategy-synthesis
description: Synthesize all GEO analysis data into a comprehensive strategic report with prioritized, actionable recommendations and a 12-week implementation roadmap. Use as the final step after geo-citation-analysis to produce the deliverable report.
metadata:
  author: castor
  version: "1.0"
  domain: geo
  execution-modes: light, deep
---

# GEO Strategy Synthesis

## Purpose

Synthesize all GEO analysis data (company value, prompts, test results, citations) into a comprehensive strategic report with prioritized, actionable recommendations.

## Prerequisites

**Required Inputs**:
1. Company value data: `/data/geo/company-value-{company}-{mode}.json`
2. Generated prompts: `/data/geo/prompts-{company}-{mode}.json`
3. Test results: `/data/geo/test-results-{company}-{mode}.json`
4. Citation analysis: `/data/geo/citation-analysis-{company}-{mode}.json`

**No external tools required** -- Uses Read, Write, Edit only.

## Execution Modes

### LIGHT Mode
- **Report Length**: 2-3 pages
- **Content**: High-level findings + top 3 recommendations
- **Expected Time**: 2-3 minutes

### DEEP Mode
- **Report Length**: 15-20 pages
- **Content**: Comprehensive analysis + detailed 12-week roadmap
- **Expected Time**: 5-8 minutes

## Workflow Steps

### Step 1: Load All Data Sources

```
Read and parse:
1. /data/geo/company-value-{company}-{mode}.json
2. /data/geo/prompts-{company}-{mode}.json
3. /data/geo/test-results-{company}-{mode}.json
4. /data/geo/citation-analysis-{company}-{mode}.json

Validate all files exist and are parseable.
```

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
  }
}
```

Calculate breakdowns by engine, question type, funnel stage, and competitive position. See `references/workflow-detail.md` for full metric schemas.

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
      "competitor_visibility": "Zendesk 35%, Intercom 28%",
      "opportunity_value": "+15-20% overall visibility if fixed"
    }
  ]
}
```

**High-Value Opportunities**: Identify keyword families, content gaps, and engine-specific opportunities with estimated impact and effort.

### Step 4: Develop Strategic Recommendations

**Prioritization Framework**:
```
Priority = (Impact x Feasibility) / Effort

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
    "Research keyword family",
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
  "rationale": "Data-driven justification for this recommendation"
}
```

### Step 5: Create Implementation Roadmap

**LIGHT Mode**: Simple task list with top 3 quick wins.

**DEEP Mode**: Detailed 12-week plan:

**Phase 1: Quick Wins (Weeks 1-2)**
- Create pillar page for top keyword gap
- Optimize top 3 existing pages (FAQ sections, structured data, internal linking)
- Expected Impact: +3-5% visibility

**Phase 2: Content Sprint (Weeks 3-6)**
- Create 3 problem-solution articles targeting pain points
- Create 2 awareness-stage guides
- Promote and monitor
- Expected Impact: +5-7% visibility

**Phase 3: Technical Optimization (Weeks 7-8)**
- Implement Schema.org across all content
- Build topic cluster architecture
- Improve internal linking structure
- Add "Key Takeaways" sections
- Expected Impact: +2-4% visibility

**Phase 4: Authority Building (Weeks 9-12)**
- Outreach for authoritative backlinks
- Create original research/survey
- Guest posts on high-authority sites
- Expected Impact: +3-5% visibility

**Total Projected Impact**: +13-21% visibility improvement

### Step 6: Generate Report

**LIGHT Mode Report**: `/docs/marketing/geo-analysis-{company}-light.md`

Contents:
- Executive Summary (current performance, top 3 opportunities)
- Quick Wins (next 2-4 weeks with time and impact estimates)
- Expected Results (timeline, visibility improvement, investment)
- Next Steps

**DEEP Mode Report**: `/docs/marketing/geo-analysis-{company}-deep.md`

Contents:
- Executive Summary (key findings, strengths, critical gaps, top 3 opportunities)
- Current Performance Analysis (overall metrics, by engine, by question type, by funnel stage)
- Competitive Benchmarking
- Content Performance
- Critical Gaps & Opportunities
- Strategic Recommendations (prioritized with action plans)
- Implementation Roadmap (12-week Gantt chart)
- Success Metrics (leading indicators, lagging indicators, 12-week targets)
- Appendix (links to data files)

See `references/workflow-detail.md` for full report templates.

## Validation Checks

Before saving report:

1. **Data Completeness**: All input files successfully loaded
2. **Metrics Calculated**: All key performance metrics computed
3. **Recommendations Present**: At least 3 prioritized recommendations
4. **Roadmap Included**: Timeline with specific action items
5. **File Links Work**: All references to data files are valid

## Report Quality Guidelines

### Good Report Characteristics
- **Data-Driven**: Every recommendation backed by specific data
- **Actionable**: Clear action items with timelines
- **Prioritized**: Recommendations ranked by impact/effort
- **Realistic**: Honest about effort and timeline required
- **Measurable**: Specific success metrics defined

### Bad Report Examples
- Vague recommendations ("improve content")
- No prioritization (everything is "high priority")
- Unrealistic timelines ("increase visibility 50% in 1 week")
- No metrics ("make things better")
- Missing rationale (why these recommendations?)

## Agent Workflow

```
1. Load all 4 data files from previous steps
2. Calculate key metrics
3. Identify gaps and opportunities
4. Generate prioritized recommendations
5. Create implementation roadmap
6. Write report (LIGHT or DEEP template)
7. Save markdown to /docs/marketing/
8. Provide summary to user:
   "GEO strategy complete!
    Current visibility: 16.8% (vs 25-35% benchmark)
    Top opportunity: 'AI customer support' content (+8-10%)
    12-week roadmap created
    Expected improvement: +15-20% visibility
    Full report: /docs/marketing/geo-analysis-{company}-deep.md"
```

## Next Steps After Synthesis

1. **User Reviews Report**: Human reviews recommendations
2. **Approval Gate**: User approves strategy or requests changes
3. **Implementation Begins**: Content creation, optimization work
4. **Progress Tracking**: Weekly check-ins on roadmap
5. **Re-Analysis**: Run GEO analysis again in 4-8 weeks to measure progress
