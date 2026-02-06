# Ads Audience Insights - Detailed Workflow Reference

This document contains detailed JSON output schemas, segmentation examples, and platform-specific analysis templates for the ads-audience-insights skill.

---

## Data Collection Format (Step 1)

### Structured Data Format

```json
{
  "platform": "meta_ads",
  "audience_breakdown": {
    "by_age": [
      {"age_range": "25-34", "spend": 2500, "conversions": 85, "cpa": 29.41, "roas": 3.8},
      {"age_range": "35-44", "spend": 1800, "conversions": 45, "cpa": 40.00, "roas": 2.5}
    ],
    "by_gender": [],
    "by_location": []
  }
}
```

---

## Performance Scoring Detail (Step 2)

### Calculation

```javascript
// Calculate key metrics
CTR = (Clicks / Impressions) * 100
CPC = Spend / Clicks
Conversion_Rate = (Conversions / Clicks) * 100
CPA = Spend / Conversions
ROAS = Revenue / Spend

// Performance score (0-100)
Audience_Performance_Score =
  (CTR_vs_Avg * 0.25) +
  (CPA_vs_Avg * 0.35) +
  (ROAS_vs_Avg * 0.40)
```

### Segmentation Example

```json
{
  "platform": "meta_ads",
  "segment_type": "age",
  "segments": [
    {
      "segment": "25-34",
      "impressions": 125000,
      "clicks": 1250,
      "spend": 2500,
      "conversions": 85,
      "revenue": 9500,
      "metrics": {
        "ctr": 1.00,
        "cpc": 2.00,
        "conversion_rate": 6.80,
        "cpa": 29.41,
        "roas": 3.80
      },
      "vs_account_average": {
        "ctr": "+11%",
        "cpa": "-18%",
        "roas": "+27%"
      },
      "performance_score": 87,
      "category": "STAR AUDIENCE",
      "recommendation": "SCALE - Increase budget allocation by 30%"
    },
    {
      "segment": "55-64",
      "impressions": 80000,
      "clicks": 560,
      "spend": 1400,
      "conversions": 12,
      "revenue": 840,
      "metrics": {
        "ctr": 0.70,
        "cpc": 2.50,
        "conversion_rate": 2.14,
        "cpa": 116.67,
        "roas": 0.60
      },
      "vs_account_average": {
        "ctr": "-22%",
        "cpa": "+297%",
        "roas": "-80%"
      },
      "performance_score": 18,
      "category": "POOR - EXCLUDE",
      "recommendation": "Exclude 55-64 age range from targeting"
    }
  ]
}
```

---

## Demographic Insights Detail (Step 3)

### Age Analysis Example

```json
{
  "age_insights": {
    "best_age_range": "25-34",
    "best_age_performance": {
      "cpa": 29.41,
      "roas": 3.8,
      "conversion_share": "42%"
    },
    "worst_age_range": "55-64",
    "worst_age_performance": {
      "cpa": 116.67,
      "roas": 0.6,
      "conversion_share": "3%"
    },
    "key_finding": "25-34 age group drives 42% of conversions at lowest CPA - should be primary target",
    "recommendations": [
      "Exclude 55-64 age range (ROAS 0.6)",
      "Increase bids for 25-34 age range",
      "Test creative specifically for 35-44 (moderate performance, untapped potential)"
    ]
  }
}
```

### Gender Analysis Example

```json
{
  "gender_insights": {
    "female_performance": {
      "conversion_rate": 8.2,
      "cpa": 28.50,
      "roas": 4.2,
      "share_of_conversions": "65%"
    },
    "male_performance": {
      "conversion_rate": 5.1,
      "cpa": 42.30,
      "roas": 2.8,
      "share_of_conversions": "35%"
    },
    "key_finding": "Female audience converts 60% better (8.2% vs 5.1%) with 32% lower CPA",
    "recommendations": [
      "Adjust budget: 70% female, 30% male (from current 50/50)",
      "Create female-focused ad creative",
      "Test female-specific messaging in ad copy"
    ]
  }
}
```

### Location Analysis Example

```json
{
  "location_insights": {
    "top_locations": [
      {"location": "California", "conversions": 180, "cpa": 32.50, "roas": 3.9},
      {"location": "New York", "conversions": 145, "cpa": 35.80, "roas": 3.6},
      {"location": "Texas", "conversions": 120, "cpa": 38.20, "roas": 3.2}
    ],
    "poor_locations": [
      {"location": "Montana", "conversions": 2, "cpa": 225.00, "roas": 0.4}
    ],
    "recommendations": [
      "Exclude low-population states with <10 conversions and ROAS <1.0",
      "Increase bids by 15% in California (best ROAS)",
      "Test geo-specific ad copy for top 3 markets"
    ]
  }
}
```

---

## Behavioral & Interest Insights Detail (Step 4)

### Google Ads In-Market Audiences

```json
{
  "in_market_audiences": [
    {
      "audience": "Business Software > CRM Software",
      "performance": {
        "impressions": 45000,
        "conversions": 95,
        "cpa": 38.95,
        "roas": 3.5
      },
      "vs_account_avg": {"cpa": "-5%", "roas": "+17%"},
      "status": "Strong performer",
      "recommendation": "Increase bids by 20%"
    },
    {
      "audience": "Business Software > Project Management",
      "performance": {
        "conversions": 12,
        "cpa": 92.50,
        "roas": 1.1
      },
      "status": "Underperformer",
      "recommendation": "Exclude or reduce bids by 50%"
    }
  ]
}
```

### Meta Ads Interest Targeting

```json
{
  "interest_insights": [
    {
      "interest": "Small Business Owners",
      "metrics": {"ctr": 1.2, "cpa": 28.50, "roas": 4.1, "engagement_rate": 3.5},
      "category": "STAR INTEREST",
      "recommendation": "Create dedicated campaign for this audience"
    },
    {
      "interest": "Marketing Automation",
      "metrics": {"ctr": 0.95, "cpa": 35.20, "roas": 3.2, "engagement_rate": 2.8},
      "category": "GOOD",
      "recommendation": "Continue targeting, test lookalikes"
    }
  ]
}
```

### LinkedIn Professional Demographics

```json
{
  "job_title_performance": [
    {
      "job_title_category": "VP of Marketing",
      "metrics": {
        "impressions": 15000, "clicks": 85, "conversions": 8,
        "cpa": 125.00, "ctr": 0.57
      },
      "vs_account_avg": {"cpa": "+15% (but higher LTV justifies)", "ctr": "+30%"},
      "recommendation": "Continue - high LTV offsets higher CPA"
    },
    {
      "job_title_category": "Coordinator / Associate",
      "metrics": {"conversions": 2, "cpa": 450.00, "ctr": 0.18},
      "recommendation": "Exclude - too junior for $10K+ product"
    }
  ],
  "seniority_insights": {
    "best_seniority": "Director",
    "worst_seniority": "Entry-level",
    "recommendation": "Focus on Director+ levels, exclude Entry and Coordinator"
  }
}
```

---

## Device & Placement Analysis Detail (Step 5)

### Device Performance

```json
{
  "device_insights": {
    "mobile": {
      "conversion_share": "72%", "cpa": 32.50,
      "conversion_rate": 7.2, "roas": 3.8
    },
    "desktop": {
      "conversion_share": "25%", "cpa": 45.80,
      "conversion_rate": 4.5, "roas": 2.6
    },
    "tablet": {
      "conversion_share": "3%", "cpa": 85.00,
      "conversion_rate": 2.1, "roas": 1.2
    },
    "key_finding": "Mobile drives 72% of conversions with best CPA and ROAS",
    "recommendations": [
      "Increase mobile bids by 25%",
      "Decrease tablet bids by 50% (or exclude)",
      "Ensure landing pages are mobile-optimized",
      "Consider mobile-specific creative"
    ]
  }
}
```

### Placement Performance (Meta Ads)

```json
{
  "placement_insights": {
    "instagram_feed": {"cpa": 28.20, "roas": 4.5, "ctr": 1.35},
    "facebook_feed": {"cpa": 35.60, "roas": 3.2, "ctr": 0.92},
    "audience_network": {"cpa": 95.50, "roas": 0.9, "ctr": 0.45},
    "recommendations": [
      "Allocate 60% of budget to Instagram Feed (best ROAS)",
      "Exclude Audience Network (ROAS < 1.0)",
      "Test Instagram Reels (emerging format)"
    ]
  }
}
```

---

## Frequency & Saturation Analysis Detail (Step 6)

### Frequency Analysis

```json
{
  "frequency_analysis": {
    "audience_name": "Retargeting - Website Visitors (30 days)",
    "current_frequency": 5.8,
    "audience_size": 15000,
    "status": "CRITICAL - Ad Fatigue",
    "symptoms": [
      "CTR declined from 1.2% to 0.7% over last 14 days",
      "CPC increased from $2.50 to $3.80",
      "ROAS dropped from 4.2 to 2.8"
    ],
    "recommendations": [
      "Reduce daily budget from $150 to $100",
      "Refresh creative (new images/video)",
      "Expand remarketing window to 90 days",
      "Set frequency cap at 4 impressions per 7 days"
    ]
  }
}
```

---

## Audience Expansion Opportunities Detail (Step 7)

### Lookalike Recommendations

```json
{
  "lookalike_recommendations": [
    {
      "platform": "meta_ads",
      "source_audience": "Converters - Last 90 Days (1,200 people)",
      "lookalike_size": "1%",
      "estimated_reach": "2.1M (US)",
      "expected_performance": "CPA: $32-38 (based on source CPA: $30)",
      "priority": "HIGH",
      "test_budget": "$500 for 7 days"
    },
    {
      "platform": "google_ads",
      "source_audience": "Website Visitors - 30 Days",
      "similar_audience_tier": "2%",
      "estimated_reach": "5M",
      "priority": "MEDIUM",
      "test_budget": "$300 for 7 days"
    }
  ]
}
```

### Interest Expansion

```
If "Small Business Owners" performs well, test:
  - "Entrepreneurship"
  - "Business Management"
  - "Startup Companies"
  - "Business Owner"

If "Marketing Automation" performs well, test:
  - "Email Marketing"
  - "CRM Software"
  - "Digital Marketing"
  - "Marketing Strategy"
```

### Audience Stacking

```
Combine demographic + interest + behavior for precision:

Example Stack:
  Age: 25-44
  + Gender: Female
  + Interest: Small Business Owners
  + Behavior: Business Decision Maker
  = Highly targeted, likely to convert

Test vs broad targeting to compare performance
```

---

## Exclusion Recommendations Detail (Step 8)

```json
{
  "recommended_exclusions": [
    {
      "exclusion_type": "age_range",
      "value": "18-24",
      "reason": "ROAS 0.5, CPA $128 (target: $40)",
      "platform": "meta_ads",
      "expected_impact": "Save $800/month in wasted spend"
    },
    {
      "exclusion_type": "placement",
      "value": "Audience Network",
      "reason": "ROAS 0.6, low quality traffic",
      "platform": "meta_ads",
      "expected_impact": "Improve overall ROAS by 15%"
    },
    {
      "exclusion_type": "job_seniority",
      "value": "Entry-level",
      "reason": "0% conversion rate, CPA $450",
      "platform": "linkedin_ads",
      "expected_impact": "Save $600/month"
    }
  ]
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
    "generated_at": "2024-01-15T17:00:00Z"
  },
  "executive_summary": {
    "key_finding": "25-34 female audience drives 42% of conversions at 35% lower CPA than account average",
    "best_audience": {
      "segment": "Female, Age 25-34, Interest: Small Business Owners",
      "platform": "Meta Ads",
      "cpa": 26.50,
      "roas": 4.8,
      "recommendation": "SCALE - Increase budget by 50%"
    },
    "worst_audience": {
      "segment": "Male, Age 55-64",
      "platform": "Meta Ads",
      "cpa": 142.00,
      "roas": 0.5,
      "recommendation": "EXCLUDE - Losing money"
    }
  },
  "top_3_actions": [
    {
      "priority": 1,
      "action": "Exclude age 55-64 from all Meta campaigns",
      "rationale": "ROAS of 0.5, CPA $142 (target: $35)",
      "expected_impact": "Save $1,200/month in wasted spend",
      "effort": "2 minutes",
      "how_to": "Meta Ads Manager -> All campaigns -> Edit -> Exclude 55-64 age range"
    },
    {
      "priority": 2,
      "action": "Increase budget for 25-34 female audience by 50%",
      "rationale": "Best performing segment (ROAS 4.8, CPA $26.50)",
      "expected_impact": "Generate $4,500 additional revenue/month",
      "effort": "5 minutes",
      "how_to": "Create dedicated ad set for this audience with increased budget"
    },
    {
      "priority": 3,
      "action": "Create 1% lookalike audience from converters (Meta)",
      "rationale": "Top audience expansion opportunity based on best performers",
      "expected_impact": "Reach 2M+ similar users, projected CPA ~$30",
      "effort": "10 minutes",
      "how_to": "Meta Ads Manager -> Audiences -> Create Lookalike -> Source: Converters -> Size: 1%"
    }
  ],
  "projected_impact": {
    "monthly_savings_from_exclusions": "$1,200",
    "additional_revenue_from_scaling": "$4,500",
    "estimated_roas_improvement": "3.2 -> 3.9 (+22%)"
  }
}
```

---

## DEEP Mode Audience Strategy Document (Step 9)

```json
{
  "audience_strategy": {
    "target_audience_profile": {
      "primary_audience": {
        "demographics": {
          "age": "25-44",
          "gender": "Female-leaning (65% female, 35% male)",
          "location": "US (focus: CA, NY, TX)",
          "income": "$75K+ household income"
        },
        "professional_profile": {
          "job_titles": ["VP of Marketing", "Marketing Director", "Marketing Manager"],
          "seniority": "Manager to VP level",
          "company_size": "50-500 employees",
          "industries": ["Technology", "SaaS", "E-commerce"]
        },
        "interests_behaviors": {
          "interests": ["Small Business Owners", "Marketing Automation", "Digital Marketing"],
          "behaviors": ["Business Decision Makers", "Tech Early Adopters"],
          "in_market": ["Business Software", "Marketing Services"]
        }
      },
      "secondary_audience": {
        "demographics": {"age": "35-54", "gender": "Male", "location": "US + Canada"},
        "professional_profile": {
          "job_titles": ["CMO", "VP of Sales", "Business Owner"],
          "company_size": "100-1000 employees"
        }
      }
    },
    "platform_allocation": {
      "google_ads": {
        "budget_allocation": "50%",
        "primary_audiences": [
          "In-Market: Business Software",
          "Remarketing: Website Visitors (30 days)",
          "Similar Audiences: 1% Converters"
        ],
        "targeting_strategy": "Intent-based (search campaigns) + remarketing"
      },
      "meta_ads": {
        "budget_allocation": "35%",
        "primary_audiences": [
          "Lookalike: 1% Top Customers",
          "Interest: Small Business Owners + Marketing Automation",
          "Retargeting: Website Visitors + Video Viewers"
        ],
        "targeting_strategy": "Lookalikes + interest stacking + retargeting"
      },
      "linkedin_ads": {
        "budget_allocation": "15%",
        "primary_audiences": [
          "Job Title: VP/Director of Marketing",
          "Company Size: 50-500 employees",
          "Lookalike: Customer List"
        ],
        "targeting_strategy": "Precision B2B targeting for high-value leads"
      }
    },
    "testing_roadmap": {
      "month_1": [
        "Test 1% lookalikes on Meta (best performers)",
        "Test similar audiences on Google (website converters)",
        "Refine age targeting (exclude 18-24 and 55+)"
      ],
      "month_2": [
        "Test interest expansion on Meta (5 new related interests)",
        "Test broader lookalikes (3%, 5%) if 1% performs well",
        "Test new job titles on LinkedIn"
      ],
      "month_3": [
        "Test Advantage+ audiences (Meta) vs manual targeting",
        "Test geo-expansion (international markets)",
        "Launch Account-Based Marketing on LinkedIn"
      ]
    }
  }
}
```

---

## Agent Summary Example

```
Audience Insights Analysis Complete!

Best Audience: Female, 25-34, Small Business Owners
- CPA: $26.50 (vs avg $39.80)
- ROAS: 4.8 (vs avg 3.2)
- 36% of conversions

Worst Audience: Male, 55-64
- CPA: $225 (vs avg $39.80)
- ROAS: 0.4
- EXCLUDE to save $1,200/month

Top 3 Actions:
1. Exclude 55-64 age range -> Save $1,200/month
2. Scale 25-34 female audience -> +$4,500 revenue/month
3. Create 1% lookalike from converters -> Reach 2.1M similar users

Projected Impact: +$14,100/month, +34% ROAS improvement

Full report: /data/ads/audience-insights-acme-deep.json
```
