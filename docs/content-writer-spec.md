# Content Writer Agent - Design Specification

## Overview
The content-writer agent is responsible for **actually generating content** based on strategies, plans, and briefs created by the content-strategist agent.

## Key Differentiators

**Content-Strategist**: Plans WHAT to create (strategy, calendar, topics)
**Content-Writer**: Creates the actual content (blog posts, social, emails, etc.)

## Parallel Execution Architecture

The content-writer can generate **multiple pieces of content in parallel** by:

1. **Batch Processing**: Receives a list of content briefs
2. **Parallel Generation**: Uses TodoWrite to track multiple pieces being written simultaneously
3. **Quality Control**: Reviews and refines each piece before finalizing
4. **Output Management**: Saves all pieces to organized workspace

### Example Workflow:

```
Input: Content calendar with 10 blog posts
↓
content-writer splits into 3 parallel tasks:
├─ Posts 1-3 → Generate in sequence
├─ Posts 4-6 → Generate in sequence
└─ Posts 7-10 → Generate in sequence

Using TodoWrite to show:
[██████████░░░░] 70% (7/10 posts)
✓ Post 1: "Top 10 AI Customer Support Tips" (completed)
✓ Post 2: "How to Reduce Ticket Volume" (completed)
⟳ Post 7: "Customer Support Metrics Guide" (in progress)
○ Post 8: "Chatbot Best Practices" (pending)
```

## Agent Capabilities

### Content Types Supported:
1. **Blog Posts** (long-form, 1000-2500 words)
2. **Social Media** (Twitter, LinkedIn, Facebook)
3. **Email Campaigns** (newsletters, drip campaigns, promotional)
4. **Landing Pages** (hero, features, benefits, CTAs)
5. **Product Descriptions** (short, compelling copy)
6. **Ad Copy** (Google Ads, Facebook Ads, LinkedIn Ads)
7. **Case Studies** (customer stories, results)
8. **White Papers** (technical, in-depth)
9. **Video Scripts** (YouTube, product demos)
10. **Website Copy** (homepage, about, services)

### Content Formats:
- Markdown (default)
- HTML (for web pages)
- Plain text (for emails)
- JSON (structured data)

## Tools Available

```python
content_writer_tools = [
    'Read',           # Read briefs, strategies, templates
    'Write',          # Write new content pieces
    'Edit',           # Refine and edit content
    'MultiEdit',      # Edit multiple files at once
    'Grep',           # Search for references, examples
    'Glob',           # Find related content, templates
    'TodoWrite',      # Track parallel content generation
    'WebSearch',      # Research topics, find stats
    'WebFetch',       # Analyze competitor content, get examples
]
```

## Skills Required

### Core Skills:
1. **blog-post-writer.md** - Generate SEO-optimized blog posts
2. **social-media-content.md** - Create engaging social posts
3. **email-campaign-writer.md** - Write email sequences
4. **ad-copy-generator.md** - Create compelling ad copy
5. **landing-page-writer.md** - Write conversion-focused pages

### Utility Skills:
6. **content-brief-parser.md** - Parse content strategy output
7. **parallel-content-batch.md** - Coordinate parallel generation
8. **content-quality-review.md** - Review and refine content

## Input/Output Specification

### Input Sources:

**From content-strategist:**
```json
/data/clients/{client-id}/analyses/content/content-strategy-{timestamp}.json
```

Contains:
- Content calendar
- Topic ideas and headlines
- Target keywords
- Audience personas
- Channel distribution plan

**Content Brief Format:**
```json
{
  "content_id": "blog-001",
  "type": "blog_post",
  "title": "10 Ways AI Improves Customer Support",
  "target_audience": "B2B SaaS managers",
  "primary_keyword": "AI customer support",
  "secondary_keywords": ["support automation", "AI help desk"],
  "target_word_count": 1500,
  "tone": "professional, helpful",
  "key_points": [
    "Automated ticket routing",
    "Sentiment analysis",
    "Response suggestions"
  ],
  "cta": "Start free trial",
  "deadline": "2024-02-01"
}
```

### Output Structure:

```
/data/clients/{client-id}/content/
├── blog/
│   ├── 2024-01-15-ai-customer-support-tips.md
│   ├── 2024-01-20-reduce-ticket-volume.md
│   └── metadata.json
├── social/
│   ├── linkedin-week-1.json
│   ├── twitter-week-1.json
│   └── metadata.json
├── email/
│   ├── welcome-series-email-1.md
│   └── metadata.json
└── ads/
    ├── google-ads-campaign-1.json
    └── metadata.json
```

## Parallel Generation Strategy

### Batch Processing Modes:

**Mode 1: Parallel-by-Type** (Generate all blog posts in parallel)
```
Input: 5 blog posts
Process: Generate all 5 simultaneously using TodoWrite
Timeline: 15-20 minutes for all 5
```

**Mode 2: Parallel-by-Channel** (Generate content for each channel in parallel)
```
Input: 1 blog + 5 social posts + 2 emails
Process:
├─ Blog (15 min)
├─ Social (10 min)  ← Parallel
└─ Email (10 min)   ← Parallel
Timeline: 15 minutes total (not 35 minutes sequential)
```

**Mode 3: Sequential-with-Progress** (Generate one-by-one with tracking)
```
Input: 10 pieces of various types
Process: Generate sequentially but show progress
Timeline: Variable, with clear progress updates
```

## Quality Standards

Each piece of content must include:

✓ **SEO Optimization** (if applicable)
  - Primary keyword in title, first 100 words
  - Header structure (H1, H2, H3)
  - Meta description
  - Internal links

✓ **Brand Consistency**
  - Tone matches brand guidelines
  - Terminology consistent
  - Voice appropriate for audience

✓ **Formatting**
  - Proper markdown/HTML structure
  - Scannable (short paragraphs, bullets)
  - Clear CTAs

✓ **Quality Checks**
  - No grammar errors
  - No factual errors (verify claims)
  - Meets word count targets
  - Includes all key points from brief

## Workflow Integration

```
1. content-strategist creates strategy
   Output: /analyses/content/content-strategy-{date}.json

2. User reviews and approves plan

3. content-writer reads strategy
   Parses content briefs
   Groups by type/priority

4. content-writer generates content in parallel
   Uses TodoWrite to show progress
   Saves each piece as completed

5. content-writer provides summary
   "Generated 10 pieces of content:
    - 5 blog posts (7,500 words total)
    - 3 email campaigns (15 emails)
    - 2 social media batches (20 posts)

    All content saved to /data/clients/acme/content/"
```

## Agent Prompt Template

```
You are Castor's content writer - an expert at creating high-quality, engaging content across all formats.

**Your Role:**
- Take content briefs and create finished, publishable content
- Generate multiple pieces in parallel when possible
- Maintain brand voice and quality standards
- Optimize for SEO and conversion

**Process:**
1. Read content strategy/briefs from /data/clients/{client}/analyses/content/
2. Parse content requirements (type, keywords, tone, word count)
3. Use TodoWrite to plan parallel content generation
4. Generate each piece of content
5. Apply quality checks and refinements
6. Save to /data/clients/{client}/content/{type}/
7. Update progress and provide summary

**Quality Requirements:**
- SEO optimized (keywords, headers, meta)
- Brand consistent (tone, voice, terminology)
- Well formatted (scannable, clear structure)
- Actionable (includes CTAs, next steps)
- Accurate (fact-check claims, cite sources)

**Parallel Generation:**
When generating multiple pieces:
- Use TodoWrite to track each piece
- Show progress: [███████░░░] 70% (7/10)
- Generate similar types together (all blogs, then all social)
- Maintain quality across all pieces
```

## Next Steps

1. Create skill files:
   - blog-post-writer.md
   - social-media-content.md
   - email-campaign-writer.md
   - parallel-content-batch.md

2. Add agent definition to marketing_agent.py

3. Test parallel generation with sample content brief

4. Integrate with content-strategist workflow
