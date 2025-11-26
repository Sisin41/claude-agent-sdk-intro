# SEO Technical Audit

## Purpose
Evaluate technical SEO health of a website, identify critical issues affecting search engine crawling, indexing, and ranking, and provide prioritized fix recommendations.

---

## Execution Modes

### QUICK Mode (5-10 minutes)
**Goal**: Identify top 5 critical technical issues
**Scope**: Homepage + 5-10 key pages
**Output**: High-level issue list with quick fixes

### COMPREHENSIVE Mode (20-30 minutes)
**Goal**: Complete technical SEO audit across entire site
**Scope**: Full site analysis (crawl simulation)
**Output**: Detailed audit report with implementation roadmap

---

## Prerequisites

**Required Input**:
- Website URL/domain
- Access level (public pages only, or sitemap access)

**Optional**:
- List of priority pages to check
- Competitor sites for benchmarking

---

## Workspace & File Management

###Client Workspace Setup

**Before starting, ensure client workspace exists**:
```bash
CLIENT_ID="client-slug"  # e.g., "acme-corp"

# Check if workspace exists
if [ ! -d "/data/clients/${CLIENT_ID}" ]; then
    # Create workspace structure
    mkdir -p /data/clients/${CLIENT_ID}/{analyses/{geo,seo,ads,competitive,content},context,history,raw-data,temp}
    echo "Created workspace for ${CLIENT_ID}"
fi
```

### Load Client Context

**Always load company profile at start**:
```python
Read(f"/data/clients/{CLIENT_ID}/context/company-profile.json")
# Extract: website, industry, target keywords, competitors
```

**Load marketing goals for strategic context**:
```python
Read(f"/data/clients/{CLIENT_ID}/context/marketing-goals.json")
# Extract: traffic targets, ranking goals, priority pages
```

### File Naming Convention

**Analysis files**:
```
/data/clients/{client-id}/analyses/seo/seo-audit-{YYYY-MM-DD-HHMMSS}.json
```

**Generate timestamp**:
```bash
timestamp=$(date +"%Y-%m-%d-%H%M%S")
```

### Save Analysis Results

**At end of audit, save to workspace**:
```python
analysis_file = f"/data/clients/{CLIENT_ID}/analyses/seo/seo-audit-{timestamp}.json"
Write(analysis_file, json.dumps(audit_results, indent=2))
```

**Update analysis timeline**:
```python
timeline = Read(f"/data/clients/{CLIENT_ID}/history/analysis-timeline.json")
timeline["analyses"].append({
    "analysis_id": f"seo-audit-{timestamp}",
    "type": "seo",
    "subtype": "audit",
    "timestamp": timestamp,
    "agent": "seo-analyst",
    "status": "completed",
    "file_path": analysis_file,
    "summary": "Technical SEO audit found X issues...",
    "key_findings": [...],
    "recommendations_count": len(recommendations)
})
Write(f"/data/clients/{CLIENT_ID}/history/analysis-timeline.json", timeline)
```

### Using Bash for Data Analysis

**When you have site speed data to analyze**:
```python
Bash("""
python3 << 'EOF'
import json

# Sample data analysis
pages = [
    {"url": "/home", "load_time": 4.2},
    {"url": "/pricing", "load_time": 3.1},
    {"url": "/features", "load_time": 5.3}
]

# Calculate statistics
avg_load_time = sum(p["load_time"] for p in pages) / len(pages)
slow_pages = [p for p in pages if p["load_time"] > 3.0]

print(f"Average load time: {avg_load_time:.2f}s")
print(f"Slow pages (>3s): {len(slow_pages)}")
EOF
""")
```

**For processing crawl data from CSV**:
```python
# If you have raw crawl data exported
Bash("""
python3 << 'EOF'
import pandas as pd
import json

df = pd.read_csv('/data/clients/{CLIENT_ID}/raw-data/crawl-data-{date}.csv')

# Analyze issues
issues = {
    "missing_meta_desc": len(df[df['meta_description'].isna()]),
    "duplicate_titles": df['title'].duplicated().sum(),
    "broken_links": len(df[df['status_code'] != 200]),
    "thin_content": len(df[df['word_count'] < 300])
}

print(json.dumps(issues, indent=2))
EOF
""")
```

---

## Technical SEO Categories

### 1. Crawlability & Indexability
### 2. Site Structure & Navigation
### 3. Page Speed & Core Web Vitals
### 4. Mobile-Friendliness
### 5. On-Page SEO Elements
### 6. Schema Markup & Structured Data
### 7. Security & HTTPS
### 8. XML Sitemap & Robots.txt

---

## Workflow Steps

### Step 1: Homepage Analysis

**Check Critical Elements**:

```
WebFetch: {homepage_url}

Analyze:
1. Title Tag
   - Present? (CRITICAL)
   - Unique? (Best practice)
   - Length: 50-60 characters (Optimal)
   - Includes primary keyword? (Best practice)

2. Meta Description
   - Present? (Important)
   - Unique? (Best practice)
   - Length: 150-160 characters (Optimal)
   - Compelling CTA? (Best practice)

3. H1 Tag
   - Present? (CRITICAL)
   - Only one H1? (Best practice)
   - Includes primary keyword? (Best practice)

4. Heading Structure
   - Logical hierarchy? (H1 → H2 → H3)
   - No skipped levels? (H1 → H3 is bad)

5. Internal Links
   - At least 3 internal links? (Best practice)
   - All links working? (CRITICAL)
   - Descriptive anchor text? (Best practice)

6. Images
   - All have alt text? (Important)
   - Images optimized? (Check file size)
   - Lazy loading implemented? (Performance)

7. HTTPS
   - Site uses HTTPS? (CRITICAL)
   - Mixed content warnings? (CRITICAL)
```

**Issue Scoring**:
```
CRITICAL: Blocks indexing or causes major ranking loss
HIGH: Significant SEO impact
MEDIUM: Moderate impact, best practice
LOW: Minor optimization opportunity
```

---

### Step 2: Core Page Analysis

**QUICK Mode**: Check 5 key pages
**COMPREHENSIVE Mode**: Check 20-30 pages across site sections

**Pages to Prioritize**:
```
1. Homepage
2. Top 3-5 product/service pages
3. About page
4. Contact page
5. Top 3 blog posts (by traffic)
6. Pricing page (if applicable)
```

**For Each Page**:
```
WebFetch: {page_url}

Check:
- Title uniqueness (no duplicates across site)
- Meta description uniqueness
- Word count (>300 words minimum)
- Internal linking (presence and relevance)
- External links (to authoritative sources)
- Content freshness (if date available)
- URL structure (short, descriptive, keyword-rich)
```

---

### Step 3: Technical Infrastructure Check

**A. XML Sitemap**:
```
WebFetch: {site}/sitemap.xml

Check:
- Sitemap exists? (CRITICAL)
- Properly formatted XML? (CRITICAL)
- All important pages included? (Important)
- No broken URLs in sitemap? (CRITICAL)
- Sitemap submitted to Google? (Check robots.txt reference)
```

**B. Robots.txt**:
```
WebFetch: {site}/robots.txt

Check:
- Robots.txt exists? (Best practice)
- Not blocking important pages? (CRITICAL)
- Sitemap referenced? (Best practice)
- User-agent directives correct? (Important)
```

**C. Canonical Tags**:
```
For each page analyzed:

Check:
- Canonical tag present? (Best practice)
- Points to correct URL? (CRITICAL if present)
- Self-referencing on main pages? (Best practice)
- Resolves duplicate content issues? (Important)
```

**D. SSL/HTTPS**:
```
Check:
- Site accessible via HTTPS? (CRITICAL)
- HTTP redirects to HTTPS? (CRITICAL)
- Mixed content warnings? (CRITICAL)
- Valid SSL certificate? (CRITICAL)
```

---

### Step 4: Page Speed Analysis

**Since we can't run Lighthouse directly, use proxy methods**:

**Method 1: WebFetch Performance**:
```
Time how long WebFetch takes:
- < 2 seconds: Good
- 2-4 seconds: Fair
- > 4 seconds: Poor (CRITICAL issue)
```

**Method 2: Research Page Speed**:
```
WebSearch: site:{domain} page speed
WebSearch: {domain} core web vitals

Look for:
- Published speed test results
- Google PageSpeed insights mentions
- User complaints about speed
```

**Method 3: Resource Analysis**:
```
From WebFetch HTML:

Analyze:
- Number of images (>20 = potential issue)
- Inline CSS size (>50KB = issue)
- Number of external scripts (>10 = issue)
- Use of CDN? (Check image/script URLs)
- Image format (WebP preferred)
```

**Page Speed Checklist**:
```
✓ Images optimized/compressed?
✓ Lazy loading implemented?
✓ CSS/JS minified?
✓ Browser caching enabled?
✓ CDN usage?
✓ Server response time <200ms?
```

---

### Step 5: Mobile-Friendliness

**Check Mobile Optimization**:

```
From WebFetch HTML, look for:

1. Viewport Meta Tag
   <meta name="viewport" content="width=device-width, initial-scale=1">
   - Present? (CRITICAL)

2. Responsive Design Indicators
   - Media queries in CSS? (Best practice)
   - Flexible grid layouts? (Best practice)
   - No fixed-width elements? (Best practice)

3. Mobile-Specific Issues
   - Touch targets (buttons) large enough? (>48px)
   - No Flash content? (CRITICAL)
   - Readable font sizes? (>12px)
```

**WebSearch Check**:
```
WebSearch: site:{domain} mobile
WebSearch: {domain} mobile friendly

Look for:
- Google Mobile-Friendly test results
- User feedback about mobile experience
```

---

### Step 6: Schema Markup Analysis

**Check for Structured Data**:

```
From WebFetch HTML, search for:

<script type="application/ld+json">

Common Schema Types:
- Organization (Homepage)
- Article (Blog posts)
- Product (E-commerce)
- FAQ (FAQ pages)
- BreadcrumbList (Navigation)
- Review (Product/service pages)

For each page:
- Schema present? (Best practice)
- Properly formatted JSON-LD? (CRITICAL if present)
- Appropriate schema type? (Best practice)
- All required fields included? (Important)
```

**Schema Priority**:
```
Homepage: Organization schema (HIGH priority)
Blog posts: Article schema (HIGH priority)
Product pages: Product schema (HIGH priority)
FAQ pages: FAQ schema (MEDIUM priority)
All pages: BreadcrumbList (MEDIUM priority)
```

---

### Step 7: On-Page SEO Elements

**For Sample of Pages**:

```
Check:

1. Title Tags
   - Unique across all pages? (CRITICAL)
   - Optimal length (50-60 chars)? (Best practice)
   - Keyword placement? (Best practice)

2. Meta Descriptions
   - Unique across all pages? (Important)
   - Optimal length (150-160 chars)? (Best practice)
   - Include CTA? (Best practice)

3. Header Tags (H1-H6)
   - One H1 per page? (Best practice)
   - Logical hierarchy? (Best practice)
   - Include keywords? (Best practice)

4. URL Structure
   - Short and descriptive? (Best practice)
   - Keywords included? (Best practice)
   - No unnecessary parameters? (Best practice)
   - Hyphens vs underscores? (Use hyphens)

5. Image Optimization
   - Alt text on all images? (Important)
   - Descriptive file names? (Best practice)
   - Appropriate file size? (<100KB ideal)

6. Internal Linking
   - 3+ internal links per page? (Best practice)
   - Descriptive anchor text? (Best practice)
   - No broken links? (CRITICAL)
```

---

### Step 8: Content Quality Signals

```
For key pages:

1. Content Length
   - Homepage: 300+ words (Best practice)
   - Blog posts: 1000+ words (Best practice)
   - Product pages: 500+ words (Best practice)

2. Content Freshness
   - Date published visible? (Best practice for blogs)
   - Recently updated? (Helps rankings)

3. Duplicate Content
   - Check if content appears elsewhere:
     WebSearch: "exact sentence from page"
   - If found on other sites = duplicate content issue

4. Keyword Usage
   - Primary keyword in title? (Best practice)
   - Primary keyword in H1? (Best practice)
   - Natural keyword density? (1-2%)
   - LSI keywords present? (Best practice)
```

---

### Step 9: Site Architecture Review

**QUICK Mode**: Analyze homepage links

**COMPREHENSIVE Mode**: Map full site structure

**Analyze**:

```
1. Navigation Structure
   - Clear main navigation? (Best practice)
   - Breadcrumbs present? (Best practice)
   - Footer links organized? (Best practice)

2. Site Depth
   - All pages reachable within 3 clicks from homepage? (Best practice)
   - Orphan pages (no internal links)? (CRITICAL issue)

3. Link Distribution
   - Important pages get more internal links? (Best practice)
   - Link equity flows to priority pages? (Best practice)

4. URL Structure
   - Consistent URL patterns? (Best practice)
   - Subdirectories vs parameters? (Subdirectories preferred)
   - Trailing slashes consistent? (Best practice)
```

---

### Step 10: Common Technical Issues Check

**Critical Issues to Flag**:

```
1. Broken Links
   - WebFetch pages and check all link responses
   - Flag any 404 errors (CRITICAL)

2. Redirect Chains
   - Check if pages redirect multiple times
   - Should be 1 redirect max (Best practice)

3. Missing Canonical Tags
   - Critical for sites with URL parameters
   - Critical for paginated content

4. Duplicate Title Tags/Meta Descriptions
   - Highly common issue
   - HIGH priority fix

5. Missing Alt Text
   - Important for accessibility + SEO
   - MEDIUM priority

6. Slow Page Speed
   - >3 seconds load time
   - HIGH priority

7. Not Mobile-Friendly
   - No viewport tag
   - CRITICAL priority

8. No HTTPS
   - HTTP only
   - CRITICAL priority

9. Missing XML Sitemap
   - No sitemap.xml
   - HIGH priority

10. Robots.txt Blocking Important Pages
    - Accidentally blocking /blog/ or key sections
    - CRITICAL priority
```

---

### Step 11: Competitive Benchmarking

**COMPREHENSIVE Mode Only**:

```
For each competitor:

WebFetch: {competitor_homepage}

Compare:
- Page speed (faster/slower than yours?)
- Schema markup (more comprehensive?)
- Content length (longer/more detailed?)
- Internal linking (better structure?)
- Mobile optimization (better implementation?)

Identify:
- What they do better technically
- Quick wins you can copy
- Areas where you're ahead
```

---

### Step 12: Issue Prioritization

**Categorize All Issues**:

```json
{
  "critical_issues": [
    {
      "issue": "Homepage not accessible via HTTPS",
      "severity": "CRITICAL",
      "impact": "Security warnings, ranking penalty",
      "fix_effort": "LOW",
      "fix_time": "1 hour",
      "priority": 1
    }
  ],
  "high_priority_issues": [ ... ],
  "medium_priority_issues": [ ... ],
  "low_priority_issues": [ ... ]
}
```

**Priority Matrix**:
```
Priority = (Impact × Urgency) / Effort

Impact: CRITICAL=5, HIGH=4, MEDIUM=3, LOW=2
Urgency: Blocks indexing=5, Ranking factor=4, Best practice=3, Nice-to-have=2
Effort: LOW=1, MEDIUM=2, HIGH=3
```

---

### Step 13: Output Generation

**QUICK Mode Output** (`/data/seo/tech-audit-{site}-quick.json`):

```json
{
  "metadata": {
    "mode": "QUICK",
    "site": "acmecorp.com",
    "pages_analyzed": 6,
    "generated_at": "2024-01-15T13:00:00Z"
  },
  "overall_health_score": 72,
  "critical_issues_count": 2,
  "high_issues_count": 5,
  "top_5_issues": [
    {
      "issue": "Missing meta descriptions on 4/6 pages",
      "severity": "HIGH",
      "affected_pages": ["/about", "/pricing", "/contact", "/blog"],
      "fix": "Add unique meta descriptions to each page",
      "estimated_time": "2 hours",
      "priority": 1
    },
    {
      "issue": "Slow homepage load time (4.2 seconds)",
      "severity": "HIGH",
      "fix": "Optimize images, enable compression, use CDN",
      "estimated_time": "4 hours",
      "priority": 2
    }
  ],
  "recommendations": [
    "Fix missing meta descriptions (Priority 1)",
    "Optimize page speed (Priority 2)",
    "Add schema markup to homepage (Priority 3)"
  ]
}
```

**COMPREHENSIVE Mode Output** (`/data/seo/tech-audit-{site}-comprehensive.json`):

```json
{
  "metadata": {
    "mode": "COMPREHENSIVE",
    "site": "acmecorp.com",
    "pages_analyzed": 28,
    "generated_at": "2024-01-15T13:00:00Z",
    "audit_duration_minutes": 25
  },
  "overall_health_score": 68,
  "scores_by_category": {
    "crawlability": 85,
    "on_page_seo": 60,
    "page_speed": 45,
    "mobile_friendly": 90,
    "schema_markup": 30,
    "site_structure": 75
  },
  "issues_summary": {
    "critical": 3,
    "high": 12,
    "medium": 18,
    "low": 7,
    "total": 40
  },
  "critical_issues": [
    {
      "id": "crit_001",
      "issue": "robots.txt blocking /blog/ directory",
      "category": "Crawlability",
      "severity": "CRITICAL",
      "affected_urls": ["All blog content (~50 posts)"],
      "impact": "Blog content not indexed by search engines",
      "fix": "Remove 'Disallow: /blog/' from robots.txt",
      "fix_effort": "LOW",
      "estimated_time": "5 minutes",
      "priority_score": 25.0,
      "priority_rank": 1
    }
  ],
  "high_priority_issues": [ ... ],
  "medium_priority_issues": [ ... ],
  "low_priority_issues": [ ... ],
  "competitive_comparison": {
    "your_site": {
      "health_score": 68,
      "page_speed": "Fair (3.2s)",
      "schema_coverage": "30%"
    },
    "competitor_avg": {
      "health_score": 78,
      "page_speed": "Good (2.1s)",
      "schema_coverage": "65%"
    },
    "gaps": [
      "Competitors have better page speed",
      "Competitors use more schema markup",
      "Your site has better mobile optimization"
    ]
  },
  "implementation_roadmap": {
    "week_1_quick_wins": [
      "Fix robots.txt blocking blog",
      "Add missing meta descriptions",
      "Fix broken links (3 found)"
    ],
    "week_2_4_medium_effort": [
      "Implement schema markup on key pages",
      "Optimize images site-wide",
      "Fix duplicate title tags"
    ],
    "month_2_3_long_term": [
      "Comprehensive page speed optimization",
      "Site architecture improvements",
      "Full schema markup implementation"
    ]
  },
  "estimated_fix_time": {
    "critical_issues": "1 hour",
    "high_priority": "12 hours",
    "all_issues": "40 hours"
  }
}
```

---

## Validation Checks

- At least 5 pages analyzed
- All critical technical elements checked
- Issues categorized by severity
- Fix recommendations provided
- Time estimates included

---

## Usage Example

**Agent Workflow**:
```
1. Read this skill file
2. Determine mode (QUICK or COMPREHENSIVE)
3. Use TodoWrite to track audit:
   [ ] Homepage analysis
   [ ] Core pages check
   [ ] Technical infrastructure
   [ ] Page speed analysis
   [ ] Mobile-friendliness
   [ ] Schema markup
   [ ] On-page SEO
   [ ] Site architecture
   [ ] Issue identification
   [ ] Prioritization
4. Execute audit steps
5. Save JSON to /data/seo/
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

---

## Next Skill

Audit findings feed into:
→ **`content-optimization.md`** for on-page improvements
→ Strategy synthesis for overall SEO plan

---

## MCP Tools Needed

**Current**: Built-in tools sufficient (WebFetch, WebSearch, Read, Write)

**Future Enhancement** (optional):
- `mcp__SEO__site_crawler` - Full site crawl for comprehensive analysis
- `mcp__SEO__speed_tester` - Lighthouse API integration for accurate speed scores
- `mcp__SEO__schema_validator` - Automated schema markup validation
