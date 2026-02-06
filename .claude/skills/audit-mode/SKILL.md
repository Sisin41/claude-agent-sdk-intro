---
name: audit-mode
description: Run a quick marketing audit for one or more companies. Executes GEO LIGHT and SEO LIGHT in parallel, then Content Gen LIGHT (which depends on both), then wraps everything into a branded report via the report-builder skill. Supports multi-company batch execution.
metadata:
  author: castor
  version: "1.0"
  domain: system
  execution-modes: standard
allowed-tools: Bash(scripts/api/*) Read Write Edit
---

# Audit Mode

Quick 360-degree marketing snapshot. Runs parallel analyses, generates content recommendations, and produces a branded report.

## When to Use

- User says "run an audit", "audit this company", "quick marketing check"
- User provides one or more company names/domains
- User wants a fast overview, not a deep dive

## Execution Flow

```
Input: Company name + domain
         │
         ├──→ GEO LIGHT ──┐
         │                 ├──→ Content Gen LIGHT ──→ Report Builder ──→ audit-report.html
         └──→ SEO LIGHT ──┘
              (parallel)        (sequential)           (sequential)
```

## Step 1: Initialize

Create the audit workspace and blackboard:

```
/data/audits/{batch-id}/
└── {company-slug}/
    ├── blackboard.json
    ├── inputs/
    │   └── company-profile.json
    └── outputs/
```

**Blackboard initial state**: See [blackboard schema](references/blackboard-schema.md).

Set all phases to `pending`. Set `status` to `in_progress`.

### Company Profile

If no existing profile, create a minimal one:

```json
{
  "name": "Company Name",
  "slug": "company-name",
  "domain": "company.com",
  "industry": "inferred or provided",
  "description": "brief description from web search"
}
```

Use `WebSearch` to gather basic company info if not provided.

## Step 2: Run GEO LIGHT + SEO LIGHT (Parallel)

Fire BOTH analyses simultaneously in a single message using parallel Task calls:

**GEO LIGHT agent prompt**:
```
Run a GEO LIGHT analysis for {company_name} ({domain}).

Context: Read company profile from /data/audits/{batch-id}/{slug}/inputs/company-profile.json

Execute:
1. Generate 10-15 test prompts across key categories (comparison, recommendation, informational)
2. For each prompt, query ChatGPT, Perplexity, and Gemini using scripts/api/query-chatgpt.sh, scripts/api/query-perplexity.sh, scripts/api/query-gemini.sh
3. Analyze brand mentions and citations in responses
4. Calculate visibility scores per engine

Write output to: /data/audits/{batch-id}/{slug}/outputs/geo-light.json

Output schema:
{
  "visibility_scores": { "chatgpt": 0.0, "perplexity": 0.0, "gemini": 0.0, "average": 0.0 },
  "brand_mentions": { "total": 0, "by_engine": {} },
  "top_opportunities": [ { "type": "", "description": "", "impact": "high|medium|low" } ],
  "competitor_visibility": { "competitor_name": 0.0 },
  "summary": "2-3 sentence executive summary"
}
```

**SEO LIGHT agent prompt**:
```
Run an SEO LIGHT analysis for {company_name} ({domain}).

Context: Read company profile from /data/audits/{batch-id}/{slug}/inputs/company-profile.json

Execute:
1. WebSearch for "{domain} site:" to assess indexed pages
2. WebSearch for top 5-10 industry keywords to check rankings
3. WebFetch the homepage and 2-3 key pages for on-page SEO signals
4. Identify top keyword opportunities and technical issues

Write output to: /data/audits/{batch-id}/{slug}/outputs/seo-light.json

Output schema:
{
  "domain_authority_estimate": "low|medium|high",
  "indexed_pages_estimate": 0,
  "top_keywords": [ { "keyword": "", "estimated_position": 0, "search_volume": "" } ],
  "technical_issues": [ { "issue": "", "severity": "high|medium|low" } ],
  "content_gaps": [ { "topic": "", "opportunity": "", "difficulty": "" } ],
  "quick_wins": [ "actionable recommendation" ],
  "summary": "2-3 sentence executive summary"
}
```

Update blackboard: set `geo-light` and `seo-light` to `in_progress`.

## Step 3: Run Content Gen LIGHT (Sequential)

**Wait** for both GEO and SEO to complete. Read their outputs, then fire Content Gen:

**Content Gen LIGHT agent prompt**:
```
Generate content recommendations based on GEO and SEO analysis results.

Read inputs:
- GEO results: /data/audits/{batch-id}/{slug}/outputs/geo-light.json
- SEO results: /data/audits/{batch-id}/{slug}/outputs/seo-light.json
- Company profile: /data/audits/{batch-id}/{slug}/inputs/company-profile.json

Execute:
1. Cross-reference GEO visibility gaps with SEO keyword opportunities
2. Identify 5-8 content pieces that would improve both AI visibility and organic search
3. For each, provide: title, type (blog/guide/comparison), target keywords, AI citation angle
4. Prioritize by combined impact (GEO + SEO lift)

Write output to: /data/audits/{batch-id}/{slug}/outputs/content-light.json

Output schema:
{
  "content_recommendations": [
    {
      "priority": 1,
      "title": "Proposed content title",
      "type": "blog|guide|comparison|case-study",
      "target_keywords": ["kw1", "kw2"],
      "geo_angle": "How this improves AI visibility",
      "seo_angle": "How this improves organic search",
      "estimated_impact": "high|medium|low"
    }
  ],
  "strategy_summary": "2-3 sentence summary of content direction",
  "quick_wins": ["immediate actions"]
}
```

Update blackboard: set `content-gen-light` to `in_progress`, then `completed`.

## Step 4: Build Report

Fire the `report-builder` skill:

```
Build a branded audit report.

Read all outputs from: /data/audits/{batch-id}/{slug}/outputs/
- geo-light.json
- seo-light.json
- content-light.json
- Company profile from inputs/company-profile.json

Generate a self-contained HTML report at:
/data/audits/{batch-id}/{slug}/outputs/report.html
```

Update blackboard: set `report` to `completed`. Set overall audit `status` to `completed`.

## Multi-Company Batch

When auditing multiple companies:

1. Create `manifest.json` listing all companies
2. For EACH company, fire a separate `Task` agent with this entire audit-mode skill
3. All company audits run in parallel (the orchestrator handles this)
4. Monitor `manifest.json` for batch completion

```
manifest.json tracks:
- Total companies
- Completed / In Progress / Pending / Failed counts
- Per-company status and blackboard paths
```

## Error Handling

- If GEO fails but SEO succeeds: run Content Gen with SEO-only data, note gap in report
- If SEO fails but GEO succeeds: run Content Gen with GEO-only data, note gap in report
- If both fail: mark audit as failed, report error to user
- If Content Gen fails: still build report with GEO + SEO data (skip content section)

## References

- [Blackboard Schema](references/blackboard-schema.md) - JSON schemas for tracking
