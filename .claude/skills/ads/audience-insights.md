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
- Campaign data (from campaign-analysis.md OR provided separately)
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
```
1. Demographic Audiences:
   - Age ranges
   - Gender
   - Parental status
   - Household income

2. In-Market Audiences:
   - Users actively researching/ready to buy
   - Category-based (e.g., "Business Software")

3. Affinity Audiences:
   - Based on interests and habits
   - Broader reach (awareness stage)

4. Custom Intent Audiences:
   - Based on keywords, URLs, apps
   - Created by advertiser

5. Remarketing Audiences:
   - Website visitors
   - App users
   - Customer lists (Customer Match)
   - YouTube engagers

6. Similar Audiences:
   - Lookalikes based on remarketing lists
```

### Meta Ads Audiences
```
1. Core Audiences (targeting):
   - Demographics (age, gender, education, etc.)
   - Location
   - Interests
   - Behaviors
   - Connections

2. Custom Audiences:
   - Website visitors (Meta Pixel)
   - Customer lists
   - App activity
   - Offline activity
   - Engagement (video views, Instagram, Facebook page)

3. Lookalike Audiences:
   - 1% (most similar)
   - 2-10% (broader)
   - Based on: Converters, Page Likes, Custom Lists

4. Advantage+ Audiences:
   - Automated targeting by Meta AI
```

### LinkedIn Ads Audiences
```
1. Professional Demographics:
   - Job title
   - Job function
   - Seniority level
   - Company name
   - Company size
   - Company industry
   - Years of experience
   - Skills

2. Matched Audiences:
   - Website retargeting
   - Contact targeting (email lists)
   - Account-based marketing (company lists)
   - Lookalike audiences

3. Interest-Based:
   - Member interests
   - Member groups
```

---

## Workflow Steps

### Step 1: Data Collection

**Option A: Platform Reports Provided**

```
Read audience performance data:

Google Ads: Audience Report
- Navigate to: Audiences → Demographics / Audience segments
- Metrics: Impressions, Clicks, CTR, Conversions, CPA, ROAS

Meta Ads: Breakdown Report
- Navigate to: Ads Manager → Breakdown by Age/Gender/Location/Placement
- Metrics: Reach, Impressions, Clicks, CPA, ROAS, Frequency

LinkedIn Ads: Demographics Report
- Navigate to: Campaign Manager → Demographics
- Metrics: Impressions, Clicks, CTR, Conversions, CPA

Parse data into structured format:
{
  "platform": "meta_ads",
  "audience_breakdown": {
    "by_age": [
      {"age_range": "25-34", "spend": 2500, "conversions": 85, "cpa": 29.41, "roas": 3.8},
      {"age_range": "35-44", "spend": 1800, "conversions": 45, "cpa": 40.00, "roas": 2.5}
    ],
    "by_gender": [ ... ],
    "by_location": [ ... ]
  }
}
```

**Option B: No Detailed Data Available**

```
If user doesn't have audience breakdowns:
1. Request high-level campaign data
2. Make informed estimates based on:
   - Industry benchmarks
   - Target market (B2B vs B2C)
   - Product price point
3. Provide recommendations based on best practices
```

---

### Step 2: Audience Performance Analysis

**For Each Audience Segment**:

```javascript
// Calculate key metrics
CTR = (Clicks / Impressions) × 100
CPC = Spend / Clicks
Conversion_Rate = (Conversions / Clicks) × 100
CPA = Spend / Conversions
ROAS = Revenue / Spend

// Performance score (0-100)
Audience_Performance_Score =
  (CTR_vs_Avg × 0.25) +
  (CPA_vs_Avg × 0.35) +  // CPA weighted highest
  (ROAS_vs_Avg × 0.40)

// Categorize
if (ROAS >= Target_ROAS × 1.5) → "STAR AUDIENCE"
else if (ROAS >= Target_ROAS) → "GOOD AUDIENCE"
else if (ROAS >= Target_ROAS × 0.7) → "NEEDS OPTIMIZATION"
else → "POOR - CONSIDER EXCLUDING"
```

**Audience Segmentation Example**:

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

### Step 3: Demographic Insights

**Analyze performance by demographics**:

#### Age Analysis

```
For each age range:
  Calculate: CPA, ROAS, Conversion Rate
  Compare to account average
  Identify best and worst performing

Insights:
- Best performing age range(s)
- Worst performing age range(s)
- Age distribution of conversions
- Opportunities (underinvested age groups with good performance)

Example Insights:
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

#### Gender Analysis

```
Compare male vs female vs unknown:
  - Conversion rates
  - CPA
  - ROAS
  - Engagement patterns (Meta: reactions, shares)

Example Insights:
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

#### Location Analysis

```
Analyze by:
  - Country
  - State/Region
  - City (if data available)
  - DMA (Designated Market Area) for US

Identify:
  - Highest converting locations
  - Most cost-effective locations
  - Underperforming locations to exclude

Example:
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

### Step 4: Behavioral & Interest Insights

**DEEP Mode Only** - Analyze audience interests and behaviors:

#### Google Ads: In-Market & Affinity Audiences

```
For each In-Market audience:
  Compare: CPA, ROAS vs account average

Example:
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
      "vs_account_avg": {
        "cpa": "-5%",
        "roas": "+17%"
      },
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

#### Meta Ads: Interest Targeting

```
If detailed interest data available:

For each interest category:
  Analyze: CTR, CPA, ROAS, Engagement Rate

Example:
{
  "interest_insights": [
    {
      "interest": "Small Business Owners",
      "metrics": {
        "ctr": 1.2,
        "cpa": 28.50,
        "roas": 4.1,
        "engagement_rate": 3.5
      },
      "category": "STAR INTEREST",
      "recommendation": "Create dedicated campaign for this audience"
    },
    {
      "interest": "Marketing Automation",
      "metrics": {
        "ctr": 0.95,
        "cpa": 35.20,
        "roas": 3.2,
        "engagement_rate": 2.8
      },
      "category": "GOOD",
      "recommendation": "Continue targeting, test lookalikes"
    }
  ]
}
```

#### LinkedIn: Professional Demographics

```
Analyze by:
  - Job Title
  - Job Function (e.g., Marketing, IT, Sales)
  - Seniority (Entry, Manager, Director, VP, C-Level)
  - Company Size
  - Industry

Example:
{
  "job_title_performance": [
    {
      "job_title_category": "VP of Marketing",
      "metrics": {
        "impressions": 15000,
        "clicks": 85,
        "conversions": 8,
        "cpa": 125.00,
        "ctr": 0.57
      },
      "vs_account_avg": {
        "cpa": "+15% (but higher LTV justifies)",
        "ctr": "+30%"
      },
      "recommendation": "Continue - high LTV offsets higher CPA"
    },
    {
      "job_title_category": "Coordinator / Associate",
      "metrics": {
        "conversions": 2,
        "cpa": 450.00,
        "ctr": 0.18
      },
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

### Step 5: Device & Placement Analysis

**Analyze performance by device and ad placement**:

#### Device Performance

```
Compare:
  - Desktop
  - Mobile
  - Tablet

Metrics: CTR, CPA, ROAS, Conversion Rate

Example:
{
  "device_insights": {
    "mobile": {
      "conversion_share": "72%",
      "cpa": 32.50,
      "conversion_rate": 7.2,
      "roas": 3.8
    },
    "desktop": {
      "conversion_share": "25%",
      "cpa": 45.80,
      "conversion_rate": 4.5,
      "roas": 2.6
    },
    "tablet": {
      "conversion_share": "3%",
      "cpa": 85.00,
      "conversion_rate": 2.1,
      "roas": 1.2
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

#### Placement Performance (Meta Ads Specific)

```
Compare placements:
  - Facebook Feed
  - Instagram Feed
  - Facebook Stories
  - Instagram Stories
  - Reels
  - Audience Network
  - Messenger

Example:
{
  "placement_insights": {
    "instagram_feed": {
      "cpa": 28.20,
      "roas": 4.5,
      "ctr": 1.35
    },
    "facebook_feed": {
      "cpa": 35.60,
      "roas": 3.2,
      "ctr": 0.92
    },
    "audience_network": {
      "cpa": 95.50,
      "roas": 0.9,
      "ctr": 0.45
    },
    "recommendations": [
      "Allocate 60% of budget to Instagram Feed (best ROAS)",
      "Exclude Audience Network (ROAS < 1.0)",
      "Test Instagram Reels (emerging format)"
    ]
  }
}
```

---

### Step 6: Audience Overlap & Saturation Analysis

**DEEP Mode Only** - Identify audience fatigue and overlap:

#### Frequency Analysis (Meta Ads)

```
Check average frequency (how many times same person sees ad):

Optimal Frequency: 2-3
Warning: 4-5
Critical: 6+

If Frequency > 4.0:
  - Audience too small or budget too high
  - Ad fatigue likely
  - CTR declining, CPC increasing

Recommendations:
  - Expand audience size
  - Refresh creative
  - Reduce budget
  - Set frequency cap

Example:
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

#### Audience Saturation

```
Saturation indicators:
  - Decreasing reach despite constant budget
  - Increasing CPM/CPC over time
  - Declining CTR
  - Audience size <50K (Meta) or <10K (LinkedIn)

Recommendations when saturated:
  - Expand audience (broaden targeting)
  - Create lookalike audiences
  - Explore new audience segments
  - Test Advantage+ (Meta) for automated expansion
```

---

### Step 7: Audience Expansion Opportunities

**Identify new audiences to test**:

#### Lookalike/Similar Audience Recommendations

```
Based on best performing audiences, recommend lookalikes:

Google Ads - Similar Audiences:
  Source: Website visitors who converted
  Recommendation: Create 1%, 2%, 5% similar audiences

Meta Ads - Lookalike Audiences:
  Source Options:
    1. Top 1% of customers by LTV
    2. All converters (last 90 days)
    3. High-engagers (video views 75%+)
  Recommendation: Test 1%, 3%, 5% lookalikes

LinkedIn - Lookalike Audiences:
  Source: Customer email list (1000+ contacts)
  Recommendation: Test lookalikes in same industries

Example:
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

#### Interest Expansion (Meta Ads)

```
Suggest related interests based on top performers:

If "Small Business Owners" performs well:
  Test:
    - "Entrepreneurship"
    - "Business Management"
    - "Startup Companies"
    - "Business Owner"

If "Marketing Automation" performs well:
  Test:
    - "Email Marketing"
    - "CRM Software"
    - "Digital Marketing"
    - "Marketing Strategy"
```

#### Audience Stacking (Multi-Layering)

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

### Step 8: Exclusion Recommendations

**Identify audiences to exclude** for better efficiency:

```
Exclusion Criteria:
  - ROAS < 0.7 AND sufficient data (>100 clicks)
  - Very high CPA (>2x target)
  - Low conversion rate (<50% of account avg)

Example Exclusions:
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
      "exclusion_type": "gender",
      "value": "male",
      "reason": "Female audience converts 3x better with 50% lower CPA",
      "platform": "meta_ads",
      "expected_impact": "May be too aggressive - consider reducing budget instead"
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

### Step 9: Audience Strategy Document

**DEEP Mode Only** - Create comprehensive audience strategy:

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
        "demographics": {
          "age": "35-54",
          "gender": "Male",
          "location": "US + Canada"
        },
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

### Step 10: Output Generation

**LIGHT Mode Output** (`/data/ads/audience-insights-{company}-light.json`):

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
      "how_to": "Meta Ads Manager → All campaigns → Edit → Exclude 55-64 age range"
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
      "how_to": "Meta Ads Manager → Audiences → Create Lookalike → Source: Converters → Size: 1%"
    }
  ],
  "projected_impact": {
    "monthly_savings_from_exclusions": "$1,200",
    "additional_revenue_from_scaling": "$4,500",
    "estimated_roas_improvement": "3.2 → 3.9 (+22%)"
  }
}
```

**DEEP Mode Output** (`/data/ads/audience-insights-{company}-deep.json`):

```json
{
  "metadata": {
    "mode": "DEEP",
    "company": "AcmeCorp",
    "date_range": "2024-01-01 to 2024-01-31",
    "platforms_analyzed": ["google_ads", "meta_ads", "linkedin_ads"],
    "audience_segments_analyzed": 47,
    "generated_at": "2024-01-15T17:00:00Z",
    "analysis_duration_minutes": 26
  },
  "demographic_insights": {
    "age": {
      "performance_by_age": [
        {
          "age_range": "25-34",
          "spend": 4500,
          "conversions": 145,
          "cpa": 31.03,
          "roas": 4.2,
          "conversion_share": "36%",
          "vs_account_avg": {"cpa": "-22%", "roas": "+31%"},
          "category": "STAR SEGMENT"
        },
        {
          "age_range": "35-44",
          "spend": 3200,
          "conversions": 98,
          "cpa": 32.65,
          "roas": 3.8,
          "conversion_share": "24%",
          "vs_account_avg": {"cpa": "-18%", "roas": "+19%"},
          "category": "STRONG SEGMENT"
        },
        {
          "age_range": "55-64",
          "spend": 1800,
          "conversions": 8,
          "cpa": 225.00,
          "roas": 0.4,
          "conversion_share": "2%",
          "vs_account_avg": {"cpa": "+464%", "roas": "-87%"},
          "category": "POOR - EXCLUDE"
        }
      ],
      "key_insights": [
        "25-44 age range drives 60% of conversions",
        "55+ age range has ROAS <1.0 - should be excluded",
        "18-24 has good CTR but low conversion rate - possible awareness play"
      ],
      "recommendations": [
        "Focus 70% of budget on 25-44 age range",
        "Exclude 55-64 age range entirely",
        "Test 18-24 for top-of-funnel awareness campaigns only"
      ]
    },
    "gender": {
      /* Similar detailed breakdown */
    },
    "location": {
      /* Similar detailed breakdown */
    }
  },
  "behavioral_insights": {
    "google_in_market": [ /* ... */ ],
    "meta_interests": [ /* ... */ ],
    "linkedin_professional": [ /* ... */ ]
  },
  "device_placement_insights": {
    /* Device and placement analysis */
  },
  "audience_saturation_analysis": {
    "audiences_at_risk": [
      {
        "audience": "Retargeting - 30 Day Website Visitors",
        "frequency": 6.2,
        "status": "CRITICAL SATURATION",
        "symptoms": [
          "CTR declined 42% over last 14 days",
          "CPC up 38%",
          "ROAS dropped from 5.2 to 3.1"
        ],
        "recommendations": [
          "Immediate: Reduce budget by 40%",
          "Refresh creative within 48 hours",
          "Expand to 90-day window",
          "Set frequency cap at 3 per 7 days"
        ]
      }
    ]
  },
  "audience_expansion_roadmap": {
    "immediate_opportunities": [
      {
        "type": "lookalike",
        "platform": "meta_ads",
        "source": "Top 20% Customers by LTV (450 people)",
        "lookalike_size": "1%",
        "estimated_reach": "2.1M",
        "test_budget": "$500 for 7 days",
        "expected_cpa": "$28-35",
        "priority": "HIGH"
      }
    ],
    "month_1_3_expansion": [ /* ... */ ],
    "long_term_tests": [ /* ... */ ]
  },
  "exclusion_recommendations": {
    /* Detailed exclusions */
  },
  "ideal_customer_profile": {
    "data_driven_icp": {
      "demographics": {
        "age": "25-44 (sweet spot: 30-38)",
        "gender": "65% female, 35% male",
        "location": "Top metros: SF Bay Area, NYC, LA, Austin, Seattle",
        "income": "$75K-150K household"
      },
      "professional": {
        "titles": ["Marketing Director", "VP of Marketing", "Marketing Manager"],
        "seniority": "Manager to VP",
        "company_size": "50-500 employees",
        "industries": ["SaaS", "Technology", "E-commerce"]
      },
      "behavioral": {
        "interests": ["Small Business Owners", "Marketing Automation", "Entrepreneurship"],
        "device_preference": "72% mobile",
        "best_placements": ["Instagram Feed", "Facebook Feed"],
        "engagement_pattern": "High video engagement (75%+ watch time)"
      }
    }
  },
  "budget_reallocation": {
    /* Detailed budget recommendations by audience segment */
  },
  "projected_impact": {
    "if_all_recommendations_implemented": {
      "exclusions_savings": "$2,400/month",
      "scaling_top_audiences": "+$8,500 revenue/month",
      "new_audience_tests": "+$3,200 revenue/month (if successful)",
      "total_impact": "+$14,100/month",
      "roas_improvement": "3.2 → 4.3 (+34%)"
    }
  }
}
```

---

## Validation Checks

1. **Data Completeness**: At least 3 audience dimensions analyzed (age, gender, location minimum)
2. **Statistical Significance**: Flag segments with <50 clicks as "Insufficient Data"
3. **Recommendations Prioritized**: All recommendations have priority and expected impact
4. **ICP Defined**: DEEP mode includes data-driven ideal customer profile
5. **Expansion Plan**: At least 3 lookalike/similar audience recommendations

---

## Usage Example

**Agent Workflow**:
```
1. Read this skill file
2. Collect audience data (from platform reports or campaign-analysis.md)
3. Determine mode (LIGHT or DEEP)
4. Use TodoWrite to track analysis:
   [ ] Data collection
   [ ] Demographic analysis
   [ ] Behavioral insights
   [ ] Device/placement analysis
   [ ] Saturation check
   [ ] Expansion opportunities
   [ ] Exclusion recommendations
   [ ] Output generation
5. Execute analysis
6. Save JSON to /data/ads/
7. Provide summary:
   "Audience Insights Analysis Complete!

    Best Audience: Female, 25-34, Small Business Owners
    - CPA: $26.50 (vs avg $39.80)
    - ROAS: 4.8 (vs avg 3.2)
    - 36% of conversions

    Worst Audience: Male, 55-64
    - CPA: $225 (vs avg $39.80)
    - ROAS: 0.4
    - EXCLUDE to save $1,200/month

    Top 3 Actions:
    1. Exclude 55-64 age range → Save $1,200/month
    2. Scale 25-34 female audience → +$4,500 revenue/month
    3. Create 1% lookalike from converters → Reach 2.1M similar users

    Projected Impact: +$14,100/month, +34% ROAS improvement

    Full report: /data/ads/audience-insights-acme-deep.json"
```

---

## Integration with Other Skills

**Works with**:
- **campaign-analysis.md** - Uses campaign data to extract audience insights
- **creative-optimization.md** - Inform creative decisions based on audience preferences

---

## MCP Tools Needed

**Current**: Built-in tools sufficient (Read, Write)

**Future Enhancement**:
- `mcp__AdsAPI__audience_builder` - Automated lookalike/similar audience creation
- `mcp__Analytics__customer_matching` - Match ad data with CRM for LTV analysis
