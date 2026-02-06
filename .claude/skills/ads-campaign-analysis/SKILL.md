---
name: ads-campaign-analysis
description: >
  Analyze advertising campaign performance across Google Ads, Meta Ads, and LinkedIn Ads to identify optimization opportunities, budget allocation improvements, and ROI enhancement strategies.
  Use when you need a performance snapshot or comprehensive audit of ad campaigns.
metadata:
  author: castor
  version: "1.0"
  domain: ads
  execution-modes: light, deep
---

# Ads Campaign Analysis

## Purpose

Analyze advertising campaign performance across Google Ads, Meta Ads (Facebook/Instagram), and LinkedIn Ads to identify optimization opportunities, budget allocation improvements, and ROI enhancement strategies.

---

## Execution Modes

### LIGHT Mode (5-10 minutes)
**Goal**: Quick performance snapshot and top 3 optimization opportunities
**Scope**: High-level metrics across all platforms
**Output**: Executive summary with immediate action items

### DEEP Mode (20-30 minutes)
**Goal**: Comprehensive campaign audit with detailed insights
**Scope**: Campaign-level, ad group-level, and ad-level analysis
**Output**: Detailed optimization roadmap with platform-specific recommendations

---

## Prerequisites

**Required Input**:
- Campaign performance data (CSV export OR screenshots OR manual entry)
- Date range for analysis (last 7, 30, or 90 days)
- Advertising platforms used (Google Ads, Meta Ads, LinkedIn Ads)
- Campaign objectives (awareness, leads, sales, etc.)

**Optional**:
- Historical performance data (for trend analysis)
- Budget constraints
- Target KPIs (ROAS, CPA, CTR goals)
- Competitor benchmarks

**Data Sources** (in order of preference):
1. CSV exports from ads platforms
2. Screenshots of performance dashboards
3. Manual data entry
4. Estimates based on industry benchmarks

---

## Workspace & File Management

### Client Workspace Setup

Before starting, ensure client workspace exists:
```bash
CLIENT_ID="client-slug"
if [ ! -d "/data/clients/${CLIENT_ID}" ]; then
    mkdir -p /data/clients/${CLIENT_ID}/{analyses/{geo,seo,ads,competitive,content},context,history,raw-data,temp}
fi
```

### Load Client Context

Load marketing goals for ROAS/CPA targets:
```
Read: /data/clients/{CLIENT_ID}/context/marketing-goals.json
Extract: ROAS target, budget, KPIs
```

### Load Raw Campaign Data

If client has uploaded CSV exports:
```
List available data files in /data/clients/{CLIENT_ID}/raw-data/
Load platform-specific exports (google-ads-export, meta-ads-export, etc.)
```

### Analyze with Python (Bash)

Use `Bash` with Python/pandas for CSV analysis, statistical significance testing (scipy chi-square for A/B tests), and performance forecasting (numpy polyfit for trend extrapolation).

### Save Analysis Results

```
File: /data/clients/{CLIENT_ID}/analyses/ads/ads-campaign-analysis-{timestamp}.json
Update: /data/clients/{CLIENT_ID}/history/analysis-timeline.json
```

---

## Key Metrics by Platform

### Google Ads
**Primary**: Impressions, Clicks, CTR, CPC, Conversions, Conversion Rate, CPA, ROAS, Quality Score, Impression Share
**Secondary**: Search Impression Share, Top of Page Rate, Outranking Share, Bounce Rate, Avg Position

### Meta Ads (Facebook/Instagram)
**Primary**: Reach, Impressions, Frequency, CTR (All/Link), CPC, CPM, Conversions, CPA, ROAS, Quality Ranking
**Secondary**: Engagement Rate, Video Views/Watch Time, Landing Page View Rate, Add to Cart, Purchase Rate

### LinkedIn Ads
**Primary**: Impressions, Clicks, CTR, CPC, Conversions, CPA, Lead Form Completion Rate, Social Actions
**Secondary**: Engagement Rate, Video View Rate, Download Rate, Connection Requests, Page Follows

---

## Industry Benchmarks

```json
{
  "google_ads": {
    "search": {"avg_ctr": 3.17, "avg_cpc": 2.69, "avg_conversion_rate": 3.75},
    "display": {"avg_ctr": 0.46, "avg_cpc": 0.63, "avg_conversion_rate": 0.77}
  },
  "meta_ads": {
    "feed": {"avg_ctr": 0.90, "avg_cpc": 1.72, "avg_conversion_rate": 9.21},
    "stories": {"avg_ctr": 0.79, "avg_cpc": 1.09, "avg_conversion_rate": 10.63}
  },
  "linkedin_ads": {
    "sponsored_content": {"avg_ctr": 0.44, "avg_cpc": 5.26, "avg_conversion_rate": 2.35},
    "text_ads": {"avg_ctr": 0.025, "avg_cpc": 2.00, "avg_conversion_rate": 0.50}
  }
}
```

---

## Workflow Steps

### Step 1: Data Collection & Validation

Collect data via CSV exports, screenshots (using image reading capability), or manual input. Validate: date range matches, all key metrics present, no data errors, currency consistent.

### Step 2: Calculate Derived Metrics

For each campaign:
- CTR = (Clicks / Impressions) x 100
- CPC = Cost / Clicks
- Conversion Rate = (Conversions / Clicks) x 100
- CPA = Cost / Conversions
- ROAS = Revenue / Cost
- ROI = ((Revenue - Cost) / Cost) x 100
- Wasted Spend = Cost x (1 - Conversion Rate)

Compare all metrics against industry benchmarks.

### Step 3: Performance Scoring

Score each campaign 0-100:
- CTR Score (25% weight)
- CPC Score (25% weight)
- Conversion Rate Score (30% weight)
- ROAS Score (20% weight)

Categorize:
- **EXCELLENT** (80+): Scale aggressively
- **GOOD** (60-79): Optimize for improvement
- **NEEDS IMPROVEMENT** (40-59): Significant changes needed
- **POOR** (<40): Urgent action / pause

### Step 4: Identify Performance Issues

**Diagnostic Framework** for common issues:

- **Low CTR**: Poor ad copy, weak creative, irrelevant targeting, low ad position, ad fatigue
- **High CPC**: Competitive keywords, low Quality Score, broad match issues, overbidding
- **Low Conversion Rate**: Poor landing page, unqualified traffic, weak offer, high friction
- **Low ROAS**: High CPA eating margins, low order value, wrong products, attribution issues
- **High Frequency** (Meta): Ad fatigue from oversaturation

Each issue includes diagnostic questions and specific remediation recommendations.

### Step 5: Cross-Platform Analysis (DEEP Mode)

Compare performance across all platforms. Identify best platform by ROAS and conversion volume. Recommend budget reallocation toward higher-performing platforms.

### Step 6: Campaign Ranking & Prioritization

Rank all campaigns by ROAS, Efficiency Score, and Health Score. Categorize into: Top Performers (SCALE), Solid Performers (OPTIMIZE), Underperformers (PAUSE/RESTRUCTURE), Testing Campaigns (MONITOR).

### Step 7: Quick Win Identification

Find immediate optimization opportunities:
1. **Pause Underperformers**: ROAS < 1.0 for 30+ days -> Pause (1 min effort)
2. **Scale Top Performers**: ROAS > Target x 1.5 -> Increase budget 30% (2 min effort)
3. **Add Negative Keywords**: High CPC + Low Conv Rate -> Add negatives (10 min effort)
4. **Adjust Bids**: High-converting keywords with low impression share -> Increase bids 20-30% (5 min effort)
5. **Refresh Creative**: Meta Ads Frequency > 4.0 -> Rotate new creative (30 min effort)

### Step 8: Detailed Recommendations by Platform (DEEP Mode)

Platform-specific optimization strategies for Google Ads (search, bidding, audience, budget), Meta Ads (creative, audience, structure, placement), and LinkedIn Ads (targeting, format, bidding, creative).

### Step 9: Budget Reallocation Recommendations

Calculate optimal budget allocation using efficiency scores. Apply constraints: min $500/month per campaign, max 30% budget shift per month.

### Step 10: Output Generation

Save analysis to `/data/ads/campaign-analysis-{company}-{mode}.json`.

> For detailed diagnostic frameworks, scoring examples, platform-specific strategies, and full output schemas, see `references/workflow-detail.md`.

---

## Output Schema (Summary)

**LIGHT Mode** includes:
- Executive summary with overall health score and key insights
- Top performers and underperformers with recommendations
- Top 3 quick wins with current situation, action, expected impact, effort, and how-to
- Expected total impact (monthly savings + additional revenue + ROAS improvement)

**DEEP Mode** additionally includes:
- Detailed campaign-by-campaign analysis with metrics, benchmarks, issues, and recommendations
- Cross-platform comparison with budget reallocation
- Optimization roadmap (immediate, week 1, week 2-4, ongoing)
- Projected impact if all recommendations implemented

---

## Validation Checks

1. **Data Completeness**: All required metrics present for each campaign
2. **Calculations Accurate**: CTR, CPC, ROAS calculated correctly
3. **Benchmarks Applied**: Compared to industry standards
4. **Issues Identified**: At least one issue/opportunity per underperforming campaign
5. **Recommendations Actionable**: Clear, specific action steps with expected impact
6. **Quick Wins Prioritized**: LIGHT mode has 3-5 immediate actions

---

## Usage Example

```
1. Read this skill file
2. Collect campaign data (CSV, screenshots, or manual input)
3. Determine mode (LIGHT or DEEP)
4. Use TodoWrite to track analysis steps
5. Execute analysis steps
6. Save JSON to /data/ads/
7. Provide summary with overall performance, top/worst campaigns, quick wins, projected impact
```

---

## Related Skills

- **ads-audience-insights** - Deep dive into which audiences perform best
- **ads-creative-optimization** - Optimize ad creative based on performance data

---

## Tool Usage

**Current**: Built-in tools sufficient (Read for CSV/images, Write for output, Bash for Python analysis)

**Future Enhancement** (when available via `scripts/api/`):
- Google Ads API for live data
- Meta Ads API for Facebook/Instagram data
- LinkedIn Campaign Manager API
- Multi-touch attribution modeling API
