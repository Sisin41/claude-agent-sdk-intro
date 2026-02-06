---
name: content-parallel-batch
description: >
  Generate multiple pieces of content simultaneously with progress tracking and quality consistency.
  Use this skill when producing 3-10 content pieces in parallel rather than sequentially for 2x faster output.
metadata:
  author: castor
  version: "1.0"
  domain: content
  execution-modes: light, deep
---

# Parallel Content Batch Generation

## Purpose

Generate multiple pieces of content simultaneously, tracking progress and maintaining quality across all pieces. This skill enables production of 5-10 pieces of content in parallel rather than sequentially.

---

## CRITICAL: Load All Analysis Artifacts First

**Before generating ANY batch of content, you MUST load these artifacts ONCE and use across ALL pieces:**

```
STEP 0: Load Shared Context (5 minutes, done ONCE for entire batch)

1. Company Context (REQUIRED):
   Read: /data/clients/{client-id}/context/company-profile.json
   -> Company values, differentiators, mission

2. Brand Guidelines (REQUIRED):
   Read: /data/clients/{client-id}/context/brand-guidelines.json
   -> Tone, voice, terminology

3. GEO Analysis (if available):
   Read: /data/clients/{client-id}/analyses/geo/geo-analysis-{latest}.json
   -> Citation opportunities, visibility gaps, content structure

4. SEO Analysis (if available):
   Read: /data/clients/{client-id}/analyses/seo/seo-analysis-{latest}.json
   -> Target keywords, content gaps, ranking opportunities

5. Competitor Analysis (if available):
   Read: /data/clients/{client-id}/analyses/competitor/competitor-analysis-{latest}.json
   -> Differentiation angles, competitor positioning
```

**Key Efficiency Gain:** By loading these ONCE and using across all pieces in the batch, you save 2-3 minutes per piece, ensure consistency, and can reference insights instantly while writing.

---

## When to Use This Skill

**Use parallel batch when:**
- Generating 3+ pieces of similar content (e.g., 5 blog posts)
- Content shares similar structure (e.g., all how-to guides)
- Deadline is tight and need fast output
- Content briefs are complete and clear

**Use sequential (content-blog-writer) when:**
- Only 1-2 pieces needed
- Content types are very different (blog + video script)
- Complex research required for each piece
- Each piece builds on the previous one

---

## How Parallel Generation Works

**Traditional Sequential Approach:**
```
Generate Post 1 (10 min) -> Generate Post 2 (10 min) -> Generate Post 3 (10 min)
Total Time: 30 minutes for 3 posts
```

**Parallel Batch Approach:**
```
Set up all 3 posts -> Generate all in one session -> Review all together
Total Time: 15 minutes for 3 posts
```

**Key Benefit**: 2x faster content generation with maintained quality.

---

## Input Requirements

**Required Input:**
```json
{
  "batch_id": "blog-batch-2024-01",
  "content_briefs": [
    {
      "content_id": "blog-001",
      "type": "blog_post",
      "title": "10 Ways AI Improves Customer Support",
      "target_keyword": "AI customer support",
      "word_count": 1500,
      "key_points": ["automated routing", "sentiment analysis", "analytics"]
    },
    {
      "content_id": "blog-002",
      "type": "blog_post",
      "title": "How to Reduce Support Ticket Volume by 50%",
      "target_keyword": "reduce support tickets",
      "word_count": 1500,
      "key_points": ["self-service", "knowledge base", "automation"]
    },
    {
      "content_id": "blog-003",
      "type": "blog_post",
      "title": "Customer Support Metrics That Actually Matter",
      "target_keyword": "support metrics",
      "word_count": 1200,
      "key_points": ["CSAT", "response time", "resolution rate"]
    }
  ],
  "brand_guidelines": {
    "tone": "professional, helpful",
    "voice": "expert but approachable",
    "avoid": ["jargon", "overly sales-y language"]
  },
  "output_directory": "/data/clients/acme/content/blog/"
}
```

---

## Workflow Steps

### Step 1: Batch Preparation

**Parse and validate input:**

```
Read content brief file:
/data/clients/{client-id}/analyses/content/content-strategy-{date}.json

Extract content briefs for this batch
Validate each brief has:
- title
- type
- target_keyword (if SEO content)
- word_count or length guidance
- key_points or outline

Count total pieces: N
Estimate time: N x 8-12 minutes = X minutes total
```

**Group by similarity:**
```
Group 1: Blog posts (similar structure) - blog-001, blog-002, blog-003
Group 2: Social posts (similar length/format) - social-001 through social-010
Group 3: Email campaigns (similar structure) - email-001, email-002

Generate each group in parallel within itself
```

### Step 2: Initialize Progress Tracking

Use TodoWrite to create tracking for each piece in the batch. Update status as each piece progresses through generation.

### Step 3: Parallel Content Generation

**For each content piece in the batch:**

#### A. Create Content Outline (Fast)
Generate outlines for all pieces before writing body content.

#### B. Generate Content (Parallel)
Write all sections for all posts simultaneously:
```
Instead of:
  Write all of Post 1 -> Write all of Post 2 -> Write all of Post 3

Do:
  Write intros for all 3 -> Write main content for all 3 -> Write conclusions for all 3
```
This maintains consistency and speeds up generation.

#### C. Apply SEO Optimization (Parallel)
For each post simultaneously:
- Primary keyword in title, first 100 words, 2-3 H2 headers
- Secondary keywords throughout
- Meta description (150-160 chars)
- Internal links (3-5 per post)
- Alt text for images

#### D. Format and Structure (Parallel)
Apply consistent formatting to all posts:
- H1 for title, H2 for main sections, H3 for sub-sections
- Bullet points for lists
- Bold for key phrases
- Blockquotes for testimonials/quotes

### Step 4: Quality Review (Batch)

**Review all pieces together for consistency:**
- Tone consistency across all posts
- Brand guidelines adherence (no jargon, consistent terminology, similar CTAs)
- SEO requirements met (keywords, meta descriptions, internal links)
- Formatting consistency (same header structure, paragraph lengths, CTA placement)
- Quality standards (word counts within 10% of target, no grammar errors, all key points covered)

### Step 5: Save and Finalize

**Save all content pieces:**
```
For each generated piece:
Write to: /data/clients/{client-id}/content/{type}/{filename}

Filename format:
- Blog: YYYY-MM-DD-title-slug.md
- Social: {platform}-{date}.json
- Email: {campaign-name}-email-{number}.md
```

**Create batch metadata:**
```json
Write to: /data/clients/{client-id}/content/batch-metadata-{batch-id}.json

{
  "batch_id": "blog-batch-2024-01",
  "generated_at": "2024-01-15T10:30:00Z",
  "content_pieces": [
    {
      "content_id": "blog-001",
      "title": "10 Ways AI Improves Customer Support",
      "filename": "2024-01-15-ai-customer-support-tips.md",
      "word_count": 1534,
      "status": "complete",
      "seo_score": 95
    }
  ],
  "total_word_count": 4234,
  "average_seo_score": 93.7,
  "generation_time_minutes": 18,
  "quality_checks_passed": true
}
```

### Step 6: Final Progress Update

Mark all todos as complete and report batch summary.

---

## Output Format

**Summary Message:**
```
Batch Content Generation Complete!

Batch ID: blog-batch-2024-01
Pieces Generated: 5 blog posts
Total Word Count: 4,234 words
Generation Time: 18 minutes
Average Time Per Piece: 3.6 minutes

Quality Metrics:
- SEO Score: 93.7/100 (excellent)
- Brand Consistency: 100%
- Word Count Accuracy: 100% (all within +/-10%)
- Grammar Errors: 0

Content Saved To: /data/clients/acme/content/blog/
```

---

## Validation Checklist

Before marking batch complete:

- All pieces meet word count targets (+/-10%)
- All SEO requirements satisfied
- Brand tone consistent across all pieces
- Formatting consistent across all pieces
- All key points from briefs covered
- No grammar or spelling errors
- All files saved to correct locations
- Metadata file created
- TodoWrite shows 100% complete

> For detailed examples, execution timelines, and performance optimization tips, see `references/workflow-detail.md`.

---

## Related Skills

- `content-blog-writer` - For individual blog post generation within the batch
