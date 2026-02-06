# Competitor Analysis - Detailed Reference

This file contains detailed analysis templates, example JSON outputs, and research methods for each competitive dimension.

## Dimension 1: Market Positioning - Detailed Template

```
For each competitor analyze:

1. Target Audience
   - SMB, Mid-market, Enterprise?
   - Industry verticals?
   - Geographic focus?

2. Value Proposition
   - What's their main benefit claim?
   - How do they differentiate?
   - What's their unique angle?

3. Pricing Strategy
   - Freemium, Free trial, Demo-only?
   - Price range (low, mid, premium)?
   - Pricing model (per-user, flat, usage-based)?

4. Brand Positioning
   - Challenger, Leader, Innovator, Specialist?
   - Premium vs Value vs Balanced?
```

**Example Output**:
```json
{
  "competitor": "Competitor A",
  "positioning": {
    "target_audience": "Enterprise (1000+ employees)",
    "industries": ["Technology", "Financial Services"],
    "value_prop": "Most Secure AI Customer Support Platform",
    "pricing_tier": "Premium ($150-300/user/month)",
    "brand_position": "Market Leader, Security-Focused"
  }
}
```

---

## Dimension 2: GEO Analysis - Detailed Template

```
Method: Test key prompts used in your GEO analysis

For each competitor:
  Test 10-15 high-value prompts:
  - "Best {category} for {use case}"
  - "How to {solve problem}"
  - "{Category} comparison"

  Track:
  - Visibility % (how often mentioned)
  - Citation quality (source authority)
  - Position when mentioned (1st, 2nd, 3rd+)
  - Sentiment (positive, neutral, negative)
```

**Example Comparison Matrix**:
```json
{
  "geo_competitive_analysis": {
    "your_company": {
      "visibility": "12%",
      "avg_position": 3.2,
      "citation_quality": "Medium"
    },
    "competitor_a": {
      "visibility": "45%",
      "avg_position": 1.8,
      "citation_quality": "High",
      "advantage": "3.75x more visible, better positioning"
    },
    "competitor_b": {
      "visibility": "28%",
      "avg_position": 2.5,
      "citation_quality": "Medium-High"
    }
  },
  "key_insights": [
    "Competitor A dominates AI search with 45% visibility vs your 12%",
    "They have 15+ thought leadership articles cited by AI engines",
    "Gap: Strong presence in 'how-to' queries (you're missing)"
  ]
}
```

---

## Dimension 3: SEO Performance - Detailed Template

```
Metrics to Research:

1. Domain Authority (estimate via search)
   WebSearch: "{competitor_domain} domain authority"

2. Ranking Keywords
   WebSearch: "site:{competitor_domain} best"
   WebSearch: "{industry keywords}" -> Check if competitor ranks

3. Organic Traffic (estimate)
   WebSearch: "{competitor_domain} traffic"
   Look for: Published case studies, third-party estimates

4. Backlink Profile
   WebSearch: "link:{competitor_domain}"
   Look for: High-authority backlinks (news sites, industry blogs)

5. Content Strategy
   WebSearch: "site:{competitor_domain} blog"
   Analyze:
   - Posting frequency
   - Content types (guides, comparisons, how-tos)
   - Depth (word count, detail)

6. Technical SEO
   WebFetch: {competitor_homepage}
   Check:
   - Page load speed (use WebFetch timing)
   - Mobile-friendliness (viewport tag present?)
   - Schema markup (structured data present?)
```

**Example Analysis**:
```json
{
  "competitor": "Competitor A",
  "seo_analysis": {
    "estimated_da": "75 (vs your 45)",
    "estimated_monthly_traffic": "250K (vs your 35K)",
    "content_velocity": "12 posts/month (vs your 4/month)",
    "avg_content_length": "2,500 words (vs your 800 words)",
    "backlinks_found": "15+ from major publications (TechCrunch, Forbes)",
    "technical_seo": "Excellent (fast load, mobile-optimized, rich snippets)",
    "key_advantage": "3x more content, 7x more traffic, stronger backlink profile"
  },
  "gap_analysis": {
    "content_gap": "You publish 1/3 as often with 1/3 the depth",
    "authority_gap": "Missing major publication backlinks",
    "technical_gap": "Minimal - both sites technically sound"
  }
}
```

---

## Dimension 4: Paid Advertising - Detailed Template

```
Research Methods:

1. Google Ads Presence
   WebSearch: "{competitor_brand}"
   WebSearch: "{industry keywords}"
   Check:
   - Brand search ads?
   - Competitor keyword bidding?
   - Non-brand search ads?
   - Ad copy approach (benefit, feature, offer-focused?)

2. Meta Ads (Facebook Ad Library)
   WebSearch: "Facebook Ad Library {competitor_name}"
   Visit: https://www.facebook.com/ads/library/
   Analyze:
   - Number of active ads
   - Ad formats (image, video, carousel)
   - Messaging themes
   - Targeting approach
   - Offer types (free trial, demo, discount)

3. LinkedIn Ads (limited visibility)
   WebSearch: "{competitor_name} LinkedIn ads"
   Estimate activity based on:
   - Sponsored posts visible on LinkedIn
   - Job postings for paid media roles

4. Display/Retargeting
   Visit competitor site, then browse web
   Note retargeting ad presence
```

**Example Analysis**:
```json
{
  "competitor": "Competitor A",
  "paid_ads_analysis": {
    "google_ads": {
      "active": true,
      "brand_bidding": "Yes (on own brand + competitors)",
      "non_brand": "Extensive (20+ ad variations found)",
      "ad_copy_style": "Benefit-focused with specific metrics",
      "extensions": "Sitelinks, Callouts, Structured Snippets (comprehensive)",
      "estimated_spend": "$50K-100K/month (based on keyword coverage)"
    },
    "meta_ads": {
      "active_ads_count": 35,
      "ad_formats": "Video (60%), Image (30%), Carousel (10%)",
      "messaging_themes": [
        "ROI/Cost savings (40% of ads)",
        "Ease of use (30%)",
        "Customer testimonials (30%)"
      ],
      "offers": "14-day free trial (consistent across ads)",
      "creative_refresh_rate": "~Weekly (high testing velocity)"
    },
    "linkedin_ads": {
      "estimated_activity": "Moderate (5-10 ads visible)",
      "targeting": "Enterprise, IT/Marketing decision-makers"
    }
  },
  "key_advantages": [
    "Much higher ad spend ($50-100K vs your $30K)",
    "Video-first approach (you use mostly images)",
    "Aggressive brand bidding (including competitor keywords)",
    "High testing velocity (35 Meta ads vs your 8)"
  ]
}
```

---

## Dimension 5: Content Marketing - Detailed Template

```
Content Audit:

1. Blog/Resource Center
   WebFetch: {competitor_domain}/blog
   Analyze:
   - Post frequency (posts/month)
   - Content types (how-to, comparison, news, case study)
   - Depth (average word count)
   - Multimedia (videos, infographics, podcasts?)

2. Gated Content/Lead Magnets
   WebSearch: "site:{competitor_domain} download"
   WebSearch: "{competitor_name} ebook OR guide OR whitepaper"
   Find:
   - Number of lead magnets
   - Topics covered
   - Quality/production value

3. Video Content
   WebSearch: "{competitor_name} YouTube"
   Visit YouTube channel
   Metrics:
   - Subscriber count
   - View counts
   - Upload frequency
   - Video types (demos, tutorials, webinars)

4. Podcasts/Webinars
   WebSearch: "{competitor_name} podcast OR webinar"

5. Social Media Content
   Check: LinkedIn, Twitter, Instagram (if B2C)
   Metrics:
   - Follower counts
   - Engagement rates
   - Post frequency
   - Content themes
```

**Example Analysis**:
```json
{
  "competitor": "Competitor A",
  "content_marketing": {
    "blog": {
      "posts_per_month": 12,
      "avg_word_count": 2500,
      "content_mix": {
        "how_to_guides": "40%",
        "industry_insights": "30%",
        "product_updates": "20%",
        "case_studies": "10%"
      }
    },
    "lead_magnets": {
      "count": 8,
      "types": ["eBooks (4)", "Templates (2)", "Calculators (2)"],
      "quality": "High (professional design, 30-50 pages)"
    },
    "video": {
      "youtube_subscribers": "15K",
      "avg_views": "2.5K per video",
      "upload_frequency": "2 per week",
      "content_types": ["Product demos (50%)", "Customer stories (30%)", "Tips & tricks (20%)"]
    },
    "social_media": {
      "linkedin_followers": "45K",
      "twitter_followers": "12K",
      "post_frequency": "Daily on LinkedIn, 3x/week on Twitter",
      "engagement_rate": "4.2% (LinkedIn - above industry avg)"
    }
  },
  "key_strengths": [
    "3x your blog output with better depth",
    "8 lead magnets vs your 2",
    "Active YouTube presence (you have none)",
    "Strong LinkedIn engagement"
  ]
}
```

---

## Dimension 6: Product & Features - Detailed Template

```
Feature Comparison:

1. Core Features
   WebFetch: {competitor_domain}/features
   List:
   - All features they promote
   - Unique features (you don't have)
   - Missing features (you have, they don't)

2. Pricing
   WebFetch: {competitor_domain}/pricing
   Compare:
   - Price points
   - Features per tier
   - Free trial length
   - Discount strategies

3. Integrations
   WebFetch: {competitor_domain}/integrations
   Count:
   - Number of integrations
   - Key integration categories
   - Your integrations vs theirs

4. Customer Reviews
   WebSearch: "site:g2.com {competitor_name}"
   Metrics:
   - Overall rating
   - Number of reviews
   - Common praise themes
   - Common complaint themes
```

**Example Matrix**:
```json
{
  "product_comparison": {
    "features": {
      "your_product": 35,
      "competitor_a": 42,
      "competitor_b": 38
    },
    "unique_to_competitor_a": [
      "Advanced AI Sentiment Analysis",
      "Multi-language Support (15 languages)",
      "Custom Workflow Builder"
    ],
    "unique_to_you": [
      "Real-time Collaboration",
      "Built-in Video Chat"
    ],
    "pricing": {
      "your_starter": "$29/user/mo",
      "competitor_a_starter": "$39/user/mo (more expensive)",
      "competitor_b_starter": "$25/user/mo (cheaper)"
    },
    "reviews": {
      "your_rating": "4.5 (85 reviews)",
      "competitor_a": "4.7 (450 reviews)",
      "competitor_b": "4.3 (180 reviews)"
    }
  },
  "key_insights": [
    "Competitor A has more reviews (5.3x) - stronger social proof",
    "You're mid-priced ($29 vs $25-39 range)",
    "Feature parity mostly achieved, but missing multi-language support",
    "Your unique features (video chat) not heavily promoted by competitors"
  ]
}
```

---

## Full Light Mode Output Example

```json
{
  "metadata": {
    "mode": "QUICK",
    "company": "AcmeCorp",
    "competitors_analyzed": 3,
    "generated_at": "2024-01-15T19:00:00Z"
  },
  "executive_summary": {
    "competitive_position": "CHALLENGER - Strong product, weak brand awareness",
    "top_3_insights": [
      "Competitor A dominates awareness channels (SEO, GEO, Ads) with 3-5x your investment",
      "You have unique features (real-time collab, video) but under-promoted",
      "Gap in mid-market ($29/user) positioning - opportunity to own this segment"
    ],
    "biggest_threat": "Competitor A launching cheaper tier to capture your market",
    "biggest_opportunity": "AI search engines (GEO) - only 12% visibility vs 45%, high upside"
  },
  "competitor_comparison": {
    "competitor_a": {
      "position": "Market Leader",
      "strengths": ["Brand recognition", "Feature breadth", "Marketing spend"],
      "weaknesses": ["High price", "Complex UI (per reviews)"],
      "vs_you": "Beats you on awareness, you beat on price and ease of use"
    },
    "competitor_b": {
      "position": "Value Player",
      "strengths": ["Lowest price", "Simple UI"],
      "weaknesses": ["Limited features", "Poor support"],
      "vs_you": "You have better features and support, they have lower price"
    },
    "competitor_c": {
      "position": "Emerging Challenger",
      "strengths": ["Fast growth", "Modern UI", "Aggressive pricing"],
      "weaknesses": ["New to market", "Limited integrations"],
      "vs_you": "Growing fast - watch closely, could become major threat"
    }
  },
  "quick_wins": [
    {
      "opportunity": "Increase GEO visibility",
      "action": "Create 10 thought leadership pieces for AI citation",
      "impact": "Move from 12% to 25% visibility (2x)",
      "effort": "Medium",
      "timeline": "60 days"
    },
    {
      "opportunity": "Promote unique features",
      "action": "Campaign highlighting real-time collaboration + video vs competitors",
      "impact": "Better differentiation, higher conversion rate",
      "effort": "Low",
      "timeline": "30 days"
    },
    {
      "opportunity": "Mid-market positioning",
      "action": "Messaging: 'Enterprise features at SMB prices'",
      "impact": "Clearer positioning, attract mid-market buyers",
      "effort": "Low",
      "timeline": "Immediate"
    }
  ]
}
```
