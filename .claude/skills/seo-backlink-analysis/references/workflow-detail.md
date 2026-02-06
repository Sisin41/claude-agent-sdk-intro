# SEO Backlink Analysis - Detailed Reference

This file contains detailed link quality scoring, outreach templates, opportunity schemas, and output schemas referenced by the main SKILL.md.

## Link Quality Score Calculation

```
Link Quality Score = (Authority x 0.4) + (Relevance x 0.3) + (Link Type x 0.2) + (Placement x 0.1)

Example:
Authority: 85/100 (Tier 2)
Relevance: 90/100 (HIGH, same industry)
Link Type: 80/100 (Editorial)
Placement: 90/100 (In-content)

Score = (85 x 0.4) + (90 x 0.3) + (80 x 0.2) + (90 x 0.1)
      = 34 + 27 + 16 + 9
      = 86/100 (EXCELLENT link)
```

### Authority Tiers

```
Tier 1 (90-100): Major publications (Forbes, TechCrunch), .edu/.gov domains
Tier 2 (70-89): Industry leaders, established blogs
Tier 3 (40-69): Niche sites, smaller publications
Tier 4 (<40): Low-quality directories, spam sites
```

### Relevance Scoring

```
HIGH relevance x HIGH authority = 10/10 (ideal link)
HIGH relevance x MEDIUM authority = 8/10 (great link)
MEDIUM relevance x HIGH authority = 7/10 (good link)
LOW relevance x ANY authority = 3/10 (weak link)
```

### Link Type Quality

```
Editorial (mentioned naturally in content): BEST
Resource page: GREAT
Guest post: GOOD
Directory listing: OKAY
Forum signature: WEAK
Comment link: WEAK/SPAM
```

### Anchor Text Health

```
Branded ("AcmeCorp"): NATURAL
Exact match keyword ("AI customer support software"): GOOD (if not overused)
Generic ("click here", "website"): WEAK (but natural)
URL (https://acmecorp.com): NATURAL

Healthy distribution: 60-70% branded, 10-15% exact match, 10-15% partial match, 5-10% generic
Red flag: >50% exact match keyword anchor text
```

## Opportunity Prioritization Formula

```
Priority Score = (Authority x Relevance x Success Rate) / Effort

Authority: 0-100 (domain authority estimate)
Relevance: 0-100 (how relevant to your business)
Success Rate: 0-100 (likelihood of obtaining link)
Effort: 1-10 (1=very easy, 10=very hard)
```

### Example Calculations

```
Opportunity 1: List on Capterra
Authority: 80, Relevance: 95, Success Rate: 90, Effort: 2
Score = (80 x 95 x 90) / 2 = 342,000 -> HIGH PRIORITY

Opportunity 2: Guest post on Forbes
Authority: 98, Relevance: 70, Success Rate: 10, Effort: 9
Score = (98 x 70 x 10) / 9 = 7,622 -> LOWER PRIORITY (despite high authority)
```

## Outreach Email Templates

### Template 1: Unlinked Mention

```
Subject: Quick thank you for mentioning [Your Company]!

Hi [Name],

I came across your article "[Article Title]" and wanted to say thanks for mentioning [Your Company]!

I noticed the mention doesn't link back to our site. Would you consider adding a link to [Your URL]? It would help readers who want to learn more about [specific benefit/feature you provide].

Either way, thanks for the shout-out!

Best,
[Your Name]
[Your Title]
[Your Company]
```

### Template 2: Resource Page Inclusion

```
Subject: Resource suggestion for [Page Title]

Hi [Name],

I found your resource page on [topic] and noticed you've included [Competitor A] and [Competitor B].

I wanted to suggest adding [Your Company] ([Your URL]) to your list. We're a [brief description] that helps [target audience] [main benefit].

Here's why it might be a good fit:
- [Unique feature/benefit 1]
- [Unique feature/benefit 2]
- [Social proof - number of customers, awards, etc.]

If you think it's relevant, I'd be honored to be included!

Thanks for curating such a helpful resource.

Best,
[Your Name]
```

### Template 3: Broken Link Replacement

```
Subject: Found a broken link on [Page Title]

Hi [Name],

I was reading your article "[Article Title]" and noticed one of your links is broken:

[Broken URL]

I have a similar resource that might work as a replacement:
[Your URL] - [Brief description of your content]

It covers [topics] and might be helpful for your readers.

Hope this helps! Let me know if you need any other info.

Best,
[Your Name]
```

### Template 4: Guest Post Pitch

```
Subject: Guest post idea: [Specific Topic]

Hi [Name],

I'm a big fan of [Blog Name] - especially your recent post on [specific article].

I'd love to contribute a guest post on [specific topic idea]. Here's a quick outline:

[Article Title]
- [Key point 1]
- [Key point 2]
- [Key point 3]
- [Unique angle or data you'll include]

I've written for [Other Publications] and have [relevant expertise/credentials].

Would this be a good fit for your audience?

Thanks for considering!

Best,
[Your Name]
[Your Title]
[Your Company]
```

## Toxic Link Red Flags

```
1. Very low quality domains
   - Spam directories
   - Link farms
   - Adult content sites
   - Gambling sites (if irrelevant)

2. Suspicious patterns:
   - Hundreds of links from same domain
   - Links from foreign-language sites (if not your market)
   - Links from penalized sites

3. Exact match anchor text overuse:
   - If >50% of backlinks use exact match keywords
   - Can appear manipulative to Google

Research Method:
WebSearch: "{your domain}" spam
WebSearch: "{your domain}" negative SEO
WebSearch: site:{suspicious_domain} {your_domain}
```

## Link Building Opportunity Types

### A. Industry Directories

Common directories to check:
- G2.com
- Capterra.com
- Product Hunt
- AlternativeTo
- SoftwareAdvice
- GetApp
- Crunchbase

For each: check if listed, evaluate authority, verify competitors are listed, determine free vs paid, assign priority.

### B. Resource Pages

Search queries:
```
"best {category} tools"
"{category} resources"
inurl:resources {industry}
intitle:resources {niche}
```

For each, WebFetch to check: curated list?, high quality site?, recently updated?, competitors listed?, contact info available?

### C. Guest Post Opportunities

Search queries:
```
"{industry} guest post"
"{niche} write for us"
"{industry} contribute"
inurl:write-for-us {industry}
```

Extract: submission guidelines, topic preferences, dofollow link policy, authority estimate, audience relevance.

### D. Broken Link Building

```
Strategy:
1. Find resource pages in your industry
2. Check for broken links
3. If broken link found:
   - Create similar/better content
   - Outreach: "Found broken link, have replacement resource"
```

### E. Unlinked Brand Mentions

```
WebSearch: "{company name}" -site:{your_domain}
WebSearch: "{product name}" -site:{your_domain}
WebSearch: "{CEO name}" "{company}"

For each: WebFetch to check if link exists
If no link -> outreach opportunity
```

### F. HARO / PR Opportunities

Platforms:
- HARO (Help A Reporter Out)
- SourceBottle
- JournoRequests (Twitter)

Action: Sign up, respond to relevant journalist queries, provide expert quotes, earn editorial links.

### G. Podcast & Interview Opportunities

For each podcast, check: audience size/relevance, link in show notes (SEO value), authority of podcast website. Pitch unique expertise and specific topic ideas.

## Output Schemas

### Light Mode Output

File: `/data/seo/backlink-analysis-{site}-quick.json`

```json
{
  "metadata": {
    "mode": "QUICK",
    "site": "acmecorp.com",
    "competitors_analyzed": 2,
    "opportunities_identified": 12,
    "generated_at": "2024-01-15T15:00:00Z"
  },
  "current_profile_estimate": {
    "referring_domains_found": 45,
    "high_quality_links": 12,
    "average_link_quality": 62,
    "notable_backlinks": [
      {
        "source": "techcrunch.com",
        "quality_score": 92,
        "type": "editorial"
      },
      {
        "source": "producthunt.com",
        "quality_score": 75,
        "type": "directory"
      }
    ]
  },
  "competitor_comparison": {
    "your_estimated_domains": 45,
    "competitor_avg_domains": 150,
    "gap": "Competitors have 3x more backlinks",
    "key_differences": [
      "Competitors more active with guest posting",
      "Competitors featured in more publications",
      "Competitors listed in more directories"
    ]
  },
  "top_5_opportunities": [
    {
      "rank": 1,
      "type": "directory_listing",
      "target": "Capterra.com",
      "authority": 80,
      "effort": "low",
      "time_estimate": "30 minutes",
      "success_rate": "90%",
      "action": "Submit company listing at capterra.com/submit",
      "priority_score": 342000
    },
    {
      "rank": 2,
      "type": "directory_listing",
      "target": "G2.com",
      "authority": 85,
      "effort": "low",
      "time_estimate": "45 minutes",
      "success_rate": "85%",
      "action": "Create company profile and request reviews",
      "priority_score": 320000
    },
    {
      "rank": 3,
      "type": "unlinked_mention",
      "target": "saas-industry-blog.com/article",
      "authority": 60,
      "effort": "low",
      "time_estimate": "15 minutes",
      "success_rate": "70%",
      "action": "Email author requesting link addition",
      "priority_score": 180000
    },
    {
      "rank": 4,
      "type": "resource_page",
      "target": "best-customer-support-tools.com",
      "authority": 65,
      "effort": "medium",
      "time_estimate": "1 hour",
      "success_rate": "50%",
      "action": "Outreach to request inclusion in tools list",
      "priority_score": 95000
    },
    {
      "rank": 5,
      "type": "guest_post",
      "target": "customer-experience-blog.com",
      "authority": 70,
      "effort": "medium",
      "time_estimate": "5 hours",
      "success_rate": "60%",
      "action": "Pitch guest post: 'How AI Reduces Support Costs by 50%'",
      "priority_score": 120000
    }
  ],
  "quick_action_plan": {
    "week_1": [
      "Submit to Capterra (30 min)",
      "Submit to G2 (45 min)",
      "Outreach to unlinked mention (15 min)",
      "Total: ~1.5 hours, Expected: 2-3 new high-quality links"
    ],
    "week_2": [
      "Resource page outreach (5 targets, 1 hour each)",
      "Expected: 1-2 new links"
    ]
  }
}
```

### Deep Mode Output

File: `/data/seo/backlink-analysis-{site}-comprehensive.json`

```json
{
  "metadata": {
    "mode": "COMPREHENSIVE",
    "site": "acmecorp.com",
    "competitors_analyzed": 4,
    "opportunities_identified": 45,
    "generated_at": "2024-01-15T15:00:00Z",
    "analysis_duration_minutes": 28
  },
  "current_backlink_profile": {
    "estimated_metrics": {
      "referring_domains": 45,
      "total_backlinks": 120,
      "dofollow_links": 85,
      "nofollow_links": 35
    },
    "quality_breakdown": {
      "excellent_links": 8,
      "good_links": 18,
      "average_links": 14,
      "weak_links": 5,
      "toxic_links": 0
    },
    "link_type_breakdown": {
      "editorial": 12,
      "directory": 18,
      "guest_post": 5,
      "social_profile": 8,
      "other": 2
    },
    "top_10_backlinks": [
      {
        "source_domain": "techcrunch.com",
        "source_url": "https://techcrunch.com/ai-startups-2024",
        "authority": 95,
        "quality_score": 92,
        "type": "editorial",
        "anchor_text": "AcmeCorp",
        "link_status": "dofollow",
        "value": "Extremely high - major publication + editorial mention"
      }
    ],
    "anchor_text_distribution": {
      "branded": "65%",
      "exact_match": "15%",
      "partial_match": "12%",
      "generic": "8%",
      "health": "Good - natural distribution"
    }
  },
  "competitor_analysis": {
    "competitors": [
      {
        "domain": "competitor-a.com",
        "estimated_referring_domains": 280,
        "estimated_backlinks": 850,
        "average_link_quality": 71,
        "top_link_sources": [
          "forbes.com (editorial)",
          "venturebeat.com (editorial)",
          "industry-resource-hub.com (resource page)"
        ],
        "link_building_strategies": [
          "Very active PR/media outreach",
          "Regular guest posting (8+ posts/month)",
          "Comprehensive directory coverage",
          "Podcast circuit (5+ appearances)"
        ]
      }
    ],
    "competitive_gaps": {
      "referring_domains_gap": "Competitors have 4-6x more referring domains",
      "quality_gap": "Competitor links are +6-9 points higher quality on average",
      "strategy_gaps": [
        "Lack PR/media coverage (competitors have 15+ major publications)",
        "Guest posting inactive (competitors publish 8-10/month)",
        "Podcast presence minimal (competitors on 5+ shows)",
        "Directory coverage incomplete (missing 12 major directories)"
      ]
    }
  },
  "link_gaps": {
    "total_gaps": 67,
    "high_priority_gaps": 23,
    "gap_categories": {
      "directory_gaps": [
        {
          "directory": "capterra.com",
          "competitors_present": 4,
          "authority": 80,
          "difficulty": "easy",
          "action": "Submit listing"
        }
      ],
      "editorial_gaps": [
        {
          "publication": "venturebeat.com",
          "competitors_featured": 3,
          "authority": 90,
          "difficulty": "hard",
          "action": "Pitch product launch or funding news"
        }
      ],
      "resource_page_gaps": [
        {
          "page": "best-ai-tools.com/customer-support",
          "competitors_listed": 4,
          "authority": 65,
          "difficulty": "medium",
          "action": "Outreach for inclusion"
        }
      ]
    }
  },
  "opportunities": {
    "total_opportunities": 45,
    "quick_wins": [
      {
        "type": "directory_listing",
        "targets": ["Capterra", "G2", "GetApp", "SoftwareAdvice"],
        "count": 4,
        "total_time": "3 hours",
        "expected_links": 3,
        "priority": "HIGH"
      }
    ],
    "medium_effort": [
      {
        "type": "resource_pages",
        "target_count": 15,
        "total_time": "12 hours",
        "expected_links": 5,
        "priority": "MEDIUM"
      }
    ],
    "long_term": [
      {
        "type": "PR_coverage",
        "target_count": 5,
        "total_time": "20+ hours",
        "expected_links": 2,
        "priority": "LOW"
      }
    ]
  },
  "toxic_links": {
    "count": 0,
    "note": "Limited analysis without backlink tool access. Recommend full audit with Ahrefs/Moz/GSC.",
    "suspicious_patterns": []
  },
  "outreach_plan": {
    "campaigns": [
      {
        "name": "Directory Submissions Blitz",
        "timeline": "Week 1-2",
        "targets": 10,
        "effort": "5 hours",
        "expected_success": "80%",
        "expected_links": 8,
        "roi": "Very High (low effort, high success)"
      },
      {
        "name": "Unlinked Mention Outreach",
        "timeline": "Week 1",
        "targets": 5,
        "effort": "2 hours",
        "expected_success": "60%",
        "expected_links": 3,
        "roi": "High"
      },
      {
        "name": "Resource Page Campaign",
        "timeline": "Month 1-2",
        "targets": 20,
        "effort": "15 hours",
        "expected_success": "30%",
        "expected_links": 6,
        "roi": "Medium"
      },
      {
        "name": "Guest Post Initiative",
        "timeline": "Month 2-3",
        "targets": 12,
        "effort": "60 hours",
        "expected_success": "50%",
        "expected_links": 6,
        "roi": "Medium (high effort but quality links)"
      },
      {
        "name": "HARO/PR Opportunities",
        "timeline": "Ongoing",
        "targets": "Variable",
        "effort": "2 hours/week",
        "expected_success": "20%",
        "expected_links": "1-2/month",
        "roi": "High (when successful - major publications)"
      }
    ],
    "outreach_templates_included": 4,
    "tracking_spreadsheet_recommended": true
  },
  "implementation_roadmap": {
    "month_1": {
      "focus": "Quick wins - directories and unlinked mentions",
      "tasks": [
        "Submit to 10 major directories (5 hours)",
        "Outreach to 5 unlinked mentions (2 hours)",
        "Research 20 resource pages for Month 2 (3 hours)",
        "Set up HARO account and start monitoring (1 hour)"
      ],
      "expected_new_links": "10-12",
      "time_investment": "11 hours"
    },
    "month_2": {
      "focus": "Resource page outreach + guest post prep",
      "tasks": [
        "Resource page outreach (20 targets, 15 hours)",
        "Pitch 10 guest posts (5 hours)",
        "Write 3-4 guest posts (20 hours)",
        "Continue HARO responses (8 hours)"
      ],
      "expected_new_links": "8-10",
      "time_investment": "48 hours"
    },
    "month_3": {
      "focus": "Guest post publishing + PR push",
      "tasks": [
        "Publish guest posts (4-6 articles)",
        "Pitch product news to tech publications (10 hours)",
        "Second round resource page outreach (10 hours)",
        "Podcast pitching (5 hours)"
      ],
      "expected_new_links": "10-15",
      "time_investment": "25 hours"
    },
    "ongoing": {
      "tasks": [
        "HARO responses (2 hours/week)",
        "Monthly guest post (5 hours/month)",
        "Monitor new unlinked mentions (1 hour/week)",
        "Quarterly directory updates"
      ]
    }
  },
  "estimated_results": {
    "3_month_projection": {
      "new_referring_domains": "25-35",
      "total_referring_domains": "70-80 (from current 45)",
      "improvement": "55-78% increase",
      "domain_authority_impact": "+3-5 points (estimated)",
      "ranking_impact": "2-5 position improvements for competitive keywords"
    },
    "6_month_projection": {
      "new_referring_domains": "50-70",
      "total_referring_domains": "95-115",
      "improvement": "111-155% increase",
      "domain_authority_impact": "+5-8 points",
      "ranking_impact": "5-10 position improvements"
    }
  }
}
```
