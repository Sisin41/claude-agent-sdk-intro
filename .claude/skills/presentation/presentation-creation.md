# Marketing Presentation Creation

## Purpose
Create professional marketing presentations from analysis data (GEO, SEO, Ads, Competitor analysis) with compelling narratives, data visualizations, and actionable recommendations in various formats.

---

## Execution Modes

### SIMPLE Mode (10-15 minutes)
**Goal**: Create concise executive summary presentation (5-10 slides)
**Scope**: High-level findings and top recommendations
**Output**: Executive-ready slide deck in markdown format

### COMPREHENSIVE Mode (30-45 minutes)
**Goal**: Create detailed analysis presentation (20-40 slides)
**Scope**: In-depth findings, visualizations, supporting data, implementation roadmap
**Output**: Full presentation deck with detailed appendix

---

## Prerequisites

**Required Input**:
- Analysis data from skills (GEO, SEO, Ads, Competitor)
  - JSON files from /data/geo/, /data/seo/, /data/ads/, etc.
- Presentation objective (inform, persuade, recommend)
- Target audience (executives, marketing team, board)

**Optional**:
- Brand colors and logo
- Company background information
- Specific formatting requirements

---

## Presentation Formats

### Format 1: Executive Summary (5-10 slides)
```
Target Audience: C-level, busy executives
Duration: 5-10 minute read
Purpose: Quick overview of findings and recommendations

Structure:
1. Title Slide
2. Executive Summary (1 slide)
3. Key Findings (2-3 slides)
4. Recommendations (1-2 slides)
5. Next Steps (1 slide)
```

### Format 2: Detailed Analysis (20-30 slides)
```
Target Audience: Marketing team, stakeholders
Duration: 20-30 minute presentation
Purpose: Comprehensive analysis with supporting data

Structure:
1. Title + Agenda
2. Executive Summary
3. Methodology
4. Detailed Findings (10-15 slides)
5. Competitive Analysis (3-5 slides)
6. Recommendations (3-5 slides)
7. Implementation Roadmap (2-3 slides)
8. Appendix (data tables, sources)
```

### Format 3: Pitch Deck (10-15 slides)
```
Target Audience: Clients, prospects, investors
Duration: 15-20 minute presentation
Purpose: Persuade and sell solution/strategy

Structure:
1. Title + Hook
2. Problem Statement
3. Current Situation Analysis
4. Our Solution/Recommendation
5. Results/Proof (case studies, projections)
6. Implementation Plan
7. Investment Required
8. Expected ROI
9. Next Steps
```

---

## Workflow Steps

### Step 1: Data Collection & Review

**Load analysis data**:

```
Read all relevant data files:
- GEO analysis: /data/geo/*-{company}-*.json
- SEO analysis: /data/seo/*-{company}-*.json
- Ads analysis: /data/ads/*-{company}-*.json
- Competitor analysis: /data/competitor/*-{company}-*.json

Extract key metrics:
- Overall performance scores
- Top opportunities
- Critical issues
- Recommendations
- Projected impact
```

**Example data extraction**:
```json
{
  "data_sources": [
    {
      "source": "GEO Strategy - DEEP Mode",
      "file": "/data/geo/strategy-synthesis-acme-deep.json",
      "key_findings": [
        "Brand visibility: 12% across AI engines (target: 40%)",
        "Top gap: Missing from 78% of consideration-stage queries",
        "Quick win: Optimize for 5 high-value prompts → +15% visibility in 30 days"
      ],
      "top_recommendation": "Focus on thought leadership content for AI citation"
    },
    {
      "source": "Ads Campaign Analysis - DEEP Mode",
      "file": "/data/ads/campaign-analysis-acme-deep.json",
      "key_findings": [
        "Overall ROAS: 3.2 (GOOD)",
        "Google Ads best performer (ROAS 4.2)",
        "LinkedIn underperforming (ROAS 1.8)"
      ],
      "top_recommendation": "Reallocate budget: +10% Google, -7% LinkedIn"
    }
  ]
}
```

---

### Step 2: Determine Narrative Arc

**Based on presentation format and audience**:

#### Executive Summary Narrative:
```
Arc: Situation → Problem → Solution → Impact

1. Where We Are (current state)
2. What's Working / Not Working (findings)
3. What We Recommend (actions)
4. Expected Results (projections)
```

#### Detailed Analysis Narrative:
```
Arc: Context → Deep Dive → Insights → Roadmap

1. Background and Methodology
2. Current Performance Analysis
3. Competitive Landscape
4. Opportunity Identification
5. Strategic Recommendations
6. Implementation Plan
```

#### Pitch Deck Narrative:
```
Arc: Problem → Agitate → Solution → Proof → Close

1. The Problem (pain points)
2. Why It Matters (urgency, cost of inaction)
3. Our Solution (strategy/service)
4. Proof It Works (data, case studies)
5. Investment & ROI
6. Call to Action
```

---

### Step 3: Create Slide Outline

**SIMPLE Mode - Executive Summary Example**:

```markdown
# Marketing Performance Analysis - Executive Summary
**For: AcmeCorp**
**Date: January 2024**

---

## Slide 1: Title
- Marketing Performance Analysis
- Executive Summary
- January 2024

## Slide 2: Executive Summary
**Current State**: Overall marketing performance is GOOD (68/100) but with significant untapped potential

**Key Findings**:
- GEO: Only 12% brand visibility in AI search engines (target: 40%)
- Ads: ROAS 3.2 with opportunity to improve to 4.5+
- SEO: Technical health 65/100, missing 15+ quick wins

**Recommendation**: Focus on 3 high-impact initiatives for 90-day sprint
**Projected Impact**: +35% overall marketing efficiency, +$45K monthly revenue

## Slide 3: Key Finding #1 - GEO Opportunity
**Issue**: Missing from 78% of high-value AI search queries
**Impact**: Losing awareness to competitors in fastest-growing channel
**Quick Win**: Optimize for top 5 prompts → +15% visibility in 30 days
**Investment**: $5K (content creation)

## Slide 4: Key Finding #2 - Ads Budget Misallocation
**Issue**: LinkedIn delivering 1.8 ROAS vs Google's 4.2 ROAS
**Impact**: $2,500/month wasted on underperforming platform
**Quick Win**: Reallocate budget → +$8K monthly revenue
**Investment**: 2 hours (campaign adjustments)

## Slide 5: Key Finding #3 - SEO Quick Wins Missed
**Issue**: 15+ critical SEO issues blocking 20-30% organic growth
**Impact**: Missing ~500 qualified visitors/month
**Quick Win**: Fix top 5 technical issues → +25% organic traffic in 60 days
**Investment**: $3K (development time)

## Slide 6: 90-Day Roadmap
**Month 1**: Implement all quick wins
- Ads reallocation
- Top 5 SEO fixes
- 5 GEO content pieces

**Month 2**: Expand winners
- Scale top-performing ad campaigns
- Content expansion
- GEO testing expansion

**Month 3**: Optimize and measure
- Refinement based on data
- Additional testing
- Results reporting

## Slide 7: Expected ROI
**Investment**: $15K over 90 days
**Expected Return**:
- Month 1: +$12K revenue
- Month 2: +$28K revenue
- Month 3: +$45K revenue

**ROI**: 567% over 90 days
**Payback Period**: <30 days

## Slide 8: Next Steps
**This Week**:
1. Approve budget ($15K)
2. Prioritize initiatives

**Next Week**:
1. Begin ads reallocation
2. Start SEO fixes
3. Brief content team on GEO strategy

**Decision Required**: Proceed with 90-day sprint? (Yes/No)
```

---

### Step 4: Create Data Visualizations

**For each slide with data**, create appropriate visualization:

#### Visualization Type 1: Performance Scorecard

```markdown
## Current Marketing Performance

| Category | Score | Status | Benchmark |
|----------|-------|---------|-----------|
| GEO (AI Visibility) | 12% | 🔴 Poor | 40% |
| SEO (Organic) | 65/100 | 🟡 Fair | 80+ |
| Paid Ads ROAS | 3.2 | 🟢 Good | 3.0 |
| Content Engagement | 72/100 | 🟢 Good | 70 |
| **Overall Score** | **68/100** | **🟡 Fair** | **75+** |

**Interpretation**: Good foundation but missing key opportunities in emerging channels (GEO) and technical optimization (SEO).
```

#### Visualization Type 2: Opportunity Matrix

```markdown
## Opportunity Prioritization Matrix

```
        Impact
          ↑
    HIGH  |  [Fix SEO Issues]     [GEO Content Strategy]
          |  Quick Win #1         Strategic Initiative
          |
          |
  MEDIUM  |  [Creative Refresh]   [Audience Expansion]
          |
          |
     LOW  |  [Minor Tweaks]       [Long-term Tests]
          |
          └──────────────────────────────────────────→
               LOW          MEDIUM          HIGH
                         Effort/Cost
```

**Focus Area**: Top-right quadrant (High Impact, Medium-High Effort)
```

#### Visualization Type 3: Trend Chart

```markdown
## ROAS Trend by Platform (Last 90 Days)

```
ROAS
 6.0 ┤
 5.0 ┤              ╭──Google Ads
 4.0 ┤         ╭────╯
 3.0 ┤    ╭────╯
 2.0 ┤────╯                ╭────Meta Ads
 1.0 ┤              ╭──────╯
 0.0 ┼────────────────────────────────────
     Jan   Feb   Mar   Apr   May   Jun
```

**Insight**: Google Ads ROAS improving (+40% since Jan), Meta stable, LinkedIn declining
```

#### Visualization Type 4: Before/After Comparison

```markdown
## Projected Impact of Recommendations

### Current State (January 2024)
- Monthly Marketing Spend: $30,000
- Monthly Revenue Generated: $96,000
- ROAS: 3.2
- Cost per Acquisition: $42

### After Implementation (April 2024 - Projected)
- Monthly Marketing Spend: $30,000 *(same)*
- Monthly Revenue Generated: $135,000 *(+41%)*
- ROAS: 4.5 *(+41%)*
- Cost per Acquisition: $29 *(31% lower)*

**Net Impact**: +$39,000 monthly revenue with same budget
```

#### Visualization Type 5: Waterfall Chart (Text-Based)

```markdown
## Revenue Impact Breakdown

```
$140K ┤
      │                                              ┌─────┐
$120K ┤                    ┌──────┐    ┌─────┐      │     │ $135K
      │                    │      │    │     │      │Final│
$100K ┤      ┌──────┐      │ +$28K│    │+$8K │      │     │
      │      │      │      │(GEO) │    │(Ads)│      │     │
 $80K ┤      │ $96K │      │      │    │     │      │     │
      │      │Current      └──────┘    └─────┘      └─────┘
 $60K ┤      │      │
      │      └──────┘
 $40K ┤
      └────────────────────────────────────────────────────
           Base     +GEO     +Ads    +SEO      Total
```

**Contribution**: GEO (72%), Ads (21%), SEO (7%)
```

---

### Step 5: Write Slide Content

**Slide Structure Best Practices**:

```markdown
## Slide Title (Clear, Specific)

**One Sentence Summary** (tells the main point immediately)

Supporting Points:
- Bullet 1 (concise, data-driven)
- Bullet 2 (action-oriented)
- Bullet 3 (specific, not vague)

**Insight/So What**: Why this matters (1 sentence)

[Optional: Visual/Chart/Data]
```

**Good Example**:
```markdown
## Google Ads Outperforming Other Platforms by 2.3x

**Google Ads delivers $4.20 for every $1 spent, significantly outperforming Meta ($3.50) and LinkedIn ($1.80)**

Performance Breakdown:
- Google Ads: ROAS 4.2, CPA $33, 450 conversions/month
- Meta Ads: ROAS 3.5, CPA $38, 320 conversions/month
- LinkedIn Ads: ROAS 1.8, CPA $58, 80 conversions/month

**Recommendation**: Shift 10% of budget from LinkedIn to Google ($1,500/month) to capture additional $6,300 in revenue.
```

**Bad Example**:
```markdown
## Platform Performance

Our platforms are performing differently.

- Google is good
- Meta is okay
- LinkedIn needs work

We should optimize.
```
*Issues: Vague, no data, no clear recommendation*

---

### Step 6: Build Presentation (Markdown Format)

**SIMPLE Mode - Full Example**:

```markdown
# AcmeCorp Marketing Analysis
## Executive Summary - January 2024

---

## 📊 Executive Summary

**Current State**: Marketing performance is GOOD (68/100) with significant untapped potential in emerging channels

| Metric | Current | Target | Gap |
|--------|---------|--------|-----|
| Overall ROAS | 3.2 | 4.5 | +41% upside |
| GEO Visibility | 12% | 40% | Missing AI search |
| SEO Health | 65/100 | 80+ | 15+ quick wins |
| Monthly Revenue | $96K | $135K | $39K opportunity |

**Key Recommendation**: 90-day sprint focusing on 3 high-impact initiatives
**Projected ROI**: 567% ($15K investment → $85K additional revenue over 90 days)

---

## 🎯 Finding #1: Invisible in AI Search (GEO)

**Issue**: AcmeCorp appears in only 12% of high-value AI search queries (ChatGPT, Perplexity, Gemini)

**Impact**:
- Missing 88% of queries where competitors appear
- Losing awareness in fastest-growing search channel
- 0% visibility in consideration-stage queries (most valuable)

**Root Cause**: Lack of citeable thought leadership content

**Quick Win Opportunity**:
- Create 5 targeted content pieces optimized for AI citation
- Expected: +15% visibility in 30 days
- Investment: $5,000 (content creation)

---

## 💰 Finding #2: Ads Budget Misallocated

**Issue**: LinkedIn Ads delivering 1.8 ROAS while Google Ads delivers 4.2 ROAS

**Current Allocation**:
- Google: $15,000/month (50%) → ROAS 4.2 ✅
- Meta: $10,000/month (33%) → ROAS 3.5 ✅
- LinkedIn: $5,000/month (17%) → ROAS 1.8 ❌

**Impact**: $2,500/month wasted on underperforming platform

**Quick Win**:
- Reallocate: Google 60% (+$3K), Meta 30% (+$1K), LinkedIn 10% (-$4K)
- Expected: +$8,000 monthly revenue
- Investment: 2 hours (campaign adjustments)

---

## 🔧 Finding #3: SEO Quick Wins Missed

**Issue**: 15 critical technical SEO issues blocking organic growth

**Top 5 Issues** (Immediate Impact):
1. Missing meta descriptions (28 pages) → +15% CTR
2. Slow page load (4.2s avg) → +20% rankings
3. Broken links (12 found) → Better crawlability
4. Missing schema markup → Better visibility in SERPs
5. Duplicate title tags (8 pages) → -penalty risk

**Impact**: Missing ~500 qualified organic visitors/month

**Quick Win**:
- Fix top 5 issues in 2 weeks
- Expected: +25% organic traffic in 60 days
- Investment: $3,000 (dev time)

---

## 🗓️ 90-Day Implementation Roadmap

### Month 1: Quick Wins (February)
**Week 1-2**:
- ✅ Reallocate ads budget (immediate)
- ✅ Fix top 5 SEO issues
- ✅ Brief content team on GEO

**Week 3-4**:
- ✅ Publish 5 GEO content pieces
- ✅ Monitor ad performance post-reallocation
- ✅ Begin SEO tracking

**Expected Month 1 Impact**: +$12,000 revenue

### Month 2: Scale Winners (March)
- Expand GEO content (10 more pieces)
- Increase Google Ads budget (if performing)
- Launch SEO content optimization
- Test new ad creative

**Expected Month 2 Impact**: +$28,000 revenue

### Month 3: Optimize (April)
- Refine based on data
- Expand successful initiatives
- Comprehensive performance review

**Expected Month 3 Impact**: +$45,000 revenue

---

## 💵 Expected Return on Investment

| Investment Area | Cost | Timeline | Expected Return |
|----------------|------|----------|-----------------|
| GEO Content Creation | $5,000 | 90 days | $28,000 |
| SEO Technical Fixes | $3,000 | 60 days | $6,000 |
| Ads Optimization | $0 | Immediate | $24,000 |
| Strategy & PM | $7,000 | 90 days | $27,000 |
| **Total** | **$15,000** | **90 days** | **$85,000** |

**ROI Metrics**:
- Total ROI: 567%
- Payback Period: 28 days
- Monthly Recurring Benefit: $45,000 (ongoing after Month 3)

---

## ✅ Next Steps & Decision Required

**Immediate Actions (This Week)**:
1. [ ] Review and approve $15,000 budget
2. [ ] Prioritize initiatives (confirm or adjust)
3. [ ] Assign team responsibilities

**Week 2 Actions**:
1. [ ] Execute ads reallocation
2. [ ] Begin SEO fixes (coordinate with dev team)
3. [ ] Kick off GEO content creation

**Decision Required**: **Approve 90-day sprint and $15K budget?**
- ✅ **Yes** → Proceed with implementation next week
- ❌ **No** → Schedule follow-up to address concerns

**Questions? Contact**: [Your Name], [Email], [Phone]

---

## 📎 Appendix: Data Sources

All recommendations based on comprehensive analysis:
- GEO Analysis (DEEP mode): 100 prompts tested across 3 AI engines
- SEO Technical Audit: 28 pages analyzed, 40+ issues identified
- Ads Campaign Analysis: 12 campaigns, 30 days performance data
- Competitive Analysis: 4 competitors benchmarked

**Data Files Available Upon Request**:
- `/data/geo/strategy-synthesis-acme-deep.json`
- `/data/seo/tech-audit-acme-comprehensive.json`
- `/data/ads/campaign-analysis-acme-deep.json`
```

---

### Step 7: Add Design Guidance (For Implementation)

**Visual Design Best Practices**:

```markdown
## Design Guidelines for Presentation

### Color Scheme
**Primary**: Use brand colors
**Accents**:
- Green (#28a745) for positive/wins
- Red (#dc3545) for issues/losses
- Yellow (#ffc107) for warnings/cautions
- Blue (#007bff) for neutral/informational

### Typography
- **Titles**: Bold, 32-36pt
- **Body**: Regular, 18-24pt
- **Captions**: Light, 14-16pt
- **Font**: Sans-serif (Arial, Helvetica, or brand font)

### Layout
- **Max bullet points per slide**: 5
- **Max words per bullet**: 15
- **White space**: 30-40% of slide should be empty
- **Alignment**: Left-aligned text, centered titles

### Data Visualization
- **Charts**: Simple, clear, large fonts
- **Colors**: Consistent with scheme
- **Labels**: Always label axes and data points
- **Source**: Include data source citation

### Slide Transitions
- **Keep simple**: No fancy animations
- **Consistency**: Same transition throughout
- **Timing**: If presenting live, practice timing
```

---

### Step 8: Create Variants for Different Audiences

**COMPREHENSIVE Mode Only** - Create multiple versions:

```markdown
## Presentation Variants

### Variant 1: C-Level Executive (5 slides, 5 minutes)
- Focus: ROI, risk, decision required
- Detail level: High-level only
- Visuals: Simple charts, big numbers
- Tone: Direct, concise

### Variant 2: Marketing Team (25 slides, 30 minutes)
- Focus: Tactical execution, methodology
- Detail level: Granular data, step-by-step
- Visuals: Detailed charts, examples
- Tone: Collaborative, educational

### Variant 3: Board/Investor (10 slides, 15 minutes)
- Focus: Strategic positioning, competitive advantage
- Detail level: Market context, competitive analysis
- Visuals: Market trends, positioning maps
- Tone: Strategic, forward-looking
```

---

### Step 9: Output Generation

**Save presentation in multiple formats**:

#### Format 1: Markdown (Primary Output)

```
Output: /output/presentations/{company}-{topic}-{date}.md

Benefits:
- Easy to read and edit
- Version control friendly
- Can be converted to slides using tools (Marp, reveal.js)
- Portable and shareable
```

#### Format 2: PowerPoint-Ready Structure

```
Output: /output/presentations/{company}-{topic}-{date}-pptx-structure.md

Include slide-by-slide breakdown with:
- Slide number
- Title
- Content (bullets)
- Visual placeholder (chart type, data source)
- Speaker notes

Can be used to quickly build PowerPoint manually or via automation
```

#### Format 3: Google Slides Format

```
Similar to PowerPoint structure but with Google Slides-specific formatting
```

---

### Step 10: Quality Checks

**Before finalizing, validate**:

```
✓ Data Accuracy:
  - All numbers match source data
  - Calculations correct
  - Projections realistic and sourced

✓ Narrative Flow:
  - Logical progression
  - Each slide builds on previous
  - Clear beginning, middle, end
  - Strong call-to-action

✓ Visual Clarity:
  - Charts are readable
  - Colors are consistent
  - Text is concise
  - No overcrowded slides

✓ Actionability:
  - Clear recommendations
  - Specific next steps
  - Ownership assigned (or assignable)
  - Timeline realistic

✓ Audience Appropriateness:
  - Right level of detail
  - Appropriate tone
  - Matches time constraints
  - Addresses audience concerns
```

---

## Validation Checks

1. **Slide Count**: SIMPLE 5-10 slides, COMPREHENSIVE 20-40 slides
2. **Data Citations**: All data points sourced from analysis files
3. **Visualizations**: At least 3-5 charts/tables included
4. **Recommendations**: Specific, actionable, prioritized
5. **ROI Calculation**: Present and realistic
6. **Next Steps**: Clear and time-bound

---

## Usage Example

**Agent Workflow**:
```
1. Read this skill file
2. Load analysis data from /data/ directories
3. Determine presentation format (Executive, Detailed, Pitch)
4. Determine mode (SIMPLE or COMPREHENSIVE)
5. Use TodoWrite to track creation:
   [ ] Data collection
   [ ] Narrative planning
   [ ] Slide outline
   [ ] Data visualizations
   [ ] Content writing
   [ ] Design guidance
   [ ] Quality check
   [ ] Output generation
6. Build presentation in markdown
7. Save to /output/presentations/
8. Provide summary:
   "Presentation Created Successfully!

    Format: Executive Summary
    Slides: 8 slides
    Target Audience: C-level executives
    Duration: 10 minutes

    Key Slides:
    - Executive Summary (scores, ROI)
    - 3 Key Findings (GEO, Ads, SEO)
    - 90-Day Roadmap
    - Expected ROI (567%)
    - Next Steps & Decision

    Output Files:
    - /output/presentations/acmecorp-marketing-analysis-jan2024.md
    - /output/presentations/acmecorp-marketing-analysis-jan2024-pptx-structure.md

    Next: Review presentation and implement in PowerPoint/Google Slides"
```

---

## Integration with Other Skills

**Requires data from**:
- All analysis skills (GEO, SEO, Ads, Competitor)
- **data-visualization.md** - For creating compelling charts

**Feeds into**:
- Client/stakeholder meetings
- Strategy planning sessions
- Board presentations

---

## MCP Tools Needed

**Current**: Built-in tools sufficient (Read, Write)

**Future Enhancement**:
- `mcp__Presentation__slide_generator` - Auto-generate PowerPoint/Google Slides
- `mcp__Presentation__chart_creator` - Create visual charts as PNG/SVG files
- `mcp__Presentation__template_library` - Pre-built presentation templates
