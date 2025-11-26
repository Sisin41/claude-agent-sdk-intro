# Company Value Identification for GEO

## Purpose
Extract comprehensive company positioning, ICP, services, and pain points to generate effective GEO test prompts. This data feeds all subsequent GEO workflow steps.

---

## Execution Modes

### LIGHT Mode (5-10 minutes)
**Goal**: Quick understanding of company basics

**Research Depth**: 2-3 sources
**Output**: Essential positioning data only

### DEEP Mode (20-30 minutes)
**Goal**: Comprehensive company understanding

**Research Depth**: 10+ sources
**Output**: Detailed ICP analysis, competitive positioning, full service mapping

---

## Workflow Steps

### Step 1: Initial Research

**Inputs Required**:
- Company name or domain (required)
- Industry (optional - will research if not provided)

**Actions (LIGHT)**:
```
1. WebSearch: "[company name] about services products"
2. WebFetch: Company homepage (e.g., acmecorp.com)
3. WebFetch: About page (e.g., acmecorp.com/about)
```

**Actions (DEEP)**:
```
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
```

**Expected Time**:
- LIGHT: 2 minutes
- DEEP: 5-8 minutes

---

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

**LIGHT Mode**: Extract from homepage and about page only

**DEEP Mode**: Cross-reference multiple sources, validate data accuracy

---

### Step 3: ICP (Ideal Customer Profile) Identification

#### LIGHT Mode Approach

**Goal**: Identify 1-2 primary customer types

**Data Sources**:
- "Who we serve" section on website
- Customer testimonials on homepage
- About page target market description

**Output Format**:
```json
{
  "icp_profiles": [
    {
      "persona_name": "Head of Support",
      "role": "Head of Customer Support",
      "company_size": "50-500 employees",
      "industry": "SaaS",
      "top_pain_points": [
        "High ticket volume",
        "Slow response times"
      ]
    }
  ]
}
```

**Time**: 1-2 minutes

---

#### DEEP Mode Approach

**Goal**: Identify 3-5 detailed customer personas with psychographics

**Data Sources**:
- Customer testimonials (extract job titles, company info)
- Case studies (identify patterns in customer profiles)
- Review sites (G2, Capterra - what types of companies review them?)
- LinkedIn analysis (optional - who follows them?)

**Output Format**:
```json
{
  "icp_profiles": [
    {
      "persona_name": "Head of Support (SMB SaaS)",
      "demographics": {
        "role": "Head of Customer Support",
        "seniority": "Director level",
        "company_size": "50-500 employees",
        "industry_verticals": ["SaaS", "E-commerce"],
        "company_stage": "Growth stage (Series A-C)"
      },
      "psychographics": {
        "goals": [
          "Reduce cost per ticket by 30%",
          "Improve CSAT from 3.5 to 4.5",
          "Scale support without hiring"
        ],
        "pain_points": [
          "Ticket volume growing 20% month-over-month",
          "Agents overwhelmed, high burnout",
          "Inconsistent support quality across team",
          "Lack of visibility into support metrics"
        ],
        "buying_triggers": [
          "Ticket backlog exceeds 3 days",
          "Customer churn increases",
          "Support costs exceed revenue growth"
        ],
        "decision_criteria": [
          "ROI within 6 months",
          "Easy implementation (< 2 weeks)",
          "Integrates with existing tools",
          "Pricing transparency"
        ]
      },
      "buyer_journey": {
        "awareness": "Realizes support is bottleneck to growth",
        "consideration": "Evaluating AI automation vs hiring",
        "decision": "Comparing 3-5 vendor solutions",
        "retention": "Looking for advanced features, analytics"
      },
      "content_preferences": {
        "formats": ["Case studies with ROI data", "Product demos", "Free trials"],
        "depth": "Tactical how-to guides",
        "channels": ["LinkedIn", "Industry blogs", "Peer recommendations"]
      }
    }
  ]
}
```

**Time**: 8-12 minutes

**Analysis Techniques**:
1. **Pattern Recognition**: Look for repeated job titles in testimonials
2. **Problem Clustering**: Group similar pain points across customers
3. **Company Profile Analysis**: Identify common company sizes/types
4. **Buying Signal Detection**: What triggers them to purchase?

---

### Step 4: Geography & Market Analysis

#### LIGHT Mode

**Data to Extract**:
- Primary headquarters location
- Primary market (US, Global, Europe, etc.)
- Languages supported (from website footer or pricing page)

**Output**:
```json
{
  "geographies": {
    "headquarters": "San Francisco, CA",
    "primary_market": "United States",
    "languages": ["English"]
  }
}
```

**Time**: 1 minute

---

#### DEEP Mode

**Data to Extract**:
- All operating regions
- Revenue breakdown by geography (if available)
- Market maturity by region
- Localization strategy
- Regional competitors

**Research Steps**:
1. WebSearch: "[company] international expansion"
2. WebSearch: "[company] European customers" (or other regions)
3. Check website for language selectors
4. Review case studies for customer locations
5. Check pricing page for currency options

**Output**:
```json
{
  "geographies": {
    "headquarters": "San Francisco, CA",
    "regions": [
      {
        "region": "North America",
        "countries": ["United States", "Canada"],
        "revenue_estimate": "85% of total",
        "market_maturity": "Primary market",
        "languages": ["English"],
        "local_competitors": ["Zendesk", "Intercom"]
      },
      {
        "region": "Europe",
        "countries": ["UK", "Germany", "France"],
        "revenue_estimate": "12% of total",
        "market_maturity": "Growing",
        "languages": ["English", "German", "French"],
        "local_competitors": ["Freshdesk EU", "Local providers"]
      }
    ]
  }
}
```

**Time**: 3-5 minutes

---

### Step 5: Service & Product Mapping

#### LIGHT Mode

**Goal**: List core services/products

**Data Sources**:
- Homepage value propositions
- Features page headlines
- Pricing page tier names

**Output**:
```json
{
  "services": [
    {
      "name": "AI Ticket Routing",
      "category": "Core",
      "description": "Automatically routes tickets to right agent"
    },
    {
      "name": "Response Suggestions",
      "category": "Core",
      "description": "AI-powered response recommendations"
    }
  ]
}
```

**Time**: 2 minutes

---

#### DEEP Mode

**Goal**: Comprehensive service taxonomy with differentiators

**Data Sources**:
- Features page (full analysis)
- Pricing page (feature mapping to tiers)
- Product docs or help center
- Competitor comparison pages
- Case studies (which features do customers mention?)

**Output**:
```json
{
  "services": [
    {
      "name": "AI-Powered Ticket Routing",
      "category": "Core",
      "description": "Machine learning routes tickets to most qualified agent based on content, urgency, and agent expertise",
      "pain_points_addressed": [
        "Tickets routed to wrong department (delays)",
        "VIP customers not prioritized",
        "Routing based on round-robin vs skill match"
      ],
      "benefits": [
        "40% faster first response time",
        "85% first-contact resolution",
        "Reduced agent frustration"
      ],
      "differentiators": [
        "Learns from 1M+ historical tickets vs rule-based",
        "Understands context beyond keywords",
        "Auto-escalates critical issues"
      ],
      "pricing_tier": "Available in Basic tier and up",
      "customer_evidence": "Mentioned in 8/10 case studies",
      "competitive_comparison": "More accurate than Zendesk's routing (per customer reviews)"
    }
  ]
}
```

**Time**: 5-8 minutes

**Analysis Method**:
1. List all features from features page
2. Map features to pricing tiers
3. Identify which features are unique (differentiators)
4. Cross-reference with customer testimonials
5. Compare to competitor feature sets (if available)

---

### Step 6: Pain Points & Value Proposition Mapping

#### LIGHT Mode

**Goal**: Identify top 3-5 pain points

**Data Sources**:
- Homepage hero copy ("Are you struggling with X?")
- Problem/solution sections
- Customer testimonials

**Output**:
```json
{
  "pain_points": [
    {
      "pain_point": "High ticket volume overwhelming team",
      "severity": "High",
      "evidence": "Mentioned in homepage hero"
    }
  ]
}
```

**Time**: 1-2 minutes

---

#### DEEP Mode

**Goal**: Hierarchical pain point mapping with evidence

**Data Sources**:
- All website copy mentioning problems
- Customer testimonials (before/after states)
- Case studies (what problems did they solve?)
- Review sites (common complaints about alternatives)

**Output**:
```json
{
  "pain_points_hierarchy": {
    "critical_pain_points": [
      {
        "pain_point": "Ticket volume growing faster than team capacity",
        "severity": "Critical",
        "urgency": "Immediate",
        "impact": "Business-threatening (customer churn)",
        "evidence": [
          "Homepage: '40% month-over-month ticket growth'",
          "Case study: Acme Corp had 3-day backlog before solution",
          "G2 reviews: Common problem driving purchase"
        ],
        "how_product_solves": "AI automation handles 60% of routine tickets",
        "quantified_benefit": "Reduce ticket backlog from 3 days to 4 hours"
      }
    ],
    "high_priority_pain_points": [...],
    "medium_priority_pain_points": [...],
    "low_priority_pain_points": [...]
  },
  "value_propositions": [
    {
      "value_prop": "Reduce support costs by 50% without sacrificing quality",
      "target_persona": "CFO, Head of Support",
      "supporting_evidence": "Average customer saves $120K/year (case studies)",
      "key_metrics": ["50% cost reduction", "40% faster response", "95% CSAT"]
    }
  ]
}
```

**Time**: 6-10 minutes

**Analysis Framework**:
1. **Jobs-to-be-Done**: What job is customer hiring this product to do?
2. **Pain Severity Matrix**: Map urgency vs impact
3. **Evidence Strength**: How many sources mention this pain?
4. **Solution Fit**: How directly does product address pain?

---

### Step 7: Brand Positioning & Competitive Context

#### LIGHT Mode (Skip for LIGHT)

Not included in LIGHT mode.

---

#### DEEP Mode Only

**Goal**: Understand how company positions itself vs competitors

**Data Sources**:
- Homepage messaging
- About page mission/vision
- Competitor comparison pages on website
- Review sites (how are they rated vs competitors?)

**Research Steps**:
1. WebSearch: "[company] vs [competitor1] vs [competitor2]"
2. WebFetch: Company's comparison page (if exists)
3. WebSearch: site:g2.com "[company]" vs "[competitor]"
4. Analyze tone, messaging, brand personality

**Output**:
```json
{
  "brand_positioning": {
    "positioning_statement": "AI-first customer support automation for fast-growing SaaS companies who need enterprise quality without enterprise prices",
    "key_differentiators": [
      "40% faster implementation than Zendesk",
      "Fraction of enterprise platform cost",
      "Built specifically for SaaS (not generic support)"
    ],
    "brand_personality": ["Approachable", "Data-driven", "Fast-moving"],
    "messaging_themes": [
      "ROI focus (quantified benefits)",
      "Speed (fast setup, fast results)",
      "Simplicity (vs complex enterprise tools)"
    ]
  },
  "competitive_positioning": {
    "primary_competitors": ["Zendesk", "Intercom", "Freshdesk"],
    "positioning_vs_competition": {
      "vs_zendesk": "Faster, cheaper, SaaS-specific (vs generic enterprise)",
      "vs_intercom": "Better AI, lower cost (vs marketing-focused)",
      "vs_freshdesk": "Superior AI, modern UX (vs legacy platform)"
    },
    "target_switch_customers": "Zendesk customers frustrated with cost/complexity"
  }
}
```

**Time**: 5-7 minutes

---

## Step 8: Data Synthesis & Output

**Goal**: Combine all research into structured JSON output

**Output Files**:

### LIGHT Mode Output
**File**: `/data/geo/company-value-{company_name}-light.json`

```json
{
  "execution_mode": "LIGHT",
  "company_overview": { ... },
  "icp_profiles": [ ... ],  // 1-2 personas
  "geographies": { ... },  // Basic info
  "services": [ ... ],  // List of services
  "pain_points": [ ... ],  // Top 3-5
  "value_propositions": [ ... ],  // 1-2 main value props
  "generated_at": "2024-01-15T10:30:00Z",
  "time_taken_seconds": 420
}
```

**Time**: 1 minute (synthesis)
**Total LIGHT Time**: 5-10 minutes

---

### DEEP Mode Output
**File**: `/data/geo/company-value-{company_name}-deep.json`

```json
{
  "execution_mode": "DEEP",
  "company_overview": { ... },  // Comprehensive
  "icp_profiles": [ ... ],  // 3-5 detailed personas
  "geographies": { ... },  // Regional breakdown
  "services": [ ... ],  // Full feature mapping
  "pain_points_hierarchy": { ... },  // Categorized pain points
  "value_propositions": [ ... ],  // Multiple value props
  "brand_positioning": { ... },  // Competitive context
  "competitive_positioning": { ... },
  "data_sources": [
    "https://acmecorp.com",
    "https://acmecorp.com/about",
    "https://g2.com/products/acme/reviews",
    ...
  ],
  "generated_at": "2024-01-15T10:30:00Z",
  "time_taken_seconds": 1680
}
```

**Time**: 2-3 minutes (synthesis)
**Total DEEP Time**: 20-30 minutes

---

## Error Handling

**If website is inaccessible**:
- Try WebSearch for cached/archive versions
- Search for press releases, news articles
- Check LinkedIn company page
- Flag as "limited data" in output

**If key data is missing**:
- Mark fields as `null` with `"data_quality": "incomplete"`
- Note in `warnings` array what's missing
- Continue with available data

**Validation**:
- Company name must be identified
- At least 1 ICP profile required
- At least 3 services/pain points for LIGHT
- At least 5 services/pain points for DEEP

---

## Usage Example

**Agent Workflow**:
```
1. Read this skill file for guidance
2. Determine mode (LIGHT or DEEP) based on user request
3. Execute research steps sequentially
4. Use TodoWrite to track progress:
   - [ ] Company overview research
   - [ ] ICP identification
   - [ ] Geography mapping
   - [ ] Service mapping
   - [ ] Pain point analysis
   - [ ] Data synthesis
5. Save JSON output to /data/geo/
6. Provide summary to user
7. Pass data to next skill (prompt-generation.md)
```

---

## Next Skill
Once complete, this data feeds into:
→ **`prompt-generation.md`** to create targeted test prompts

---

## MCP Tools Needed

**Current**: Built-in tools sufficient (WebSearch, WebFetch, Write)

**Future Enhancement** (optional):
- `mcp__GEO__company_enrichment` - Automated company data enrichment from databases
- `mcp__GEO__competitor_discovery` - Automated competitor identification
