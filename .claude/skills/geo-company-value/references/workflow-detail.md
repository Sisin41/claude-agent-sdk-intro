# Company Value Identification - Detailed Reference

This file contains detailed output schemas, examples, and extended data formats referenced by the main SKILL.md.

## ICP Output Schemas

### LIGHT Mode ICP Output

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

### DEEP Mode ICP Output

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

## Geography Output Schemas

### LIGHT Mode Geography Output

```json
{
  "geographies": {
    "headquarters": "San Francisco, CA",
    "primary_market": "United States",
    "languages": ["English"]
  }
}
```

### DEEP Mode Geography Output

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

## Service & Product Output Schemas

### LIGHT Mode Service Output

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

### DEEP Mode Service Output

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

## Pain Points Output Schemas

### LIGHT Mode Pain Points Output

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

### DEEP Mode Pain Points Output

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
    "high_priority_pain_points": [],
    "medium_priority_pain_points": [],
    "low_priority_pain_points": []
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

## Brand Positioning Output Schema (DEEP Only)

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

## Full Output File Examples

### LIGHT Mode Complete Output

**File**: `/data/geo/company-value-{company_name}-light.json`

```json
{
  "execution_mode": "LIGHT",
  "company_overview": {
    "company_name": "Acme Corp",
    "domain": "acmecorp.com",
    "industry": "Customer Support SaaS",
    "tagline": "AI-powered support for growing teams",
    "elevator_pitch": "Acme provides AI-driven customer support automation that helps SaaS companies reduce ticket volume by 60% while improving customer satisfaction."
  },
  "icp_profiles": [],
  "geographies": {},
  "services": [],
  "pain_points": [],
  "value_propositions": [],
  "generated_at": "2024-01-15T10:30:00Z",
  "time_taken_seconds": 420
}
```

### DEEP Mode Complete Output

**File**: `/data/geo/company-value-{company_name}-deep.json`

```json
{
  "execution_mode": "DEEP",
  "company_overview": {},
  "icp_profiles": [],
  "geographies": {},
  "services": [],
  "pain_points_hierarchy": {},
  "value_propositions": [],
  "brand_positioning": {},
  "competitive_positioning": {},
  "data_sources": [
    "https://acmecorp.com",
    "https://acmecorp.com/about",
    "https://g2.com/products/acme/reviews"
  ],
  "generated_at": "2024-01-15T10:30:00Z",
  "time_taken_seconds": 1680
}
```
