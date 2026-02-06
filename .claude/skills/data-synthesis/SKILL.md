---
name: data-synthesis
description: Synthesize data from multiple marketing analyses to identify cross-channel patterns, resolve conflicts, prioritize opportunities, and generate cohesive strategic recommendations. Use after completing multiple channel analyses to create unified strategic narratives.
metadata:
  author: castor
  version: "1.0"
  domain: shared
  execution-modes: light, deep
---

# Data Synthesis & Strategic Insights

## Purpose

Synthesize data from multiple marketing analyses (GEO, SEO, Ads, Competitor, Content) to identify cross-channel patterns, resolve conflicts, prioritize opportunities, and generate cohesive strategic recommendations.

## When to Use This Skill

Use this skill AFTER completing multiple channel analyses to:
- Combine insights from different sources
- Identify patterns across channels
- Resolve conflicting data or recommendations
- Prioritize initiatives by impact
- Create unified strategic narratives
- Generate executive summaries

## Prerequisites

**Required Input**:
- At least 2 data sources from: GEO analysis, SEO analysis, Ads campaign analysis, Competitor analysis, Content performance data, Audience insights

**Optional**:
- Business goals (revenue targets, market share, etc.)
- Resource constraints (budget, team size)
- Strategic priorities

## Workflow Steps

### Step 1: Data Collection & Inventory

Load all available analysis files and extract key metrics from each source:

```javascript
const dataInventory = {
  geo: readJSON('/data/geo/strategy-synthesis-acme-deep.json'),
  seo: readJSON('/data/seo/tech-audit-acme-comprehensive.json'),
  seo_keywords: readJSON('/data/seo/keywords-acme-comprehensive.json'),
  seo_content: readJSON('/data/seo/content-optimization-acme-comprehensive.json'),
  ads_campaigns: readJSON('/data/ads/campaign-analysis-acme-deep.json'),
  ads_audience: readJSON('/data/ads/audience-insights-acme-deep.json'),
  ads_creative: readJSON('/data/ads/creative-optimization-acme-deep.json'),
  competitor: readJSON('/data/competitor/competitive-analysis-acme-deep.json')
};
```

Extract key metrics (visibility %, health scores, ROAS, traffic, top issues, top opportunities) from each source for cross-referencing.

### Step 2: Cross-Channel Pattern Identification

Look for three types of patterns across channels:

**Pattern Type 1: Audience Alignment**
Do insights about target audience align across channels? If ads, SEO, and GEO all point to the same core audience segment, that is a strong alignment signal -- double down across ALL channels.

**Pattern Type 2: Channel Conflicts**
Are different channels telling different stories? For example, ads data may say "reduce LinkedIn budget" while competitor analysis shows competitors heavily investing in LinkedIn. Conflicts require deeper investigation -- the issue may be execution, not the channel itself.

**Pattern Type 3: Reinforcing Signals**
Do multiple channels point to the same opportunity? When GEO, SEO, and competitor data all identify a content gap, that is a reinforcing signal pointing to a foundational issue that affects all channels simultaneously.

See `references/workflow-detail.md` for detailed examples of each pattern type with resolution frameworks.

### Step 3: Opportunity Prioritization Matrix

Score all recommendations from all analyses using a weighted priority formula:

```
priority_score = (impact * 0.40) + ((100 - effort) * 0.30) + (strategic_fit * 0.20) + (confidence * 0.10)
```

Categorize each opportunity as:
- **QUICK WIN**: High impact, low effort (implement immediately)
- **STRATEGIC INITIATIVE**: High impact, high effort (plan and resource)
- **FILL-IN**: Low impact, low effort (do when capacity allows)
- **DEPRIORITIZE**: Low impact, high effort (skip or defer)

### Step 4: Conflict Resolution

When recommendations from different analyses compete for the same resources:

1. **Calculate ROI** for each competing recommendation
2. **Consider strategic fit** -- immediate revenue need vs long-term growth vs competitive positioning
3. **Apply phased approach** -- split budget across initiatives, evaluate monthly, shift to winner

Common conflict types:
- **Budget Allocation**: Multiple channels requesting same budget pool
- **Messaging & Positioning**: Different value propositions resonating in different channels

See `references/workflow-detail.md` for detailed conflict resolution frameworks with examples.

### Step 5: Strategic Theme Identification

Extract 3-5 overarching strategic themes from all insights. Each theme should have:
- Evidence from multiple sources
- Clear impact assessment
- Priority rating (HIGH / MEDIUM / LOW)

Example themes:
1. "Content is the Multiplier" -- content improvements benefit ALL channels
2. "Mid-Market White Space" -- positioning opportunity in underserved segment
3. "Paid Acquisition Efficiency Gap" -- quick revenue wins through budget reallocation
4. "AI Search First-Mover Window Closing" -- time-sensitive GEO opportunity
5. "Feature Parity Achieved, Awareness Lacking" -- product strong, go-to-market weak

### Step 6: Create Unified Narrative

Synthesize all findings into a cohesive strategic story:

```
1. Current State: Summarize overall position with data
2. Root Cause: Identify the single core issue (if applicable)
3. The Opportunity: Highlight fundamental advantages
4. Strategic Recommendation: 2-3 pillar strategy
5. Expected Outcomes: Quantified 90-day projections
6. Investment Required: Specific budget with ROI calculation
7. Risk Mitigation: Address top risks with concrete mitigations
8. Success Metrics: Monthly tracking KPIs with current/target values
```

See `references/workflow-detail.md` for a complete narrative example.

### Step 7: Output Generation

Save synthesis report to `/data/synthesis/` as structured JSON:

```json
{
  "metadata": {
    "report_type": "Strategic Synthesis",
    "company": "{company}",
    "data_sources": 8,
    "analyses_synthesized": ["GEO", "SEO", "Ads", "Competitor", "Audience", "Creative"],
    "generated_at": "{timestamp}"
  },
  "executive_summary": {
    "current_state": "...",
    "root_cause": "...",
    "strategic_themes": ["..."],
    "recommended_strategy": "...",
    "expected_roi": "...",
    "confidence_level": "..."
  },
  "cross_channel_insights": {
    "audience_alignment": { "status": "...", "core_audience": "...", "recommendation": "..." },
    "messaging_synthesis": { "unified_message": "...", "channel_adaptations": {} },
    "budget_optimization": { "current_allocation": {}, "recommended_allocation": {}, "expected_impact": "..." }
  },
  "opportunity_ranking": {
    "quick_wins": [],
    "strategic_initiatives": []
  },
  "conflict_resolutions": [],
  "implementation_roadmap": {
    "month_1": { "focus": "...", "actions": [], "expected_impact": "..." },
    "month_2": { "focus": "...", "actions": [], "expected_impact": "..." },
    "month_3": { "focus": "...", "actions": [], "expected_impact": "..." }
  },
  "risk_assessment": { "high_risks": [], "medium_risks": [], "low_risks": [] },
  "success_metrics": []
}
```

See `references/workflow-detail.md` for a complete populated JSON output example.

## Validation Checks

```
- At least 2 data sources synthesized
- Cross-channel patterns identified
- Conflicts resolved with clear rationale
- Opportunities prioritized by impact
- Unified narrative created
- Strategic themes extracted (3-5)
- Implementation roadmap provided
- ROI calculations included
- Risk assessment completed
- Success metrics defined
```

## Agent Workflow

```
1. Read this skill file
2. Load all available analysis data files
3. Track synthesis with TodoWrite:
   [ ] Data collection
   [ ] Cross-channel pattern identification
   [ ] Opportunity prioritization
   [ ] Conflict resolution
   [ ] Strategic theme extraction
   [ ] Narrative creation
   [ ] Roadmap development
   [ ] Risk assessment
   [ ] Output generation
4. Execute synthesis steps
5. Save to /data/synthesis/
6. Provide strategic summary
```

## Integration with Other Skills

**Requires data from**:
- ALL analysis skills (GEO, SEO, Ads, Competitor, etc.)

**Feeds into**:
- `presentation-creation` skill for executive presentations
- Strategic planning sessions
- Quarterly business reviews
