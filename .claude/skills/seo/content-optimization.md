# SEO Content Optimization

## Purpose
Analyze and optimize existing website content for improved search engine rankings, focusing on on-page SEO elements, content quality, keyword targeting, and user intent alignment.

---

## Execution Modes

### QUICK Mode (5-10 minutes)
**Goal**: Optimize top 3-5 priority pages with quick wins
**Scope**: Homepage + key landing pages
**Output**: Priority optimization checklist with immediate actions

### COMPREHENSIVE Mode (20-30 minutes)
**Goal**: Full content audit across entire site
**Scope**: All important pages (20-30 pages)
**Output**: Detailed content optimization roadmap with implementation plan

---

## Prerequisites

**Required Input**:
- Website URL/domain
- Target keywords (from keyword-research.md) OR will research during execution

**Optional**:
- List of priority pages
- Existing content performance data (if available)
- Target audience/ICP information

**Recommended Prior Skills**:
- Run `keyword-research.md` first to identify target keywords
- Run `technical-audit.md` to identify technical barriers

---

## Content Optimization Categories

### 1. On-Page SEO Elements
### 2. Content Quality & Depth
### 3. Keyword Optimization
### 4. User Intent Alignment
### 5. Internal Linking Structure
### 6. Content Freshness & Updates
### 7. Multimedia Optimization
### 8. Readability & UX

---

## Workflow Steps

### Step 1: Page Selection & Prioritization

**QUICK Mode**:
```
Select 3-5 priority pages:
1. Homepage (always include)
2. Top 2-3 traffic pages (or best opportunity pages)
3. Top 1-2 conversion pages

If traffic data unavailable:
- Homepage
- Main service/product page
- About page
- Top blog post (if applicable)
- Contact/pricing page
```

**COMPREHENSIVE Mode**:
```
Select 20-30 pages across:
1. Homepage (1)
2. Main service/product pages (5-8)
3. Blog posts (10-15)
4. Supporting pages (about, contact, pricing, etc.) (4-6)

Prioritization criteria:
- Current traffic (high traffic = high priority)
- Ranking position (positions 6-20 = quick win opportunity)
- Business value (conversion pages = high priority)
- Content age (old content = needs refresh)
```

**Output**: List of pages to optimize with priority scores

---

### Step 2: Target Keyword Assignment

**For Each Page**:

```
Option A: Use keyword research data
Read: /data/seo/keywords-{site}-{mode}.json
Match pages to target keywords based on:
- Page topic relevance
- Keyword search volume
- Current ranking (if available)

Option B: Research keywords for each page
For each page:
  WebSearch: site:{domain} {page topic}
  Identify what keywords the page currently ranks for

  WebSearch: {page topic} keyword ideas
  Identify what keywords the page SHOULD target

Assign to each page:
- Primary keyword (1)
- Secondary keywords (2-3)
- LSI keywords (5-10 related terms)
```

**Example Output**:
```json
{
  "page": "/products/ai-customer-support",
  "current_url": "https://acme.com/products/ai-customer-support",
  "primary_keyword": "AI customer support software",
  "secondary_keywords": [
    "customer support automation",
    "AI help desk software",
    "automated customer service"
  ],
  "lsi_keywords": [
    "ticket automation",
    "chatbot integration",
    "support analytics",
    "customer satisfaction",
    "response time reduction"
  ]
}
```

---

### Step 3: Content Analysis (Current State)

**For Each Page**:

```
WebFetch: {page_url}

Analyze Current State:

1. Title Tag
   ✓ Present? (Yes/No)
   ✓ Length: X characters (Optimal: 50-60)
   ✓ Includes primary keyword? (Yes/No)
   ✓ Compelling/click-worthy? (Yes/No)
   ✓ Unique? (Check against other pages)

2. Meta Description
   ✓ Present? (Yes/No)
   ✓ Length: X characters (Optimal: 150-160)
   ✓ Includes primary keyword? (Yes/No)
   ✓ Includes call-to-action? (Yes/No)
   ✓ Unique? (Check against other pages)

3. URL Structure
   ✓ Short and descriptive? (Yes/No)
   ✓ Includes keywords? (Yes/No)
   ✓ Clean (no parameters)? (Yes/No)
   ✓ Uses hyphens? (Yes/No)

4. H1 Tag
   ✓ Present? (CRITICAL)
   ✓ Only one H1? (Best practice)
   ✓ Includes primary keyword? (Yes/No)
   ✓ <70 characters? (Yes/No)

5. Header Hierarchy (H2-H6)
   ✓ Logical structure? (H1→H2→H3)
   ✓ No skipped levels? (H1→H3 is bad)
   ✓ Keywords in headers? (Yes/No)
   ✓ Count: X H2s, Y H3s, Z H4s

6. Content Length
   ✓ Word count: X words
   ✓ Meets minimum? (Blog: 1000+, Product: 500+, Homepage: 300+)

7. Keyword Usage
   ✓ Primary keyword in first 100 words? (Yes/No)
   ✓ Primary keyword frequency: X times
   ✓ Keyword density: X% (Target: 1-2%)
   ✓ LSI keywords present: X/10

8. Content Quality
   ✓ Well-structured paragraphs? (Yes/No)
   ✓ Uses bullet points/lists? (Yes/No)
   ✓ Includes examples? (Yes/No)
   ✓ Original content? (Check for duplication)

9. Internal Links
   ✓ Count: X internal links
   ✓ Descriptive anchor text? (Yes/No)
   ✓ Links to relevant pages? (Yes/No)
   ✓ No broken links? (CRITICAL)

10. External Links
    ✓ Count: X external links
    ✓ Links to authoritative sources? (Yes/No)
    ✓ All links working? (CRITICAL)

11. Images
    ✓ Count: X images
    ✓ All have alt text? (Yes/No)
    ✓ Alt text descriptive? (Yes/No)
    ✓ File names descriptive? (Yes/No)

12. Content Freshness
    ✓ Date published visible? (Yes/No)
    ✓ Last updated: X (if available)
    ✓ Content outdated? (Yes/No)

13. Readability
    ✓ Short sentences? (Yes/No)
    ✓ Short paragraphs? (<150 words)
    ✓ Subheadings every 300 words? (Yes/No)
    ✓ Easy to scan? (Yes/No)

14. User Intent Match
    ✓ Content matches search intent? (Informational/Commercial/Transactional)
    ✓ Answers user questions? (Yes/No)
    ✓ Clear next steps/CTA? (Yes/No)
```

**Score Current State**:
```
Calculate optimization score (0-100):
- On-page elements (title, meta, H1, URL): 30 points
- Content quality (length, structure, readability): 30 points
- Keyword optimization: 20 points
- Links (internal, external): 10 points
- Images/multimedia: 10 points
```

---

### Step 4: Competitive Content Analysis

**QUICK Mode**: Skip this step

**COMPREHENSIVE Mode**:

```
For each page:
  Identify top 3 ranking competitors:
  WebSearch: {primary_keyword}

  For each competitor page:
    WebFetch: {competitor_url}

    Analyze:
    - Word count (are they longer?)
    - Content depth (more detailed?)
    - Header structure (better organized?)
    - Multimedia (more images/videos?)
    - Internal links (better linking?)
    - Content freshness (more recent?)

  Identify content gaps:
  - Topics covered by competitors but missing from your content
  - Questions answered by competitors that you don't address
  - Content formats used (lists, tables, FAQs, etc.)
```

**Example Gap Analysis**:
```json
{
  "page": "/products/ai-customer-support",
  "primary_keyword": "AI customer support software",
  "your_content": {
    "word_count": 450,
    "topics_covered": ["AI automation", "ticket routing"],
    "content_format": "paragraphs"
  },
  "top_competitor_avg": {
    "word_count": 1200,
    "topics_covered": ["AI automation", "ticket routing", "sentiment analysis", "chatbot integration", "analytics", "pricing comparison"],
    "content_format": "paragraphs + comparison table + FAQ"
  },
  "content_gaps": [
    "Missing sentiment analysis explanation",
    "No chatbot integration details",
    "No analytics/reporting section",
    "No pricing comparison table",
    "No FAQ section"
  ]
}
```

---

### Step 5: Optimization Recommendations

**For Each Page**, generate specific recommendations:

#### A. Title Tag Optimization

```
Current: "AI Customer Support | Acme Corp"
Issues:
- Generic, not compelling
- Doesn't highlight unique value
- Only 33 characters (could be longer)

Optimized: "AI Customer Support Software - Reduce Tickets by 50% | Acme"
Improvements:
✓ Includes primary keyword
✓ Adds value proposition ("Reduce Tickets by 50%")
✓ 59 characters (optimal length)
✓ More compelling/click-worthy
```

#### B. Meta Description Optimization

```
Current: "Acme provides AI customer support solutions for businesses."
Issues:
- Boring, generic
- No call-to-action
- Only 62 characters (too short)
- Doesn't highlight benefits

Optimized: "Automate 50% of support tickets with Acme's AI customer support software. Reduce response times, improve satisfaction, and scale your team. Start free trial today!"
Improvements:
✓ Includes primary keyword
✓ Specific benefit ("Automate 50%")
✓ Multiple value props (reduce time, improve satisfaction, scale)
✓ Clear CTA ("Start free trial")
✓ 158 characters (optimal length)
```

#### C. H1 Optimization

```
Current: "Customer Support"
Issues:
- Too short, vague
- Doesn't include primary keyword
- Not compelling

Optimized: "AI Customer Support Software That Scales With Your Business"
Improvements:
✓ Includes primary keyword
✓ Highlights benefit ("Scales With Your Business")
✓ More specific and compelling
✓ 60 characters (good length)
```

#### D. Header Structure Optimization

```
Current Structure:
H1: Customer Support
H2: Features
H2: Benefits
H2: Pricing

Issues:
- Too generic
- Doesn't target keywords
- No clear content flow

Optimized Structure:
H1: AI Customer Support Software That Scales With Your Business

H2: How AI Customer Support Automation Works
  H3: Intelligent Ticket Routing
  H3: Sentiment Analysis & Prioritization
  H3: Automated Response Suggestions

H2: Key Benefits of AI Support Automation
  H3: Reduce Ticket Volume by 50%
  H3: Cut Response Times by 70%
  H3: Improve Customer Satisfaction Scores

H2: AI Customer Support Features
  H3: Chatbot Integration
  H3: Advanced Analytics & Reporting
  H3: Multi-Channel Support

H2: Compare AI Support Platforms
  [Comparison table]

H2: Frequently Asked Questions
  H3: How does AI customer support work?
  H3: Is AI support better than traditional help desk?
  H3: How much does AI customer support software cost?

Improvements:
✓ Keywords in headers (H2s target secondary keywords)
✓ Logical flow (How it works → Benefits → Features → Comparison → FAQ)
✓ Specific, descriptive headers
✓ Targets user questions (FAQ section)
```

#### E. Content Expansion Recommendations

```
Current: 450 words
Target: 1200-1500 words (based on competitor analysis)

Add These Sections:

1. "How AI Customer Support Works" (200 words)
   - Explain the technology
   - Step-by-step process
   - Use case examples

2. "Sentiment Analysis for Support Tickets" (150 words)
   - What is sentiment analysis?
   - Why it matters for support
   - How Acme implements it

3. "Chatbot Integration" (150 words)
   - Integration options
   - Benefits of chatbots + AI routing
   - Implementation process

4. "Analytics & Reporting" (150 words)
   - Key metrics tracked
   - Dashboard examples
   - ROI measurement

5. "Comparison Table" (100 words + table)
   - Acme vs Competitor A vs Competitor B
   - Feature comparison
   - Pricing comparison

6. "FAQ Section" (200 words)
   - 5-7 common questions
   - Concise, direct answers
   - Target long-tail keywords

7. "Case Study / Results" (150 words)
   - Customer testimonial
   - Specific results (% improvement)
   - Industry context

Total New Content: ~1100 words
New Total: ~1550 words ✓
```

#### F. Keyword Optimization

```
Primary Keyword: "AI customer support software"
Current Usage: 2 times (0.4% density)
Target Usage: 12-15 times (1-1.5% density)

Placement Recommendations:
✓ Title tag (done)
✓ Meta description (done)
✓ H1 (done)
✓ First 100 words (PRIORITY - currently missing!)
✓ At least 2 H2s
✓ Throughout body content (natural placement)
✓ Image alt text (1-2 images)
✓ URL (if feasible to change)

Secondary Keywords - Add Usage:
- "customer support automation" (currently 0 → target 5-7)
- "AI help desk software" (currently 0 → target 3-5)
- "automated customer service" (currently 1 → target 4-6)

LSI Keywords - Integrate Naturally:
- ticket automation
- chatbot integration
- support analytics
- customer satisfaction
- response time reduction
- support team efficiency
- AI routing
- sentiment analysis
- knowledge base
- self-service support

Action: Rewrite first paragraph to include primary keyword
Current: "Acme helps businesses provide better customer service with our platform."
Optimized: "Acme's AI customer support software helps businesses automate up to 50% of support tickets, reducing response times and improving customer satisfaction. Our customer support automation platform uses intelligent ticket routing, sentiment analysis, and chatbot integration to help your team handle more requests with less effort."

Keywords Added: ✓ Primary, ✓ 2 secondary, ✓ 4 LSI
```

#### G. Internal Linking Optimization

```
Current: 2 internal links (insufficient)
Target: 5-8 internal links

Add Links To:
1. Blog post about "How AI Improves Customer Support"
   Anchor: "learn how AI improves customer support"
   Context: In "How It Works" section

2. Case study page
   Anchor: "see customer results"
   Context: After mentioning benefits

3. Features comparison page
   Anchor: "compare AI support features"
   Context: In features section

4. Pricing page
   Anchor: "view pricing plans"
   Context: At end of page (CTA)

5. Knowledge base article on "Setting Up AI Routing"
   Anchor: "setting up intelligent ticket routing"
   Context: In "How It Works" section

6. About page
   Anchor: "about Acme's approach to customer support"
   Context: In introduction

Guidelines:
✓ Use descriptive anchor text (not "click here")
✓ Link to relevant pages
✓ Natural placement in content
✓ Don't overdo it (8 max)
```

#### H. External Linking Optimization

```
Current: 0 external links (not good)
Target: 2-4 external links to authoritative sources

Add Links To:
1. Industry research/statistics
   Example: "According to Gartner, AI-powered customer service reduces costs by up to 30%"
   Link to: Gartner research report

2. Technology explanation
   Example: "Sentiment analysis uses natural language processing (NLP) to understand customer emotions"
   Link to: Wikipedia or authoritative tech blog explaining NLP

3. Industry benchmark
   Example: "The average customer support response time in SaaS is 12 hours"
   Link to: Industry benchmark report (HubSpot, Zendesk, etc.)

Benefits:
✓ Shows content is well-researched
✓ Builds trust with readers
✓ Positive SEO signal (linking to authorities)
```

#### I. Image Optimization

```
Current: 3 images, 1 has alt text
Target: 5-7 images, all with optimized alt text

Add Images:
1. Hero image (AI support dashboard screenshot)
   Alt: "AI customer support software dashboard showing ticket routing"
   File name: ai-customer-support-dashboard.jpg

2. How it works diagram
   Alt: "Diagram showing how AI customer support automation routes tickets"
   File name: ai-support-automation-workflow.jpg

3. Feature screenshot (sentiment analysis)
   Alt: "Sentiment analysis feature highlighting urgent customer tickets"
   File name: ai-sentiment-analysis-feature.jpg

4. Results graph (ticket volume reduction)
   Alt: "Graph showing 50% reduction in support ticket volume with AI automation"
   File name: ticket-volume-reduction-graph.jpg

5. Comparison table (as image or HTML table)
   Alt: "AI customer support software comparison: Acme vs competitors"
   File name: ai-support-software-comparison-table.jpg

Image Optimization Checklist:
✓ Descriptive file names (keywords included)
✓ Alt text on all images (include keywords naturally)
✓ Optimized file size (<100KB per image)
✓ Use WebP format if possible
✓ Lazy loading enabled
```

#### J. Content Freshness Optimization

```
Current: No publish date visible, content appears outdated

Recommendations:
1. Add publish date (if not present)
2. Add "Last updated: [Date]" at top
3. Refresh outdated information:
   - Update statistics (use 2024 data)
   - Update feature mentions (add recently launched features)
   - Update pricing if changed
   - Update screenshots (current UI)

4. Add "Updated for 2024" to title if appropriate
   Example: "AI Customer Support Software - Complete 2024 Guide"

5. Schedule regular content updates:
   - Major updates: Every 6 months
   - Minor updates: Every quarter
   - News/statistics: As they change
```

#### K. Readability Optimization

```
Current Issues:
- Long paragraphs (200+ words)
- Few bullet points
- Dense text blocks
- No visual breaks

Improvements:
1. Break long paragraphs
   - Target: 2-4 sentences per paragraph
   - Max: 150 words per paragraph

2. Add bullet points/numbered lists
   - Benefits section → bullet list
   - Features section → bullet list
   - FAQ answers → numbered steps

3. Add visual breaks
   - Subheadings every 200-300 words
   - Images between sections
   - Pull quotes or callout boxes

4. Improve sentence structure
   - Average sentence length: <20 words
   - Avoid complex jargon
   - Use active voice

5. Add formatting
   - Bold important phrases
   - Italics for emphasis
   - Highlight key statistics
```

#### L. User Intent Optimization

```
Primary Keyword: "AI customer support software"
Search Intent: Commercial Investigation (users researching solutions)

Current Content Type: Product description (partial match)
Optimal Content Type: Comprehensive guide + product pitch

Add These Elements:

1. Educational Content (satisfy informational intent):
   - "What is AI customer support?" section
   - "How does AI support work?" section
   - Benefits explanation (not just features)

2. Comparison Content (satisfy comparison intent):
   - Feature comparison table
   - "Why choose Acme?" section
   - Competitor alternatives mentioned

3. Decision Support (satisfy transactional intent):
   - Pricing information
   - "Start free trial" CTA (prominent)
   - "Talk to sales" option
   - Customer testimonials/proof

4. Question Answering:
   - FAQ section (7-10 questions)
   - Target long-tail queries like:
     * "How much does AI customer support cost?"
     * "Is AI support better than human support?"
     * "How long does it take to implement AI support?"

Result: Content serves all funnel stages (awareness → consideration → decision)
```

---

### Step 6: Priority & Effort Scoring

**For Each Page**, score recommendations:

```json
{
  "page": "/products/ai-customer-support",
  "current_score": 45,
  "potential_score": 85,
  "improvement_potential": 40,
  "recommendations": [
    {
      "category": "Title Tag",
      "priority": "HIGH",
      "effort": "LOW",
      "impact": "HIGH",
      "time_estimate": "5 minutes",
      "priority_score": 9.0
    },
    {
      "category": "Meta Description",
      "priority": "HIGH",
      "effort": "LOW",
      "impact": "MEDIUM",
      "time_estimate": "5 minutes",
      "priority_score": 8.0
    },
    {
      "category": "Content Expansion",
      "priority": "MEDIUM",
      "effort": "HIGH",
      "impact": "HIGH",
      "time_estimate": "4 hours",
      "priority_score": 6.0
    },
    {
      "category": "Internal Linking",
      "priority": "MEDIUM",
      "effort": "MEDIUM",
      "impact": "MEDIUM",
      "time_estimate": "30 minutes",
      "priority_score": 5.0
    }
  ]
}
```

**Priority Score Formula**:
```
Priority Score = (Impact × Urgency) / Effort

Impact: HIGH=5, MEDIUM=3, LOW=2
Urgency: Always HIGH for underperforming pages=5
Effort: LOW=1, MEDIUM=2, HIGH=3

Sort recommendations by priority score (descending)
```

---

### Step 7: Content Optimization Roadmap

**Generate implementation plan**:

```
Group recommendations by effort level:

QUICK WINS (Low effort, high impact):
- Title tag updates (5 min per page)
- Meta description updates (5 min per page)
- H1 optimization (5 min per page)
- Add primary keyword to first paragraph (10 min per page)

Week 1 Tasks:
- Implement all quick wins
- Time: 2-3 hours
- Impact: Immediate (rankings may improve in 1-2 weeks)

MEDIUM EFFORT (Medium effort, medium-high impact):
- Header structure reorganization (30 min per page)
- Internal linking optimization (30 min per page)
- Image addition and optimization (1 hour per page)
- FAQ section addition (1 hour per page)

Week 2-3 Tasks:
- Implement medium effort improvements
- Time: 8-12 hours
- Impact: 2-4 weeks

HIGH EFFORT (High effort, high impact):
- Content expansion (add 500-1000 words) (4-6 hours per page)
- Competitive content gaps (research + write) (3-4 hours per page)
- Comparison tables creation (2 hours per page)

Month 2 Tasks:
- Implement high effort improvements
- Time: 20-30 hours
- Impact: 4-8 weeks

ONGOING MAINTENANCE:
- Content freshness updates (quarterly)
- New internal links as new content published
- Update statistics and examples (bi-annually)
```

---

### Step 8: Output Generation

**QUICK Mode Output** (`/data/seo/content-optimization-{site}-quick.json`):

```json
{
  "metadata": {
    "mode": "QUICK",
    "site": "acmecorp.com",
    "pages_analyzed": 5,
    "generated_at": "2024-01-15T14:00:00Z"
  },
  "summary": {
    "avg_current_score": 52,
    "avg_potential_score": 78,
    "avg_improvement": 26,
    "total_quick_wins": 15,
    "estimated_time_quick_wins": "2-3 hours"
  },
  "pages": [
    {
      "url": "https://acmecorp.com/",
      "page_type": "homepage",
      "current_score": 65,
      "potential_score": 85,
      "primary_keyword": "AI customer support platform",
      "quick_wins": [
        {
          "element": "Title Tag",
          "current": "Customer Support Platform | AcmeCorp",
          "optimized": "AI Customer Support Platform - Automate 50% of Tickets | AcmeCorp",
          "impact": "HIGH",
          "time": "5 minutes"
        },
        {
          "element": "Meta Description",
          "current": "AcmeCorp provides customer support solutions.",
          "optimized": "Transform your customer support with AcmeCorp's AI platform. Automate tickets, reduce response times by 70%, and improve satisfaction. Start free trial today!",
          "impact": "MEDIUM",
          "time": "5 minutes"
        },
        {
          "element": "H1",
          "current": "Customer Support Made Easy",
          "optimized": "AI Customer Support Platform That Scales With Your Business",
          "impact": "HIGH",
          "time": "5 minutes"
        }
      ]
    }
  ],
  "implementation_plan": {
    "week_1_quick_wins": [
      "Update all title tags (5 pages × 5 min = 25 min)",
      "Update all meta descriptions (5 pages × 5 min = 25 min)",
      "Optimize all H1 tags (5 pages × 5 min = 25 min)",
      "Add primary keyword to first paragraph (5 pages × 10 min = 50 min)"
    ],
    "total_time_week_1": "2 hours 5 minutes",
    "expected_impact": "10-20% improvement in click-through rates within 2-4 weeks"
  }
}
```

**COMPREHENSIVE Mode Output** (`/data/seo/content-optimization-{site}-comprehensive.json`):

```json
{
  "metadata": {
    "mode": "COMPREHENSIVE",
    "site": "acmecorp.com",
    "pages_analyzed": 28,
    "total_recommendations": 156,
    "generated_at": "2024-01-15T14:00:00Z",
    "analysis_duration_minutes": 25
  },
  "summary": {
    "avg_current_score": 48,
    "avg_potential_score": 82,
    "avg_improvement": 34,
    "score_breakdown": {
      "on_page_elements": 55,
      "content_quality": 42,
      "keyword_optimization": 38,
      "links": 51,
      "multimedia": 45
    }
  },
  "competitive_insights": {
    "avg_competitor_content_length": 1450,
    "your_avg_content_length": 520,
    "content_gap": "Competitors have 2.8x more content on average",
    "common_elements_missing": [
      "FAQ sections (80% of competitors have)",
      "Comparison tables (60% of competitors have)",
      "Video content (40% of competitors have)",
      "Customer testimonials (90% of competitors have)"
    ]
  },
  "pages": [
    {
      "url": "https://acmecorp.com/products/ai-support",
      "page_type": "product_page",
      "current_score": 45,
      "potential_score": 85,
      "improvement_potential": 40,
      "primary_keyword": "AI customer support software",
      "current_ranking": "Position 18 (estimated)",
      "target_ranking": "Position 3-5",
      "analysis": {
        "title_tag": {
          "current": "AI Customer Support | AcmeCorp",
          "issues": ["Generic", "No value prop", "Only 33 chars"],
          "optimized": "AI Customer Support Software - Reduce Tickets by 50% | AcmeCorp",
          "improvements": ["Adds primary keyword", "Includes value prop", "Optimal length (59 chars)"]
        },
        "meta_description": {
          "current": "AcmeCorp provides AI customer support solutions for businesses.",
          "issues": ["Boring", "No CTA", "Too short (62 chars)"],
          "optimized": "Automate 50% of support tickets with AcmeCorp's AI customer support software. Reduce response times, improve satisfaction, and scale your team. Start free trial today!",
          "improvements": ["Specific benefit", "Clear CTA", "Optimal length (158 chars)"]
        },
        "content_length": {
          "current": 450,
          "target": 1500,
          "gap": 1050,
          "sections_to_add": [
            "How AI Customer Support Works (200 words)",
            "Sentiment Analysis Explained (150 words)",
            "Chatbot Integration (150 words)",
            "Analytics & Reporting (150 words)",
            "Comparison Table (100 words + table)",
            "FAQ Section (200 words)",
            "Case Study (150 words)"
          ]
        },
        "keyword_optimization": {
          "primary_keyword_usage": {
            "current": 2,
            "target": 12,
            "current_density": "0.4%",
            "target_density": "1.2%"
          },
          "secondary_keywords_usage": {
            "customer support automation": {"current": 0, "target": 6},
            "AI help desk software": {"current": 0, "target": 4}
          },
          "missing_placements": [
            "First 100 words (CRITICAL)",
            "H2 headers (add to 2 headers)",
            "Image alt text (add to 2 images)"
          ]
        },
        "internal_linking": {
          "current_links": 2,
          "target_links": 6,
          "links_to_add": [
            {
              "target_page": "/blog/how-ai-improves-customer-support",
              "anchor_text": "learn how AI improves customer support",
              "context": "In 'How It Works' section"
            },
            {
              "target_page": "/case-studies",
              "anchor_text": "see customer results",
              "context": "After benefits section"
            },
            {
              "target_page": "/pricing",
              "anchor_text": "view pricing plans",
              "context": "CTA at end of page"
            }
          ]
        },
        "competitive_gaps": [
          "Missing sentiment analysis explanation (3/3 competitors have)",
          "No chatbot integration details (2/3 competitors have)",
          "No comparison table (3/3 competitors have)",
          "No FAQ section (3/3 competitors have)"
        ]
      },
      "recommendations": [
        {
          "category": "Title Tag",
          "priority": "HIGH",
          "effort": "LOW",
          "impact": "HIGH",
          "time_estimate": "5 minutes",
          "priority_score": 9.0,
          "action": "Update title tag to include primary keyword and value proposition"
        },
        {
          "category": "Content Expansion",
          "priority": "HIGH",
          "effort": "HIGH",
          "impact": "HIGH",
          "time_estimate": "6 hours",
          "priority_score": 7.5,
          "action": "Add 1050 words covering: How it works, sentiment analysis, chatbot integration, analytics, comparison table, FAQ, case study"
        }
      ]
    }
  ],
  "implementation_roadmap": {
    "week_1_quick_wins": {
      "tasks": [
        "Update all title tags (28 pages)",
        "Update all meta descriptions (28 pages)",
        "Optimize all H1 tags (28 pages)",
        "Add primary keyword to first paragraph (28 pages)"
      ],
      "time_estimate": "8-10 hours",
      "expected_impact": "15-25% improvement in CTR within 2-4 weeks",
      "priority_pages": [
        "/products/ai-support",
        "/",
        "/blog/customer-support-best-practices"
      ]
    },
    "week_2_4_medium_effort": {
      "tasks": [
        "Reorganize header structure (top 10 pages)",
        "Add internal links (all 28 pages)",
        "Optimize images and add alt text (all pages)",
        "Add FAQ sections (top 5 pages)"
      ],
      "time_estimate": "20-25 hours",
      "expected_impact": "Improved user engagement and internal link equity"
    },
    "month_2_3_high_effort": {
      "tasks": [
        "Expand content on top 10 pages (1000+ words each)",
        "Create comparison tables (5 pages)",
        "Add competitive analysis sections",
        "Produce case studies and testimonials"
      ],
      "time_estimate": "60-80 hours",
      "expected_impact": "Significant ranking improvements (3-10 positions) within 2-3 months"
    },
    "ongoing_maintenance": {
      "quarterly": [
        "Update statistics and data",
        "Add new internal links as content published",
        "Refresh outdated screenshots"
      ],
      "bi_annually": [
        "Major content refresh on top pages",
        "Competitive analysis update",
        "Add new sections based on trends"
      ]
    }
  },
  "estimated_results": {
    "traffic_increase": "40-60% increase in organic traffic within 3-6 months",
    "ranking_improvements": "Average improvement of 5-8 positions for target keywords",
    "engagement_improvements": "20-30% increase in time on page, 15-20% decrease in bounce rate"
  }
}
```

---

## Validation Checks

Before saving output:

1. **Minimum Pages**: QUICK ≥3, COMPREHENSIVE ≥20
2. **All Pages Have**: Primary keyword assigned, current score, recommendations
3. **Recommendations Prioritized**: Sorted by priority score
4. **Implementation Roadmap**: Realistic time estimates, phased approach
5. **Quick Wins Identified**: At least 3-5 quick wins per page

---

## Usage Example

**Agent Workflow**:
```
1. Read this skill file
2. Determine mode (QUICK or COMPREHENSIVE)
3. Use TodoWrite to track optimization:
   [ ] Page selection
   [ ] Keyword assignment
   [ ] Content analysis
   [ ] Competitive analysis (COMPREHENSIVE only)
   [ ] Generate recommendations
   [ ] Priority scoring
   [ ] Create roadmap
   [ ] Output generation
4. Execute optimization steps
5. Save JSON to /data/seo/
6. Provide summary:
   "Content Optimization Analysis Complete!

    Pages Analyzed: 28
    Average Current Score: 48/100 (Needs Improvement)
    Average Potential Score: 82/100 (Good)
    Improvement Potential: +34 points

    Quick Wins (Week 1 - 8-10 hours):
    - Update 28 title tags
    - Update 28 meta descriptions
    - Optimize H1 tags
    - Add keywords to first paragraphs
    Impact: +15-25% CTR within 2-4 weeks

    Top Priority Page: /products/ai-support
    Current: 45/100 | Potential: 85/100
    Main Issues: Short content (450 words), missing keywords, no FAQ
    Recommended: Expand to 1500 words, add FAQ, optimize title/meta

    Full report: /data/seo/content-optimization-acme-comprehensive.json"
```

---

## Integration with Other Skills

**Before running this skill**:
- **keyword-research.md** - Identifies target keywords for each page
- **technical-audit.md** - Ensures technical barriers are identified

**After running this skill**:
- **backlink-analysis.md** - Identifies link building opportunities for optimized content
- **Content creation** - Use recommendations to guide new content creation

---

## MCP Tools Needed

**Current**: Built-in tools sufficient (WebFetch, WebSearch, Read, Write)

**Future Enhancement** (optional):
- `mcp__SEO__content_analyzer` - Automated readability scoring, keyword density analysis
- `mcp__SEO__competitor_content_scraper` - Automated competitive content analysis at scale
- `mcp__SEO__content_gap_identifier` - ML-powered content gap detection
