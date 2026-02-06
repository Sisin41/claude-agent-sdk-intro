---
name: content-blog-writer
description: >
  Generate high-quality, SEO-optimized blog posts that engage readers, rank in search engines, and drive conversions.
  Use this skill for standalone single blog posts or as part of parallel batch generation via content-parallel-batch.
metadata:
  author: castor
  version: "1.0"
  domain: content
  execution-modes: light, deep
---

# Blog Post Writer

## Purpose

Generate high-quality, SEO-optimized blog posts that engage readers, rank in search engines, and drive conversions. Can be used standalone for single posts or as part of parallel batch generation.

---

## CRITICAL: Load Prior Analysis First

**Before writing ANY blog post, you MUST read and integrate these artifacts:**

### 1. Company Context (REQUIRED)
```
Read: /data/clients/{client-id}/context/company-profile.json

Extract:
- Core values (e.g., "transparency", "innovation", "customer-first")
- Key differentiators (e.g., "Real-time analytics", "24/7 support")
- Mission statement
- Target customer profile

Use these to: Inform messaging, shape examples, create authentic voice
```

### 2. GEO Analysis (if available)
```
Read: /data/clients/{client-id}/analyses/geo/geo-analysis-{latest}.json

Extract:
- Citation opportunities (structure content to get AI citations)
- Visibility gaps (topics to cover)
- Competitor citation analysis (what works for them)
- Suggested content structures (for LLM-friendly formatting)

Use these to: Structure sections for AI search visibility, fill content gaps
```

### 3. SEO Analysis (if available)
```
Read: /data/clients/{client-id}/analyses/seo/seo-analysis-{latest}.json

Extract:
- Target keywords (don't guess - use what SEO agent found!)
- Content gaps (specific topics missing from existing content)
- Competitor keyword analysis
- Ranking opportunities

Use these to: Optimize keywords, fill content gaps, target ranking opportunities
```

### 4. Competitor Analysis (if available)
```
Read: /data/clients/{client-id}/analyses/competitor/competitor-analysis-{latest}.json

Extract:
- Competitor positioning (how they message)
- Differentiation angles (how we're better)
- Content gaps in competitor content

Use these to: Differentiate naturally, highlight competitive advantages
```

### 5. Brand Guidelines (if available)
```
Read: /data/clients/{client-id}/context/brand-guidelines.json

Extract:
- Tone (professional, casual, technical, friendly?)
- Voice (expert, approachable, authoritative?)
- Terminology preferences
- Words/phrases to avoid

Use these to: Maintain brand consistency
```

**Why This Matters:**
Without these artifacts, content will be generic. WITH them, content is:
- Authentic (reflects company values)
- Strategic (targets right keywords from SEO analysis)
- Differentiated (uses competitor insights)
- Citation-optimized (structured for GEO opportunities)
- Brand-consistent (follows guidelines)

---

## Post Types Supported

1. **How-To Guides** - Step-by-step instructions
2. **Listicles** - "10 Ways to...", "Top 5..."
3. **Ultimate Guides** - Comprehensive, long-form (2500+ words)
4. **Case Studies** - Customer success stories
5. **Comparison Posts** - "X vs Y", "Best tools for..."
6. **Opinion/Thought Leadership** - Industry insights
7. **News/Trends** - Latest developments
8. **Problem-Solution** - Address pain points

---

## Input Requirements

**Minimum Required:**
```json
{
  "title": "10 Ways AI Improves Customer Support",
  "target_keyword": "AI customer support",
  "word_count": 1500
}
```

**Complete Brief (Recommended):**
```json
{
  "content_id": "blog-001",
  "title": "10 Ways AI Improves Customer Support in 2024",
  "target_keyword": "AI customer support",
  "secondary_keywords": ["support automation", "AI help desk", "customer service AI"],
  "word_count": 1500,
  "target_audience": "B2B SaaS support managers",
  "tone": "professional, helpful, data-driven",
  "key_points": [
    "Automated ticket routing",
    "Sentiment analysis",
    "Response suggestions",
    "Analytics and reporting"
  ],
  "cta": "Start free trial",
  "internal_links": [
    "/features/ai-routing",
    "/blog/support-automation-guide",
    "/case-studies"
  ],
  "publish_date": "2024-02-01",
  "author": "Marketing Team",
  "meta_description": "Discover 10 proven ways AI customer support software improves response times, reduces costs, and boosts satisfaction. Includes real examples and ROI data."
}
```

---

## Workflow Steps

### Step 1: Research & Preparation (2-3 minutes)

- **Competitor Research**: Use `WebSearch` for the target keyword. Analyze top 3 ranking posts for word count, structure, topics covered, and gaps to fill.
- **Keyword Validation**: Use `WebSearch` for related search terms. Identify LSI keywords (semantic terms) to include naturally.
- **Supporting Data**: Use `WebSearch` for statistics about the topic. Find 3-5 compelling stats with credible sources (Gartner, Forrester, industry reports).

### Step 2: Create Detailed Outline (2 minutes)

Follow the standard blog post structure:
- **H1 Title** with primary keyword
- **Introduction** (150-200 words): Hook, problem statement, solution preview, value proposition
- **Main Content** (1000-1300 words): H2 sections with secondary keywords, each containing key point, example, supporting data, takeaway
- **FAQ Section** (optional, 200 words): 3-5 common questions targeting long-tail keywords
- **Conclusion** (150-200 words): Recap benefits, strong CTA, next steps

### Step 3: Write Introduction (5 minutes)

**Formula:** Hook (stat/question/pain point) -> Problem -> Solution -> Preview

Checklist:
- Primary keyword in first 100 words
- 2-3 compelling statistics
- Problem clearly stated
- Solution previewed
- Value proposition clear
- ~150-200 words

### Step 4: Write Main Content Body (15-20 minutes)

**For each H2 section:**
- What it is (1-2 sentences)
- How it works (2-3 sentences)
- Real example or case study (2-3 sentences)
- Supporting data with citation (1 sentence)
- Key takeaway (1 sentence)
- Each section: ~150-180 words

### Step 5: Write FAQ Section (5 minutes)

- Target long-tail keywords
- Answer concisely but completely
- Include specific numbers/timeframes
- Address common objections
- 5-7 questions, each answer 60-100 words

### Step 6: Write Conclusion with Strong CTA (3 minutes)

**Formula:** Recap -> Benefits -> CTA -> Next Steps
- Recap 3-5 key benefits
- Strong, specific CTA ("Start free trial" not "Learn more")
- Multiple CTA options (trial, demo, resources)
- 3-5 internal links to related content
- 150-200 words

### Step 7: SEO Optimization (3 minutes)

- Primary keyword: 1-1.5% density (15-20 times in 1500 words)
- Placement: title, first 100 words, 2-3 H2 headers, meta description, URL slug, image alt text
- Secondary keywords: 5-7 mentions each
- LSI keywords: sprinkled naturally
- Meta description: 150-160 characters
- Internal linking: 3-5 links with descriptive anchor text

### Step 8: Formatting & Readability (2 minutes)

- Paragraphs: 2-4 sentences max
- Sentences: average <20 words
- Subheadings: every 200-300 words
- Bold key terms and stats
- Bullet points for scannable lists
- Blockquotes for testimonials
- Image suggestions with alt text

> For detailed examples, templates, and section-by-section writing guides, see `references/workflow-detail.md`.

---

## Output Format

**Save as Markdown:**

```markdown
File: /data/clients/{client-id}/content/blog/YYYY-MM-DD-title-slug.md

---
title: "Post Title Here"
slug: "title-slug"
publish_date: "YYYY-MM-DD"
author: "Author Name"
category: "Category"
tags: ["tag1", "tag2"]
meta_description: "150-160 char description"
featured_image: "/images/image-name.jpg"
word_count: 1547
target_keyword: "primary keyword"
seo_score: 95
---

[Content here...]
```

---

## Quality Validation

Before finalizing, verify:

- **Word Count**: Target met +/-10%, no fluff
- **SEO Requirements**: Primary keyword 15-20 times, secondary 5-7 each, meta description 150-160 chars, correct H1/H2/H3 structure
- **Content Quality**: All key points covered, real examples included, stats cited with sources, actionable takeaways
- **Readability**: 8th-10th grade level, avg sentence <20 words, 2-4 sentence paragraphs, scannable formatting
- **Brand Consistency**: Tone matches guidelines, terminology consistent, CTAs match brand voice
- **Technical**: No grammar/spelling errors, all links working, images have alt text, Markdown correct

---

## Integration with Parallel Batch

**Standalone:** Generate 1 blog post in 25-30 minutes with thorough research.

**Parallel Batch (via content-parallel-batch):**
Generate 5 blog posts in 60-75 minutes (12-15 min each). When called from parallel batch:
- Skip Step 1 (research done centrally)
- Use shared outline structure
- Generate main content only
- Batch formatting applied later

---

## Related Skills

- `content-parallel-batch` - For generating multiple blog posts simultaneously
