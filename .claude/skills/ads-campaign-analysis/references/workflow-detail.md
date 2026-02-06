# Ads Campaign Analysis - Detailed Workflow Reference

This document contains detailed diagnostic frameworks, scoring examples, platform-specific strategies, and full output schemas for the ads-campaign-analysis skill.

---

## Data Analysis with Python (Bash)

### Analyze Google Ads CSV with pandas

```python
Bash("""
python3 << 'EOF'
import pandas as pd
import json

# Load campaign data
df = pd.read_csv('/data/clients/{CLIENT_ID}/raw-data/google-ads-export-2024-01-12.csv')

# Calculate key metrics
analysis = {
    "total_spend": float(df['spend'].sum()),
    "total_conversions": int(df['conversions'].sum()),
    "avg_ctr": float(df['ctr'].mean()),
    "avg_roas": float(df['roas'].mean()),
    "campaigns_analyzed": len(df['campaign'].unique()),
    "top_campaigns": df.nlargest(5, 'roas')[['campaign', 'roas', 'spend', 'conversions']].to_dict('records'),
    "underperforming": df.nsmallest(5, 'roas')[['campaign', 'roas', 'spend']].to_dict('records'),
    "by_campaign_type": df.groupby('campaign').agg({
        'spend': 'sum', 'conversions': 'sum', 'roas': 'mean'
    }).to_dict('index')
}

print(json.dumps(analysis, indent=2))
EOF
""")
```

### Statistical Significance Testing for A/B Tests

```python
Bash("""
python3 << 'EOF'
from scipy import stats

variant_a = {"clicks": 850, "conversions": 42}
variant_b = {"clicks": 920, "conversions": 58}

observed = [[variant_a["conversions"], variant_a["clicks"] - variant_a["conversions"]],
            [variant_b["conversions"], variant_b["clicks"] - variant_b["conversions"]]]

chi2, p_value = stats.chi2_contingency(observed)[:2]

if p_value < 0.05:
    print(f"Statistically significant difference (p={p_value:.4f})")
else:
    print(f"Not statistically significant (p={p_value:.4f})")
    print("Need more data before making decisions")
EOF
""")
```

### Forecast Future Performance

```python
Bash("""
python3 << 'EOF'
import numpy as np

historical_roas = [2.1, 2.3, 2.5, 2.8, 2.7, 3.0]
current_spend = 50000

trend = np.polyfit(range(len(historical_roas)), historical_roas, 1)
next_month_roas = np.polyval(trend, len(historical_roas))
projected_revenue = current_spend * next_month_roas

print(f"Projected ROAS next month: {next_month_roas:.2f}")
print(f"With ${current_spend:,} spend, projected revenue: ${projected_revenue:,.2f}")
EOF
""")
```

---

## Performance Scoring Detail (Step 3)

### Scoring Formulas

```javascript
// Individual metric scores (normalized to 0-100)
CTR_Score = Math.min((CTR / Benchmark_CTR) * 50, 100)
CPC_Score = Math.min((Benchmark_CPC / CPC) * 50, 100)  // Lower CPC = better
Conversion_Rate_Score = Math.min((Conversion_Rate / Benchmark_Conv_Rate) * 50, 100)
ROAS_Score = Math.min((ROAS / Target_ROAS) * 50, 100)

// Overall campaign health score (weighted average)
Campaign_Health_Score =
  (CTR_Score * 0.25) +
  (CPC_Score * 0.25) +
  (Conversion_Rate_Score * 0.30) +
  (ROAS_Score * 0.20)
```

### Example Scoring

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

## Diagnostic Framework Detail (Step 4)

### Issue Type 1: Low CTR

```
If CTR < Benchmark_CTR * 0.7:

Potential Causes:
- Poor ad copy (not compelling)
- Weak headline/creative
- Irrelevant targeting (wrong audience)
- Low ad position (Google Ads)
- Ad fatigue (Meta Ads - high frequency)

Diagnostic Questions:
1. Is CTR consistently low across all ad groups? -> Ad copy issue
2. Is CTR low for specific keywords/audiences? -> Targeting issue
3. Has CTR declined over time? -> Ad fatigue
4. Is impression share low? -> Budget/bid issue

Recommendations:
- A/B test new ad copy with stronger value propositions
- Refine audience targeting
- Increase bids for high-value keywords
- Refresh creative assets (Meta Ads)
- Use dynamic keyword insertion (Google Ads)
```

### Issue Type 2: High CPC

```
If CPC > Benchmark_CPC * 1.3:

Potential Causes:
- Highly competitive keywords
- Low Quality Score (Google Ads)
- Poor relevance score (Meta Ads)
- Broad match keywords driving up costs
- Bidding too aggressively

Recommendations:
- Improve Quality Score (better ad relevance, landing page experience)
- Add negative keywords (Google Ads)
- Test long-tail keywords (lower competition)
- Adjust bidding strategy (manual CPC -> target CPA)
- Expand audience (reduce competition)
```

### Issue Type 3: Low Conversion Rate

```
If Conversion_Rate < Benchmark_Conv_Rate * 0.7:

Potential Causes:
- Poor landing page experience
- Traffic not qualified (wrong audience)
- Weak offer/value proposition
- High friction in conversion process
- Slow landing page load time

Recommendations:
- Optimize landing page (speed, clarity, CTA)
- Refine targeting (negative keywords, audience exclusions)
- Strengthen offer (better incentive, urgency)
- Simplify conversion process (fewer form fields)
- A/B test landing page variations
```

### Issue Type 4: Low ROAS / Negative ROI

```
If ROAS < Target_ROAS:

Potential Causes:
- High CPA eating into margins
- Low average order value
- Wrong products promoted
- Attribution issues

Recommendations:
- Focus on high-value products/services
- Improve conversion rate to lower CPA
- Adjust bids for profitability (target ROAS bidding)
- Upsell/cross-sell strategies
- Review attribution model
```

### Issue Type 5: High Frequency (Meta Ads)

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

## Cross-Platform Analysis Detail (Step 5)

```json
{
  "cross_platform_comparison": {
    "google_ads": {
      "total_spend": 15000, "conversions": 450, "cpa": 33.33,
      "roas": 4.2, "efficiency_rank": 1
    },
    "meta_ads": {
      "total_spend": 8000, "conversions": 320, "cpa": 25.00,
      "roas": 3.1, "efficiency_rank": 2
    },
    "linkedin_ads": {
      "total_spend": 5000, "conversions": 85, "cpa": 58.82,
      "roas": 1.8, "efficiency_rank": 3
    },
    "insights": [
      "Google Ads has highest ROAS (4.2) - allocate more budget here",
      "Meta Ads has lowest CPA ($25) - best for lead generation",
      "LinkedIn Ads has high CPA ($58.82) but may have higher lead quality"
    ],
    "budget_reallocation": {
      "current_allocation": {"google_ads": "53.6%", "meta_ads": "28.6%", "linkedin_ads": "17.8%"},
      "recommended_allocation": {"google_ads": "60%", "meta_ads": "30%", "linkedin_ads": "10%"}
    }
  }
}
```

---

## Campaign Categorization Detail (Step 6)

```json
{
  "top_performers": [
    {
      "campaign": "Brand Search - Google",
      "roas": 5.8, "health_score": 87,
      "recommendation": "SCALE - Increase budget by 30-50%"
    }
  ],
  "solid_performers": [
    {
      "campaign": "Retargeting - Meta",
      "roas": 3.2, "health_score": 68,
      "recommendation": "OPTIMIZE - Small improvements can boost ROAS"
    }
  ],
  "underperformers": [
    {
      "campaign": "Cold Audience - LinkedIn",
      "roas": 0.8, "health_score": 32,
      "recommendation": "PAUSE OR RESTRUCTURE - Losing money"
    }
  ],
  "testing_campaigns": [
    {
      "campaign": "New Product Launch - Google",
      "roas": 1.5, "health_score": 45,
      "recommendation": "MONITOR - Give 2 more weeks of data before deciding"
    }
  ]
}
```

---

## Quick Win Example (Step 7)

```json
{
  "quick_win_id": "qw_001",
  "type": "pause_underperformer",
  "campaign": "Cold Audience - LinkedIn Display",
  "current_performance": {
    "spend": "$2,500", "conversions": 12,
    "cpa": "$208.33", "roas": "0.6"
  },
  "issue": "ROAS of 0.6 = losing $1,000/month",
  "action": "Pause campaign immediately",
  "expected_impact": "Save $2,500/month in wasted spend",
  "effort": "1 minute",
  "priority": "CRITICAL"
}
```

---

## Platform-Specific Recommendations Detail (Step 8)

### Google Ads Recommendations

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

### Meta Ads Recommendations

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
   - Exclude underperforming placements (e.g., Audience Network)
   - Test Instagram Stories vs Feed separately
```

### LinkedIn Ads Recommendations

```
1. Audience Targeting:
   - Use job title targeting (more specific = better for B2B)
   - Layer company size, industry, seniority
   - Test Matched Audiences (retargeting, website visitors)
   - Use Account-Based Marketing (ABM) for enterprise

2. Ad Format Selection:
   - Lead Gen Forms: Best for capturing leads (higher conversion rate)
   - Sponsored Content: Best for engagement and awareness
   - Message Ads: High engagement but use sparingly

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

## Budget Reallocation Example (Step 9)

```json
{
  "current_monthly_budget": 30000,
  "campaigns": [
    {
      "name": "Brand Search - Google",
      "current_budget": 8000, "current_percentage": "26.7%",
      "roas": 5.8,
      "recommended_budget": 12000, "recommended_percentage": "40%",
      "change": "+$4,000 (+50%)",
      "rationale": "Highest ROAS - scale aggressively"
    },
    {
      "name": "Cold Audience - LinkedIn",
      "current_budget": 5000, "current_percentage": "16.7%",
      "roas": 0.8,
      "recommended_budget": 1000, "recommended_percentage": "3.3%",
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

## LIGHT Mode Full Output Schema (Step 10)

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
        "spend": 8000, "roas": 5.8,
        "recommendation": "Increase budget by 50%"
      }
    ],
    "underperformers": [
      {
        "campaign": "Cold Audience - LinkedIn Display",
        "spend": 2500, "roas": 0.6,
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
      "how_to": "Go to LinkedIn Campaign Manager -> Select campaign -> Click 'Pause'"
    },
    {
      "priority": 2,
      "action": "Increase budget for 'Brand Search - Google' by 50%",
      "current_situation": "ROAS of 5.8 but budget-limited",
      "expected_impact": "Generate additional $8,000 revenue/month",
      "effort": "2 minutes",
      "how_to": "Google Ads -> Campaigns -> Edit daily budget from $265 to $400"
    },
    {
      "priority": 3,
      "action": "Add 15 negative keywords to 'Non-Brand Search - Google'",
      "current_situation": "High CPC ($4.20) with low conversion rate (2.1%)",
      "expected_impact": "Reduce wasted spend by $500/month",
      "effort": "10 minutes",
      "how_to": "Review Search Terms Report -> Identify irrelevant queries -> Add as negative keywords"
    }
  ],
  "expected_total_impact": {
    "monthly_savings": "$1,500",
    "additional_revenue": "$8,000",
    "net_improvement": "$9,500/month",
    "roas_improvement": "3.2 -> 4.0 (+25%)"
  }
}
```

---

## DEEP Mode Campaign Detail Example

```json
{
  "campaign_id": "camp_001",
  "platform": "google_ads",
  "campaign_name": "Brand Search",
  "campaign_type": "Search",
  "status": "Active",
  "budget": {"daily": 265, "monthly": 8000, "utilization": "100%"},
  "performance": {
    "impressions": 45000, "clicks": 2160, "ctr": 4.8, "cpc": 3.70,
    "conversions": 180, "conversion_rate": 8.33, "cpa": 44.44,
    "revenue": 46800, "roas": 5.85, "quality_score_avg": 8.2
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
}
```

---

## DEEP Mode Optimization Roadmap

```json
{
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

## Agent Summary Example

```
Campaign Analysis Complete!

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
1. Pause LinkedIn campaign -> Save $1,000/month
2. Increase Google brand budget -> +$8,000 revenue/month
3. Add negative keywords -> Reduce waste by $500/month

Total Projected Impact: +$9,500/month (+31% ROAS improvement)

Full report: /data/ads/campaign-analysis-acme-deep.json
```
