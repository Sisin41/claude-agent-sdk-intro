# SEO Keyword Research

## Purpose
Identify high-value keyword opportunities through comprehensive research of search volume, competition, and user intent to guide content strategy and optimization efforts.

---

## Execution Modes

### QUICK Mode (15-20 keywords, 5-10 minutes)
**Goal**: Fast identification of top keyword opportunities
**Research Depth**: Basic search analysis
**Output**: Prioritized list of 15-20 keywords

### COMPREHENSIVE Mode (30-50 keywords, 20-30 minutes)
**Goal**: Detailed keyword strategy with clusters and intent mapping
**Research Depth**: Deep competitive analysis, long-tail exploration
**Output**: Full keyword strategy with topic clusters

---

## Prerequisites

**Required Input**:
- Website/domain to optimize
- Industry/niche
- Target audience (optional - can research)
- Competitors (optional - can identify)

---

## Workflow Steps

### Step 1: Seed Keyword Identification

**Goal**: Identify 10-15 seed keywords that represent core business topics

**Data Sources**:
- Website content (homepage, about page, service pages)
- Competitor websites
- Industry terminology

**QUICK Mode**:
```
1. WebFetch: Read target website homepage
2. Extract main topics/services from content
3. Identify 5-10 seed keywords from services
4. Add industry-standard terms
```

**COMPREHENSIVE Mode**:
```
1. WebFetch: Homepage, services pages, product pages
2. Extract all major topics
3. WebSearch: "{industry} services" to find terminology
4. WebSearch: "site:{competitor.com}" to see their keywords
5. Compile 15-20 seed keywords
```

**Example Seed Keywords** (for AI customer support company):
```
- AI customer support
- Customer support automation
- AI chatbot support
- Support ticket automation
- Customer service AI
- Automated helpdesk
- AI support agents
- Customer support software
- Support automation tools
```

**Output**: List of seed keywords with notes on relevance

---

### Step 2: Keyword Expansion

**Goal**: Expand seed keywords into 30-100+ variations

**Expansion Techniques**:

**1. Question-Based Keywords**:
```
- "how to {seed keyword}"
- "what is {seed keyword}"
- "why {seed keyword}"
- "{seed keyword} guide"
- "{seed keyword} tutorial"
```

**2. Comparison Keywords**:
```
- "best {seed keyword}"
- "{seed keyword} vs {alternative}"
- "top {seed keyword}"
- "{seed keyword} comparison"
- "{seed keyword} alternatives"
```

**3. Problem-Solving Keywords**:
```
- "{problem} solution"
- "fix {problem}"
- "improve {metric}"
- "reduce {negative outcome}"
```

**4. Long-Tail Variations**:
```
- "{seed keyword} for {audience}"
- "{seed keyword} for {industry}"
- "{seed keyword} for {company size}"
- "{seed keyword} with {feature}"
```

**QUICK Mode Process**:
```
For each of top 5 seed keywords:
  - Generate 2-3 variations using techniques above
  - Result: ~15-20 total keywords
```

**COMPREHENSIVE Mode Process**:
```
For each of 15 seed keywords:
  - Generate 3-5 variations per technique
  - Add industry-specific modifiers
  - Add geographic modifiers if applicable
  - Result: 50-100+ total keywords
```

---

### Step 3: Search Volume Estimation

**Goal**: Estimate monthly search volume for each keyword

**Since we don't have direct access to tools like Ahrefs/SEMrush, use proxy methods**:

**Method 1: Google Autocomplete Analysis**
```
WebSearch: "[keyword]"
- If appears in autocomplete → HIGH volume (10K+ searches/month)
- If shows related searches → MEDIUM volume (1K-10K)
- If no suggestions → LOW volume (<1K)
```

**Method 2: Research Published Data**
```
WebSearch: "[keyword] search volume"
WebSearch: "keyword research [industry]"
- Look for blog posts with keyword data
- Check industry reports with search trends
```

**Method 3: Competitive Analysis**
```
WebSearch: site:{competitor.com} "[keyword]"
- If competitor has dedicated page → likely HIGH volume
- If in blog post → MEDIUM volume
- If not found → check if they're missing opportunity
```

**Volume Categories**:
```
- HIGH: 10,000+ monthly searches
- MEDIUM: 1,000-10,000 monthly searches
- LOW: 100-1,000 monthly searches
- VERY LOW: <100 monthly searches
```

**QUICK Mode**: Estimate volume for top 15-20 keywords only

**COMPREHENSIVE Mode**: Estimate volume for all 50+ keywords

---

### Step 4: Keyword Difficulty Assessment

**Goal**: Estimate how hard it is to rank for each keyword

**Difficulty Factors**:

**1. Domain Authority of Ranking Pages**
```
WebSearch: "[keyword]"
Check top 5 results:
- If majority are major brands (Forbes, HubSpot, etc.) → HIGH difficulty
- If mix of brands and blogs → MEDIUM difficulty
- If mostly smaller sites → LOW difficulty
```

**2. Content Quality**
```
WebFetch: Top 3 ranking pages
Assess:
- Word count (longer = more competitive)
- Content depth (comprehensive = harder to beat)
- Freshness (recently updated = more competitive)
```

**3. Intent Match**
```
Does current content match search intent?
- Perfect match → Harder to displace
- Partial match → Opportunity exists
- Poor match → Easier to rank with better content
```

**Difficulty Score** (0-100):
```
0-30: Easy - Can rank quickly with quality content
31-60: Medium - Needs good content + some backlinks
61-80: Hard - Requires comprehensive content + strong backlinks
81-100: Very Hard - Extremely competitive, long-term effort
```

**QUICK Mode**: Assess difficulty for top 15 keywords

**COMPREHENSIVE Mode**: Assess difficulty for all keywords + create difficulty distribution chart

---

### Step 5: User Intent Classification

**Goal**: Categorize keywords by user intent

**Intent Types**:

**1. Informational** (Learning/Research):
```
Examples:
- "what is AI customer support"
- "how does support automation work"
- "AI chatbot guide"

Content Type: Blog posts, guides, tutorials
Funnel Stage: Awareness
```

**2. Commercial** (Comparing Options):
```
Examples:
- "best AI customer support tools"
- "top support automation platforms"
- "AI support software comparison"

Content Type: Comparison articles, listicles, reviews
Funnel Stage: Consideration
```

**3. Transactional** (Ready to Buy):
```
Examples:
- "AI customer support software pricing"
- "buy support automation tool"
- "[specific product] demo"

Content Type: Product pages, pricing pages, demos
Funnel Stage: Decision
```

**4. Navigational** (Looking for specific brand):
```
Examples:
- "[brand name] support"
- "[product name] login"
- "[company] pricing"

Content Type: Brand/product pages
Funnel Stage: Retention or Decision
```

**Intent Distribution**:
```
QUICK Mode: Classify top 15-20 keywords

COMPREHENSIVE Mode:
- Classify all keywords
- Group by intent
- Create intent-based content plan
```

---

### Step 6: Opportunity Scoring

**Goal**: Prioritize keywords by opportunity (value vs. difficulty)

**Opportunity Formula**:
```
Opportunity Score = (Search Volume Score × Intent Value) / (Difficulty Score + 1)

Where:
- Search Volume Score: HIGH=3, MEDIUM=2, LOW=1
- Intent Value: Transactional=3, Commercial=2, Informational=1
- Difficulty Score: 0-100 (lower is better)
```

**Example**:
```
Keyword: "best AI customer support tools"
- Volume: HIGH (3)
- Intent: Commercial (2)
- Difficulty: 45
- Opportunity = (3 × 2) / (45 + 1) = 6/46 = 0.13

Keyword: "AI customer support tutorial"
- Volume: LOW (1)
- Intent: Informational (1)
- Difficulty: 20
- Opportunity = (1 × 1) / (20 + 1) = 1/21 = 0.05

First keyword is higher opportunity!
```

**Priority Tiers**:
```
P1 (High Priority): Opportunity Score > 0.10
P2 (Medium Priority): Opportunity Score 0.05-0.10
P3 (Low Priority): Opportunity Score < 0.05
```

---

### Step 7: Competitive Gap Analysis

**Goal**: Identify keywords where competitors rank but you don't

**Process**:

**QUICK Mode**:
```
1. Identify top 2 competitors
2. WebSearch: site:{competitor.com} [seed keyword]
3. Note pages they have that you don't
4. Flag as opportunity gaps
```

**COMPREHENSIVE Mode**:
```
1. Identify top 3-5 competitors
2. For each competitor:
   WebSearch: site:{competitor.com} [seed keyword category]
   List all their ranking pages
3. For your site:
   WebSearch: site:{your-site.com} [seed keyword category]
   List your ranking pages
4. Compare and identify gaps:
   - Keywords they rank for, you don't
   - Content types they have, you don't
   - Topics they cover, you don't
```

**Gap Categories**:
```
- Critical Gaps: High-volume keywords, competitor ranks top 3, you don't rank
- Opportunity Gaps: Medium-volume, competitor ranks, but content is weak
- Quick Win Gaps: Low difficulty keywords, easy to create content for
```

---

### Step 8: Keyword Grouping & Clustering

**Goal**: Organize keywords into topic clusters for content planning

**QUICK Mode**: Simple grouping by theme

**COMPREHENSIVE Mode**: Detailed topic cluster architecture

**Clustering Method**:

**1. Identify Pillar Topics** (Broad, high-volume keywords):
```
Example Pillar: "AI Customer Support"
- Search volume: HIGH
- Intent: Informational
- Content: Comprehensive 3000+ word guide
```

**2. Group Supporting Keywords** (Related, more specific):
```
Cluster around "AI Customer Support" pillar:
- "AI customer support benefits"
- "AI customer support features"
- "AI customer support implementation"
- "AI customer support ROI"
- "AI customer support best practices"
- "AI customer support challenges"
```

**3. Map Internal Linking**:
```
Pillar Page: "Complete Guide to AI Customer Support"
  ↓ Links to:
  - Cluster Article 1: "10 Benefits of AI Customer Support"
  - Cluster Article 2: "How to Implement AI Support"
  - Cluster Article 3: "Calculating AI Support ROI"
  ← All cluster articles link back to pillar
```

**Typical Cluster Structure**:
```
1 Pillar Page → 5-10 Cluster Articles
```

---

### Step 9: Content Recommendations

**Goal**: Recommend specific content to create for each keyword

**For Each Priority Keyword**:

```json
{
  "keyword": "best AI customer support tools",
  "priority": "P1",
  "recommended_content": {
    "format": "Comparison article / Listicle",
    "word_count": "2500-3500 words",
    "structure": [
      "Introduction - What to look for in AI support tools",
      "Top 10 AI customer support tools (detailed reviews)",
      "Feature comparison table",
      "Pricing comparison",
      "Use case recommendations",
      "Conclusion with top pick"
    ],
    "required_elements": [
      "Comparison table",
      "Screenshots/demos",
      "Pros/cons for each tool",
      "Real customer reviews",
      "Pricing information"
    ],
    "internal_links": [
      "Link to pillar: 'AI Customer Support Guide'",
      "Link to: 'AI Support Pricing Guide'",
      "Link to: 'AI Support Implementation'"
    ],
    "target_outcome": "Rank in top 5, capture comparison traffic"
  }
}
```

---

### Step 10: Output Generation

**QUICK Mode Output** (`/data/seo/keywords-{site}-quick.json`):

```json
{
  "metadata": {
    "mode": "QUICK",
    "site": "acmecorp.com",
    "total_keywords": 18,
    "generated_at": "2024-01-15T12:00:00Z"
  },
  "keywords": [
    {
      "keyword": "AI customer support",
      "search_volume": "HIGH",
      "difficulty": 65,
      "user_intent": "informational",
      "opportunity_score": 0.046,
      "priority": "P2",
      "notes": "High competition but high value"
    },
    {
      "keyword": "best AI customer support tools",
      "search_volume": "MEDIUM",
      "difficulty": 45,
      "user_intent": "commercial",
      "opportunity_score": 0.087,
      "priority": "P1",
      "notes": "Good opportunity - create comparison article"
    }
  ],
  "summary": {
    "p1_keywords": 5,
    "p2_keywords": 8,
    "p3_keywords": 5,
    "recommended_next_steps": [
      "Create comparison article for 'best AI customer support tools'",
      "Write guide for 'AI customer support implementation'",
      "Optimize existing content for 'customer support automation'"
    ]
  }
}
```

**COMPREHENSIVE Mode Output** (`/data/seo/keywords-{site}-comprehensive.json`):

```json
{
  "metadata": {
    "mode": "COMPREHENSIVE",
    "site": "acmecorp.com",
    "total_keywords": 52,
    "topic_clusters": 3,
    "generated_at": "2024-01-15T12:00:00Z"
  },
  "keywords": [
    {
      "keyword": "AI customer support",
      "search_volume": "HIGH",
      "search_volume_estimate": "12000",
      "difficulty": 65,
      "difficulty_reasoning": "Major brands rank top 5, comprehensive content required",
      "user_intent": "informational",
      "opportunity_score": 0.046,
      "priority": "P2",
      "current_ranking": null,
      "competitor_rankings": {
        "zendesk.com": 2,
        "intercom.com": 5
      },
      "gap_type": "critical",
      "recommended_content": {
        "format": "Ultimate guide",
        "word_count": "3500+",
        "effort_hours": 24
      }
    }
  ],
  "topic_clusters": [
    {
      "pillar_keyword": "AI customer support",
      "pillar_content": {
        "title": "Complete Guide to AI Customer Support",
        "url_slug": "/ai-customer-support-guide",
        "word_count": 4000,
        "effort_hours": 32
      },
      "cluster_keywords": [
        "AI customer support benefits",
        "AI customer support implementation",
        "AI customer support ROI",
        "AI customer support features",
        "AI customer support pricing"
      ],
      "estimated_traffic_potential": "15000-20000 monthly visits"
    }
  ],
  "competitive_gaps": [
    {
      "keyword": "AI support chatbot comparison",
      "gap_type": "critical",
      "competitor_with_content": "intercom.com",
      "their_ranking": 3,
      "opportunity": "Create better comparison with more tools"
    }
  ],
  "content_recommendations": [
    {
      "priority": 1,
      "title": "Top 10 AI Customer Support Tools (2024 Comparison)",
      "target_keywords": ["best AI customer support tools", "AI support software comparison"],
      "format": "Comparison article",
      "estimated_traffic": "3000-5000/month",
      "effort_hours": 16
    }
  ]
}
```

---

## Error Handling

**If website is inaccessible**:
- Use WebSearch for cached versions
- Research industry keywords generically
- Flag limited data availability

**If competitors unknown**:
- WebSearch: "{industry} top companies"
- WebSearch: "{main keyword} companies"
- Use industry leaders as proxies

**If no clear keywords found**:
- Use industry-standard terminology
- Research similar companies
- Start with broad seed keywords

---

## Validation Checks

- At least 10 keywords identified
- All keywords have search volume estimates
- All keywords have difficulty scores
- All keywords have intent classification
- At least 3 P1 (high priority) keywords identified

---

## Usage Example

**Agent Workflow**:
```
1. Read this skill file
2. Determine mode (QUICK or COMPREHENSIVE)
3. Use TodoWrite to track progress:
   [ ] Identify seed keywords
   [ ] Expand keyword variations
   [ ] Estimate search volume
   [ ] Assess difficulty
   [ ] Classify user intent
   [ ] Score opportunities
   [ ] Analyze competitive gaps
   [ ] Group into clusters
   [ ] Generate recommendations
4. Execute research steps
5. Save JSON to /data/seo/
6. Provide summary to user:
   "Found 52 keyword opportunities
    - 12 high priority (P1)
    - 25 medium priority (P2)
    - 15 low priority (P3)

    Top opportunity: 'best AI customer support tools'
    - Volume: MEDIUM (2K-5K searches/month)
    - Difficulty: 45 (medium)
    - Opportunity score: 0.087

    Recommended: Create comparison article

    Full research: /data/seo/keywords-acme-comprehensive.json"
```

---

## Next Skill

This keyword data feeds into:
→ **`content-optimization.md`** for optimizing existing content
→ **`technical-audit.md`** for site-wide optimization

---

## MCP Tools Needed

**Current**: Built-in tools sufficient (WebSearch, WebFetch, Read, Write)

**Future Enhancement** (optional):
- `mcp__SEO__keyword_research` - API integration with SEMrush/Ahrefs for precise volume data
- `mcp__SEO__serp_analyzer` - Automated SERP analysis for difficulty scoring
