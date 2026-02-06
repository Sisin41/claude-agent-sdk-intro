# SEO Technical Audit - Detailed Reference

This file contains detailed checklists, scoring methods, workspace setup, data analysis patterns, and output schemas referenced by the main SKILL.md.

## Workspace Setup

### Client Workspace Structure

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

Always load company profile at start:
```python
Read(f"/data/clients/{CLIENT_ID}/context/company-profile.json")
# Extract: website, industry, target keywords, competitors
```

Load marketing goals for strategic context:
```python
Read(f"/data/clients/{CLIENT_ID}/context/marketing-goals.json")
# Extract: traffic targets, ranking goals, priority pages
```

### File Naming Convention

Analysis files:
```
/data/clients/{client-id}/analyses/seo/seo-audit-{YYYY-MM-DD-HHMMSS}.json
```

### Save Analysis Results

At end of audit, save to workspace:
```python
analysis_file = f"/data/clients/{CLIENT_ID}/analyses/seo/seo-audit-{timestamp}.json"
Write(analysis_file, json.dumps(audit_results, indent=2))
```

Update analysis timeline:
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

## Data Analysis with Bash

### Site Speed Analysis

```python
Bash("""
python3 << 'EOF'
import json

pages = [
    {"url": "/home", "load_time": 4.2},
    {"url": "/pricing", "load_time": 3.1},
    {"url": "/features", "load_time": 5.3}
]

avg_load_time = sum(p["load_time"] for p in pages) / len(pages)
slow_pages = [p for p in pages if p["load_time"] > 3.0]

print(f"Average load time: {avg_load_time:.2f}s")
print(f"Slow pages (>3s): {len(slow_pages)}")
EOF
""")
```

### Processing Crawl Data from CSV

```python
Bash("""
python3 << 'EOF'
import pandas as pd
import json

df = pd.read_csv('/data/clients/{CLIENT_ID}/raw-data/crawl-data-{date}.csv')

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

## Detailed Page Analysis Checklist

### Homepage Analysis Full Checklist

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
   - Logical hierarchy? (H1 -> H2 -> H3)
   - No skipped levels? (H1 -> H3 is bad)

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

### Pages to Prioritize

```
1. Homepage
2. Top 3-5 product/service pages
3. About page
4. Contact page
5. Top 3 blog posts (by traffic)
6. Pricing page (if applicable)
```

## Page Speed Checklist

```
- Images optimized/compressed?
- Lazy loading implemented?
- CSS/JS minified?
- Browser caching enabled?
- CDN usage?
- Server response time <200ms?
```

## Mobile-Friendliness Checklist

```
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

## Schema Priority by Page Type

```
Homepage: Organization schema (HIGH priority)
Blog posts: Article schema (HIGH priority)
Product pages: Product schema (HIGH priority)
FAQ pages: FAQ schema (MEDIUM priority)
All pages: BreadcrumbList (MEDIUM priority)
```

## Issue Priority Matrix

```
Priority = (Impact x Urgency) / Effort

Impact: CRITICAL=5, HIGH=4, MEDIUM=3, LOW=2
Urgency: Blocks indexing=5, Ranking factor=4, Best practice=3, Nice-to-have=2
Effort: LOW=1, MEDIUM=2, HIGH=3
```

## Output Schemas

### Light Mode Output

File: `/data/seo/tech-audit-{site}-quick.json`

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

### Deep Mode Output

File: `/data/seo/tech-audit-{site}-comprehensive.json`

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
  "high_priority_issues": [],
  "medium_priority_issues": [],
  "low_priority_issues": [],
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
