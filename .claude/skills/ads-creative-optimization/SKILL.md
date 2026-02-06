---
name: ads-creative-optimization
description: >
  Analyze ad creative performance (copy, images, videos) across platforms, identify winning creative elements, detect creative fatigue, and provide data-driven recommendations for creative testing and optimization.
  Use when you need to understand which creatives work best and plan systematic A/B tests.
metadata:
  author: castor
  version: "1.0"
  domain: ads
  execution-modes: light, deep
---

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

### Google Ads
- **Search Ads**: Headlines (up to 15), Descriptions (up to 4), Display Path, Ad Extensions
- **Display/Discovery Ads**: Images (multiple sizes), Headlines, Descriptions, Logos, CTA button
- **Video Ads (YouTube)**: Video creative, Headline, Description, CTA overlay

### Meta Ads
- **Image/Carousel Ads**: Primary Text, Headline, Description, Image(s), CTA button
- **Video Ads**: Video creative, Primary Text, Headline, Description, CTA button, Thumbnail
- **Stories Ads**: Image or Video, Text overlay (minimal), Swipe-up CTA

### LinkedIn Ads
- **Sponsored Content**: Introductory Text, Image or Video, Headline, CTA button
- **Message Ads**: Subject line, Message body, CTA button text, Banner image
- **Text Ads**: Headline, Description, Small image

---

## Workflow Steps

### Step 1: Creative Data Collection

Collect performance data per creative: Impressions, Clicks/CTR, Spend, Conversions, CPA, ROAS, and Engagement metrics (likes, shares, comments for Meta).

Data can come from ad-level reports, separate creative libraries matched to performance data, or screenshots (using image reading capability for OCR extraction).

### Step 2: Creative Performance Scoring

For each creative, calculate:
- CTR, CPC, Conversion Rate, CPA, ROAS, Engagement Rate (Meta)

Creative Performance Score (0-100) weighted:
- CTR vs avg (30%) - click-through is strong signal
- CPA vs avg (35%) - conversion efficiency most important
- Engagement vs avg (20%) - indicates resonance
- ROAS vs avg (15%) - ultimate outcome

Categorize:
- **WINNING CREATIVE** (80+): Scale budget allocation
- **STRONG CREATIVE** (60-79): Maintain and iterate
- **AVERAGE CREATIVE** (40-59): Test variations
- **UNDERPERFORMING** (<40): Pause or iterate

### Step 3: Creative Element Analysis (DEEP Mode)

Break down performance by creative elements:

**Copy Analysis:**
- Headline variations (compare CTR, CPA, ROAS across different headlines)
- Identify patterns: specific benefit + proof vs generic transformation claims
- Primary text/body copy: analyze by length (short <50, medium 50-100, long >100 words)
- Opening hook analysis: question hooks, stat hooks, generic hooks

**Visual Creative Analysis:**
- Creative type performance (video vs carousel vs single image)
- Visual style performance (product screenshot vs lifestyle vs data visualization)
- Human presence analysis (with/without people)

**CTA Analysis:**
- Compare button text performance ("Learn More" vs "Start Free Trial" vs "Download Now" vs "Sign Up")
- Match CTA to funnel stage and offer type

### Step 4: Creative Fatigue Detection

Identify creatives experiencing performance decline:

**Fatigue Indicators:**
1. Frequency > 4.0 (Meta Ads)
2. CTR declining >20% from peak
3. CPC increasing >15% over time
4. Engagement rate dropping
5. Creative running >30 days without refresh

Analyze week-over-week trends for each creative. Flag creatives with CRITICAL FATIGUE for immediate action.

### Step 5: Competitive Creative Analysis (DEEP Mode)

Research competitor ads:
- Use `WebSearch` for Meta Ad Library and competitor advertisements
- Analyze messaging approach, visual style, offers, CTAs, ad formats
- Identify gaps and differentiation opportunities

### Step 6: Creative Testing Framework

Generate systematic test hypotheses across 5 test types:

1. **Headline Variations**: Benefit+metric, question hook, social proof, problem-focused
2. **Visual Creative Variations**: Video demo, testimonial video, data visualization, before/after
3. **Copy Length & Structure**: Ultra-short, long with stats, story format, bullet point format
4. **Offer Variations**: Specific trial length, discount, free demo + setup, money-back guarantee
5. **Audience-Specific Creative**: Tailored messaging and visuals for best-performing segments

Each test includes: hypothesis, variations, platform, budget, duration, and success criteria.

### Step 7: Platform Best Practices

Apply platform-specific creative guidelines:

**Google Search Ads**: Keyword in Headline 1, 3-4+ unique headlines for RSAs, include numbers/stats, test question formats, use all ad extensions.

**Meta Ads**: Hook in first 125 characters, 1-2 emojis max, short sentences for mobile, 5-word headlines, <20% text overlay on images, captions on video (85% watch without sound), hook in first 3 seconds of video.

**LinkedIn Ads**: Professional tone (no emojis), lead with value, <150 characters for visibility, avoid stock photos, 30-60 second video optimal, "Learn More" and "Download" CTAs perform best for B2B.

### Step 8: Creative Refresh Recommendations

Create creative refresh schedule with:
- Immediate actions (pause fatigued, scale winners)
- Week 1 tests (headline variations, video vs image)
- Week 2-4 tests (audience-specific creative)
- Ongoing cadence (weekly review, bi-weekly new tests, monthly major refresh)

### Step 9: Output Generation

Save analysis to `/data/ads/creative-optimization-{company}-{mode}.json`.

> For detailed scoring examples, element analysis templates, testing frameworks, and full output schemas, see `references/workflow-detail.md`.

---

## Output Schema (Summary)

**LIGHT Mode** includes:
- Executive summary with best/worst creatives and creative scores
- Fatigued creative count and winning patterns identified
- Top 3 quick wins (pause fatigued, scale winners, test new formats)
- Projected impact from each action

**DEEP Mode** additionally includes:
- Performance analysis by format, messaging approach, visual style, CTA
- Creative element insights (headlines, copy, visuals)
- Creative fatigue analysis with week-over-week trends
- Competitive creative insights
- Creative testing roadmap (immediate + month 1 + month 2-3 tests)
- Creative production needs (immediate, monthly, ongoing)
- Budget allocation for creative production and testing
- Projected impact if testing roadmap executed

---

## Validation Checks

1. **Minimum Creatives Analyzed**: LIGHT >= 5, DEEP >= 10
2. **Performance Metrics Present**: CTR, CPA, ROAS for all creatives
3. **Winning Pattern Identified**: At least 2-3 patterns across best performers
4. **Test Hypotheses Clear**: Each test has specific hypothesis and success criteria
5. **Budget Recommendations**: Testing budget allocated and justified

---

## Usage Example

```
1. Read this skill file
2. Collect creative performance data
3. Determine mode (LIGHT or DEEP)
4. Use TodoWrite to track analysis steps
5. Execute analysis
6. Save JSON to /data/ads/
7. Provide summary with best/worst creatives, key insights, top 3 actions, testing roadmap
```

---

## Related Skills

- **ads-campaign-analysis** - Uses campaign data for creative context
- **ads-audience-insights** - Create audience-specific creative variations

---

## Tool Usage

**Current**: Built-in tools sufficient (Read for images/data, Write for output, WebSearch for competitor research)

**Future Enhancement** (when available via `scripts/api/`):
- Meta Ad Library API for automated competitor ad scraping
- Video analyzer API for creative performance pattern analysis
- Image generator API for AI-generated creative variations for testing
