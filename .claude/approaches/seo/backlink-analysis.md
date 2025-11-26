# SEO Backlink Analysis

## Purpose
Analyze website backlink profile, identify link building opportunities, assess competitor link strategies, and provide actionable outreach recommendations to improve domain authority and search rankings.

---

## Execution Modes

### QUICK Mode (5-10 minutes)
**Goal**: Backlink health check and top 5 link opportunities
**Scope**: Basic profile assessment + quick wins
**Output**: Priority link building actions with outreach targets

### COMPREHENSIVE Mode (20-30 minutes)
**Goal**: Full backlink audit with competitive analysis
**Scope**: Complete profile + competitor analysis + 20-30 opportunities
**Output**: Detailed link building strategy with outreach templates

---

## Prerequisites

**Required Input**:
- Website URL/domain
- Industry/niche

**Optional**:
- Competitor domains (for comparison)
- Target keywords (from keyword-research.md)
- Existing backlink data (if available from tools like Ahrefs, Moz, SEMrush)

**Note**: This skill uses **research-based methods** since we don't have direct access to backlink databases. For comprehensive backlink data, users should combine this analysis with dedicated SEO tools.

---

## Backlink Analysis Categories

### 1. Backlink Profile Assessment
### 2. Link Quality Evaluation
### 3. Competitor Backlink Analysis
### 4. Link Gap Identification
### 5. Link Building Opportunities
### 6. Toxic Link Detection
### 7. Outreach Strategy

---

## Workflow Steps

### Step 1: Backlink Profile Discovery

**Note**: Without access to backlink tools (Ahrefs, Moz, SEMrush), we use research methods to estimate backlink profile.

#### Method 1: Search-Based Discovery

```
WebSearch: link:{domain}

This Google operator shows pages linking to the domain.
Limitations: Only shows sample of links, not comprehensive

WebSearch: "{domain}" -site:{domain}

Shows mentions of the domain across the web (potential link opportunities)

WebSearch: site:{domain} "backlinks" OR "domain authority" OR "referring domains"

Find if site has published their own backlink data
```

#### Method 2: Competitive Intelligence

```
WebSearch: {domain} backlink profile
WebSearch: {domain} domain authority
WebSearch: {domain} referring domains

Look for:
- Published case studies mentioning backlinks
- SEO tool screenshots
- Third-party analyses
- Industry reports
```

#### Method 3: Common Link Sources

```
Check common backlink sources:

1. Company listings:
   - Crunchbase: crunchbase.com/organization/{company}
   - Product Hunt: producthunt.com
   - G2: g2.com
   - Capterra: capterra.com

2. Social profiles:
   - LinkedIn company page
   - Twitter profile
   - Facebook page
   - GitHub organization

3. Industry directories:
   WebSearch: "{industry} directory"
   WebSearch: "{niche} companies list"

4. News mentions:
   WebSearch: site:techcrunch.com {company}
   WebSearch: site:venturebeat.com {company}

5. Guest posts:
   WebSearch: "guest post" OR "contributed by" {company representative name}
```

**Output**: Estimated backlink profile

```json
{
  "estimated_metrics": {
    "referring_domains_found": 45,
    "total_backlinks_identified": 120,
    "quality_breakdown": {
      "high_authority": 12,
      "medium_authority": 28,
      "low_authority": 5
    }
  },
  "top_backlinks": [
    {
      "source_domain": "techcrunch.com",
      "source_url": "https://techcrunch.com/article-about-company",
      "authority_estimate": "very_high",
      "link_type": "editorial",
      "context": "Featured in article about AI startups"
    }
  ]
}
```

---

### Step 2: Link Quality Assessment

**For Each Backlink Found**:

```
Evaluate Link Quality:

1. Domain Authority (estimate):
   WebSearch: {source_domain} domain authority

   Indicators of high authority:
   - Major publications (TechCrunch, Forbes, etc.)
   - .edu or .gov domains
   - Well-known industry sites
   - High Google ranking for competitive terms

   Authority Tiers:
   - Tier 1 (90-100): Major publications, .edu/.gov
   - Tier 2 (70-89): Industry leaders, established blogs
   - Tier 3 (40-69): Niche sites, smaller publications
   - Tier 4 (<40): Low-quality directories, spam sites

2. Relevance:
   - Same industry? (HIGH relevance)
   - Related industry? (MEDIUM relevance)
   - Unrelated? (LOW relevance)

   Relevance Score:
   HIGH × HIGH_AUTHORITY = 10/10 (ideal link)
   HIGH × MEDIUM_AUTHORITY = 8/10 (great link)
   MEDIUM × HIGH_AUTHORITY = 7/10 (good link)
   LOW × ANY_AUTHORITY = 3/10 (weak link)

3. Link Type:
   - Editorial (mentioned naturally in content): BEST
   - Resource page: GREAT
   - Guest post: GOOD
   - Directory listing: OKAY
   - Forum signature: WEAK
   - Comment link: WEAK/SPAM

4. Link Placement:
   - In-content link: BEST
   - Sidebar: OKAY
   - Footer: WEAK
   - Author bio: OKAY

5. Anchor Text:
   WebFetch: {source_url}

   Check anchor text:
   - Branded ("AcmeCorp"): NATURAL
   - Exact match keyword ("AI customer support software"): GOOD (if not overused)
   - Generic ("click here", "website"): WEAK (but natural)
   - URL (https://acmecorp.com): NATURAL

6. Follow vs NoFollow:
   Check if link has rel="nofollow"
   - Dofollow: PASSES LINK EQUITY (better for SEO)
   - Nofollow: NO LINK EQUITY (still valuable for traffic)
```

**Link Quality Score Formula**:

```
Link Quality Score = (Authority × 0.4) + (Relevance × 0.3) + (Link Type × 0.2) + (Placement × 0.1)

Example:
Authority: 85/100 (Tier 2)
Relevance: 90/100 (HIGH, same industry)
Link Type: 80/100 (Editorial)
Placement: 90/100 (In-content)

Score = (85 × 0.4) + (90 × 0.3) + (80 × 0.2) + (90 × 0.1)
      = 34 + 27 + 16 + 9
      = 86/100 (EXCELLENT link)
```

**Categorize Links**:

```json
{
  "link_quality_breakdown": {
    "excellent_links": [
      {
        "source": "techcrunch.com",
        "quality_score": 92,
        "value": "Very high authority + relevant + editorial"
      }
    ],
    "good_links": [ ... ],
    "average_links": [ ... ],
    "weak_links": [ ... ],
    "toxic_links": [
      {
        "source": "spam-directory.xyz",
        "quality_score": 5,
        "issues": ["Very low authority", "Spammy site", "Irrelevant"],
        "recommendation": "Consider disavowing"
      }
    ]
  }
}
```

---

### Step 3: Competitor Backlink Analysis

**QUICK Mode**: Analyze 1-2 competitors
**COMPREHENSIVE Mode**: Analyze 3-5 competitors

**For Each Competitor**:

```
1. Identify Competitor Backlinks:

   WebSearch: link:{competitor_domain}
   WebSearch: "{competitor_domain}" -site:{competitor_domain}

   Check same sources as Step 1:
   - Industry directories
   - News sites
   - Resource pages
   - Guest post platforms

2. Find Their Best Links:

   WebSearch: {competitor_domain} featured
   WebSearch: {competitor_domain} mentioned
   WebSearch: site:techcrunch.com {competitor_name}
   WebSearch: site:forbes.com {competitor_name}

3. Identify Patterns:

   Common link sources across competitors:
   - Which directories are they listed in?
   - Which publications feature them?
   - Which resource pages link to them?
   - What guest post platforms do they use?

4. Estimate Their Profile:

   {
     "competitor": "competitor-a.com",
     "estimated_referring_domains": 180,
     "top_backlinks_identified": [
       {
         "source": "forbes.com",
         "type": "editorial_mention",
         "context": "Featured in top 10 AI companies list"
       },
       {
         "source": "industry-blog.com",
         "type": "guest_post",
         "context": "CEO wrote guest post about AI trends"
       }
     ],
     "link_building_strategies_observed": [
       "Active guest posting on industry blogs",
       "Listed in major directories (G2, Capterra, Product Hunt)",
       "Press coverage strategy (multiple news mentions)",
       "Resource page targeting (linked from 'best tools' lists)"
     ]
   }
```

**Competitive Comparison**:

```json
{
  "backlink_comparison": {
    "your_site": {
      "estimated_referring_domains": 45,
      "high_quality_links": 12,
      "average_link_quality": 62
    },
    "competitor_a": {
      "estimated_referring_domains": 180,
      "high_quality_links": 45,
      "average_link_quality": 71
    },
    "competitor_b": {
      "estimated_referring_domains": 120,
      "high_quality_links": 30,
      "average_link_quality": 68
    },
    "gap_analysis": {
      "referring_domains_gap": "Competitors have 3-4x more referring domains",
      "quality_gap": "Competitors have higher average link quality (+6-9 points)",
      "strategic_gaps": [
        "Competitors actively publish guest posts (you don't)",
        "Competitors featured in major publications (you have limited coverage)",
        "Competitors listed in more directories"
      ]
    }
  }
}
```

---

### Step 4: Link Gap Identification

**Find Links Competitors Have That You Don't**:

```
For each competitor backlink source:
  Check if you're also linked from that source

  If NO → Link gap opportunity!

Example Analysis:

Competitor A linked from:
1. G2.com ✓ (You have this)
2. Capterra.com ✗ (You DON'T have this) → OPPORTUNITY
3. TechCrunch.com ✗ (You DON'T have this) → OPPORTUNITY
4. Industry-resource-page.com ✗ (You DON'T have this) → OPPORTUNITY

Prioritize gaps by:
- Authority of linking site (high authority = high priority)
- Relevance to your business
- Difficulty to obtain (easy wins first)
```

**Link Gap Categories**:

```json
{
  "link_gaps": {
    "directory_gaps": [
      {
        "directory": "capterra.com",
        "competitors_listed": ["competitor-a", "competitor-b"],
        "authority": "high",
        "difficulty": "easy",
        "priority": "HIGH",
        "action": "Submit company listing"
      }
    ],
    "editorial_gaps": [
      {
        "publication": "techcrunch.com",
        "competitors_mentioned": ["competitor-a"],
        "authority": "very_high",
        "difficulty": "hard",
        "priority": "MEDIUM",
        "action": "Pitch newsworthy story or product launch"
      }
    ],
    "guest_post_gaps": [
      {
        "blog": "industry-insights-blog.com",
        "competitors_published": ["competitor-b"],
        "authority": "medium",
        "difficulty": "medium",
        "priority": "HIGH",
        "action": "Pitch guest post topic"
      }
    ],
    "resource_page_gaps": [
      {
        "resource_page": "best-ai-tools.com/customer-support",
        "competitors_listed": ["competitor-a", "competitor-b"],
        "authority": "medium",
        "difficulty": "easy",
        "priority": "HIGH",
        "action": "Request inclusion in list"
      }
    ]
  }
}
```

---

### Step 5: Link Building Opportunity Discovery

**Identify New Link Opportunities** (beyond competitor gaps):

#### A. Industry Directories

```
WebSearch: "{industry} software directory"
WebSearch: "{niche} companies list"
WebSearch: "submit your {industry} company"

Common Directories:
- G2.com
- Capterra.com
- Product Hunt
- AlternativeTo
- SoftwareAdvice
- GetApp
- Crunchbase

For Each Directory:
  1. Check if already listed
  2. Evaluate authority
  3. Check if competitors are listed (validation)
  4. Determine effort (free listing vs paid)
  5. Priority score
```

#### B. Resource Pages

```
WebSearch: "best {category} tools"
WebSearch: "{category} resources"
WebSearch: inurl:resources {industry}
WebSearch: intitle:resources {niche}

Example Queries:
- "best AI customer support tools"
- "customer support software resources"
- inurl:resources customer support
- intitle:resources SaaS tools

For Each Resource Page:
  WebFetch: {resource_page_url}

  Check:
  - Is it a curated list? (GOOD)
  - High quality site? (Check domain authority estimate)
  - Recently updated? (Active = better chance)
  - Competitors listed? (Validation that you belong)
  - Contact info for submissions? (Easy outreach)
```

#### C. Guest Post Opportunities

```
WebSearch: "{industry} guest post"
WebSearch: "{niche} write for us"
WebSearch: "{industry} contribute"
WebSearch: inurl:write-for-us {industry}

Example Queries:
- "SaaS guest post"
- "customer support write for us"
- "AI industry contribute"

For Each Blog:
  WebFetch: {write_for_us_page}

  Extract:
  - Submission guidelines
  - Topic preferences
  - Author benefits (dofollow link?)
  - Domain authority estimate
  - Audience relevance
```

#### D. Broken Link Building

```
WebSearch: "{industry} resources" + "404"
WebSearch: "{competitor with broken site}" + "recommended"

Strategy:
1. Find resource pages in your industry
2. Check for broken links (tools or manual check)
3. If broken link found:
   - Create similar/better content
   - Reach out: "Hey, found broken link on your page. I have similar resource that might work as replacement."
```

#### E. Unlinked Brand Mentions

```
WebSearch: "{company name}" -site:{your_domain}
WebSearch: "{product name}" -site:{your_domain}
WebSearch: "{CEO name}" "{company}"

Find pages that mention your brand but don't link to you

For each mention:
  WebFetch: {mention_url}
  Check if they link to you

  If NO LINK → Opportunity!
  Outreach: "Thanks for mentioning us! Would you consider adding a link?"
```

#### F. Competitor Replacement

```
WebSearch: "alternatives to {competitor}"
WebSearch: "{competitor} vs"
WebSearch: "better than {competitor}"

Find comparison/alternative pages

Action:
- Reach out to page owner
- Suggest adding your product to comparison
- Provide unique angle/benefit
```

#### G. HARO / PR Opportunities

```
WebSearch: HARO {industry}
WebSearch: "{industry} journalist requests"
WebSearch: help a reporter {niche}

Platforms:
- HARO (Help A Reporter Out)
- SourceBottle
- JournoRequests (Twitter)

Action:
- Sign up for HARO
- Respond to relevant journalist queries
- Provide expert quotes
- Earn editorial links from publications
```

#### H. Podcast & Interview Opportunities

```
WebSearch: "{industry} podcast guests"
WebSearch: "{niche} interview opportunities"
WebSearch: "{industry} expert wanted"

For Each Podcast:
  Check:
  - Audience size and relevance
  - Link in show notes? (SEO value)
  - Authority of podcast website

  Pitch:
  - Your unique expertise
  - Specific topic ideas
  - Past interview experience
```

---

### Step 6: Opportunity Prioritization

**Score Each Opportunity**:

```
Priority Score = (Authority × Relevance × Success Rate) / Effort

Authority: 0-100 (domain authority estimate)
Relevance: 0-100 (how relevant to your business)
Success Rate: 0-100 (likelihood of obtaining link)
Effort: 1-10 (1=very easy, 10=very hard)

Example Calculations:

Opportunity 1: List on Capterra
Authority: 80 (high authority directory)
Relevance: 95 (very relevant to SaaS)
Success Rate: 90 (easy approval process)
Effort: 2 (just fill out form)

Score = (80 × 95 × 90) / 2 = 342,000 → HIGH PRIORITY

Opportunity 2: Guest post on Forbes
Authority: 98 (very high authority)
Relevance: 70 (somewhat relevant)
Success Rate: 10 (very competitive)
Effort: 9 (very difficult)

Score = (98 × 70 × 10) / 9 = 7,622 → LOWER PRIORITY (despite high authority)
```

**Categorize Opportunities**:

```json
{
  "opportunities_by_difficulty": {
    "quick_wins": [
      {
        "type": "directory_listing",
        "target": "Capterra.com",
        "authority": 80,
        "effort": "low",
        "time_estimate": "30 minutes",
        "success_rate": "90%",
        "priority_score": 342000
      },
      {
        "type": "unlinked_mention",
        "target": "industry-blog.com/article",
        "authority": 60,
        "effort": "low",
        "time_estimate": "15 minutes (outreach email)",
        "success_rate": "70%",
        "priority_score": 180000
      }
    ],
    "medium_effort": [
      {
        "type": "resource_page",
        "target": "best-customer-support-tools.com",
        "authority": 65,
        "effort": "medium",
        "time_estimate": "1-2 hours (outreach + follow-up)",
        "success_rate": "50%",
        "priority_score": 95000
      },
      {
        "type": "guest_post",
        "target": "saas-insights-blog.com",
        "authority": 70,
        "effort": "medium",
        "time_estimate": "4-6 hours (write + submit)",
        "success_rate": "60%",
        "priority_score": 120000
      }
    ],
    "high_effort": [
      {
        "type": "editorial_coverage",
        "target": "TechCrunch",
        "authority": 95,
        "effort": "high",
        "time_estimate": "10+ hours (PR campaign)",
        "success_rate": "15%",
        "priority_score": 45000
      }
    ]
  }
}
```

---

### Step 7: Toxic Link Detection

**Identify Potentially Harmful Links**:

```
Red Flags:
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

Research Method (without backlink tools):

WebSearch: "{your domain}" spam
WebSearch: "{your domain}" negative SEO
WebSearch: site:{suspicious_domain} {your_domain}

If you find suspicious links:
{
  "toxic_link": {
    "source": "spam-directory-123.xyz",
    "reason": "Known spam directory, very low quality",
    "recommendation": "Add to Google Disavow file",
    "priority": "HIGH"
  }
}

Note: Toxic link detection is LIMITED without access to full backlink database.
Recommendation: Use Ahrefs, Moz, or Google Search Console for comprehensive toxic link audit.
```

---

### Step 8: Outreach Strategy & Templates

**Create Outreach Plan**:

```json
{
  "outreach_campaigns": [
    {
      "campaign_name": "Directory Submissions",
      "target_count": 10,
      "time_estimate": "5 hours",
      "expected_success_rate": "80%",
      "expected_links": 8,
      "priority": "HIGH",
      "targets": [
        "Capterra.com",
        "G2.com",
        "Product Hunt",
        "AlternativeTo"
      ]
    },
    {
      "campaign_name": "Unlinked Mention Outreach",
      "target_count": 5,
      "time_estimate": "2 hours",
      "expected_success_rate": "60%",
      "expected_links": 3,
      "priority": "HIGH"
    },
    {
      "campaign_name": "Resource Page Outreach",
      "target_count": 15,
      "time_estimate": "8 hours",
      "expected_success_rate": "30%",
      "expected_links": 4,
      "priority": "MEDIUM"
    },
    {
      "campaign_name": "Guest Post Campaign",
      "target_count": 8,
      "time_estimate": "40 hours",
      "expected_success_rate": "40%",
      "expected_links": 3,
      "priority": "MEDIUM"
    }
  ]
}
```

**Outreach Email Templates**:

#### Template 1: Unlinked Mention

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

#### Template 2: Resource Page Inclusion

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

#### Template 3: Broken Link Replacement

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

#### Template 4: Guest Post Pitch

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

---

### Step 9: Output Generation

**QUICK Mode Output** (`/data/seo/backlink-analysis-{site}-quick.json`):

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

**COMPREHENSIVE Mode Output** (`/data/seo/backlink-analysis-{site}-comprehensive.json`):

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
      },
      {
        "domain": "competitor-b.com",
        "estimated_referring_domains": 195,
        "estimated_backlinks": 520,
        "average_link_quality": 68
      }
    ],
    "competitive_gaps": {
      "referring_domains_gap": "Competitors have 4-6x more referring domains",
      "quality_gap": "Competitor links are +6-9 points higher quality on average",
      "strategy_gaps": [
        "You lack PR/media coverage (competitors have 15+ major publications)",
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
      },
      {
        "type": "unlinked_mentions",
        "targets": ["blog-a.com", "blog-b.com", "news-site.com"],
        "count": 3,
        "total_time": "1 hour",
        "expected_links": 2,
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
      },
      {
        "type": "guest_posts",
        "target_count": 10,
        "total_time": "50 hours",
        "expected_links": 6,
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
    ],
    "detailed_opportunities": [
      {
        "id": "opp_001",
        "type": "directory_listing",
        "target": "Capterra.com",
        "target_url": "https://capterra.com/submit",
        "authority": 80,
        "relevance": 95,
        "difficulty": "easy",
        "effort": 2,
        "success_rate": 90,
        "priority_score": 342000,
        "time_estimate": "30 minutes",
        "action_steps": [
          "1. Create account on Capterra",
          "2. Fill out company profile",
          "3. Upload logo and screenshots",
          "4. Submit for review"
        ],
        "outreach_template": "N/A (self-service)",
        "expected_timeline": "Approved within 1-2 weeks"
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

---

## Validation Checks

Before saving output:

1. **Minimum Opportunities**: QUICK ≥10, COMPREHENSIVE ≥40
2. **Competitor Analysis**: At least 2 competitors analyzed
3. **Opportunity Prioritization**: All opportunities have priority scores
4. **Outreach Templates**: At least 3 templates included (COMPREHENSIVE)
5. **Realistic Estimates**: Success rates and time estimates are reasonable
6. **Implementation Roadmap**: Phased approach with clear timelines

---

## Important Limitations

**This skill uses research-based methods, NOT comprehensive backlink tools.**

**Limitations**:
- Cannot see full backlink profile (only sample via search)
- Cannot accurately estimate domain authority without tools
- Cannot detect all toxic links
- Cannot see competitor's full backlink profile

**Recommendations**:
For comprehensive backlink analysis, combine this skill with:
- **Ahrefs** (most comprehensive backlink database)
- **Moz** (domain authority metrics)
- **SEMrush** (backlink auditing)
- **Google Search Console** (your own backlinks + toxic link detection)

**This skill is best used for**:
- Link building opportunity discovery
- Competitor link strategy analysis
- Outreach planning
- Quick backlink health check

---

## Usage Example

**Agent Workflow**:
```
1. Read this skill file
2. Determine mode (QUICK or COMPREHENSIVE)
3. Use TodoWrite to track analysis:
   [ ] Backlink profile discovery
   [ ] Link quality assessment
   [ ] Competitor analysis
   [ ] Link gap identification
   [ ] Opportunity discovery
   [ ] Prioritization
   [ ] Outreach planning
   [ ] Output generation
4. Execute analysis steps
5. Save JSON to /data/seo/
6. Provide summary:
   "Backlink Analysis Complete!

    Current Profile (estimated):
    - 45 referring domains
    - 12 high-quality links
    - Average quality: 62/100

    Competitor Gap:
    - Competitors have 3-4x more backlinks
    - Your quality is -6 to -9 points lower
    - Main gaps: PR coverage, guest posting, directories

    Top 5 Opportunities:
    1. Capterra listing (30 min, 90% success) - QUICK WIN!
    2. G2 listing (45 min, 85% success) - QUICK WIN!
    3. Unlinked mention outreach (15 min, 70% success)
    4. Resource page: best-tools.com (1 hour, 50% success)
    5. Guest post: industry-blog.com (5 hours, 60% success)

    Month 1 Plan: 11 hours → 10-12 new links
    3-Month Projection: +25-35 referring domains (+55-78%)

    Full report: /data/seo/backlink-analysis-acme-comprehensive.json"
```

---

## Integration with Other Skills

**After running this skill**:
- Use opportunities to create content (for guest posts, resource pages)
- Coordinate with **content-optimization.md** (optimize pages before pitching for links)
- Track results over time (re-run monthly to measure progress)

---

## MCP Tools Needed

**Current**: Built-in tools sufficient (WebSearch, WebFetch, Read, Write)

**Future Enhancement** (would require paid API access):
- `mcp__SEO__backlink_checker` - Integration with Ahrefs/Moz API for accurate backlink data
- `mcp__SEO__domain_authority_checker` - Real-time DA/PA metrics
- `mcp__SEO__broken_link_finder` - Automated broken link detection on resource pages
- `mcp__SEO__outreach_tracker` - Track outreach emails, responses, link acquisitions
