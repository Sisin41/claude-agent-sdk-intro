---
name: seo-technical-audit
description: Evaluate technical SEO health of a website by analyzing crawlability, indexability, page speed, mobile-friendliness, schema markup, and on-page elements. Use to identify critical issues blocking search engine performance and generate a prioritized fix roadmap.
metadata:
  author: castor
  version: "1.0"
  domain: seo
  execution-modes: light, deep
---

# SEO Technical Audit

Evaluate technical SEO health of a website, identify critical issues affecting search engine crawling, indexing, and ranking, and provide prioritized fix recommendations.

## Execution Modes

### Light Mode (5-10 minutes)

- **Goal**: Identify top 5 critical technical issues
- **Scope**: Homepage + 5-10 key pages
- **Output**: High-level issue list with quick fixes

### Deep Mode (20-30 minutes)

- **Goal**: Complete technical SEO audit across entire site
- **Scope**: Full site analysis (crawl simulation)
- **Output**: Detailed audit report with implementation roadmap

## Prerequisites

**Required Input**:
- Website URL/domain
- Access level (public pages only, or sitemap access)

**Optional**:
- List of priority pages to check
- Competitor sites for benchmarking

## Technical SEO Categories

1. Crawlability & Indexability
2. Site Structure & Navigation
3. Page Speed & Core Web Vitals
4. Mobile-Friendliness
5. On-Page SEO Elements
6. Schema Markup & Structured Data
7. Security & HTTPS
8. XML Sitemap & Robots.txt

## Workflow

### Step 1: Homepage Analysis

`WebFetch` the homepage URL and analyze these critical elements:

1. **Title Tag**: Present, unique, 50-60 chars, includes primary keyword
2. **Meta Description**: Present, unique, 150-160 chars, compelling CTA
3. **H1 Tag**: Present, only one per page, includes primary keyword
4. **Heading Structure**: Logical hierarchy (H1 -> H2 -> H3), no skipped levels
5. **Internal Links**: At least 3, all working, descriptive anchor text
6. **Images**: All have alt text, optimized file size, lazy loading
7. **HTTPS**: Site uses HTTPS, no mixed content warnings

**Issue Severity Levels**:
- CRITICAL: Blocks indexing or causes major ranking loss
- HIGH: Significant SEO impact
- MEDIUM: Moderate impact, best practice
- LOW: Minor optimization opportunity

### Step 2: Core Page Analysis

**Light Mode**: Check 5 key pages (homepage, top product/service pages, about, contact).
**Deep Mode**: Check 20-30 pages across all site sections.

For each page, `WebFetch` the URL and check:
- Title uniqueness (no duplicates across site)
- Meta description uniqueness
- Word count (>300 words minimum)
- Internal linking (presence and relevance)
- External links (to authoritative sources)
- Content freshness
- URL structure (short, descriptive, keyword-rich)

### Step 3: Technical Infrastructure Check

**A. XML Sitemap**: `WebFetch` {site}/sitemap.xml -- check existence, proper XML format, all important pages included, no broken URLs, referenced in robots.txt.

**B. Robots.txt**: `WebFetch` {site}/robots.txt -- check existence, not blocking important pages, sitemap referenced, correct user-agent directives.

**C. Canonical Tags**: For each page, verify canonical tag present, pointing to correct URL, self-referencing on main pages.

**D. SSL/HTTPS**: Verify site accessible via HTTPS, HTTP redirects to HTTPS, no mixed content, valid certificate.

### Step 4: Page Speed Analysis

Since Lighthouse cannot be run directly, use proxy methods:

- **WebFetch Timing**: <2s Good, 2-4s Fair, >4s Poor (CRITICAL)
- **Research**: `WebSearch` for "site:{domain} page speed" and "{domain} core web vitals"
- **Resource Analysis**: From fetched HTML, count images (>20 = issue), check inline CSS size (>50KB = issue), count external scripts (>10 = issue), check CDN usage, check image formats (WebP preferred)

### Step 5: Mobile-Friendliness

From fetched HTML, check:
- Viewport meta tag present (`<meta name="viewport" content="width=device-width, initial-scale=1">`)
- Responsive design indicators (media queries, flexible grids)
- No Flash content, readable font sizes (>12px), touch targets >48px

Use `WebSearch` for "{domain} mobile friendly" to find existing test results.

### Step 6: Schema Markup Analysis

From fetched HTML, search for `<script type="application/ld+json">` blocks.

Expected schema by page type:
- Homepage: Organization schema (HIGH priority)
- Blog posts: Article schema (HIGH priority)
- Product pages: Product schema (HIGH priority)
- FAQ pages: FAQ schema (MEDIUM priority)
- All pages: BreadcrumbList (MEDIUM priority)

Verify JSON-LD is properly formatted, uses appropriate type, includes all required fields.

### Step 7: On-Page SEO Elements

For a sample of pages, check:
- Title tags unique and optimal length (50-60 chars)
- Meta descriptions unique and optimal length (150-160 chars)
- One H1 per page with logical heading hierarchy
- URL structure (short, descriptive, hyphens, no parameters)
- Image optimization (alt text, descriptive file names, <100KB)
- Internal linking (3+ per page, descriptive anchors, no broken links)

### Step 8: Content Quality Signals

For key pages, evaluate:
- Content length (homepage 300+, blog 1000+, product 500+ words)
- Content freshness (publish date visible, recently updated)
- Duplicate content (`WebSearch` "exact sentence from page" to check)
- Keyword usage (primary in title, H1, natural 1-2% density, LSI present)

### Step 9: Site Architecture Review

**Light Mode**: Analyze homepage links only.
**Deep Mode**: Map full site structure.

Check navigation clarity, breadcrumbs, footer organization, site depth (all pages within 3 clicks), orphan pages, link distribution, URL consistency.

### Step 10: Common Technical Issues Check

Flag these critical/high issues:
1. Broken links (404 errors) -- CRITICAL
2. Redirect chains (>1 redirect) -- MEDIUM
3. Missing canonical tags -- HIGH
4. Duplicate title tags/meta descriptions -- HIGH
5. Missing alt text -- MEDIUM
6. Slow page speed (>3s) -- HIGH
7. Not mobile-friendly (no viewport tag) -- CRITICAL
8. No HTTPS -- CRITICAL
9. Missing XML sitemap -- HIGH
10. Robots.txt blocking important pages -- CRITICAL

### Step 11: Competitive Benchmarking (Deep Mode Only)

For each competitor, `WebFetch` their homepage and compare page speed, schema markup coverage, content length, internal linking structure, and mobile optimization. Identify what they do better and quick wins you can copy.

### Step 12: Issue Prioritization

Categorize all issues using the priority matrix:

```
Priority = (Impact x Urgency) / Effort

Impact: CRITICAL=5, HIGH=4, MEDIUM=3, LOW=2
Urgency: Blocks indexing=5, Ranking factor=4, Best practice=3, Nice-to-have=2
Effort: LOW=1, MEDIUM=2, HIGH=3
```

### Step 13: Output Generation

Save results to `/data/seo/tech-audit-{site}-{mode}.json`. See [workflow-detail.md](references/workflow-detail.md) for complete output schemas including health scores, issue breakdowns, competitive comparisons, and implementation roadmaps.

## Workspace & File Management

### Client Workspace

Before starting, verify the client workspace exists:
```
/data/clients/{client-id}/analyses/seo/seo-audit-{YYYY-MM-DD-HHMMSS}.json
```

Load company profile and marketing goals from `/data/clients/{client-id}/context/` for strategic context. Save results to the analyses directory and update the analysis timeline.

## Validation Checks

Before saving output, verify:
- At least 5 pages analyzed
- All critical technical elements checked
- Issues categorized by severity
- Fix recommendations provided for each issue
- Time estimates included for all fixes

## Usage Example

```
1. Read this skill file
2. Determine mode (light or deep)
3. Use TodoWrite to track audit through Steps 1-13
4. Execute audit steps using WebFetch and WebSearch
5. Save JSON output to /data/seo/
6. Provide summary:
   "Technical SEO Audit Complete!

    Overall Health: 68/100 (Needs Improvement)

    Issues Found:
    - 3 CRITICAL (fix immediately!)
    - 12 HIGH priority
    - 18 MEDIUM priority

    Top Issue: robots.txt blocking blog content
    Fix: Remove 'Disallow: /blog/' line
    Time: 5 minutes
    Impact: Makes 50 blog posts indexable!

    Full report: /data/seo/tech-audit-acme-comprehensive.json"
```

## Integration with Other Skills

Audit findings feed into:
- **seo-content-optimization** for on-page improvements
- **seo-keyword-research** to understand which keywords are technically blocked
- Strategy synthesis for overall SEO plan
