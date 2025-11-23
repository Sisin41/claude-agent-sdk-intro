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
- Campaign performance data (CSV export OR access to ads platforms OR screenshots)
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

**Before starting, ensure client workspace exists**:
```bash
CLIENT_ID="client-slug"  # e.g., "acme-corp"

# Check if workspace exists
if [ ! -d "/data/clients/${CLIENT_ID}" ]; then
    mkdir -p /data/clients/${CLIENT_ID}/{analyses/{geo,seo,ads,competitive,content},context,history,raw-data,temp}
fi
```

### Load Client Context

**Load marketing goals for ROAS/CPA targets**:
```python
goals = Read(f"/data/clients/{CLIENT_ID}/context/marketing-goals.json")
# Extract: ROAS target, budget, KPIs
```

### Load Raw Campaign Data

**If client has uploaded CSV exports**:
```python
# List available data files
import os
raw_data_path = f"/data/clients/{CLIENT_ID}/raw-data/"
csv_files = [f for f in os.listdir(raw_data_path) if f.endswith('.csv')]

# Load Google Ads export
google_ads_file = f"{raw_data_path}google-ads-export-{date}.csv"
```

### Using Bash for Campaign Data Analysis

**Analyze Google Ads CSV with pandas**:
```python
Bash(f"""
python3 << 'EOF'
import pandas as pd
import json

# Load campaign data
df = pd.read_csv('/data/clients/{CLIENT_ID}/raw-data/google-ads-export-2024-01-12.csv')

# Calculate key metrics
analysis = {{
    "total_spend": float(df['spend'].sum()),
    "total_conversions": int(df['conversions'].sum()),
    "avg_ctr": float(df['ctr'].mean()),
    "avg_roas": float(df['roas'].mean()),
    "campaigns_analyzed": len(df['campaign'].unique()),

    # Top performers
    "top_campaigns": df.nlargest(5, 'roas')[['campaign', 'roas', 'spend', 'conversions']].to_dict('records'),

    # Bottom performers
    "underperforming": df.nsmallest(5, 'roas')[['campaign', 'roas', 'spend']].to_dict('records'),

    # Campaign type breakdown
    "by_campaign_type": df.groupby('campaign').agg({{
        'spend': 'sum',
        'conversions': 'sum',
        'roas': 'mean'
    }}).to_dict('index')
}}

print(json.dumps(analysis, indent=2))
EOF
""")
```

**Statistical significance testing for A/B tests**:
```python
Bash("""
python3 << 'EOF'
from scipy import stats
import pandas as pd

# Compare two ad variants
variant_a = {"clicks": 850, "conversions": 42}
variant_b = {"clicks": 920, "conversions": 58}

# Chi-square test
observed = [[variant_a["conversions"], variant_a["clicks"] - variant_a["conversions"]],
            [variant_b["conversions"], variant_b["clicks"] - variant_b["conversions"]]]

chi2, p_value = stats.chi2_contingency(observed)[:2]

if p_value < 0.05:
    print(f"✅ Statistically significant difference (p={p_value:.4f})")
    print(f"Variant B has {(variant_b['conversions']/variant_b['clicks'] - variant_a['conversions']/variant_a['clicks']) * 100:.1f}% higher conversion rate")
else:
    print(f"⚠️ Not statistically significant (p={p_value:.4f})")
    print("Need more data before making decisions")
EOF
""")
```

**Forecast future performance**:
```python
Bash("""
python3 << 'EOF'
import pandas as pd
import numpy as np

# Historical ROAS data
historical_roas = [2.1, 2.3, 2.5, 2.8, 2.7, 3.0]
current_spend = 50000

# Simple linear forecast
trend = np.polyfit(range(len(historical_roas)), historical_roas, 1)
next_month_roas = np.polyval(trend, len(historical_roas))

projected_revenue = current_spend * next_month_roas

print(f"Projected ROAS next month: {next_month_roas:.2f}")
print(f"With ${current_spend:,} spend, projected revenue: ${projected_revenue:,.2f}")
EOF
""")
```

### Save Analysis Results

**File naming**:
```bash
timestamp=$(date +"%Y-%m-%d-%H%M%S")
analysis_file="/data/clients/${CLIENT_ID}/analyses/ads/ads-campaign-analysis-${timestamp}.json"
```

**Save complete analysis**:
```python
analysis_data = {
    "analysis_id": f"ads-campaign-analysis-{timestamp}",
    "client_id": CLIENT_ID,
    "analysis_type": "ads",
    "analysis_subtype": "campaign-analysis",
    "timestamp": timestamp,
    "agent": "ads-analyst",
    "inputs": {...},
    "findings": {...},
    "recommendations": [...],
    "metrics": {...}
}

Write(analysis_file, json.dumps(analysis_data, indent=2))
```

**Update analysis timeline**:
```python
timeline = Read(f"/data/clients/{CLIENT_ID}/history/analysis-timeline.json")
timeline["analyses"].append({
    "analysis_id": f"ads-campaign-analysis-{timestamp}",
    "type": "ads",
    "subtype": "campaign-analysis",
    "timestamp": timestamp,
    "summary": f"Analyzed {num_campaigns} campaigns. Current ROAS: {avg_roas}. Top opportunity: ...",
    "file_path": analysis_file
})
Write(f"/data/clients/{CLIENT_ID}/history/analysis-timeline.json", timeline)
```

---

## Key Metrics by Platform

### Google Ads Metrics
```
Primary Metrics:
- Impressions
- Clicks
- CTR (Click-Through Rate)
- CPC (Cost Per Click)
- Conversions
- Conversion Rate
- CPA (Cost Per Acquisition)
- ROAS (Return on Ad Spend)
- Quality Score
- Impression Share

Secondary Metrics:
- Search Impression Share
- Top of Page Rate
- Outranking Share (competitor analysis)
- Bounce Rate (if Analytics linked)
- Avg. Position
```

### Meta Ads Metrics (Facebook/Instagram)
```
Primary Metrics:
- Reach
- Impressions
- Frequency
- CTR (All)
- CTR (Link Clicks)
- CPC
- CPM (Cost Per 1000 Impressions)
- Conversions
- CPA
- ROAS
- Relevance Score / Quality Ranking

Secondary Metrics:
- Engagement Rate
- Video Views / Watch Time
- Landing Page View Rate
- Add to Cart
- Purchase Conversion Rate
```

### LinkedIn Ads Metrics
```
Primary Metrics:
- Impressions
- Clicks
- CTR
- CPC
- Conversions
- CPA
- Lead Form Completion Rate
- Social Actions (likes, comments, shares)

Secondary Metrics:
- Engagement Rate
- Video View Rate
- Download Rate (for content offers)
- Connection Requests (if objective)
- Company Page Follows
```

---

## Workflow Steps

### Step 1: Data Collection & Validation

**Option A: CSV Exports Provided**
```
Read: {csv_file_path}

Validate data:
✓ Date range matches request
✓ All key metrics present
✓ No obvious data errors (negative values, nulls)
✓ Currency consistent

Parse and structure:
{
  "platform": "google_ads",
  "date_range": "2024-01-01 to 2024-01-31",
  "campaigns": [
    {
      "campaign_name": "Brand Search",
      "impressions": 45000,
      "clicks": 2250,
      "cost": 3375.00,
      "conversions": 180,
      "revenue": 13500.00
    }
  ]
}
```

**Option B: Screenshots Provided**
```
Read: {screenshot_path} (using image reading capability)

Extract metrics from screenshot:
- Identify platform (Google/Meta/LinkedIn)
- Read table rows and columns
- Extract campaign names and metrics
- Validate extracted data

Note: May require user confirmation if OCR unclear
```

**Option C: No Data Provided**
```
Ask user to provide:
1. Platform(s) to analyze
2. Number of campaigns
3. For each campaign:
   - Name
   - Impressions
   - Clicks
   - Cost
   - Conversions
   - Revenue (if applicable)

Or proceed with industry benchmarks for hypothetical analysis
```

---

### Step 2: Calculate Derived Metrics

**For Each Campaign**:

```javascript
// Core calculations
CTR = (Clicks / Impressions) × 100
CPC = Cost / Clicks
Conversion_Rate = (Conversions / Clicks) × 100
CPA = Cost / Conversions
ROAS = Revenue / Cost
ROI = ((Revenue - Cost) / Cost) × 100

// Quality indicators
Efficiency_Score = (Conversions / Cost) × 100  // Higher = better
Wasted_Spend = Cost × (1 - Conversion_Rate)    // Amount spent on non-converting clicks

// Benchmarking (compare to platform averages)
CTR_vs_Benchmark = (CTR - Industry_Avg_CTR) / Industry_Avg_CTR × 100
CPC_vs_Benchmark = (CPC - Industry_Avg_CPC) / Industry_Avg_CPC × 100
```

**Industry Benchmarks** (for comparison):

```json
{
  "google_ads": {
    "search": {
      "avg_ctr": 3.17,
      "avg_cpc": 2.69,
      "avg_conversion_rate": 3.75
    },
    "display": {
      "avg_ctr": 0.46,
      "avg_cpc": 0.63,
      "avg_conversion_rate": 0.77
    }
  },
  "meta_ads": {
    "feed": {
      "avg_ctr": 0.90,
      "avg_cpc": 1.72,
      "avg_conversion_rate": 9.21
    },
    "stories": {
      "avg_ctr": 0.79,
      "avg_cpc": 1.09,
      "avg_conversion_rate": 10.63
    }
  },
  "linkedin_ads": {
    "sponsored_content": {
      "avg_ctr": 0.44,
      "avg_cpc": 5.26,
      "avg_conversion_rate": 2.35
    },
    "text_ads": {
      "avg_ctr": 0.025,
      "avg_cpc": 2.00,
      "avg_conversion_rate": 0.50
    }
  }
}
```

---

### Step 3: Performance Scoring

**Score Each Campaign** (0-100 scale):

```javascript
// Individual metric scores (normalized to 0-100)
CTR_Score = Math.min((CTR / Benchmark_CTR) × 50, 100)
CPC_Score = Math.min((Benchmark_CPC / CPC) × 50, 100)  // Lower CPC = better
Conversion_Rate_Score = Math.min((Conversion_Rate / Benchmark_Conv_Rate) × 50, 100)
ROAS_Score = Math.min((ROAS / Target_ROAS) × 50, 100)

// Overall campaign health score (weighted average)
Campaign_Health_Score =
  (CTR_Score × 0.25) +
  (CPC_Score × 0.25) +
  (Conversion_Rate_Score × 0.30) +
  (ROAS_Score × 0.20)

// Categorize
if (Campaign_Health_Score >= 80) → "EXCELLENT"
else if (Campaign_Health_Score >= 60) → "GOOD"
else if (Campaign_Health_Score >= 40) → "NEEDS IMPROVEMENT"
else → "POOR - URGENT ACTION NEEDED"
```

**Example Scoring**:
```json
{
  "campaign": "Brand Search - Google",
  "metrics": {
    "ctr": 4.8,
    "cpc": 2.15,
    "conversion_rate": 5.2,
    "roas": 3.8
  },
  "scores": {
    "ctr_score": 75,
    "cpc_score": 62,
    "conversion_rate_score": 69,
    "roas_score": 76
  },
  "overall_health_score": 71,
  "health_status": "GOOD",
  "ranking": 2
}
```

---

### Step 4: Identify Performance Issues

**Diagnostic Framework**:

#### Issue Type 1: Low CTR
```
If CTR < Benchmark_CTR × 0.7:

Potential Causes:
- Poor ad copy (not compelling)
- Weak headline/creative
- Irrelevant targeting (wrong audience)
- Low ad position (Google Ads)
- Ad fatigue (Meta Ads - high frequency)

Diagnostic Questions:
1. Is CTR consistently low across all ad groups? → Ad copy issue
2. Is CTR low for specific keywords/audiences? → Targeting issue
3. Has CTR declined over time? → Ad fatigue
4. Is impression share low? → Budget/bid issue

Recommendations:
- A/B test new ad copy with stronger value propositions
- Refine audience targeting
- Increase bids for high-value keywords
- Refresh creative assets (Meta Ads)
- Use dynamic keyword insertion (Google Ads)
```

#### Issue Type 2: High CPC
```
If CPC > Benchmark_CPC × 1.3:

Potential Causes:
- Highly competitive keywords
- Low Quality Score (Google Ads)
- Poor relevance score (Meta Ads)
- Broad match keywords driving up costs
- Bidding too aggressively

Diagnostic Questions:
1. What is Quality Score? (Google) / Relevance Score? (Meta)
2. Are expensive keywords converting?
3. Is audience too narrow? (driving up competition)

Recommendations:
- Improve Quality Score (better ad relevance, landing page experience)
- Add negative keywords (Google Ads)
- Test long-tail keywords (lower competition)
- Adjust bidding strategy (manual CPC → target CPA)
- Expand audience (reduce competition)
```

#### Issue Type 3: Low Conversion Rate
```
If Conversion_Rate < Benchmark_Conv_Rate × 0.7:

Potential Causes:
- Poor landing page experience
- Traffic not qualified (wrong audience)
- Weak offer/value proposition
- High friction in conversion process
- Slow landing page load time

Diagnostic Questions:
1. Is bounce rate high? → Landing page issue
2. Are clicks qualified? (high intent keywords?)
3. Is conversion tracking set up correctly?

Recommendations:
- Optimize landing page (speed, clarity, CTA)
- Refine targeting (negative keywords, audience exclusions)
- Strengthen offer (better incentive, urgency)
- Simplify conversion process (fewer form fields)
- A/B test landing page variations
```

#### Issue Type 4: Low ROAS / Negative ROI
```
If ROAS < Target_ROAS:

Potential Causes:
- High CPA eating into margins
- Low average order value
- Wrong products promoted
- Attribution issues (conversions not tracked properly)

Diagnostic Questions:
1. Is CPA too high relative to customer value?
2. Are high-margin products being promoted?
3. Is attribution window appropriate?

Recommendations:
- Focus on high-value products/services
- Improve conversion rate to lower CPA
- Adjust bids for profitability (target ROAS bidding)
- Upsell/cross-sell strategies
- Review attribution model
```

#### Issue Type 5: High Frequency (Meta Ads Specific)
```
If Frequency > 3.0:

Issue: Ad fatigue - audience seeing ads too many times

Recommendations:
- Expand audience size
- Refresh creative assets
- Adjust frequency cap
- Rotate ad creatives more frequently
```

---

### Step 5: Cross-Platform Analysis

**DEEP Mode Only** - Compare performance across platforms:

```json
{
  "cross_platform_comparison": {
    "google_ads": {
      "total_spend": 15000,
      "conversions": 450,
      "cpa": 33.33,
      "roas": 4.2,
      "efficiency_rank": 1
    },
    "meta_ads": {
      "total_spend": 8000,
      "conversions": 320,
      "cpa": 25.00,
      "roas": 3.1,
      "efficiency_rank": 2
    },
    "linkedin_ads": {
      "total_spend": 5000,
      "conversions": 85,
      "cpa": 58.82,
      "roas": 1.8,
      "efficiency_rank": 3
    },
    "insights": [
      "Google Ads has highest ROAS (4.2) - allocate more budget here",
      "Meta Ads has lowest CPA ($25) - best for lead generation",
      "LinkedIn Ads has high CPA ($58.82) but may have higher lead quality - check conversion to sale rate"
    ],
    "budget_reallocation": {
      "current_allocation": {
        "google_ads": "53.6%",
        "meta_ads": "28.6%",
        "linkedin_ads": "17.8%"
      },
      "recommended_allocation": {
        "google_ads": "60%",
        "meta_ads": "30%",
        "linkedin_ads": "10%",
        "rationale": "Shift budget toward higher ROAS platforms"
      }
    }
  }
}
```

---

### Step 6: Campaign Ranking & Prioritization

**Rank all campaigns by**:

1. **ROAS** (highest to lowest)
2. **Efficiency Score** (conversions per dollar spent)
3. **Health Score** (overall performance)

**Categorize campaigns**:

```json
{
  "top_performers": [
    {
      "campaign": "Brand Search - Google",
      "roas": 5.8,
      "health_score": 87,
      "recommendation": "SCALE - Increase budget by 30-50%"
    }
  ],
  "solid_performers": [
    {
      "campaign": "Retargeting - Meta",
      "roas": 3.2,
      "health_score": 68,
      "recommendation": "OPTIMIZE - Small improvements can boost ROAS"
    }
  ],
  "underperformers": [
    {
      "campaign": "Cold Audience - LinkedIn",
      "roas": 0.8,
      "health_score": 32,
      "recommendation": "PAUSE OR RESTRUCTURE - Losing money"
    }
  ],
  "testing_campaigns": [
    {
      "campaign": "New Product Launch - Google",
      "roas": 1.5,
      "health_score": 45,
      "recommendation": "MONITOR - Give 2 more weeks of data before making decision"
    }
  ]
}
```

---

### Step 7: Quick Win Identification

**Find immediate optimization opportunities** (LIGHT Mode priority):

```
Quick Win Criteria:
- Low effort to implement
- High impact on performance
- Can be done immediately

Quick Win Types:

1. Pause Underperforming Campaigns
   Criteria: ROAS < 1.0 AND running for >30 days
   Action: Pause immediately
   Impact: Stop wasting budget
   Effort: 1 minute

2. Increase Budget for Top Performers
   Criteria: ROAS > Target × 1.5 AND not budget-limited
   Action: Increase daily budget by 30%
   Impact: Scale profitable campaigns
   Effort: 2 minutes

3. Add Negative Keywords
   Criteria: High CPC + Low Conversion Rate on specific keywords
   Action: Add irrelevant search terms as negative keywords
   Impact: Reduce wasted spend by 10-20%
   Effort: 10 minutes

4. Adjust Bids on High-Value Keywords
   Criteria: High-converting keywords with low impression share
   Action: Increase bids by 20-30%
   Impact: Capture more conversions
   Effort: 5 minutes

5. Refresh Ad Creative
   Criteria: Meta Ads with Frequency > 4.0
   Action: Rotate in new creative assets
   Impact: Improve CTR by 15-25%
   Effort: 30 minutes
```

**Quick Win Example**:
```json
{
  "quick_win_id": "qw_001",
  "type": "pause_underperformer",
  "campaign": "Cold Audience - LinkedIn Display",
  "current_performance": {
    "spend": "$2,500",
    "conversions": 12,
    "cpa": "$208.33",
    "roas": "0.6"
  },
  "issue": "ROAS of 0.6 = losing $1,000/month",
  "action": "Pause campaign immediately",
  "expected_impact": "Save $2,500/month in wasted spend",
  "effort": "1 minute",
  "priority": "CRITICAL"
}
```

---

### Step 8: Detailed Recommendations by Platform

**DEEP Mode Only** - Platform-specific optimization strategies:

#### Google Ads Recommendations

```
1. Search Campaign Optimization:
   - Add high-performing keywords from Search Terms Report
   - Add negative keywords for irrelevant searches
   - Test Responsive Search Ads (RSAs) with 10+ headlines
   - Improve Quality Score (landing page relevance, ad copy)
   - Use ad extensions (sitelinks, callouts, structured snippets)

2. Bidding Strategy:
   - If ROAS > target: Switch to Maximize Conversions
   - If CPA is priority: Switch to Target CPA bidding
   - If ROAS is priority: Switch to Target ROAS bidding
   - Use bid adjustments for devices, locations, time of day

3. Audience Targeting:
   - Layer remarketing audiences on search campaigns
   - Use Customer Match for high-value audience targeting
   - Test Similar Audiences based on converters

4. Budget Allocation:
   - Campaigns with ROAS > 4.0: Increase budget by 50%
   - Campaigns with ROAS 2-4: Maintain and optimize
   - Campaigns with ROAS < 2: Reduce budget or pause
```

#### Meta Ads Recommendations

```
1. Creative Optimization:
   - Test video vs static image (video often performs better)
   - Use user-generated content (UGC) for authenticity
   - Test multiple ad formats (carousel, single image, video)
   - Refresh creative every 2-3 weeks (combat ad fatigue)

2. Audience Strategy:
   - Build Lookalike Audiences from converters (1%, 3%, 5%)
   - Test detailed targeting vs broad targeting with Advantage+
   - Exclude past converters (unless upsell/cross-sell campaign)
   - Layer interest targeting with behavior targeting

3. Campaign Structure:
   - Consolidate ad sets (Facebook prefers fewer, larger ad sets)
   - Let algorithm optimize (don't over-segment)
   - Use Campaign Budget Optimization (CBO)

4. Placement Optimization:
   - Analyze placement report
   - Exclude underperforming placements (e.g., Audience Network if CPA too high)
   - Test Instagram Stories vs Feed separately
```

#### LinkedIn Ads Recommendations

```
1. Audience Targeting:
   - Use job title targeting (more specific = better for B2B)
   - Layer company size, industry, seniority
   - Test Matched Audiences (retargeting, website visitors)
   - Use Account-Based Marketing (ABM) for enterprise

2. Ad Format Selection:
   - Lead Gen Forms: Best for capturing leads (higher conversion rate)
   - Sponsored Content: Best for engagement and awareness
   - Message Ads: High engagement but use sparingly (can be intrusive)

3. Bidding & Budget:
   - LinkedIn is expensive - expect $5-15 CPC
   - Use cost cap bidding to control CPA
   - Start with manual bidding to understand costs
   - Budget: Minimum $10-20/day per campaign

4. Creative Best Practices:
   - Professional, value-focused messaging
   - Use statistics and data in ad copy
   - Test thought leadership content vs product-focused
   - Include social proof (customer logos, testimonials)
```

---

### Step 9: Budget Reallocation Recommendations

**Optimize budget allocation** across campaigns and platforms:

```javascript
// Calculate optimal budget allocation
For each campaign:
  Efficiency_Score = ROAS × Conversion_Volume

Total_Efficiency = Sum of all Efficiency_Scores

Optimal_Budget_Percentage = (Campaign_Efficiency_Score / Total_Efficiency) × 100

// Apply constraints
Min_Budget_Per_Campaign = $500/month (to get statistically significant data)
Max_Budget_Shift = 30% per month (don't over-shift too quickly)
```

**Budget Reallocation Example**:
```json
{
  "current_monthly_budget": 30000,
  "campaigns": [
    {
      "name": "Brand Search - Google",
      "current_budget": 8000,
      "current_percentage": "26.7%",
      "roas": 5.8,
      "recommended_budget": 12000,
      "recommended_percentage": "40%",
      "change": "+$4,000 (+50%)",
      "rationale": "Highest ROAS - scale aggressively"
    },
    {
      "name": "Cold Audience - LinkedIn",
      "current_budget": 5000,
      "current_percentage": "16.7%",
      "roas": 0.8,
      "recommended_budget": 1000,
      "recommended_percentage": "3.3%",
      "change": "-$4,000 (-80%)",
      "rationale": "Negative ROI - minimize or pause"
    }
  ],
  "expected_impact": {
    "current_total_roas": 3.2,
    "projected_total_roas": 4.1,
    "improvement": "+28% overall ROAS"
  }
}
```

---

### Step 10: Output Generation

**LIGHT Mode Output** (`/data/ads/campaign-analysis-{company}-light.json`):

```json
{
  "metadata": {
    "mode": "LIGHT",
    "company": "AcmeCorp",
    "date_range": "2024-01-01 to 2024-01-31",
    "platforms_analyzed": ["google_ads", "meta_ads", "linkedin_ads"],
    "total_spend": 30000,
    "total_conversions": 850,
    "overall_roas": 3.2,
    "generated_at": "2024-01-15T16:00:00Z"
  },
  "executive_summary": {
    "overall_health": "GOOD",
    "health_score": 68,
    "key_insights": [
      "Google Ads is top performer with 4.2 ROAS - opportunity to scale",
      "LinkedIn Ads underperforming (1.8 ROAS) - needs restructuring",
      "3 campaigns losing money (ROAS < 1.0) - immediate action needed"
    ],
    "top_performers": [
      {
        "campaign": "Brand Search - Google",
        "spend": 8000,
        "roas": 5.8,
        "recommendation": "Increase budget by 50%"
      }
    ],
    "underperformers": [
      {
        "campaign": "Cold Audience - LinkedIn Display",
        "spend": 2500,
        "roas": 0.6,
        "recommendation": "PAUSE immediately - losing $1,000/month"
      }
    ]
  },
  "top_3_quick_wins": [
    {
      "priority": 1,
      "action": "Pause 'Cold Audience - LinkedIn Display' campaign",
      "current_situation": "Spending $2,500/month with 0.6 ROAS",
      "expected_impact": "Save $1,000/month in losses",
      "effort": "1 minute",
      "how_to": "Go to LinkedIn Campaign Manager → Select campaign → Click 'Pause'"
    },
    {
      "priority": 2,
      "action": "Increase budget for 'Brand Search - Google' by 50%",
      "current_situation": "ROAS of 5.8 but budget-limited",
      "expected_impact": "Generate additional $8,000 revenue/month",
      "effort": "2 minutes",
      "how_to": "Google Ads → Campaigns → Edit daily budget from $265 to $400"
    },
    {
      "priority": 3,
      "action": "Add 15 negative keywords to 'Non-Brand Search - Google'",
      "current_situation": "High CPC ($4.20) with low conversion rate (2.1%)",
      "expected_impact": "Reduce wasted spend by $500/month",
      "effort": "10 minutes",
      "how_to": "Review Search Terms Report → Identify irrelevant queries → Add as negative keywords"
    }
  ],
  "expected_total_impact": {
    "monthly_savings": "$1,500",
    "additional_revenue": "$8,000",
    "net_improvement": "$9,500/month",
    "roas_improvement": "3.2 → 4.0 (+25%)"
  }
}
```

**DEEP Mode Output** (`/data/ads/campaign-analysis-{company}-deep.json`):

```json
{
  "metadata": {
    "mode": "DEEP",
    "company": "AcmeCorp",
    "date_range": "2024-01-01 to 2024-01-31",
    "platforms_analyzed": ["google_ads", "meta_ads", "linkedin_ads"],
    "campaigns_analyzed": 12,
    "total_spend": 30000,
    "total_conversions": 850,
    "overall_roas": 3.2,
    "generated_at": "2024-01-15T16:00:00Z",
    "analysis_duration_minutes": 28
  },
  "overall_performance": {
    "health_score": 68,
    "health_status": "GOOD",
    "spend_breakdown": {
      "google_ads": 15000,
      "meta_ads": 10000,
      "linkedin_ads": 5000
    },
    "performance_breakdown": {
      "google_ads": {"conversions": 450, "roas": 4.2},
      "meta_ads": {"conversions": 320, "roas": 3.5},
      "linkedin_ads": {"conversions": 80, "roas": 1.8}
    },
    "year_over_year_comparison": {
      "spend_change": "+15%",
      "conversions_change": "+22%",
      "roas_change": "+6%",
      "trend": "Improving efficiency"
    }
  },
  "campaign_details": [
    {
      "campaign_id": "camp_001",
      "platform": "google_ads",
      "campaign_name": "Brand Search",
      "campaign_type": "Search",
      "status": "Active",
      "budget": {
        "daily": 265,
        "monthly": 8000,
        "utilization": "100%"
      },
      "performance": {
        "impressions": 45000,
        "clicks": 2160,
        "ctr": 4.8,
        "cpc": 3.70,
        "conversions": 180,
        "conversion_rate": 8.33,
        "cpa": 44.44,
        "revenue": 46800,
        "roas": 5.85,
        "quality_score_avg": 8.2
      },
      "benchmarks": {
        "ctr_vs_industry": "+51% (excellent)",
        "cpc_vs_industry": "+38% (higher but justified by quality)",
        "conversion_rate_vs_industry": "+122% (exceptional)"
      },
      "health_score": 87,
      "health_status": "EXCELLENT",
      "ranking": 1,
      "issues": [],
      "opportunities": [
        "Budget-limited 65% of the time - increase budget",
        "Add more brand keyword variations",
        "Test Responsive Search Ads with 15 headlines"
      ],
      "recommendations": [
        {
          "type": "budget_increase",
          "priority": "HIGH",
          "action": "Increase daily budget from $265 to $400 (+50%)",
          "rationale": "ROAS of 5.85 significantly exceeds target, budget-limited frequently",
          "expected_impact": "Additional 68 conversions/month, $16,800 revenue",
          "effort": "LOW",
          "timeframe": "Immediate"
        }
      ]
    },
    {
      "campaign_id": "camp_005",
      "platform": "linkedin_ads",
      "campaign_name": "Cold Audience - IT Decision Makers",
      "campaign_type": "Sponsored Content",
      "status": "Active",
      "budget": {
        "daily": 83,
        "monthly": 2500
      },
      "performance": {
        "impressions": 125000,
        "clicks": 450,
        "ctr": 0.36,
        "cpc": 5.56,
        "conversions": 12,
        "conversion_rate": 2.67,
        "cpa": 208.33,
        "revenue": 1500,
        "roas": 0.60
      },
      "health_score": 28,
      "health_status": "POOR - URGENT ACTION",
      "ranking": 12,
      "issues": [
        "ROAS below 1.0 - losing money",
        "CTR 18% below LinkedIn average",
        "Very high CPA ($208) vs. customer LTV",
        "Low conversion rate (2.67%)"
      ],
      "root_cause_analysis": {
        "primary_issue": "Audience targeting too broad",
        "secondary_issues": [
          "Ad creative not resonating (low CTR)",
          "Possibly wrong audience tier for product price point"
        ]
      },
      "recommendations": [
        {
          "type": "pause_campaign",
          "priority": "CRITICAL",
          "action": "Pause campaign immediately",
          "rationale": "Losing $1,000/month with no path to profitability",
          "expected_impact": "Save $1,000/month",
          "effort": "IMMEDIATE",
          "timeframe": "Now"
        },
        {
          "type": "restructure",
          "priority": "MEDIUM",
          "action": "After pause, test new narrow audience (10K-50K company size only)",
          "rationale": "May be targeting too small companies for $10K+ product",
          "expected_impact": "Potential to achieve 1.5+ ROAS with better targeting",
          "effort": "MEDIUM",
          "timeframe": "Week 2"
        }
      ]
    }
  ],
  "cross_platform_insights": {
    "best_platform": "Google Ads",
    "best_platform_rationale": "Highest ROAS (4.2), most conversions (450)",
    "platform_comparison": { /* ... detailed comparison ... */ },
    "budget_reallocation": {
      "current": {"google_ads": "50%", "meta_ads": "33%", "linkedin_ads": "17%"},
      "recommended": {"google_ads": "60%", "meta_ads": "30%", "linkedin_ads": "10%"},
      "rationale": "Shift budget toward higher-performing platforms"
    }
  },
  "optimization_roadmap": {
    "immediate_actions": [
      "Pause LinkedIn 'Cold Audience' campaign",
      "Increase Google 'Brand Search' budget by 50%",
      "Add 20 negative keywords to Google 'Non-Brand Search'"
    ],
    "week_1_actions": [
      "Refresh Meta ad creative (frequency >3.5)",
      "Test new audience segments on Meta",
      "Implement Target ROAS bidding on Google top performers"
    ],
    "week_2_4_actions": [
      "A/B test landing pages for underperforming campaigns",
      "Restructure LinkedIn targeting (narrow audience)",
      "Launch retargeting campaigns across all platforms"
    ],
    "ongoing_optimizations": [
      "Weekly negative keyword additions",
      "Bi-weekly creative refresh (Meta)",
      "Monthly budget reallocation based on performance"
    ]
  },
  "projected_impact": {
    "if_all_recommendations_implemented": {
      "monthly_spend": 30000,
      "projected_conversions": 1050,
      "current_conversions": 850,
      "conversion_increase": "+23.5%",
      "projected_roas": 4.2,
      "current_roas": 3.2,
      "roas_improvement": "+31%",
      "additional_monthly_revenue": "$9,600"
    }
  }
}
```

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

**Agent Workflow**:
```
1. Read this skill file
2. Collect campaign data (CSV, screenshots, or manual input)
3. Determine mode (LIGHT or DEEP)
4. Use TodoWrite to track analysis:
   [ ] Data collection
   [ ] Metric calculations
   [ ] Performance scoring
   [ ] Issue identification
   [ ] Quick win discovery
   [ ] Platform-specific recommendations
   [ ] Budget reallocation
   [ ] Output generation
5. Execute analysis steps
6. Save JSON to /data/ads/
7. Provide summary:
   "Campaign Analysis Complete!

    Overall Performance: GOOD (68/100)
    Total Spend: $30,000
    Total Conversions: 850
    Overall ROAS: 3.2

    Top Performer: Brand Search (Google)
    - ROAS: 5.8
    - Recommendation: Increase budget by 50%

    Biggest Issue: Cold Audience (LinkedIn)
    - ROAS: 0.6 (losing $1K/month)
    - Recommendation: PAUSE immediately

    Top 3 Quick Wins:
    1. Pause LinkedIn campaign → Save $1,000/month
    2. Increase Google brand budget → +$8,000 revenue/month
    3. Add negative keywords → Reduce waste by $500/month

    Total Projected Impact: +$9,500/month (+31% ROAS improvement)

    Full report: /data/ads/campaign-analysis-acme-deep.json"
```

---

## Integration with Other Skills

**Works with**:
- **audience-insights.md** - Deep dive into which audiences perform best
- **creative-optimization.md** - Optimize ad creative based on performance data

---

## MCP Tools Needed

**Current**: Built-in tools sufficient (Read for CSV/images, Write for output)

**Future Enhancement**:
- `mcp__AdsAPI__google_ads` - Direct API integration for live data
- `mcp__AdsAPI__meta_ads` - Facebook/Instagram Ads API
- `mcp__AdsAPI__linkedin_ads` - LinkedIn Campaign Manager API
- `mcp__Analytics__attribution_analysis` - Multi-touch attribution modeling
