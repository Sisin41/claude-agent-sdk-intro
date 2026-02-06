# Parallel Content Batch - Detailed Workflow Reference

This document contains detailed examples, execution timelines, and performance optimization tips for the content-parallel-batch skill.

---

## Shared Context Loading Example

```
Generating 5 blog posts about AI customer support:

Load artifacts once (5 min) ->
  Company values: ["transparency", "innovation", "customer-first"]
  Target keywords: ["AI customer support", "support automation", "help desk AI"]
  Differentiators: ["Real-time analytics", "24/7 support", "99.9% uptime"]
  Citation opportunities: ["How AI improves support", "Benefits of automation"]

Use across all 5 posts (no re-reading!) ->
  Post 1: Weave in "customer-first" value + "Real-time analytics" differentiator
  Post 2: Optimize for "support automation" + address citation opportunity
  Post 3: Highlight "24/7 support" + use competitor differentiation angle
  ...all with consistent brand voice from guidelines

Time saved: 10-15 minutes (would have read files 5x without batching)
```

---

## Detailed Outline Generation Example

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

---

## Parallel Generation Example

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

All 3 intros generated (3 minutes)

Now generating main content sections...
```

---

## Batch Quality Checklist Detail

```json
{
  "batch_id": "blog-batch-2024-01",
  "pieces_generated": 5,
  "quality_checks": {
    "word_count_accuracy": "100% (all within target +/-10%)",
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

## Performance Optimization Tips

### Tip 1: Batch Similar Content Together

```
Good batching:
- 5 blog posts about AI customer support
- 10 social media posts for LinkedIn
- 3 email campaign sequences

Poor batching:
- 1 blog + 1 video script + 1 ad copy (too different)
- Blog posts on completely unrelated topics (no synergy)
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

### Tip 4: Use Batch Updates for Revisions

```
After generating all content, apply batch updates to:

- Add internal links to all posts at once
- Update meta descriptions across all pieces
- Fix common formatting issues in batch
- Add consistent CTAs to all pieces

Saves 50% of revision time
```

---

## Detailed Execution Timeline

### 5-Blog-Post Batch Example

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
Savings: 60% faster
```

---

## Full Output Example

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

## Integration with Other Skills

**Before using this skill:**
- Content strategy should be complete
- Content briefs should be well-defined
- Brand guidelines should be clear

**Works well with:**
- `content-blog-writer` - For individual blog generation within the batch
- Social media content skills - For social batch generation
- Content quality review skills - For post-generation review

**After using this skill:**
- Content is ready for review
- Can be published to CMS
- Can be distributed to channels

---

## Full Agent Workflow Example

```
User: "Generate 5 blog posts from the content strategy"

Agent reads: /data/clients/acme/analyses/content/content-strategy-2024-01.json
Identifies: 5 blog post briefs

Agent loads this skill: content-parallel-batch
Agent follows steps 1-6
Agent generates all 5 posts in parallel
Agent saves with metadata
Agent reports completion

Time: 18-22 minutes
Quality: High (93+ SEO score, 100% brand consistency)
```
