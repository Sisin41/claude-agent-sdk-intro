# Parallel Content Batch Generation

## Purpose
Generate multiple pieces of content simultaneously, tracking progress and maintaining quality across all pieces. This skill enables the content-writer agent to produce 5-10 pieces of content in parallel rather than sequentially.

---

## CRITICAL: Load All Analysis Artifacts First

**Before generating ANY batch of content, you MUST load these artifacts ONCE and use across ALL pieces:**

```
STEP 0: Load Shared Context (5 minutes, done ONCE for entire batch)

1. Company Context (REQUIRED):
   Read: /data/clients/{client-id}/context/company-profile.json
   → Company values, differentiators, mission

2. Brand Guidelines (REQUIRED):
   Read: /data/clients/{client-id}/context/brand-guidelines.json
   → Tone, voice, terminology

3. GEO Analysis (if available):
   Read: /data/clients/{client-id}/analyses/geo/geo-analysis-{latest}.json
   → Citation opportunities, visibility gaps, content structure

4. SEO Analysis (if available):
   Read: /data/clients/{client-id}/analyses/seo/seo-analysis-{latest}.json
   → Target keywords, content gaps, ranking opportunities

5. Competitor Analysis (if available):
   Read: /data/clients/{client-id}/analyses/competitor/competitor-analysis-{latest}.json
   → Differentiation angles, competitor positioning

**Key Efficiency Gain:**
By loading these ONCE and using across all pieces in the batch, you:
- Save 2-3 minutes per piece (no repeated file reads)
- Ensure consistency across all content
- Can reference insights instantly while writing
```

**Example:**
```
Generating 5 blog posts about AI customer support:

Load artifacts once (5 min) →
  Company values: ["transparency", "innovation", "customer-first"]
  Target keywords: ["AI customer support", "support automation", "help desk AI"]
  Differentiators: ["Real-time analytics", "24/7 support", "99.9% uptime"]
  Citation opportunities: ["How AI improves support", "Benefits of automation"]

Use across all 5 posts (no re-reading!) →
  Post 1: Weave in "customer-first" value + "Real-time analytics" differentiator
  Post 2: Optimize for "support automation" + address citation opportunity
  Post 3: Highlight "24/7 support" + use competitor differentiation angle
  ...all with consistent brand voice from guidelines

Time saved: 10-15 minutes (would have read files 5x without batching)
```

---

## How Parallel Generation Works

**Traditional Sequential Approach:**
```
Generate Post 1 (10 min) → Generate Post 2 (10 min) → Generate Post 3 (10 min)
Total Time: 30 minutes for 3 posts
```

**Parallel Batch Approach:**
```
Set up all 3 posts → Generate all in one session → Review all together
Total Time: 15 minutes for 3 posts
```

**Key Benefit**: 2x faster content generation with maintained quality

---

## When to Use This Skill

✅ **Use parallel batch when:**
- Generating 3+ pieces of similar content (e.g., 5 blog posts)
- Content shares similar structure (e.g., all how-to guides)
- Deadline is tight and need fast output
- Content briefs are complete and clear

❌ **Use sequential when:**
- Only 1-2 pieces needed
- Content types are very different (blog + video script)
- Complex research required for each piece
- Each piece builds on the previous one

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
✓ title
✓ type
✓ target_keyword (if SEO content)
✓ word_count or length guidance
✓ key_points or outline

Count total pieces: N
Estimate time: N × 8-12 minutes = X minutes total
```

**Group by similarity:**

```
Group 1: Blog posts (similar structure)
  - blog-001, blog-002, blog-003

Group 2: Social posts (similar length/format)
  - social-001 through social-010

Group 3: Email campaigns (similar structure)
  - email-001, email-002

Generate each group in parallel within itself
```

---

### Step 2: Initialize TodoWrite Tracking

**Create progress tracker:**

```
Use TodoWrite to create tracking for batch:

Example for 5 blog posts:
[██░░░░░░░░] 20% (1/5)

✓ Blog 1: "10 Ways AI Improves Customer Support" (completed)
⟳ Blog 2: "How to Reduce Support Ticket Volume" (in progress)
○ Blog 3: "Customer Support Metrics Guide" (pending)
○ Blog 4: "Best Practices for Support Teams" (pending)
○ Blog 5: "Support Automation ROI Calculator" (pending)
```

**Set up todos for each piece:**

```python
todos = [
    {
        "content": f"Generate: {brief['title']}",
        "status": "pending",
        "activeForm": f"Generating: {brief['title']}"
    }
    for brief in content_briefs
]

TodoWrite(todos=todos)
```

---

### Step 3: Parallel Content Generation

**For Each Content Piece in Batch:**

#### A. Create Content Outline (Fast)

```
For blog-001 "10 Ways AI Improves Customer Support":

Outline:
1. Introduction (150 words)
   - Hook: "Support teams are drowning in tickets"
   - Problem: Traditional support doesn't scale
   - Solution: AI automation

2. Way #1: Automated Ticket Routing (150 words)
   - What it is
   - How it works
   - Benefits

3. Way #2: Sentiment Analysis (150 words)
   [repeat structure]

...

10. Way #10: Predictive Analytics (150 words)

11. Conclusion (100 words)
   - Recap benefits
   - CTA: Start free trial

Total: ~1500 words
Keywords: Include "AI customer support" 8-10 times
```

#### B. Generate Content (Parallel)

**Key insight: Write all sections for all posts simultaneously**

```
Instead of:
  Write all of Post 1 → Write all of Post 2 → Write all of Post 3

Do:
  Write intros for all 3 → Write main content for all 3 → Write conclusions for all 3

This maintains consistency and speeds up generation
```

**Example parallel generation:**

```
Generating intros for batch (posts 1-3)...

Post 1 Intro:
"Customer support teams are drowning in tickets. The average support agent
handles 50-100 tickets per day, leading to burnout and poor customer
satisfaction. But AI customer support automation is changing the game..."

Post 2 Intro:
"Is your support team overwhelmed? If you're seeing ticket volume increase
month over month, you're not alone. But there's a proven way to reduce
support tickets by up to 50% without sacrificing quality..."

Post 3 Intro:
"Are you tracking the right customer support metrics? Many teams focus on
vanity metrics that don't actually improve customer satisfaction. Here are
the metrics that truly matter..."

✓ All 3 intros generated (3 minutes)

Now generating main content sections...
```

#### C. Apply SEO Optimization (Parallel)

```
For each post simultaneously:

✓ Primary keyword in title
✓ Primary keyword in first 100 words
✓ Primary keyword in 2-3 H2 headers
✓ Secondary keywords throughout
✓ Meta description (150-160 chars)
✓ Internal links (3-5 per post)
✓ Alt text for images

Time: 2-3 minutes per post (done in parallel)
```

#### D. Format and Structure (Parallel)

```
Apply consistent formatting to all posts:

- H1 for title
- H2 for main sections
- H3 for sub-sections
- Bullet points for lists
- Bold for key phrases
- Code blocks for examples (if applicable)
- Blockquotes for testimonials/quotes

Use MultiEdit to apply formatting across multiple files at once
```

---

### Step 4: Quality Review (Batch)

**Review all pieces together for consistency:**

```
Check across entire batch:

✓ Tone consistency
  - Are all posts using similar voice?
  - Professional but approachable maintained?

✓ Brand guidelines adherence
  - No jargon used?
  - Terminology consistent?
  - CTAs similar format?

✓ SEO requirements met
  - All have primary keywords?
  - All have meta descriptions?
  - All have internal links?

✓ Formatting consistency
  - All use same header structure?
  - All have similar paragraph lengths?
  - All have CTAs in same location?

✓ Quality standards
  - Word counts within 10% of target?
  - No grammar errors? (check with read-through)
  - All key points covered?
```

**Batch Quality Checklist:**

```json
{
  "batch_id": "blog-batch-2024-01",
  "pieces_generated": 5,
  "quality_checks": {
    "word_count_accuracy": "100% (all within target ±10%)",
    "seo_optimization": "100% (all pieces fully optimized)",
    "brand_consistency": "100% (tone maintained across all)",
    "formatting_consistency": "100% (all use same structure)",
    "grammar_errors": "0 detected",
    "key_points_coverage": "100% (all briefs fully covered)"
  },
  "ready_for_review": true
}
```

---

### Step 5: Save and Finalize

**Save all content pieces:**

```
For each generated piece:

Write to: /data/clients/{client-id}/content/{type}/{filename}

Filename format:
- Blog: YYYY-MM-DD-title-slug.md
- Social: {platform}-{date}.json
- Email: {campaign-name}-email-{number}.md

Example:
/data/clients/acme/content/blog/2024-01-15-ai-customer-support-tips.md
/data/clients/acme/content/blog/2024-01-20-reduce-ticket-volume.md
/data/clients/acme/content/blog/2024-01-25-support-metrics-guide.md
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
    },
    {
      "content_id": "blog-002",
      "title": "How to Reduce Support Ticket Volume by 50%",
      "filename": "2024-01-20-reduce-ticket-volume.md",
      "word_count": 1489,
      "status": "complete",
      "seo_score": 92
    },
    {
      "content_id": "blog-003",
      "title": "Customer Support Metrics That Actually Matter",
      "filename": "2024-01-25-support-metrics-guide.md",
      "word_count": 1211,
      "status": "complete",
      "seo_score": 94
    }
  ],
  "total_word_count": 4234,
  "average_seo_score": 93.7,
  "generation_time_minutes": 18,
  "quality_checks_passed": true
}
```

---

### Step 6: Final TodoWrite Update

**Mark all todos as complete:**

```
TodoWrite update:
[██████████] 100% (5/5)

✓ Blog 1: "10 Ways AI Improves Customer Support" (completed)
✓ Blog 2: "How to Reduce Support Ticket Volume" (completed)
✓ Blog 3: "Customer Support Metrics Guide" (completed)
✓ Blog 4: "Best Practices for Support Teams" (completed)
✓ Blog 5: "Support Automation ROI Calculator" (completed)

All content generated and saved!
```

---

## Output Format

**Summary Message:**

```
✅ Batch Content Generation Complete!

Batch ID: blog-batch-2024-01
Pieces Generated: 5 blog posts
Total Word Count: 4,234 words
Generation Time: 18 minutes
Average Time Per Piece: 3.6 minutes

Quality Metrics:
✓ SEO Score: 93.7/100 (excellent)
✓ Brand Consistency: 100%
✓ Word Count Accuracy: 100% (all within ±10%)
✓ Grammar Errors: 0

Content Saved To:
/data/clients/acme/content/blog/

Files:
1. 2024-01-15-ai-customer-support-tips.md (1,534 words)
2. 2024-01-20-reduce-ticket-volume.md (1,489 words)
3. 2024-01-25-support-metrics-guide.md (1,211 words)
4. 2024-02-01-support-team-best-practices.md (1,567 words)
5. 2024-02-05-automation-roi-calculator.md (1,433 words)

All content is ready for review and publishing!
```

---

## Performance Optimization Tips

### Tip 1: Batch Similar Content Together

```
Good batching:
✓ 5 blog posts about AI customer support
✓ 10 social media posts for LinkedIn
✓ 3 email campaign sequences

Poor batching:
✗ 1 blog + 1 video script + 1 ad copy (too different)
✗ Blog posts on completely unrelated topics (no synergy)
```

### Tip 2: Use Templates for Consistency

```
Create content templates for each type:

Blog Post Template:
- Introduction (problem/hook)
- Main content (numbered list or sections)
- Examples/case studies
- Conclusion with CTA

Apply same template to all blog posts in batch
= Faster generation + consistent quality
```

### Tip 3: Pre-Research Common Elements

```
If generating 5 blog posts about AI customer support:

Research once:
- Latest AI customer support statistics
- Industry trends
- Common pain points
- Competitor examples

Use across all 5 posts
= 5x efficiency gain
```

### Tip 4: Use MultiEdit for Batch Updates

```
After generating all content, use MultiEdit to:

- Add internal links to all posts at once
- Update meta descriptions across all pieces
- Fix common formatting issues in batch
- Add consistent CTAs to all pieces

Saves 50% of revision time
```

---

## Integration with Other Skills

**Before using this skill:**
- Content strategy should be complete
- Content briefs should be well-defined
- Brand guidelines should be clear

**Works well with:**
- `blog-post-writer.md` - For individual blog generation
- `social-media-content.md` - For social batch generation
- `content-quality-review.md` - For post-generation review

**After using this skill:**
- Content is ready for review
- Can be published to CMS
- Can be distributed to channels

---

## Example: 5-Blog-Post Batch

**Input Brief:**

```json
{
  "batch_id": "acme-blog-jan-2024",
  "content_briefs": [
    {"title": "10 AI Customer Support Best Practices", "keyword": "AI customer support", "words": 1500},
    {"title": "How to Implement Support Automation", "keyword": "support automation", "words": 1500},
    {"title": "Customer Support Metrics Guide", "keyword": "support metrics", "words": 1200},
    {"title": "Chatbot Integration Best Practices", "keyword": "chatbot integration", "words": 1500},
    {"title": "Support Team Productivity Tips", "keyword": "support team productivity", "words": 1200}
  ]
}
```

**Execution Timeline:**

```
00:00 - Parse briefs and set up todos
00:02 - Generate all outlines (5 outlines in parallel)
00:05 - Generate all introductions
00:08 - Generate main content for all posts
00:14 - Generate all conclusions and CTAs
00:16 - Apply SEO optimization to all
00:18 - Format and save all pieces
00:20 - Quality review and finalize

Total: 20 minutes for 5 posts (4 min per post)
vs. Sequential: 50 minutes (10 min per post)
Savings: 60% faster ⚡
```

---

## Validation Checklist

Before marking batch complete:

✅ All pieces meet word count targets (±10%)
✅ All SEO requirements satisfied
✅ Brand tone consistent across all pieces
✅ Formatting consistent across all pieces
✅ All key points from briefs covered
✅ No grammar or spelling errors
✅ All files saved to correct locations
✅ Metadata file created
✅ TodoWrite shows 100% complete

---

## Usage Example

**Agent receives request:**

```
User: "Generate 5 blog posts from the content strategy"

Agent reads: /data/clients/acme/analyses/content/content-strategy-2024-01.json
Identifies: 5 blog post briefs

Agent loads this skill: parallel-content-batch.md
Agent follows steps 1-6
Agent generates all 5 posts in parallel
Agent saves with metadata
Agent reports completion

Time: 18-22 minutes
Quality: High (93+ SEO score, 100% brand consistency)
```
