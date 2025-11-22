# Ads Creative Optimization

## Purpose
Analyze ad creative performance (copy, images, videos) across platforms, identify winning creative elements, detect creative fatigue, and provide data-driven recommendations for creative testing and optimization.

---

## Execution Modes

### LIGHT Mode (5-10 minutes)
**Goal**: Identify top 3 performing creatives and quick creative wins
**Scope**: High-level creative performance comparison
**Output**: Best creatives to scale + worst to pause + 3 creative tests to run

### DEEP Mode (20-30 minutes)
**Goal**: Comprehensive creative audit with systematic testing framework
**Scope**: Detailed creative element analysis (headlines, copy, visuals, CTAs)
**Output**: Creative testing roadmap with 10-15 test hypotheses

---

## Prerequisites

**Required Input**:
- Ad creative performance data (by ad or ad creative)
- Platforms used (Google Ads, Meta Ads, LinkedIn Ads)
- Campaign objectives (awareness, consideration, conversion)

**Optional**:
- Access to actual ad creatives (images, videos, copy)
- Historical creative performance (for trend analysis)
- Competitor ad examples

**Data Sources**:
1. Ad-level performance reports from platforms
2. CSV exports with creative breakdowns
3. Screenshots of ads + performance metrics
4. Creative library (images/videos + copy in files)

---

## Creative Elements by Platform

### Google Ads Creative Elements
```
Search Ads:
  - Headlines (up to 15)
  - Descriptions (up to 4)
  - Display Path
  - Ad Extensions (sitelinks, callouts, etc.)

Display/Discovery Ads:
  - Images (multiple sizes)
  - Headlines
  - Descriptions
  - Logos
  - Call-to-Action button

Video Ads (YouTube):
  - Video creative
  - Headline
  - Description
  - Call-to-Action overlay
```

### Meta Ads Creative Elements
```
Image/Carousel Ads:
  - Primary Text
  - Headline
  - Description
  - Image/Images
  - Call-to-Action button

Video Ads:
  - Video creative
  - Primary Text
  - Headline
  - Description
  - CTA button
  - Thumbnail image

Stories Ads:
  - Image or Video
  - Text overlay (minimal)
  - Swipe-up CTA
```

### LinkedIn Ads Creative Elements
```
Sponsored Content:
  - Introductory Text
  - Image or Video
  - Headline (for image ads)
  - CTA button

Message Ads:
  - Subject line
  - Message body
  - CTA button text
  - Banner image

Text Ads:
  - Headline
  - Description
  - Small image
```

---

## Workflow Steps

### Step 1: Creative Data Collection

**Option A: Ad-Level Performance Data Provided**

```
Read performance data by ad/creative:

Required metrics per creative:
- Impressions
- Clicks / CTR
- Spend
- Conversions
- CPA
- ROAS (if applicable)
- Engagement metrics (likes, shares, comments for Meta)

Structure:
{
  "platform": "meta_ads",
  "creatives": [
    {
      "creative_id": "ad_001",
      "creative_type": "single_image",
      "primary_text": "Automate 50% of your support tickets...",
      "headline": "AI Customer Support That Works",
      "cta": "Learn More",
      "image_url": "https://...",
      "performance": {
        "impressions": 45000,
        "clicks": 540,
        "ctr": 1.2,
        "spend": 1080,
        "conversions": 36,
        "cpa": 30.00,
        "roas": 4.5,
        "engagement_rate": 2.8
      }
    }
  ]
}
```

**Option B: Creative Library + Performance Data Separate**

```
If creatives provided as files:
  Read creative files (images, videos, text docs with copy)
  Match to performance data by creative_id or manual matching
```

**Option C: Screenshots Only**

```
Read screenshots using image reading:
  Extract:
  - Ad copy (primary text, headline)
  - Visual description (what's shown in image/video)
  - CTA button text
  - Performance metrics from screenshot

May require user confirmation for OCR accuracy
```

---

### Step 2: Creative Performance Scoring

**For Each Creative**:

```javascript
// Calculate key metrics
CTR = (Clicks / Impressions) × 100
CPC = Spend / Clicks
Conversion_Rate = (Conversions / Clicks) × 100
CPA = Spend / Conversions
ROAS = Revenue / Spend
Engagement_Rate = (Likes + Comments + Shares) / Reach × 100  // Meta only

// Creative Performance Score (0-100)
Creative_Score =
  (CTR_vs_Avg × 0.30) +       // Click-through is strong signal
  (CPA_vs_Avg × 0.35) +       // Conversion efficiency most important
  (Engagement_vs_Avg × 0.20) + // Engagement indicates resonance
  (ROAS_vs_Avg × 0.15)        // Ultimate outcome

// Categorize
if (Creative_Score >= 80) → "WINNING CREATIVE"
else if (Creative_Score >= 60) → "STRONG CREATIVE"
else if (Creative_Score >= 40) → "AVERAGE CREATIVE"
else → "UNDERPERFORMING - PAUSE OR ITERATE"
```

**Creative Performance Example**:

```json
{
  "creative_id": "ad_001",
  "creative_name": "Automated Support - Benefit Focus",
  "platform": "meta_ads",
  "creative_type": "single_image",
  "metrics": {
    "ctr": 1.35,
    "cpc": 2.00,
    "conversion_rate": 6.67,
    "cpa": 30.00,
    "roas": 4.5,
    "engagement_rate": 3.2
  },
  "vs_account_average": {
    "ctr": "+50%",
    "cpa": "-25%",
    "roas": "+41%",
    "engagement": "+28%"
  },
  "creative_score": 88,
  "category": "WINNING CREATIVE",
  "recommendation": "SCALE - Allocate 40% of creative budget to this ad"
}
```

---

### Step 3: Creative Element Analysis

**DEEP Mode Only** - Break down performance by creative elements:

#### Copy Analysis

**Analyze headline variations**:

```
Extract all unique headlines used
Compare performance:

Example:
{
  "headline_analysis": [
    {
      "headline": "AI Customer Support That Works",
      "ads_using": 3,
      "avg_ctr": 1.35,
      "avg_cpa": 30.00,
      "avg_roas": 4.5,
      "performance": "EXCELLENT",
      "why_it_works": [
        "Direct benefit (That Works = reassurance)",
        "Short and punchy (5 words)",
        "Clear subject (AI Customer Support)"
      ]
    },
    {
      "headline": "Transform Your Customer Support",
      "ads_using": 2,
      "avg_ctr": 0.92,
      "avg_cpa": 45.00,
      "avg_roas": 2.8,
      "performance": "AVERAGE",
      "issues": [
        "Vague (Transform how?)",
        "Generic (doesn't differentiate)",
        "No specific benefit"
      ]
    }
  ],
  "headline_insights": {
    "best_performing_pattern": "Specific benefit + proof element",
    "worst_performing_pattern": "Generic transformation claims",
    "recommendations": [
      "Use specific metrics in headlines ('50% Faster Support')",
      "Keep headlines under 6 words for clarity",
      "Test problem-focused vs benefit-focused headlines"
    ]
  }
}
```

**Analyze primary text/body copy**:

```
Compare:
  - Length (short vs long)
  - Opening hook
  - Benefit statements
  - Social proof mentions
  - Urgency/scarcity elements

Example:
{
  "copy_length_analysis": {
    "short_copy": {
      "definition": "<50 words",
      "avg_ctr": 1.25,
      "avg_cpa": 32.00,
      "best_for": "Awareness campaigns, mobile users"
    },
    "medium_copy": {
      "definition": "50-100 words",
      "avg_ctr": 1.18,
      "avg_cpa": 28.50,
      "best_for": "Consideration stage, detailed offers"
    },
    "long_copy": {
      "definition": ">100 words",
      "avg_ctr": 0.95,
      "avg_cpa": 38.00,
      "best_for": "High-involvement purchases, B2B"
    },
    "recommendation": "Medium copy (50-100 words) performs best for your audience"
  },
  "opening_hook_analysis": {
    "question_hooks": {
      "example": "Tired of endless support tickets?",
      "avg_ctr": 1.42,
      "performance": "EXCELLENT"
    },
    "stat_hooks": {
      "example": "Companies reduce support costs by 50% with AI...",
      "avg_ctr": 1.28,
      "performance": "STRONG"
    },
    "generic_hooks": {
      "example": "Improve your customer support...",
      "avg_ctr": 0.88,
      "performance": "WEAK"
    },
    "recommendation": "Question hooks perform best - test pain point questions"
  }
}
```

#### Visual Creative Analysis

**Analyze image/video performance**:

```
For each visual creative:
  - Creative type (image, video, carousel)
  - Visual style (product shot, lifestyle, illustration, screenshot)
  - Color scheme
  - Text overlay (amount, readability)
  - Human presence (yes/no)

Example:
{
  "visual_creative_analysis": {
    "creative_type_performance": {
      "video": {
        "avg_ctr": 1.68,
        "avg_engagement": 4.2,
        "avg_cpa": 28.00,
        "performance": "BEST"
      },
      "carousel": {
        "avg_ctr": 1.32,
        "avg_engagement": 2.8,
        "avg_cpa": 32.00,
        "performance": "STRONG"
      },
      "single_image": {
        "avg_ctr": 1.05,
        "avg_engagement": 1.9,
        "avg_cpa": 38.00,
        "performance": "AVERAGE"
      }
    },
    "visual_style_performance": {
      "product_screenshot": {
        "ads_tested": 4,
        "avg_ctr": 1.42,
        "avg_cpa": 29.50,
        "why_it_works": "Shows actual product, builds trust"
      },
      "lifestyle_image": {
        "ads_tested": 3,
        "avg_ctr": 0.95,
        "avg_cpa": 42.00,
        "issues": "Too generic, doesn't differentiate"
      },
      "data_visualization": {
        "ads_tested": 2,
        "avg_ctr": 1.58,
        "avg_cpa": 26.50,
        "why_it_works": "Shows clear value, attention-grabbing"
      }
    },
    "human_presence_analysis": {
      "with_people": {
        "avg_engagement": 3.5,
        "avg_ctr": 1.38,
        "note": "Higher engagement but similar conversion rate"
      },
      "without_people": {
        "avg_engagement": 2.1,
        "avg_ctr": 1.32,
        "avg_cpa": 28.00,
        "note": "Slightly better for conversion"
      }
    },
    "recommendations": [
      "Video creative performs best - create 3-4 new video ads",
      "Product screenshots convert better than lifestyle images",
      "Data visualizations highly effective - test charts showing ROI/results",
      "Text overlays: Keep minimal (<20% of image area for Facebook approval)"
    ]
  }
}
```

#### Call-to-Action (CTA) Analysis

```
Compare CTA button performance:

{
  "cta_analysis": [
    {
      "cta_text": "Learn More",
      "ads_using": 8,
      "avg_ctr": 1.25,
      "avg_conversion_rate": 6.2,
      "performance": "STRONG",
      "best_for": "Mid-funnel, educational content"
    },
    {
      "cta_text": "Start Free Trial",
      "ads_using": 5,
      "avg_ctr": 1.58,
      "avg_conversion_rate": 8.5,
      "performance": "EXCELLENT",
      "best_for": "Bottom-funnel, ready to buy"
    },
    {
      "cta_text": "Download Now",
      "ads_using": 3,
      "avg_ctr": 1.42,
      "avg_conversion_rate": 7.8,
      "performance": "STRONG",
      "best_for": "Lead gen, content offers"
    },
    {
      "cta_text": "Sign Up",
      "ads_using": 2,
      "avg_ctr": 0.88,
      "avg_conversion_rate": 4.2,
      "performance": "WEAK",
      "issues": "Too generic, no clear value"
    }
  ],
  "recommendations": [
    "'Start Free Trial' performs best - use for conversion campaigns",
    "Specific CTAs (Download, Start Trial) outperform generic (Sign Up, Learn More)",
    "Match CTA to offer: Free trial → Start Free Trial, eBook → Download Guide"
  ]
}
```

---

### Step 4: Creative Fatigue Detection

**Identify creatives experiencing performance decline**:

```
Creative Fatigue Indicators:
  1. Frequency > 4.0 (Meta Ads)
  2. CTR declining over time (>20% drop from peak)
  3. CPC increasing over time (>15% increase)
  4. Engagement rate dropping
  5. Creative running >30 days without refresh

For each creative, analyze trend:

Example:
{
  "creative_fatigue_analysis": [
    {
      "creative_id": "ad_003",
      "creative_name": "Automated Ticketing - Screenshot",
      "days_running": 45,
      "frequency": 5.2,
      "performance_trend": {
        "week_1": {"ctr": 1.58, "cpc": 1.95, "cpa": 28.50},
        "week_2": {"ctr": 1.42, "cpc": 2.15, "cpa": 31.20},
        "week_3": {"ctr": 1.25, "cpc": 2.40, "cpa": 35.80},
        "week_4": {"ctr": 1.08, "cpc": 2.78, "cpa": 42.50},
        "week_5": {"ctr": 0.95, "cpc": 3.16, "cpa": 48.20},
        "week_6": {"ctr": 0.88, "cpc": 3.41, "cpa": 52.80}
      },
      "decline_metrics": {
        "ctr_decline": "-44% from peak",
        "cpc_increase": "+75%",
        "cpa_increase": "+85%"
      },
      "fatigue_status": "CRITICAL FATIGUE",
      "recommendations": [
        "IMMEDIATE: Pause this creative",
        "Refresh with new visual (same messaging, different image/video)",
        "Or rotate out for 2-3 weeks then re-introduce"
      ],
      "priority": "HIGH"
    },
    {
      "creative_id": "ad_005",
      "days_running": 18,
      "frequency": 2.8,
      "performance_trend": "Stable - no fatigue",
      "recommendation": "Continue running, monitor weekly"
    }
  ]
}
```

---

### Step 5: Competitive Creative Analysis

**DEEP Mode Only** - Analyze competitor ad creative:

```
Research competitor ads:

Method 1: Meta Ad Library
  WebSearch: "Facebook Ad Library {competitor_name}"
  Visit: https://www.facebook.com/ads/library/
  Search competitor → View their active ads

Method 2: Google
  WebSearch: site:facebook.com/ads {competitor_name}
  WebSearch: "{competitor_name} advertisements"

For each competitor ad found:
  Analyze:
  - Messaging approach (benefit-focused, feature-focused, problem-focused)
  - Visual style
  - Offers (free trial, demo, discount)
  - CTAs
  - Ad formats used

Example Insights:
{
  "competitive_creative_analysis": {
    "competitor_a": {
      "messaging_approach": "Problem-focused - emphasizes pain points",
      "sample_headline": "Drowning in Support Tickets? We Can Help",
      "visual_style": "Data visualizations showing before/after metrics",
      "primary_offer": "Free 14-day trial",
      "cta_used": "Start Free Trial",
      "unique_angles": [
        "Uses customer testimonials prominently",
        "Shows specific metrics (50% reduction in ticket volume)",
        "Video ads feature product demo"
      ]
    },
    "gaps_and_opportunities": [
      "Competitor A uses video heavily - we should test more video",
      "Before/after metrics are compelling - create similar creative",
      "They don't mention AI explicitly - we can differentiate here",
      "Free trial offer is standard - consider longer trial or money-back guarantee"
    ]
  }
}
```

---

### Step 6: Creative Testing Framework

**Generate systematic creative test hypotheses**:

#### Test Type 1: Headline Variations

```
Current best: "AI Customer Support That Works"
CTR: 1.35%, CPA: $30

Hypothesis Tests:
1. Benefit + Metric:
   "Reduce Support Tickets by 50% with AI"
   Hypothesis: Adding specific metric will improve CTR by 15%

2. Question Hook:
   "What If You Could Automate Half Your Support Tickets?"
   Hypothesis: Question format increases engagement

3. Social Proof:
   "Join 500+ Companies Using AI Customer Support"
   Hypothesis: Social proof improves conversion rate

4. Problem-Focused:
   "Overwhelmed by Support Tickets? Here's Your Solution"
   Hypothesis: Problem statement resonates with pain point

Test Design:
- Platform: Meta Ads
- Budget: $100 per variation
- Duration: 5 days
- Success metric: CTR >1.50% AND CPA <$32
```

#### Test Type 2: Visual Creative Variations

```
Current best: Product screenshot
CTR: 1.42%, CPA: $29.50

Hypothesis Tests:
1. Video Demo (15 seconds):
   Content: Quick product walkthrough showing AI routing
   Hypothesis: Video will increase CTR by 20% and improve conversion rate

2. Customer Testimonial Video:
   Content: Customer explaining results (50% ticket reduction)
   Hypothesis: Social proof in video format will improve trust and conversion rate

3. Data Visualization:
   Content: Chart showing ticket volume before/after
   Hypothesis: Concrete results visualization will improve CTR and conversion

4. Split-screen Before/After:
   Content: Chaotic support desk vs organized AI-powered dashboard
   Hypothesis: Visual contrast makes benefit more obvious

Test Design:
- Platform: Meta Ads (Feed + Stories)
- Budget: $150 per variation
- Duration: 7 days
- Success metric: CPA <$32 AND ROAS >4.0
```

#### Test Type 3: Copy Length & Structure

```
Current best: Medium copy (75 words)
CTR: 1.25%, CPA: $32

Hypothesis Tests:
1. Ultra-Short Copy (25 words):
   "AI customer support that actually works. Reduce tickets by 50%. Free trial."
   Hypothesis: Mobile users prefer shorter copy - will improve mobile CTR

2. Long Copy with Stats (150 words):
   Full breakdown with statistics, features, proof points
   Hypothesis: Detailed copy pre-qualifies clicks, improving conversion rate

3. Story Format:
   Customer story structure (problem → solution → results)
   Hypothesis: Narrative structure more engaging, improves both CTR and conversion

4. Bullet Point Format:
   ✓ Reduce tickets 50%
   ✓ Cut response time 70%
   ✓ Improve satisfaction scores
   ✓ Free 14-day trial
   Hypothesis: Scannable format improves clarity and CTR

Test Design:
- Platform: Meta Ads
- Budget: $100 per variation
- Duration: 5 days
- Success metric: Overall efficiency (conversions per $1000 spent)
```

#### Test Type 4: Offer Variations

```
Current offer: Free trial (unspecified length)
CTR: 1.25%, Conversion Rate: 6.5%

Hypothesis Tests:
1. "Start Your Free 14-Day Trial":
   Hypothesis: Specificity increases trust and conversion rate

2. "Get 50% Off Your First Month":
   Hypothesis: Discount incentive increases immediate action

3. "Free Demo + Personalized Setup":
   Hypothesis: Added value (setup) increases perceived value and conversions

4. "Money-Back Guarantee - Try Risk-Free":
   Hypothesis: Risk reversal increases conversion rate from clicks

Test Design:
- Platform: Google Ads + Meta Ads
- Budget: $200 per variation
- Duration: 7 days
- Success metric: Conversion Rate >7.5%
```

#### Test Type 5: Audience-Specific Creative

```
Insight from audience analysis:
  Female 25-34 audience converts best (CPA $26.50, ROAS 4.8)
  BUT currently using general creative

Hypothesis:
  Creative tailored to this segment will improve performance further

Test Variations:
1. Messaging for busy entrepreneurs:
   "Scale Your Business Without Scaling Your Support Team"

2. Visual showing female business owner:
   More relatable to target audience

3. Pain points specific to growing businesses:
   "From 10 Customers to 1,000? Your Support Doesn't Have to Suffer"

Test Design:
- Platform: Meta Ads
- Targeting: Female, 25-34, Interests: Small Business Owners
- Budget: $300
- Duration: 7 days
- Success metric: ROAS >5.5 (beating current 4.8)
```

---

### Step 7: Creative Best Practices by Platform

**Platform-Specific Guidelines**:

#### Google Search Ads Best Practices

```
Headlines:
  ✓ Include primary keyword in Headline 1
  ✓ Use 3-4 unique headlines minimum (RSAs use up to 15)
  ✓ Include numbers/stats ("50% Faster")
  ✓ Add urgency where appropriate ("Limited Time")
  ✓ Test question formats

Descriptions:
  ✓ Use both description lines
  ✓ Include clear call-to-action
  ✓ Mention unique differentiators
  ✓ Add trust signals (years in business, customers served)

Ad Extensions:
  ✓ Use sitelinks (minimum 4)
  ✓ Add callouts (minimum 6)
  ✓ Include structured snippets
  ✓ Use call extensions (if phone sales)

Testing:
  - Test at least 3 headline variations
  - Rotate descriptions monthly
  - Let RSAs optimize for 30 days minimum before judging
```

#### Meta Ads Best Practices

```
Primary Text:
  ✓ Hook in first 125 characters (before "See More")
  ✓ Use emojis sparingly (1-2 max) to draw attention
  ✓ Keep sentences short (mobile-friendly)
  ✓ Include clear benefit in first sentence

Headlines:
  ✓ 5 words or less for impact
  ✓ Benefit-focused, not feature-focused
  ✓ Test with and without brand name

Images:
  ✓ 1080x1080 for Feed (square)
  ✓ 1080x1920 for Stories (9:16)
  ✓ Less than 20% text overlay (or may get limited delivery)
  ✓ Use bright, contrasting colors
  ✓ Show faces (higher engagement) for awareness
  ✓ Show product for conversion campaigns

Videos:
  ✓ Hook in first 3 seconds (most critical)
  ✓ Add captions (85% watch without sound)
  ✓ Keep under 30 seconds for Feed
  ✓ Square or vertical format (more screen space on mobile)
  ✓ Show product in first frame

Testing:
  - Test 3-5 creatives per ad set
  - Refresh creative every 2-3 weeks
  - Let each creative get 500+ impressions before judging
```

#### LinkedIn Ads Best Practices

```
Introductory Text:
  ✓ Professional tone (no emojis)
  ✓ Lead with value/benefit
  ✓ Keep under 150 characters for full visibility
  ✓ Include relevant hashtags (1-2)

Images:
  ✓ 1200x627 for Single Image Ads
  ✓ Professional, high-quality
  ✓ Avoid stock photos (use real product/people)
  ✓ Include text overlay with key message

Video:
  ✓ 30-60 seconds optimal
  ✓ Professional quality (more important than Meta)
  ✓ Thought leadership content performs well
  ✓ Captions required

CTAs:
  ✓ "Learn More" and "Download" perform best for B2B
  ✓ Avoid aggressive CTAs ("Buy Now" underperforms)

Testing:
  - LinkedIn audience smaller - need more time per test
  - Test 2-3 creatives per campaign
  - 14 days minimum test duration
```

---

### Step 8: Creative Refresh Recommendations

**Create creative refresh schedule**:

```json
{
  "creative_refresh_plan": {
    "immediate_actions": [
      {
        "action": "Pause fatigued creative (ad_003)",
        "reason": "CTR declined 44%, frequency 5.2",
        "replacement": "Test new variation: Same messaging, new visual (video instead of image)"
      },
      {
        "action": "Scale winning creative (ad_001)",
        "reason": "ROAS 4.5, Creative Score 88",
        "how": "Increase budget allocation from 20% to 40%"
      }
    ],
    "week_1_tests": [
      {
        "test_name": "Headline Variations (4 tests)",
        "budget": "$400 total",
        "timeline": "5 days",
        "expected_winner": "Benefit + Metric headline"
      },
      {
        "test_name": "Video vs Image",
        "budget": "$300 total",
        "timeline": "7 days",
        "hypothesis": "Video will improve CTR by 20%"
      }
    ],
    "week_2_4_tests": [
      {
        "test_name": "Audience-specific creative",
        "budget": "$600 total",
        "timeline": "14 days",
        "hypothesis": "Custom creative for female 25-34 will improve ROAS from 4.8 to 5.5+"
      }
    ],
    "ongoing_cadence": {
      "weekly": [
        "Review creative performance metrics",
        "Identify any declining creatives (CTR drop >15%)"
      ],
      "bi_weekly": [
        "Launch 1-2 new creative tests",
        "Refresh highest-frequency creatives"
      ],
      "monthly": [
        "Major creative refresh (new photoshoot, video production)",
        "Competitive creative audit",
        "Review winning creative patterns and create new variations"
      ]
    }
  }
}
```

---

### Step 9: Output Generation

**LIGHT Mode Output** (`/data/ads/creative-optimization-{company}-light.json`):

```json
{
  "metadata": {
    "mode": "LIGHT",
    "company": "AcmeCorp",
    "date_range": "2024-01-01 to 2024-01-31",
    "platforms_analyzed": ["google_ads", "meta_ads", "linkedin_ads"],
    "creatives_analyzed": 15,
    "generated_at": "2024-01-15T18:00:00Z"
  },
  "executive_summary": {
    "best_creative": {
      "id": "ad_001",
      "name": "Automated Support - Benefit + Screenshot",
      "platform": "meta_ads",
      "ctr": 1.35,
      "cpa": 30.00,
      "roas": 4.5,
      "creative_score": 88,
      "recommendation": "SCALE - Increase budget by 50%"
    },
    "worst_creative": {
      "id": "ad_007",
      "name": "Generic Transformation - Lifestyle Image",
      "platform": "meta_ads",
      "ctr": 0.68,
      "cpa": 58.00,
      "roas": 1.8,
      "creative_score": 32,
      "recommendation": "PAUSE immediately"
    },
    "fatigued_creatives": 2,
    "winning_patterns": [
      "Product screenshots outperform lifestyle images (1.42% vs 0.95% CTR)",
      "Specific benefit headlines beat generic (1.35% vs 0.92% CTR)",
      "Video creative has 27% higher CTR than static images"
    ]
  },
  "top_3_quick_wins": [
    {
      "priority": 1,
      "action": "Pause 2 fatigued creatives with declining performance",
      "creatives": ["ad_003", "ad_007"],
      "rationale": "CTR declined 44% and 38% respectively, driving CPA up 85%+",
      "expected_impact": "Improve overall CPA from $39 to $34 (-13%)",
      "effort": "2 minutes"
    },
    {
      "priority": 2,
      "action": "Scale winning creative (ad_001) budget by 50%",
      "rationale": "ROAS 4.5, Creative Score 88, no signs of fatigue",
      "expected_impact": "Generate additional $3,500 revenue/month",
      "effort": "2 minutes"
    },
    {
      "priority": 3,
      "action": "Test 3 video creatives (currently only using images)",
      "rationale": "Video format shows 27% higher CTR in limited testing",
      "test_budget": "$450 (3 variations × $150)",
      "test_duration": "7 days",
      "expected_impact": "If successful, could improve overall CTR from 1.12% to 1.42% (+27%)",
      "effort": "3-4 hours (video creation + setup)"
    }
  ],
  "projected_impact": {
    "pause_underperformers": "Improve CPA by 13%",
    "scale_winners": "+$3,500 revenue/month",
    "video_tests": "Potential +27% CTR improvement if adopted across campaigns"
  }
}
```

**DEEP Mode Output** (`/data/ads/creative-optimization-{company}-deep.json`):

```json
{
  "metadata": {
    "mode": "DEEP",
    "company": "AcmeCorp",
    "date_range": "2024-01-01 to 2024-01-31",
    "platforms_analyzed": ["google_ads", "meta_ads", "linkedin_ads"],
    "creatives_analyzed": 15,
    "creative_tests_recommended": 12,
    "generated_at": "2024-01-15T18:00:00Z",
    "analysis_duration_minutes": 24
  },
  "creative_performance_analysis": {
    "by_format": {
      "video": {
        "creatives_tested": 2,
        "avg_ctr": 1.68,
        "avg_cpa": 28.00,
        "avg_roas": 4.8,
        "performance": "EXCELLENT",
        "recommendation": "Expand video creative library"
      },
      "single_image": {
        "creatives_tested": 10,
        "avg_ctr": 1.05,
        "avg_cpa": 38.00,
        "avg_roas": 3.2,
        "performance": "AVERAGE"
      },
      "carousel": {
        "creatives_tested": 3,
        "avg_ctr": 1.32,
        "avg_cpa": 32.00,
        "avg_roas": 3.9,
        "performance": "STRONG"
      }
    },
    "by_messaging_approach": {
      "benefit_focused": {
        "example": "Reduce Support Tickets by 50%",
        "avg_ctr": 1.38,
        "avg_cpa": 29.50,
        "performance": "BEST"
      },
      "problem_focused": {
        "example": "Drowning in Support Tickets?",
        "avg_ctr": 1.28,
        "avg_cpa": 32.00,
        "performance": "STRONG"
      },
      "feature_focused": {
        "example": "AI-Powered Ticket Routing",
        "avg_ctr": 0.95,
        "avg_cpa": 42.00,
        "performance": "WEAK"
      }
    },
    "by_visual_style": {
      /* Detailed visual analysis */
    },
    "by_cta": {
      /* CTA performance breakdown */
    }
  },
  "creative_element_insights": {
    "headlines": {
      /* Headline analysis from Step 3 */
    },
    "copy": {
      /* Copy analysis from Step 3 */
    },
    "visuals": {
      /* Visual analysis from Step 3 */
    }
  },
  "creative_fatigue_analysis": {
    /* Fatigue analysis from Step 4 */
  },
  "competitive_insights": {
    /* Competitive analysis from Step 5 */
  },
  "creative_testing_roadmap": {
    "immediate_tests": [
      {
        "test_id": "test_001",
        "test_name": "Headline Variations - Benefit + Metric",
        "hypothesis": "Adding specific metric to headline will improve CTR by 15%",
        "variations": [
          "Control: AI Customer Support That Works",
          "Variation A: Reduce Support Tickets by 50% with AI",
          "Variation B: Cut Support Costs in Half with AI Automation",
          "Variation C: 500+ Companies Reduced Tickets 50% with Our AI"
        ],
        "platform": "meta_ads",
        "audience": "All audiences (broad test)",
        "budget": "$400 ($100 per variation)",
        "duration": "5 days",
        "success_criteria": "CTR >1.50% AND CPA <$32",
        "priority": "HIGH"
      },
      {
        "test_id": "test_002",
        "test_name": "Video Creative - Product Demo",
        "hypothesis": "Video will increase CTR by 25% and improve conversion rate",
        "variations": [
          "15-sec product demo showing AI routing",
          "30-sec customer testimonial video",
          "15-sec before/after split screen"
        ],
        "platform": "meta_ads",
        "budget": "$450 ($150 per variation)",
        "duration": "7 days",
        "success_criteria": "CTR >1.60% AND ROAS >4.5",
        "priority": "HIGH"
      }
    ],
    "month_1_tests": [
      /* 5-7 tests for month 1 */
    ],
    "month_2_3_tests": [
      /* Longer-term testing strategy */
    ]
  },
  "creative_production_needs": {
    "immediate": [
      "3 video creatives (15-30 seconds each)",
      "2 new image creatives (product screenshots with different angles)",
      "4 headline variations for RSAs (Google)"
    ],
    "month_1": [
      "Customer testimonial video (60 seconds)",
      "Carousel creative (5-7 cards showing features)",
      "10 copy variations for testing"
    ],
    "ongoing": [
      "Bi-weekly creative refresh (new images/videos)",
      "Monthly video content (product updates, use cases)",
      "Quarterly photoshoot for lifestyle/team images"
    ]
  },
  "budget_allocation": {
    "creative_production_budget": "$2,000/month recommended",
    "breakdown": {
      "video_production": "$1,000 (2 videos/month)",
      "image_creation": "$300 (design/stock photos)",
      "copywriting": "$200 (variations and testing)",
      "testing_budget": "$500 (ad spend for tests)"
    }
  },
  "projected_impact": {
    "if_testing_roadmap_executed": {
      "expected_wins": "3-4 winning creatives from 12 tests (25-33% success rate)",
      "potential_ctr_improvement": "+20-30%",
      "potential_cpa_improvement": "-15-25%",
      "potential_roas_improvement": "+25-40%",
      "monthly_revenue_impact": "+$8,000-12,000"
    }
  }
}
```

---

## Validation Checks

1. **Minimum Creatives Analyzed**: LIGHT ≥5, DEEP ≥10
2. **Performance Metrics Present**: CTR, CPA, ROAS for all creatives
3. **Winning Pattern Identified**: At least 2-3 patterns across best performers
4. **Test Hypotheses Clear**: Each test has specific hypothesis and success criteria
5. **Budget Recommendations**: Testing budget allocated and justified

---

## Usage Example

**Agent Workflow**:
```
1. Read this skill file
2. Collect creative performance data
3. Determine mode (LIGHT or DEEP)
4. Use TodoWrite to track analysis:
   [ ] Creative data collection
   [ ] Performance scoring
   [ ] Element analysis (headlines, visuals, copy)
   [ ] Fatigue detection
   [ ] Competitive research
   [ ] Testing framework
   [ ] Output generation
5. Execute analysis
6. Save JSON to /data/ads/
7. Provide summary:
   "Creative Optimization Analysis Complete!

    Best Creative: Automated Support - Benefit + Screenshot
    - CTR: 1.35% (vs avg 1.05%)
    - CPA: $30 (vs avg $39)
    - ROAS: 4.5
    - Creative Score: 88/100

    Key Insights:
    - Video outperforms images by 27% CTR
    - Benefit-focused headlines beat generic by 46%
    - Product screenshots convert better than lifestyle images

    Top 3 Actions:
    1. Pause 2 fatigued creatives → Improve CPA by 13%
    2. Scale winning creative → +$3,500 revenue/month
    3. Test 3 video creatives → Potential +27% CTR

    Testing Roadmap: 12 tests over 3 months
    Expected Impact: +25-40% ROAS improvement

    Full report: /data/ads/creative-optimization-acme-deep.json"
```

---

## Integration with Other Skills

**Works with**:
- **campaign-analysis.md** - Uses campaign data for creative context
- **audience-insights.md** - Create audience-specific creative variations

---

## MCP Tools Needed

**Current**: Built-in tools sufficient (Read for images/data, Write for output)

**Future Enhancement**:
- `mcp__Creative__meta_ad_library` - Automated competitor ad scraping
- `mcp__Creative__video_analyzer` - Analyze video creative performance patterns
- `mcp__Creative__image_generator` - AI-generated creative variations for testing
