---
name: ads-audience-insights
description: >
  Analyze audience performance across advertising platforms to identify high-value segments, uncover demographic and behavioral insights, optimize targeting, and discover audience expansion opportunities.
  Use when you need to understand which audiences convert best and where to scale or cut spend.
metadata:
  author: castor
  version: "1.0"
  domain: ads
  execution-modes: light, deep
---

# Ads Audience Insights

## Purpose

Analyze audience performance across advertising platforms to identify high-value segments, uncover demographic and behavioral insights, optimize targeting, and discover audience expansion opportunities.

---

## Execution Modes

### LIGHT Mode (5-10 minutes)
**Goal**: Identify top 3 performing audiences and quick targeting recommendations
**Scope**: High-level audience performance comparison
**Output**: Best audiences to scale + worst to pause/refine

### DEEP Mode (20-30 minutes)
**Goal**: Comprehensive audience analysis with segmentation insights
**Scope**: Detailed demographic, interest, behavioral breakdown across platforms
**Output**: Audience strategy document with expansion roadmap

---

## Prerequisites

**Required Input**:
- Audience performance data by platform (Google Ads, Meta Ads, LinkedIn Ads)
- Campaign data (from ads-campaign-analysis OR provided separately)
- Target customer profile/ICP (if available)

**Optional**:
- Customer data (age, gender, location, interests of actual customers)
- Website analytics audience data
- CRM data (for customer match/lookalike building)

**Data Sources**:
1. Audience performance reports from ads platforms
2. CSV exports with audience breakdowns
3. Screenshots of audience insights dashboards
4. Manual data entry

---

## Audience Types by Platform

### Google Ads Audiences
- **Demographic**: Age, gender, parental status, household income
- **In-Market**: Users actively researching/ready to buy (category-based)
- **Affinity**: Based on interests and habits (broader reach, awareness)
- **Custom Intent**: Based on keywords, URLs, apps (advertiser-created)
- **Remarketing**: Website visitors, app users, customer lists, YouTube engagers
- **Similar Audiences**: Lookalikes based on remarketing lists

### Meta Ads Audiences
- **Core Audiences**: Demographics, location, interests, behaviors, connections
- **Custom Audiences**: Website visitors (Pixel), customer lists, app/offline activity, engagement
- **Lookalike Audiences**: 1-10% similarity tiers based on converters, page likes, custom lists
- **Advantage+ Audiences**: Automated targeting by Meta AI

### LinkedIn Ads Audiences
- **Professional Demographics**: Job title, function, seniority, company name/size/industry, years of experience, skills
- **Matched Audiences**: Website retargeting, contact targeting, account-based marketing, lookalikes
- **Interest-Based**: Member interests, member groups

---

## Workflow Steps

### Step 1: Data Collection

Read audience performance data from platform reports:
- **Google Ads**: Audiences -> Demographics / Audience segments. Metrics: Impressions, Clicks, CTR, Conversions, CPA, ROAS.
- **Meta Ads**: Ads Manager -> Breakdown by Age/Gender/Location/Placement. Metrics: Reach, Impressions, Clicks, CPA, ROAS, Frequency.
- **LinkedIn Ads**: Campaign Manager -> Demographics. Metrics: Impressions, Clicks, CTR, Conversions, CPA.

Parse data into structured format with platform, audience breakdowns by age, gender, location, etc.

If no detailed data is available, request high-level campaign data, use industry benchmarks, and provide best-practice recommendations.

### Step 2: Audience Performance Analysis

For each audience segment, calculate:
- CTR, CPC, Conversion Rate, CPA, ROAS
- Performance Score (0-100) weighted: CTR (25%), CPA (35%), ROAS (40%)

Categorize each segment:
- **STAR AUDIENCE**: ROAS >= Target x 1.5
- **GOOD AUDIENCE**: ROAS >= Target
- **NEEDS OPTIMIZATION**: ROAS >= Target x 0.7
- **POOR - CONSIDER EXCLUDING**: ROAS < Target x 0.7

### Step 3: Demographic Insights

Analyze performance by demographics:
- **Age**: Best/worst performing age ranges, conversion distribution, underinvested groups
- **Gender**: Conversion rates, CPA, ROAS by gender, budget reallocation recommendations
- **Location**: Top converting locations, most cost-effective locations, underperformers to exclude

### Step 4: Behavioral & Interest Insights (DEEP Mode)

- **Google Ads**: In-Market and Affinity audience performance vs account average
- **Meta Ads**: Interest targeting analysis (CTR, CPA, ROAS, engagement by interest category)
- **LinkedIn**: Professional demographics (job title, function, seniority, company size, industry performance)

### Step 5: Device & Placement Analysis

- **Device**: Desktop vs Mobile vs Tablet (CTR, CPA, ROAS, conversion rate)
- **Placement** (Meta): Facebook Feed, Instagram Feed, Stories, Reels, Audience Network, Messenger performance comparison

### Step 6: Audience Overlap & Saturation Analysis (DEEP Mode)

- **Frequency Analysis** (Meta): Optimal 2-3, Warning 4-5, Critical 6+. Flag audiences with declining CTR and increasing CPC.
- **Saturation Indicators**: Decreasing reach, increasing CPM/CPC, declining CTR, small audience size (<50K Meta, <10K LinkedIn)

### Step 7: Audience Expansion Opportunities

- **Lookalike/Similar Audiences**: Recommend 1%, 3%, 5% lookalikes from best performing sources
- **Interest Expansion** (Meta): Suggest related interests based on top performers
- **Audience Stacking**: Combine demographic + interest + behavior for precision targeting

### Step 8: Exclusion Recommendations

Identify audiences to exclude for better efficiency:
- ROAS < 0.7 AND sufficient data (>100 clicks)
- Very high CPA (>2x target)
- Low conversion rate (<50% of account avg)

### Step 9: Audience Strategy Document (DEEP Mode)

Create comprehensive strategy including:
- Target audience profile (primary and secondary)
- Platform allocation with targeting strategies
- 3-month testing roadmap

### Step 10: Output Generation

Save analysis results to `/data/ads/audience-insights-{company}-{mode}.json`.

> For detailed JSON output schemas, segmentation examples, and platform-specific analysis templates, see `references/workflow-detail.md`.

---

## Output Schema (Summary)

**LIGHT Mode** includes:
- Executive summary with best/worst audiences
- Top 3 prioritized actions with rationale, expected impact, effort, and how-to instructions
- Projected monthly savings and revenue impact

**DEEP Mode** additionally includes:
- Full demographic insights (age, gender, location breakdowns)
- Behavioral insights (in-market, interests, professional demographics)
- Device and placement analysis
- Audience saturation analysis
- Expansion roadmap (immediate, month 1-3, long-term)
- Data-driven Ideal Customer Profile (ICP)
- Budget reallocation recommendations
- Projected total impact

---

## Validation Checks

1. **Data Completeness**: At least 3 audience dimensions analyzed (age, gender, location minimum)
2. **Statistical Significance**: Flag segments with <50 clicks as "Insufficient Data"
3. **Recommendations Prioritized**: All recommendations have priority and expected impact
4. **ICP Defined**: DEEP mode includes data-driven ideal customer profile
5. **Expansion Plan**: At least 3 lookalike/similar audience recommendations

---

## Usage Example

```
1. Read this skill file
2. Collect audience data (from platform reports or ads-campaign-analysis)
3. Determine mode (LIGHT or DEEP)
4. Use TodoWrite to track analysis steps
5. Execute analysis
6. Save JSON to /data/ads/
7. Provide summary with best/worst audiences, top 3 actions, and projected impact
```

---

## Related Skills

- **ads-campaign-analysis** - Uses campaign data to extract audience insights
- **ads-creative-optimization** - Inform creative decisions based on audience preferences

---

## Tool Usage

**Current**: Built-in tools sufficient (Read for data files/images, Write for output JSON)

**Future Enhancement** (when available via `scripts/api/`):
- Audience builder API for automated lookalike/similar audience creation
- Analytics API for matching ad data with CRM for LTV analysis
