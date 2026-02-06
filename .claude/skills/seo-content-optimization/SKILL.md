---
name: seo-content-optimization
description: Analyze and optimize existing website content for improved search rankings by auditing on-page SEO elements, content quality, keyword targeting, and user intent alignment. Use after keyword research to improve underperforming pages or before a content refresh.
metadata:
  author: castor
  version: "1.0"
  domain: seo
  execution-modes: light, deep
---

# SEO Content Optimization

Analyze and optimize existing website content for improved search engine rankings, focusing on on-page SEO elements, content quality, keyword targeting, and user intent alignment.

## Execution Modes

### Light Mode (5-10 minutes)

- **Goal**: Optimize top 3-5 priority pages with quick wins
- **Scope**: Homepage + key landing pages
- **Output**: Priority optimization checklist with immediate actions

### Deep Mode (20-30 minutes)

- **Goal**: Full content audit across entire site
- **Scope**: All important pages (20-30 pages)
- **Output**: Detailed content optimization roadmap with implementation plan

## Prerequisites

**Required Input**:
- Website URL/domain
- Target keywords (from seo-keyword-research) OR will research during execution

**Optional**:
- List of priority pages
- Existing content performance data
- Target audience/ICP information

**Recommended Prior Skills**:
- Run `seo-keyword-research` first to identify target keywords
- Run `seo-technical-audit` to identify technical barriers

## Content Optimization Categories

1. On-Page SEO Elements
2. Content Quality & Depth
3. Keyword Optimization
4. User Intent Alignment
5. Internal Linking Structure
6. Content Freshness & Updates
7. Multimedia Optimization
8. Readability & UX

## Workflow

### Step 1: Page Selection & Prioritization

**Light Mode** -- select 3-5 pages:
1. Homepage (always)
2. Top 2-3 traffic or opportunity pages
3. Top 1-2 conversion pages

**Deep Mode** -- select 20-30 pages:
- Homepage (1), main product/service pages (5-8), blog posts (10-15), supporting pages (4-6)
- Prioritize by current traffic, ranking position (6-20 = quick win), business value, content age

### Step 2: Target Keyword Assignment

For each page, assign keywords from prior keyword research or discover them:

**Option A**: Read `/data/seo/keywords-{site}-{mode}.json` and match pages to keywords by topic relevance and search volume.

**Option B**: For each page, `WebSearch` "site:{domain} {page topic}" to find current rankings, then `WebSearch` "{page topic} keyword ideas" for targets.

Each page gets:
- 1 primary keyword
- 2-3 secondary keywords
- 5-10 LSI (related) keywords

### Step 3: Content Analysis (Current State)

For each page, `WebFetch` the URL and analyze 14 elements:

1. **Title Tag**: Present, length (50-60 optimal), keyword included, compelling
2. **Meta Description**: Present, length (150-160 optimal), keyword + CTA included
3. **URL Structure**: Short, descriptive, keywords, clean (no parameters), hyphens
4. **H1 Tag**: Present, single H1 only, keyword included, <70 chars
5. **Header Hierarchy**: Logical H1->H2->H3, no skipped levels, keywords in headers
6. **Content Length**: Word count vs. minimums (blog 1000+, product 500+, homepage 300+)
7. **Keyword Usage**: Primary in first 100 words, density 1-2%, LSI keywords present
8. **Content Quality**: Well-structured paragraphs, bullet points, examples, original content
9. **Internal Links**: Count, descriptive anchors, relevant targets, no broken links
10. **External Links**: Count, authoritative sources, all working
11. **Images**: Count, all have alt text, descriptive file names
12. **Content Freshness**: Date visible, last updated, content outdated?
13. **Readability**: Short sentences/paragraphs, subheadings every 300 words, scannable
14. **User Intent Match**: Content matches search intent, answers questions, clear CTA

**Score each page (0-100)**:
- On-page elements (title, meta, H1, URL): 30 points
- Content quality (length, structure, readability): 30 points
- Keyword optimization: 20 points
- Links (internal, external): 10 points
- Images/multimedia: 10 points

### Step 4: Competitive Content Analysis (Deep Mode Only)

For each page, `WebSearch` the primary keyword, then `WebFetch` top 3 competitor pages.

Compare: word count, content depth, header structure, multimedia, internal links, freshness. Identify content gaps -- topics competitors cover that you do not.

### Step 5: Optimization Recommendations

For each page, generate specific recommendations across these areas:

**A. Title Tag** -- rewrite with primary keyword + value proposition at optimal length
**B. Meta Description** -- rewrite with keyword, benefits, CTA at 150-160 chars
**C. H1** -- optimize with keyword + benefit statement
**D. Header Structure** -- reorganize with keyword-rich, logical hierarchy
**E. Content Expansion** -- identify sections to add based on competitor gaps and word count targets
**F. Keyword Optimization** -- map keyword placements (first 100 words, H2s, alt text, throughout body)
**G. Internal Linking** -- identify 3-6 relevant internal link targets with descriptive anchors
**H. External Linking** -- add 2-4 links to authoritative sources (research, statistics, definitions)
**I. Image Optimization** -- add/optimize images with keyword-rich alt text and descriptive file names
**J. Content Freshness** -- update outdated stats, add "last updated" dates, schedule refresh cadence
**K. Readability** -- break paragraphs (2-4 sentences), add lists, visual breaks every 200-300 words
**L. User Intent** -- add educational sections (awareness), comparison content (consideration), CTAs (decision), FAQ (long-tail queries)

See [workflow-detail.md](references/workflow-detail.md) for detailed before/after examples of each optimization type.

### Step 6: Priority & Effort Scoring

For each recommendation, calculate priority score:

```
Priority Score = (Impact x Urgency) / Effort

Impact: HIGH=5, MEDIUM=3, LOW=2
Urgency: Always HIGH for underperforming pages = 5
Effort: LOW=1, MEDIUM=2, HIGH=3
```

Sort all recommendations by priority score (descending).

### Step 7: Content Optimization Roadmap

Group recommendations into implementation phases:

**Quick Wins (Week 1)**: Title tags, meta descriptions, H1s, keyword in first paragraph. Time: 2-3 hours (Light) / 8-10 hours (Deep). Impact: 15-25% CTR improvement in 2-4 weeks.

**Medium Effort (Week 2-4)**: Header restructure, internal linking, images, FAQ sections. Time: 8-12 hours (Light) / 20-25 hours (Deep). Impact: improved engagement.

**High Effort (Month 2-3)**: Content expansion (500-1000+ words per page), competitive gap content, comparison tables, case studies. Time: 20-30 hours (Light) / 60-80 hours (Deep). Impact: 3-10 position ranking improvements.

**Ongoing Maintenance**: Quarterly stats updates, new internal links as content published, bi-annual major refresh.

### Step 8: Output Generation

Save results to `/data/seo/content-optimization-{site}-{mode}.json`.

Light Mode: page scores, quick wins, implementation plan.
Deep Mode: full page analysis + competitive insights + detailed recommendations + roadmap + estimated results.

See [workflow-detail.md](references/workflow-detail.md) for complete output schemas.

## Validation Checks

Before saving output, verify:
- Minimum pages: Light >= 3, Deep >= 20
- All pages have primary keyword assigned, current score, and recommendations
- Recommendations sorted by priority score
- Implementation roadmap has realistic time estimates and phased approach
- At least 3-5 quick wins identified per page

## Usage Example

```
1. Read this skill file
2. Determine mode (light or deep)
3. Use TodoWrite to track progress through Steps 1-8
4. Execute optimization steps using WebFetch and WebSearch
5. Save JSON output to /data/seo/
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

    Full report: /data/seo/content-optimization-acme-comprehensive.json"
```

## Integration with Other Skills

**Before running this skill**:
- **seo-keyword-research** -- identifies target keywords for each page
- **seo-technical-audit** -- ensures technical barriers are identified

**After running this skill**:
- **seo-backlink-analysis** -- identifies link building opportunities for optimized content
- Content creation -- use recommendations to guide new content creation
