---
name: seo-backlink-analysis
description: Analyze website backlink profile, identify link building opportunities, assess competitor link strategies, and generate prioritized outreach recommendations. Use to improve domain authority, discover link gaps, and plan outreach campaigns.
metadata:
  author: castor
  version: "1.0"
  domain: seo
  execution-modes: light, deep
---

# SEO Backlink Analysis

Analyze website backlink profile, identify link building opportunities, assess competitor link strategies, and provide actionable outreach recommendations to improve domain authority and search rankings.

**Note**: This skill uses research-based methods since direct access to backlink databases (Ahrefs, Moz, SEMrush) is not available. For comprehensive backlink data, combine this analysis with dedicated SEO tools.

## Execution Modes

### Light Mode (5-10 minutes)

- **Goal**: Backlink health check and top 5 link opportunities
- **Scope**: Basic profile assessment + quick wins
- **Output**: Priority link building actions with outreach targets

### Deep Mode (20-30 minutes)

- **Goal**: Full backlink audit with competitive analysis
- **Scope**: Complete profile + competitor analysis + 20-30 opportunities
- **Output**: Detailed link building strategy with outreach templates

## Prerequisites

**Required Input**:
- Website URL/domain
- Industry/niche

**Optional**:
- Competitor domains (for comparison)
- Target keywords (from seo-keyword-research)
- Existing backlink data from third-party tools

## Backlink Analysis Categories

1. Backlink Profile Assessment
2. Link Quality Evaluation
3. Competitor Backlink Analysis
4. Link Gap Identification
5. Link Building Opportunities
6. Toxic Link Detection
7. Outreach Strategy

## Workflow

### Step 1: Backlink Profile Discovery

Discover existing backlinks using research-based methods:

**Search-Based Discovery**:
- `WebSearch` "link:{domain}" to find pages linking to the domain
- `WebSearch` "{domain}" -site:{domain} to find mentions across the web
- `WebSearch` site:{domain} "backlinks" OR "domain authority" to find self-reported data

**Common Link Sources** -- check these systematically:
- Company listings: Crunchbase, Product Hunt, G2, Capterra
- Social profiles: LinkedIn, Twitter, Facebook, GitHub
- Industry directories: `WebSearch` "{industry} directory"
- News mentions: `WebSearch` site:techcrunch.com {company}, site:venturebeat.com {company}
- Guest posts: `WebSearch` "guest post" OR "contributed by" {company representative}

### Step 2: Link Quality Assessment

For each backlink found, evaluate quality across five dimensions:

1. **Domain Authority** (estimated): Tier 1 (90-100) major publications/.edu/.gov, Tier 2 (70-89) industry leaders, Tier 3 (40-69) niche sites, Tier 4 (<40) low-quality
2. **Relevance**: Same industry = HIGH, related = MEDIUM, unrelated = LOW
3. **Link Type**: Editorial (BEST), resource page (GREAT), guest post (GOOD), directory (OKAY), forum/comment (WEAK)
4. **Placement**: In-content (BEST), author bio (OKAY), sidebar (OKAY), footer (WEAK)
5. **Anchor Text**: Branded (NATURAL), exact match keyword (GOOD if not overused), generic (WEAK but natural), URL (NATURAL)

**Link Quality Score**:
```
Score = (Authority x 0.4) + (Relevance x 0.3) + (Link Type x 0.2) + (Placement x 0.1)
```

Categorize links as: Excellent (80+), Good (60-79), Average (40-59), Weak (20-39), Toxic (<20).

### Step 3: Competitor Backlink Analysis

**Light Mode**: 1-2 competitors. **Deep Mode**: 3-5 competitors.

For each competitor:
1. `WebSearch` "link:{competitor}" and "{competitor}" -site:{competitor}
2. Check industry directories, news sites, resource pages, guest post platforms
3. Identify patterns: which directories, publications, resource pages, guest platforms they use
4. Estimate their profile size and average quality

Build a competitive comparison table showing referring domains, high-quality links, average quality, and strategic gaps.

### Step 4: Link Gap Identification

Compare competitor backlink sources against your own. For each source a competitor has that you do not, flag it as a gap opportunity.

**Gap categories**:
- **Directory gaps**: Directories where competitors are listed but you are not (typically easy to close)
- **Editorial gaps**: Publications featuring competitors (harder, requires PR/newsworthy content)
- **Guest post gaps**: Blogs where competitors have published guest content
- **Resource page gaps**: "Best tools" and resource lists that include competitors but not you

Prioritize by authority of linking site, relevance, and difficulty to obtain.

### Step 5: Link Building Opportunity Discovery

Discover new opportunities beyond competitor gaps:

**A. Industry Directories**: `WebSearch` "{industry} software directory", "{niche} companies list". Check G2, Capterra, Product Hunt, AlternativeTo, SoftwareAdvice, GetApp, Crunchbase.

**B. Resource Pages**: `WebSearch` "best {category} tools", "{category} resources", inurl:resources {industry}. `WebFetch` each to verify quality and submission process.

**C. Guest Post Opportunities**: `WebSearch` "{industry} guest post", "{niche} write for us", inurl:write-for-us {industry}. Extract submission guidelines and audience relevance.

**D. Broken Link Building**: Find resource pages with broken links; offer your content as replacement.

**E. Unlinked Brand Mentions**: `WebSearch` "{company name}" -site:{domain}. `WebFetch` mention pages to verify no link exists. Outreach to request link addition.

**F. Competitor Replacement**: `WebSearch` "alternatives to {competitor}", "{competitor} vs". Pitch inclusion in comparison articles.

**G. HARO/PR**: Monitor Help A Reporter Out, SourceBottle, JournoRequests for expert quote opportunities.

**H. Podcast/Interview**: `WebSearch` "{industry} podcast guests", "{niche} interview opportunities". Pitch as expert guest.

### Step 6: Opportunity Prioritization

Score each opportunity:

```
Priority Score = (Authority x Relevance x Success Rate) / Effort

Authority: 0-100 (domain authority estimate)
Relevance: 0-100 (business relevance)
Success Rate: 0-100 (likelihood of obtaining link)
Effort: 1-10 (1=very easy, 10=very hard)
```

Categorize into quick wins (low effort, high success), medium effort, and high effort (long-term).

### Step 7: Toxic Link Detection

Flag potentially harmful links -- spam directories, link farms, very low quality domains, exact-match anchor text overuse (>50%).

Research method: `WebSearch` "{domain}" spam, "{domain}" negative SEO.

**Limitation**: Toxic link detection is limited without full backlink database access. Recommend Ahrefs, Moz, or Google Search Console for comprehensive toxic link audit.

### Step 8: Outreach Strategy & Templates

Generate an outreach plan with campaigns, target counts, time estimates, expected success rates, and expected link counts.

Four outreach email templates are included in the reference file:
1. Unlinked Mention outreach
2. Resource Page Inclusion request
3. Broken Link Replacement pitch
4. Guest Post Pitch

See [workflow-detail.md](references/workflow-detail.md) for all templates and detailed opportunity schemas.

### Step 9: Output Generation

Save results to `/data/seo/backlink-analysis-{site}-{mode}.json`.

Light Mode: current profile estimate, competitor comparison, top 5 opportunities, quick action plan.
Deep Mode: full profile + quality breakdown + competitor analysis + link gaps + all opportunities + outreach plan + implementation roadmap + projected results.

See [workflow-detail.md](references/workflow-detail.md) for complete output schemas.

## Important Limitations

This skill uses research-based methods, NOT comprehensive backlink tools.

- Cannot see full backlink profile (only sample via search)
- Cannot accurately estimate domain authority without tools
- Cannot detect all toxic links
- Cannot see competitor's full backlink profile

For comprehensive analysis, combine with Ahrefs, Moz, SEMrush, or Google Search Console.

**Best used for**: Link building opportunity discovery, competitor strategy analysis, outreach planning, quick health checks.

## Validation Checks

Before saving output, verify:
- Minimum opportunities: Light >= 10, Deep >= 40
- At least 2 competitors analyzed
- All opportunities have priority scores
- At least 3 outreach templates included (Deep mode)
- Realistic success rates and time estimates
- Implementation roadmap with phased timelines

## Usage Example

```
1. Read this skill file
2. Determine mode (light or deep)
3. Use TodoWrite to track progress through Steps 1-9
4. Execute analysis using WebSearch and WebFetch
5. Save JSON output to /data/seo/
6. Provide summary:
   "Backlink Analysis Complete!

    Current Profile (estimated):
    - 45 referring domains
    - 12 high-quality links
    - Average quality: 62/100

    Competitor Gap:
    - Competitors have 3-4x more backlinks
    - Main gaps: PR coverage, guest posting, directories

    Top 5 Opportunities:
    1. Capterra listing (30 min, 90% success) - QUICK WIN!
    2. G2 listing (45 min, 85% success) - QUICK WIN!
    3. Unlinked mention outreach (15 min, 70% success)
    4. Resource page: best-tools.com (1 hour, 50% success)
    5. Guest post: industry-blog.com (5 hours, 60% success)

    Month 1 Plan: 11 hours -> 10-12 new links
    3-Month Projection: +25-35 referring domains (+55-78%)

    Full report: /data/seo/backlink-analysis-acme-comprehensive.json"
```

## Integration with Other Skills

**After running this skill**:
- Use opportunities to create content for guest posts and resource pages
- Coordinate with **seo-content-optimization** to optimize pages before pitching for links
- Track results over time by re-running monthly to measure progress
