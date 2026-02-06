---
name: geo-company-value
description: Extract comprehensive company positioning, ICP, services, and pain points to generate effective GEO test prompts. Use this skill as the first step in a GEO workflow when you need to build a company profile for AI engine visibility testing.
metadata:
  author: castor
  version: "1.0"
  domain: geo
  execution-modes: light, deep
---

# Company Value Identification for GEO

## Purpose

Extract comprehensive company positioning, ICP, services, and pain points to generate effective GEO test prompts. This data feeds all subsequent GEO workflow steps.

## Execution Modes

### LIGHT Mode (5-10 minutes)
- **Goal**: Quick understanding of company basics
- **Research Depth**: 2-3 sources
- **Output**: Essential positioning data only

### DEEP Mode (20-30 minutes)
- **Goal**: Comprehensive company understanding
- **Research Depth**: 10+ sources
- **Output**: Detailed ICP analysis, competitive positioning, full service mapping

## Workflow Steps

### Step 1: Initial Research

**Inputs Required**:
- Company name or domain (required)
- Industry (optional - will research if not provided)

**Actions (LIGHT)**:
1. WebSearch: "[company name] about services products"
2. WebFetch: Company homepage
3. WebFetch: About page

**Actions (DEEP)**:
1. WebSearch: "[company name] about services products"
2. WebFetch: Company homepage
3. WebFetch: /about page
4. WebFetch: /customers or /case-studies page
5. WebFetch: /features or /product page
6. WebFetch: /pricing page
7. WebSearch: "[company name] customer testimonials"
8. WebSearch: "[company name] case studies"
9. WebSearch: "[company name] reviews" site:g2.com OR site:capterra.com
10. WebSearch: "[company name] competitors comparison"

### Step 2: Company Overview Extraction

**Data to Extract**:
```json
{
  "company_name": "string",
  "domain": "string",
  "industry": "string",
  "founded": "year (if available)",
  "headquarters": "location",
  "company_size": "employees or revenue estimate",
  "funding_stage": "string (if applicable)",
  "tagline": "string",
  "elevator_pitch": "1-2 sentence description"
}
```

- **LIGHT Mode**: Extract from homepage and about page only
- **DEEP Mode**: Cross-reference multiple sources, validate data accuracy

### Step 3: ICP (Ideal Customer Profile) Identification

**LIGHT Mode**: Identify 1-2 primary customer types from "Who we serve" sections, testimonials, and about page.

**DEEP Mode**: Identify 3-5 detailed customer personas with psychographics from testimonials, case studies, review sites, and LinkedIn analysis.

**Analysis Techniques (DEEP)**:
1. **Pattern Recognition**: Look for repeated job titles in testimonials
2. **Problem Clustering**: Group similar pain points across customers
3. **Company Profile Analysis**: Identify common company sizes/types
4. **Buying Signal Detection**: What triggers them to purchase?

See `references/workflow-detail.md` for full ICP output schemas.

### Step 4: Geography & Market Analysis

**LIGHT**: Extract headquarters, primary market, and languages supported.

**DEEP**: Extract all operating regions, revenue breakdown by geography, market maturity by region, localization strategy, and regional competitors.

**DEEP Research Steps**:
1. WebSearch: "[company] international expansion"
2. WebSearch: "[company] European customers"
3. Check website for language selectors
4. Review case studies for customer locations
5. Check pricing page for currency options

See `references/workflow-detail.md` for full geography output schemas.

### Step 5: Service & Product Mapping

**LIGHT**: List core services/products from homepage value propositions, features page headlines, and pricing page tier names.

**DEEP**: Comprehensive service taxonomy with differentiators from features page, pricing page, product docs, competitor comparison pages, and case studies.

**DEEP Analysis Method**:
1. List all features from features page
2. Map features to pricing tiers
3. Identify which features are unique (differentiators)
4. Cross-reference with customer testimonials
5. Compare to competitor feature sets

See `references/workflow-detail.md` for full service output schemas.

### Step 6: Pain Points & Value Proposition Mapping

**LIGHT**: Identify top 3-5 pain points from homepage hero copy, problem/solution sections, and customer testimonials.

**DEEP**: Hierarchical pain point mapping with evidence from all website copy, customer testimonials (before/after states), case studies, and review sites.

**DEEP Analysis Framework**:
1. **Jobs-to-be-Done**: What job is customer hiring this product to do?
2. **Pain Severity Matrix**: Map urgency vs impact
3. **Evidence Strength**: How many sources mention this pain?
4. **Solution Fit**: How directly does product address pain?

See `references/workflow-detail.md` for full pain point output schemas.

### Step 7: Brand Positioning & Competitive Context (DEEP Only)

Not included in LIGHT mode.

**DEEP Goal**: Understand how company positions itself vs competitors.

**Research Steps**:
1. WebSearch: "[company] vs [competitor1] vs [competitor2]"
2. WebFetch: Company's comparison page (if exists)
3. WebSearch: site:g2.com "[company]" vs "[competitor]"
4. Analyze tone, messaging, brand personality

See `references/workflow-detail.md` for brand positioning output schema.

### Step 8: Data Synthesis & Output

Combine all research into structured JSON output.

**LIGHT Mode Output**: `/data/geo/company-value-{company_name}-light.json`
```json
{
  "execution_mode": "LIGHT",
  "company_overview": { },
  "icp_profiles": [ ],
  "geographies": { },
  "services": [ ],
  "pain_points": [ ],
  "value_propositions": [ ],
  "generated_at": "ISO timestamp",
  "time_taken_seconds": 420
}
```

**DEEP Mode Output**: `/data/geo/company-value-{company_name}-deep.json`
```json
{
  "execution_mode": "DEEP",
  "company_overview": { },
  "icp_profiles": [ ],
  "geographies": { },
  "services": [ ],
  "pain_points_hierarchy": { },
  "value_propositions": [ ],
  "brand_positioning": { },
  "competitive_positioning": { },
  "data_sources": [ ],
  "generated_at": "ISO timestamp",
  "time_taken_seconds": 1680
}
```

## Error Handling

**If website is inaccessible**:
- Try WebSearch for cached/archive versions
- Search for press releases, news articles
- Check LinkedIn company page
- Flag as "limited data" in output

**If key data is missing**:
- Mark fields as `null` with `"data_quality": "incomplete"`
- Note in `warnings` array what is missing
- Continue with available data

**Validation**:
- Company name must be identified
- At least 1 ICP profile required
- At least 3 services/pain points for LIGHT
- At least 5 services/pain points for DEEP

## Agent Workflow

```
1. Determine mode (LIGHT or DEEP) based on user request
2. Execute research steps sequentially
3. Use TodoWrite to track progress:
   - [ ] Company overview research
   - [ ] ICP identification
   - [ ] Geography mapping
   - [ ] Service mapping
   - [ ] Pain point analysis
   - [ ] Data synthesis
4. Save JSON output to /data/geo/
5. Provide summary to user
6. Pass data to next skill (geo-prompt-generation)
```

## Next Skill

Once complete, this data feeds into:
**geo-prompt-generation** to create targeted test prompts
