# Data Synthesis & Strategic Insights

## Purpose
Synthesize data from multiple marketing analyses (GEO, SEO, Ads, Competitor, Content) to identify cross-channel patterns, resolve conflicts, prioritize opportunities, and generate cohesive strategic recommendations.

---

## When to Use This Skill

Use this skill AFTER completing multiple channel analyses to:
- Combine insights from different sources
- Identify patterns across channels
- Resolve conflicting data or recommendations
- Prioritize initiatives by impact
- Create unified strategic narratives
- Generate executive summaries

---

## Prerequisites

**Required Input**:
- At least 2 data sources from:
  - GEO analysis
  - SEO analysis
  - Ads campaign analysis
  - Competitor analysis
  - Content performance data
  - Audience insights

**Optional**:
- Business goals (revenue targets, market share, etc.)
- Resource constraints (budget, team size)
- Strategic priorities

---

## Workflow Steps

### Step 1: Data Collection & Inventory

**Load all available analysis files**:

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

// Extract key metrics from each source
const keyMetrics = {
  geo: {
    visibility: dataInventory.geo.current_state.brand_visibility_percentage,
    top_opportunity: dataInventory.geo.priority_recommendations[0]
  },
  seo: {
    health_score: dataInventory.seo.overall_health_score,
    monthly_traffic: dataInventory.seo.estimated_organic_traffic,
    top_issue: dataInventory.seo.critical_issues[0]
  },
  ads: {
    overall_roas: dataInventory.ads_campaigns.overall_performance.roas,
    total_spend: dataInventory.ads_campaigns.overall_performance.spend,
    best_platform: dataInventory.ads_campaigns.cross_platform_insights.best_platform
  }
};
```

---

### Step 2: Cross-Channel Pattern Identification

**Look for patterns that emerge across multiple channels**:

#### Pattern Type 1: Audience Alignment

```
Question: Do insights about target audience align across channels?

From Ads Audience Analysis:
- Best performing: Female, 25-34, Small Business Owners
- CPA: $26.50, ROAS: 4.8

From SEO Content Optimization:
- Top engaging content: "Small Business Marketing Guide"
- High converting keyword: "marketing automation for small business"

From GEO Analysis:
- Best visibility on prompts targeting: Small business marketing needs

SYNTHESIS:
✅ STRONG ALIGNMENT - All channels point to same core audience
✅ Recommendation: Double down on "Small Business Owner" targeting across ALL channels
```

#### Pattern Type 2: Channel Conflicts

```
Question: Are different channels telling different stories?

From Ads Analysis:
- LinkedIn Ads underperforming (ROAS 1.8)
- Recommendation: Reduce LinkedIn budget

From Competitor Analysis:
- Competitors heavily investing in LinkedIn
- Strong presence at industry events (B2B focus)

SYNTHESIS:
⚠️ CONFLICT - Your LinkedIn underperformance might be execution issue, not channel issue
🔍 DEEPER DIVE NEEDED:
  - Are competitors in same B2B segment as you?
  - Is your LinkedIn creative/targeting different?
  - What's your LinkedIn content strategy vs competitors?

RESOLUTION:
Option A: If B2B is core audience → Don't abandon LinkedIn, fix approach
Option B: If B2C is primary → Reduce LinkedIn, it's right channel for competitors but wrong for you
```

#### Pattern Type 3: Reinforcing Signals

```
Question: Do multiple channels point to same opportunity?

GEO Analysis:
- Low visibility (12%) in AI search engines
- Opportunity: +15% visibility with 5 content pieces

SEO Content:
- Thin content (avg 520 words vs competitor 1,450 words)
- Recommendation: Expand content depth

Competitor Analysis:
- Competitors publish 12 posts/month vs your 4
- They have 3x organic traffic

SYNTHESIS:
🎯 REINFORCING SIGNAL - "Content Gap" appears across all analyses
💡 STRATEGIC INSIGHT: Content is your #1 bottleneck
   - Blocking GEO visibility (need citeable thought leadership)
   - Blocking SEO growth (thin content doesn't rank)
   - Allowing competitors to dominate (3x output advantage)

RECOMMENDATION:
- Triple content output: 4 → 12 posts/month
- Increase depth: 520 → 1,500 words average
- Focus on thought leadership for AI citation
- Expected impact: +15% GEO, +40% SEO traffic, narrow competitor gap
```

---

### Step 3: Opportunity Prioritization Matrix

**Score opportunities by impact, effort, and strategic fit**:

```javascript
// Collect all recommendations from all analyses
const allRecommendations = [
  ...dataInventory.geo.priority_recommendations,
  ...dataInventory.seo.implementation_roadmap.week_1_quick_wins,
  ...dataInventory.ads_campaigns.optimization_roadmap.immediate_actions,
  // ... etc
];

// Score each opportunity
const scoredOpportunities = allRecommendations.map(opp => ({
  ...opp,
  impact_score: calculateImpact(opp),        // 0-100
  effort_score: calculateEffort(opp),         // 0-100 (lower = easier)
  strategic_fit: calculateStrategicFit(opp),  // 0-100
  confidence: calculateConfidence(opp),       // 0-100

  // Overall priority score
  priority_score: (
    (impact_score * 0.40) +
    ((100 - effort_score) * 0.30) +  // Invert effort (easier = better)
    (strategic_fit * 0.20) +
    (confidence * 0.10)
  )
}));

// Rank by priority score
const rankedOpportunities = scoredOpportunities.sort((a, b) =>
  b.priority_score - a.priority_score
);
```

**Example Prioritization**:

```json
{
  "opportunity_matrix": [
    {
      "rank": 1,
      "opportunity": "Reallocate ads budget from LinkedIn to Google",
      "source": "Ads Campaign Analysis",
      "impact_score": 85,
      "effort_score": 10,
      "strategic_fit": 90,
      "confidence": 95,
      "priority_score": 90.5,
      "expected_impact": "+$8,000 monthly revenue",
      "time_to_implement": "2 hours",
      "category": "QUICK WIN"
    },
    {
      "rank": 2,
      "opportunity": "Triple content output (4 → 12 posts/month)",
      "source": "Cross-Channel Pattern (GEO + SEO + Competitor)",
      "impact_score": 95,
      "effort_score": 70,
      "strategic_fit": 95,
      "confidence": 85,
      "priority_score": 80.5,
      "expected_impact": "+15% GEO visibility, +40% SEO traffic",
      "time_to_implement": "Ongoing (3-6 months)",
      "category": "STRATEGIC INITIATIVE"
    },
    {
      "rank": 3,
      "opportunity": "Fix top 5 SEO technical issues",
      "source": "SEO Technical Audit",
      "impact_score": 70,
      "effort_score": 30,
      "strategic_fit": 75,
      "confidence": 90,
      "priority_score": 76.0,
      "expected_impact": "+25% organic traffic",
      "time_to_implement": "2 weeks",
      "category": "QUICK WIN"
    }
  ]
}
```

---

### Step 4: Conflict Resolution

**Identify and resolve conflicting recommendations**:

#### Conflict Type 1: Budget Allocation

```
Source A (Ads Analysis):
- Recommendation: Increase Google Ads budget by $5,000/month

Source B (SEO Analysis):
- Recommendation: Invest $5,000/month in content creation

Source C (GEO Analysis):
- Recommendation: Invest $3,000/month in thought leadership content

CONFLICT: Limited budget ($8,000 available), but $13,000 in recommendations

RESOLUTION FRAMEWORK:
1. Calculate ROI for each:
   - Google Ads: $5K → $25K revenue (5x ROAS) = $20K return
   - SEO Content: $5K → $12K revenue over 6 months = $7K return (but ongoing)
   - GEO Content: $3K → $8K revenue over 6 months = $5K return (but emerging channel)

2. Consider strategic fit:
   - Immediate revenue need? → Prioritize Google Ads
   - Long-term growth goal? → Balance Ads + Content
   - Competitive positioning? → Content + GEO

3. Phased approach:
   Month 1: Google Ads (+$3K), SEO Content (+$3K), GEO Content (+$2K) = $8K total
   Month 2: Evaluate results, shift budget to winner
   Month 3+: Scale winning channel

SYNTHESIZED RECOMMENDATION:
- Allocate $8K across all three (hedged approach)
- Prioritize quick wins (Google Ads) for cash flow
- Invest in content (SEO+GEO) for long-term compounding
- Re-evaluate monthly based on performance
```

#### Conflict Type 2: Messaging & Positioning

```
Source A (Ads Audience Insights):
- Best performing message: "Reduce support tickets by 50%"
- Benefit-focused, metric-heavy

Source B (Competitor Analysis):
- Competitors lead with: "Easiest to use customer support platform"
- Simplicity-focused, ease-of-use

Source C (GEO Analysis):
- AI engines cite you for: "AI-powered automation"
- Technology-focused, innovation

CONFLICT: Different value propositions resonating in different channels

RESOLUTION:
1. Segmentation approach:
   - Paid ads (high intent): "Reduce tickets by 50%" (results-driven)
   - Organic/GEO (research phase): "AI-powered automation" (education)
   - Competitive differentiation: "Easiest AI support platform" (combines both)

2. Unified framework:
   Core: "AI customer support that's powerful and easy"
   Proof: "Reduce tickets 50%"
   Differentiation: "Unlike competitors, we're both powerful AND simple"

SYNTHESIZED MESSAGING:
- Hero message: "The Easiest Way to Reduce Support Tickets by 50%"
  (Combines ease of use + results)
- Supporting: "Powered by AI, designed for humans"
- Proof points: Customer testimonials showing both ease AND results
```

---

### Step 5: Strategic Theme Identification

**Extract overarching strategic themes**:

```
Review all insights and identify 3-5 strategic themes:

Theme 1: "Content is the Multiplier"
Evidence:
- GEO visibility blocked by lack of citeable content
- SEO rankings limited by thin content
- Competitors winning with 3x content output
- Paid ads need supporting content for conversion

Impact: Content improvements benefit ALL channels simultaneously
Priority: HIGH - foundational issue

Theme 2: "Mid-Market White Space"
Evidence:
- Your pricing ($29/user) between Competitor B ($25) and A ($39)
- Competitor A targeting enterprise, B targeting SMB
- Mid-market (100-500 employees) underserved
- Your feature set matches mid-market needs

Impact: Clear positioning opportunity in gap
Priority: MEDIUM - requires messaging shift

Theme 3: "Paid Acquisition Efficiency Gap"
Evidence:
- Google Ads ROAS 4.2 (excellent)
- Meta Ads ROAS 3.5 (good)
- LinkedIn ROAS 1.8 (poor)
- Budget misallocated to underperforming channels

Impact: Quick revenue wins through reallocation
Priority: HIGH - low effort, high return

Theme 4: "AI Search Engine First-Mover Window Closing"
Evidence:
- GEO visibility currently 12% (low but measurable)
- Competitors at 28-45% (ahead but not dominant)
- AI search adoption growing 50% YoY
- Window to establish presence before saturation

Impact: Future-proofing brand visibility
Priority: MEDIUM-HIGH - time-sensitive

Theme 5: "Feature Parity Achieved, Awareness Lacking"
Evidence:
- Product features comparable to competitors
- Unique features (video, real-time collab) not well known
- Weak brand recognition (85 reviews vs competitor's 450)
- Low organic reach (SEO, GEO both lagging)

Impact: Product is strong, go-to-market is weak
Priority: HIGH - build awareness engine
```

---

### Step 6: Create Unified Narrative

**Synthesize into cohesive story**:

```markdown
## Strategic Narrative: AcmeCorp Marketing Analysis

### Current State
AcmeCorp has built a strong product with unique features (real-time collaboration, built-in video) and competitive pricing ($29/user). However, the company faces a **visibility crisis** across all marketing channels:

- **GEO**: Only 12% visibility in AI search engines (vs 45% for competitors)
- **SEO**: 35K monthly organic traffic (vs 250K for Competitor A)
- **Ads**: Solid ROAS (3.2) but underutilizing best-performing channels
- **Brand**: Weak awareness (85 reviews vs 450 for competitors)

### Root Cause
Deep analysis across all channels points to a **single core issue**: **Content deficit**

The company produces 1/3 the content volume (4 posts/month vs 12) with 1/3 the depth (520 words vs 1,450 words) compared to competitors. This content gap cascades across all channels:

1. **GEO Impact**: AI engines can't cite AcmeCorp (insufficient thought leadership)
2. **SEO Impact**: Thin content doesn't rank (algorithm favors comprehensive content)
3. **Paid Ads Impact**: Weak organic presence requires higher paid spend
4. **Competitive Impact**: Competitors dominate awareness with content advantage

### The Opportunity
Despite the visibility deficit, AcmeCorp has **three fundamental advantages**:

1. **Product Differentiation**: Unique features competitors lack (video, real-time collab)
2. **Positioning White Space**: Mid-market gap between enterprise (Competitor A) and SMB (Competitor B) solutions
3. **Paid Efficiency**: Google Ads ROAS of 4.2 shows strong unit economics when audience is reached

The challenge isn't product-market fit—it's **awareness generation**.

### Strategic Recommendation
**Three-Pillar Strategy** to close visibility gap:

**Pillar 1: Content Acceleration** (Foundational)
- Triple content output: 4 → 12 posts/month
- Double content depth: 520 → 1,500 words
- Focus on thought leadership (AI citation + SEO ranking)
- Timeline: 90 days to ramp up
- Expected Impact: +15% GEO visibility, +40% SEO traffic

**Pillar 2: Paid Optimization** (Immediate Revenue)
- Reallocate budget from LinkedIn to Google (+$4K/month)
- Scale top-performing campaigns (Google Brand Search)
- Test video creative (addressing creative gap vs competitors)
- Timeline: Immediate
- Expected Impact: +$8K monthly revenue

**Pillar 3: Positioning Clarity** (Differentiation)
- Own mid-market segment: "Enterprise features at SMB prices"
- Lead with unique features (video, real-time collab)
- Messaging: "Reduce tickets 50% without complexity"
- Timeline: 30 days
- Expected Impact: Better conversion rates, clearer competitive position

### Expected Outcomes (90 Days)
- **Revenue**: +$45K/month (+47% growth)
- **ROAS**: 3.2 → 4.5 (+41% improvement)
- **Organic Traffic**: +40% (SEO improvements)
- **GEO Visibility**: 12% → 25% (AI search)
- **Competitive Position**: Stronger differentiation in mid-market

### Investment Required
- Content Production: $15K (ramp-up + 3 months)
- Ads Reallocation: $0 (budget neutral)
- Positioning/Messaging: $5K (creative refresh)
- **Total: $20K over 90 days**
- **ROI: 675% ($135K additional revenue / $20K investment)**

### Risk Mitigation
**Risk 1**: Content quality decline with 3x output increase
*Mitigation*: Hire 2 specialist writers vs generalists, implement editorial process

**Risk 2**: Google Ads scaling hits diminishing returns
*Mitigation*: Phase budget increase (+30% month 1, assess, then +20% more if performing)

**Risk 3**: Messaging change confuses existing customers
*Mitigation*: Test new messaging with new audience segments first, gradual rollout

### Success Metrics (Track Monthly)
1. Content velocity: # of posts published
2. GEO visibility: % of test prompts with brand mention
3. SEO traffic: Organic sessions (Google Analytics)
4. Ads ROAS: Revenue / Spend by platform
5. Brand awareness: Review count, branded search volume

---

**Decision Required**: Approve three-pillar strategy and $20K budget for 90-day sprint?
```

---

### Step 7: Output Generation

**Create synthesis report**:

```json
{
  "metadata": {
    "report_type": "Strategic Synthesis",
    "company": "AcmeCorp",
    "data_sources": 8,
    "analyses_synthesized": ["GEO", "SEO", "Ads", "Competitor", "Audience", "Creative"],
    "generated_at": "2024-01-15T20:00:00Z",
    "synthesis_duration_minutes": 35
  },
  "executive_summary": {
    "current_state": "Strong product, weak visibility",
    "root_cause": "Content deficit (1/3 volume, 1/3 depth vs competitors)",
    "strategic_themes": [
      "Content is the multiplier (affects all channels)",
      "Mid-market positioning white space",
      "Paid efficiency proven, needs scale",
      "AI search first-mover window closing"
    ],
    "recommended_strategy": "Three-pillar: Content Acceleration + Paid Optimization + Positioning Clarity",
    "expected_roi": "675% over 90 days",
    "confidence_level": "HIGH (85%)"
  },
  "cross_channel_insights": {
    "audience_alignment": {
      "status": "STRONG ALIGNMENT",
      "core_audience": "Female, 25-34, Small Business Owners",
      "evidence_sources": ["Ads Audience", "SEO Content", "GEO Prompts"],
      "recommendation": "Double down on this segment across ALL channels"
    },
    "messaging_synthesis": {
      "unified_message": "The Easiest Way to Reduce Support Tickets by 50%",
      "rationale": "Combines top-performing benefit (50% reduction) with competitive advantage (ease)",
      "channel_adaptations": {
        "paid_ads": "Lead with metric (50% reduction)",
        "organic_seo": "Lead with problem (ticket overload solutions)",
        "geo_content": "Lead with technology (AI automation explained)"
      }
    },
    "budget_optimization": {
      "current_allocation": {"google": 50, "meta": 33, "linkedin": 17},
      "recommended_allocation": {"google": 60, "meta": 30, "linkedin": 10},
      "shift_rationale": "Google ROAS 2.3x better than LinkedIn",
      "expected_impact": "+26% overall ROAS"
    }
  },
  "opportunity_ranking": {
    "quick_wins": [
      {
        "rank": 1,
        "opportunity": "Reallocate ads budget (LinkedIn → Google)",
        "impact": "$8K/month revenue",
        "effort": "2 hours",
        "roi": "4000%"
      },
      {
        "rank": 2,
        "opportunity": "Fix top 5 SEO technical issues",
        "impact": "+25% organic traffic",
        "effort": "2 weeks",
        "roi": "300%"
      }
    ],
    "strategic_initiatives": [
      {
        "rank": 1,
        "initiative": "Content acceleration (3x output)",
        "impact": "Multi-channel (GEO +15%, SEO +40%, Ads conversion +12%)",
        "effort": "3-6 months",
        "investment": "$15K",
        "roi": "560%"
      },
      {
        "rank": 2,
        "initiative": "Mid-market positioning campaign",
        "impact": "Better conversion rates, competitive differentiation",
        "effort": "1-2 months",
        "investment": "$5K",
        "roi": "280%"
      }
    ]
  },
  "conflict_resolutions": [
    {
      "conflict": "Budget allocation (Ads vs SEO vs GEO)",
      "competing_recommendations": {
        "ads": "$5K more to Google Ads",
        "seo": "$5K to content creation",
        "geo": "$3K to thought leadership"
      },
      "resolution": "Phased allocation: $3K Ads, $3K SEO, $2K GEO = $8K total",
      "rationale": "Hedged approach balances immediate revenue (Ads) with long-term growth (Content)"
    }
  ],
  "implementation_roadmap": {
    "month_1": {
      "focus": "Quick wins + Foundation",
      "actions": [
        "Reallocate ads budget (immediate)",
        "Fix SEO technical issues (week 1-2)",
        "Hire 2 content writers (week 1-2)",
        "Launch positioning refresh (week 3-4)"
      ],
      "expected_impact": "+$12K revenue"
    },
    "month_2": {
      "focus": "Content ramp + Paid scale",
      "actions": [
        "Publish 12 pieces (3x current output)",
        "Increase Google Ads budget 30%",
        "Test video creative",
        "Monitor GEO visibility weekly"
      ],
      "expected_impact": "+$28K revenue"
    },
    "month_3": {
      "focus": "Optimize + Measure",
      "actions": [
        "Refine content based on GEO/SEO performance",
        "Scale winning ad creative",
        "Comprehensive results review",
        "Plan next 90-day sprint"
      ],
      "expected_impact": "+$45K revenue (cumulative)"
    }
  },
  "risk_assessment": {
    "high_risks": [
      {
        "risk": "Content quality suffers with 3x output increase",
        "likelihood": "Medium",
        "impact": "High",
        "mitigation": "Hire specialists, implement editorial process, quality > quantity if needed"
      }
    ],
    "medium_risks": [
      {
        "risk": "Google Ads scaling hits diminishing returns",
        "likelihood": "Medium",
        "impact": "Medium",
        "mitigation": "Phase increase (+30%, assess, then +20% more only if ROAS maintained)"
      }
    ],
    "low_risks": []
  },
  "success_metrics": [
    {
      "metric": "Monthly Revenue",
      "current": "$96K",
      "target_90_days": "$135K",
      "measurement": "Ads platform revenue tracking"
    },
    {
      "metric": "Overall ROAS",
      "current": "3.2",
      "target_90_days": "4.5",
      "measurement": "Revenue / Ad Spend"
    },
    {
      "metric": "GEO Visibility",
      "current": "12%",
      "target_90_days": "25%",
      "measurement": "Monthly prompt testing (100 prompts)"
    },
    {
      "metric": "Organic Traffic",
      "current": "35K/month",
      "target_90_days": "49K/month",
      "measurement": "Google Analytics"
    },
    {
      "metric": "Content Output",
      "current": "4 posts/month",
      "target_90_days": "12 posts/month",
      "measurement": "Editorial calendar"
    }
  ]
}
```

---

## Validation Checks

```
✓ At least 2 data sources synthesized
✓ Cross-channel patterns identified
✓ Conflicts resolved with clear rationale
✓ Opportunities prioritized by impact
✓ Unified narrative created
✓ Strategic themes extracted (3-5)
✓ Implementation roadmap provided
✓ ROI calculations included
✓ Risk assessment completed
✓ Success metrics defined
```

---

## Usage Example

**Agent Workflow**:
```
1. Read this skill file
2. Load all available analysis data files
3. Use TodoWrite to track synthesis:
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

---

## Integration with Other Skills

**Requires data from**:
- ALL analysis skills (GEO, SEO, Ads, Competitor, etc.)

**Feeds into**:
- **presentation-creation.md** - Executive presentations
- Strategic planning sessions
- Quarterly business reviews

---

## MCP Tools Needed

**Current**: Built-in tools sufficient (Read, Write, data processing)

**Future Enhancement**:
- `mcp__Analytics__data_integrator` - Auto-load and normalize data from all sources
- `mcp__Analytics__pattern_detector` - ML-powered pattern identification
- `mcp__Analytics__scenario_planner` - Model different strategic scenarios
