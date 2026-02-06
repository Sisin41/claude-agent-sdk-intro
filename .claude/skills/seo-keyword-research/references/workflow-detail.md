# SEO Keyword Research - Detailed Reference

This file contains detailed examples, output schemas, and expansion templates referenced by the main SKILL.md.

## Seed Keyword Examples

Example seed keywords for an AI customer support company:
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

## Keyword Expansion Templates

### Question-Based Keywords
```
- "how to {seed keyword}"
- "what is {seed keyword}"
- "why {seed keyword}"
- "{seed keyword} guide"
- "{seed keyword} tutorial"
```

### Comparison Keywords
```
- "best {seed keyword}"
- "{seed keyword} vs {alternative}"
- "top {seed keyword}"
- "{seed keyword} comparison"
- "{seed keyword} alternatives"
```

### Problem-Solving Keywords
```
- "{problem} solution"
- "fix {problem}"
- "improve {metric}"
- "reduce {negative outcome}"
```

### Long-Tail Variations
```
- "{seed keyword} for {audience}"
- "{seed keyword} for {industry}"
- "{seed keyword} for {company size}"
- "{seed keyword} with {feature}"
```

## Search Volume Estimation Methods

### Method 1: Google Autocomplete Analysis
```
WebSearch: "[keyword]"
- If appears in autocomplete -> HIGH volume (10K+ searches/month)
- If shows related searches -> MEDIUM volume (1K-10K)
- If no suggestions -> LOW volume (<1K)
```

### Method 2: Research Published Data
```
WebSearch: "[keyword] search volume"
WebSearch: "keyword research [industry]"
- Look for blog posts with keyword data
- Check industry reports with search trends
```

### Method 3: Competitive Analysis
```
WebSearch: site:{competitor.com} "[keyword]"
- If competitor has dedicated page -> likely HIGH volume
- If in blog post -> MEDIUM volume
- If not found -> check if they're missing opportunity
```

## Opportunity Score Calculation

```
Opportunity Score = (Search Volume Score x Intent Value) / (Difficulty Score + 1)

Where:
- Search Volume Score: HIGH=3, MEDIUM=2, LOW=1
- Intent Value: Transactional=3, Commercial=2, Informational=1
- Difficulty Score: 0-100 (lower is better)
```

### Example Calculations

```
Keyword: "best AI customer support tools"
- Volume: HIGH (3)
- Intent: Commercial (2)
- Difficulty: 45
- Opportunity = (3 x 2) / (45 + 1) = 6/46 = 0.13

Keyword: "AI customer support tutorial"
- Volume: LOW (1)
- Intent: Informational (1)
- Difficulty: 20
- Opportunity = (1 x 1) / (20 + 1) = 1/21 = 0.05

First keyword is higher opportunity.
```

### Priority Tiers
```
P1 (High Priority): Opportunity Score > 0.10
P2 (Medium Priority): Opportunity Score 0.05-0.10
P3 (Low Priority): Opportunity Score < 0.05
```

## Competitive Gap Categories

```
- Critical Gaps: High-volume keywords, competitor ranks top 3, you don't rank
- Opportunity Gaps: Medium-volume, competitor ranks, but content is weak
- Quick Win Gaps: Low difficulty keywords, easy to create content for
```

## Topic Cluster Architecture

### Pillar Topic Example
```
Pillar: "AI Customer Support"
- Search volume: HIGH
- Intent: Informational
- Content: Comprehensive 3000+ word guide
```

### Supporting Keywords Example
```
Cluster around "AI Customer Support" pillar:
- "AI customer support benefits"
- "AI customer support features"
- "AI customer support implementation"
- "AI customer support ROI"
- "AI customer support best practices"
- "AI customer support challenges"
```

### Internal Linking Map
```
Pillar Page: "Complete Guide to AI Customer Support"
  -> Links to:
  - Cluster Article 1: "10 Benefits of AI Customer Support"
  - Cluster Article 2: "How to Implement AI Support"
  - Cluster Article 3: "Calculating AI Support ROI"
  <- All cluster articles link back to pillar

Typical: 1 Pillar Page -> 5-10 Cluster Articles
```

## Content Recommendation Schema

For each priority keyword:
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

## Output Schemas

### Light Mode Output

File: `/data/seo/keywords-{site}-quick.json`

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

### Deep Mode Output

File: `/data/seo/keywords-{site}-comprehensive.json`

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
