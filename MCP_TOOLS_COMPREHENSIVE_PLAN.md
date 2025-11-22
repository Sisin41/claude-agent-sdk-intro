# MCP Tools Comprehensive Inventory & Development Plan

## Executive Summary

**Total MCP Tools Identified**: 33 tools across 8 categories
**Priority Tiers**:
- **P0 (Critical)**: 2 tools - Block GEO functionality without them
- **P1 (High)**: 8 tools - Major productivity gains, enable key workflows
- **P2 (Medium)**: 12 tools - Nice-to-have enhancements
- **P3 (Low)**: 11 tools - Future optimizations

**Development Timeline**: 16 weeks (4 months) for P0-P1 tools
**Estimated Engineering Effort**: 6-8 engineer-months
**Estimated Cost**: $120K-160K (assuming $50K/month per engineer)

---

## Table of Contents

1. [Complete Tool Inventory](#complete-tool-inventory)
2. [Priority P0 Tools (Critical)](#priority-p0-tools)
3. [Priority P1 Tools (High Value)](#priority-p1-tools)
4. [Priority P2 Tools (Medium Value)](#priority-p2-tools)
5. [Priority P3 Tools (Low Priority)](#priority-p3-tools)
6. [Development Roadmap](#development-roadmap)
7. [Technical Architecture](#technical-architecture)
8. [Resource Requirements](#resource-requirements)
9. [Testing Strategy](#testing-strategy)
10. [Deployment Plan](#deployment-plan)

---

## Complete Tool Inventory

### Category 1: GEO (Generative Engine Optimization) - 2 tools

| Tool ID | Tool Name | Priority | Source Skill | Purpose |
|---------|-----------|----------|--------------|---------|
| GEO-001 | run_multi_engine_test | **P0** | multi-engine-testing.md | Execute 10-100 prompts across ChatGPT/Perplexity/Gemini in parallel |
| GEO-002 | analyze_citations | **P0** | citation-analysis.md | Analyze 100-1000 citations using parallel LLM calls |

### Category 2: SEO - 10 tools

| Tool ID | Tool Name | Priority | Source Skill | Purpose |
|---------|-----------|----------|--------------|---------|
| SEO-001 | keyword_research_api | P1 | keyword-research.md | Fetch search volume, difficulty, CPC from SEO tools |
| SEO-002 | serp_analyzer | P1 | keyword-research.md | Analyze top 10 SERP results for keywords |
| SEO-003 | crawler | P1 | technical-audit.md | Crawl website for technical SEO issues |
| SEO-004 | pagespeed_analyzer | P2 | technical-audit.md | Detailed page speed analysis with recommendations |
| SEO-005 | schema_validator | P2 | technical-audit.md | Validate and suggest schema markup improvements |
| SEO-006 | content_analyzer | P2 | content-optimization.md | Readability, keyword density, content quality scoring |
| SEO-007 | competitor_content_scraper | P2 | content-optimization.md | Automated competitive content analysis at scale |
| SEO-008 | content_gap_identifier | P3 | content-optimization.md | ML-powered content gap detection |
| SEO-009 | backlink_checker | P1 | backlink-analysis.md | Integration with Ahrefs/Moz API for backlink data |
| SEO-010 | domain_authority_checker | P2 | backlink-analysis.md | Real-time DA/PA metrics |
| SEO-011 | broken_link_finder | P3 | backlink-analysis.md | Automated broken link detection on resource pages |
| SEO-012 | outreach_tracker | P3 | backlink-analysis.md | Track outreach emails, responses, link acquisitions |

### Category 3: Ads Analytics - 7 tools

| Tool ID | Tool Name | Priority | Source Skill | Purpose |
|---------|-----------|----------|--------------|---------|
| ADS-001 | google_ads_api | P1 | campaign-analysis.md | Direct Google Ads API integration for live data |
| ADS-002 | meta_ads_api | P1 | campaign-analysis.md | Facebook/Instagram Ads API integration |
| ADS-003 | linkedin_ads_api | P1 | campaign-analysis.md | LinkedIn Campaign Manager API integration |
| ADS-004 | attribution_analysis | P2 | campaign-analysis.md | Multi-touch attribution modeling |
| ADS-005 | audience_builder | P2 | audience-insights.md | Automated lookalike/similar audience creation |
| ADS-006 | customer_matching | P2 | audience-insights.md | Match ad data with CRM for LTV analysis |
| ADS-007 | meta_ad_library_scraper | P3 | creative-optimization.md | Automated competitor ad scraping |
| ADS-008 | video_analyzer | P3 | creative-optimization.md | Analyze video creative performance patterns |
| ADS-009 | image_generator | P3 | creative-optimization.md | AI-generated creative variations for testing |

### Category 4: Presentation & Visualization - 6 tools

| Tool ID | Tool Name | Priority | Source Skill | Purpose |
|---------|-----------|----------|--------------|---------|
| PRES-001 | slide_generator | P2 | presentation-creation.md | Auto-generate PowerPoint/Google Slides |
| PRES-002 | chart_creator | P2 | presentation-creation.md | Create visual charts as PNG/SVG files |
| PRES-003 | template_library | P3 | presentation-creation.md | Pre-built presentation templates |
| VIZ-001 | chart_generator | P2 | data-visualization.md | Generate actual PNG/SVG chart images |
| VIZ-002 | chart_templates | P3 | data-visualization.md | Pre-built chart templates library |
| VIZ-003 | accessibility_checker | P3 | data-visualization.md | Validate color contrast and screen reader compatibility |

### Category 5: Dashboard - 3 tools

| Tool ID | Tool Name | Priority | Source Skill | Purpose |
|---------|-----------|----------|--------------|---------|
| DASH-001 | data_connector | P1 | dashboard-creation.md | Connect to live data sources (Google Ads, Meta, etc.) |
| DASH-002 | chart_library | P2 | dashboard-creation.md | Pre-built chart components |
| DASH-003 | template_gallery | P3 | dashboard-creation.md | Ready-made dashboard templates |

### Category 6: Competitive Intelligence - 3 tools

| Tool ID | Tool Name | Priority | Source Skill | Purpose |
|---------|-----------|----------|--------------|---------|
| COMP-001 | brand_monitoring | P2 | competitor-analysis.md | Track competitor changes over time |
| COMP-002 | ad_spy | P2 | competitor-analysis.md | Automated competitor ad tracking |
| COMP-003 | seo_comparison | P2 | competitor-analysis.md | Real-time SEO metrics comparison |

### Category 7: Analytics & Synthesis - 3 tools

| Tool ID | Tool Name | Priority | Source Skill | Purpose |
|---------|-----------|----------|--------------|---------|
| ANLY-001 | data_integrator | P2 | data-synthesis.md | Auto-load and normalize data from all sources |
| ANLY-002 | pattern_detector | P3 | data-synthesis.md | ML-powered pattern identification |
| ANLY-003 | scenario_planner | P3 | data-synthesis.md | Model different strategic scenarios |

---

## Priority P0 Tools (Critical)

### GEO-001: run_multi_engine_test

**Status**: ✅ **FULLY SPECIFIED** in `MCP_TOOLS_REQUIREMENTS.md`

**Summary**:
- Execute 10-100 prompts across ChatGPT, Perplexity, Gemini in parallel
- 50 concurrent requests, <90 seconds for 300 tests
- Rate limiting with exponential backoff
- Citation extraction and brand mention detection

**Engineering Effort**: 3-4 weeks (1 engineer)
**Dependencies**: API access to ChatGPT, Perplexity, Gemini
**Estimated Cost**: $15K-20K development + $0.50-2.00 per test run (API costs)

**Key Technical Requirements**:
```typescript
interface RunMultiEngineTestInput {
  prompts: PromptTest[];          // 10-100 prompts
  engines: EngineConfig[];        // ChatGPT, Perplexity, Gemini
  max_concurrent?: number;        // Default: 50
  retry_failed?: boolean;         // Default: true
  timeout_ms?: number;            // Default: 10000
}

interface TestResult {
  prompt_id: string;
  engine: string;
  response: string;
  citations: Citation[];
  brand_mentioned: boolean;
  brand_position?: number;
  latency_ms: number;
  error?: string;
}
```

**Performance Targets**:
- 300 tests in <90 seconds (vs 14 minutes sequential)
- 95%+ success rate
- <$2 per full DEEP mode test run

---

### GEO-002: analyze_citations

**Status**: ✅ **FULLY SPECIFIED** in `MCP_TOOLS_REQUIREMENTS.md`

**Summary**:
- Analyze 100-1000 citations using parallel LLM calls (Claude Haiku)
- Relevance scoring, sentiment analysis, brand context
- 50 concurrent requests, <3 minutes for 900 citations

**Engineering Effort**: 2-3 weeks (1 engineer)
**Dependencies**: Anthropic API (Claude Haiku)
**Estimated Cost**: $10K-15K development + $0.11-0.25 per DEEP run

**Key Technical Requirements**:
```typescript
interface AnalyzeCitationsInput {
  test_results: TestResult[];
  brand_info: { brand_name: string; domain: string; competitors?: string[] };
  analysis_mode: 'light' | 'deep';
  max_concurrent?: number;        // Default: 50
  llm_model?: string;             // Default: 'claude-haiku-3-5'
}

interface CitationAnalysis {
  relevance_score: number;        // 0-100
  sentiment: 'positive' | 'neutral' | 'negative';
  brand_context: string;
  competitor_mentions: string[];
  key_points: string[];
  authority_score: number;
}
```

**Performance Targets**:
- 900 citations in <3 minutes
- Cost: <$0.30 per DEEP run
- 90%+ accuracy on sentiment classification

---

## Priority P1 Tools (High Value)

### SEO-001: keyword_research_api

**Purpose**: Fetch keyword metrics (search volume, difficulty, CPC) from SEO data providers

**Priority Justification**: Critical for keyword research skill, no reliable free alternatives

**Technical Specification**:

```typescript
interface KeywordResearchInput {
  keywords: string[];              // 10-100 keywords to research
  location?: string;               // Default: 'US'
  language?: string;               // Default: 'en'
  include_related?: boolean;       // Default: false
}

interface KeywordMetrics {
  keyword: string;
  search_volume: number;           // Monthly average
  difficulty: number;              // 0-100 (SEO difficulty)
  cpc: number;                     // Average cost per click
  competition: 'low' | 'medium' | 'high';
  trend: number[];                 // Last 12 months volume
  related_keywords?: string[];     // If include_related=true
}

interface KeywordResearchOutput {
  keywords: KeywordMetrics[];
  data_source: 'semrush' | 'ahrefs' | 'moz';
  timestamp: string;
}
```

**API Provider Options**:
1. **SEMrush API** - $200/month + per-request costs
2. **Ahrefs API** - $500/month minimum
3. **Moz API** - Free tier: 2,500 rows/month, Paid: $250/month

**Recommended**: Moz API (free tier sufficient for most use cases)

**Engineering Effort**: 1-2 weeks
**Estimated Cost**: $5K-8K development + $0-250/month API costs

---

### SEO-002: serp_analyzer

**Purpose**: Analyze top 10 SERP results for target keywords

**Technical Specification**:

```typescript
interface SerpAnalyzerInput {
  keyword: string;
  location?: string;
  device?: 'desktop' | 'mobile';
}

interface SerpResult {
  position: number;
  url: string;
  title: string;
  description: string;
  domain: string;
  domain_authority?: number;
  word_count?: number;
  has_featured_snippet: boolean;
  has_video: boolean;
  has_images: boolean;
}

interface SerpAnalysis {
  keyword: string;
  results: SerpResult[];
  avg_word_count: number;
  featured_snippet_present: boolean;
  your_position?: number;
  competitive_analysis: {
    avg_da: number;
    content_length_range: [number, number];
    common_content_types: string[];
  };
}
```

**Implementation Options**:
1. **SerpAPI** - $50/month (100 searches/day)
2. **ScraperAPI** - $49/month (5,000 API calls)
3. **Custom scraper** - Free but less reliable

**Recommended**: SerpAPI (most reliable, handles CAPTCHAs)

**Engineering Effort**: 2 weeks
**Estimated Cost**: $8K-10K development + $50/month

---

### SEO-003: crawler

**Purpose**: Crawl website for technical SEO issues (broken links, missing meta tags, slow pages, etc.)

**Technical Specification**:

```typescript
interface CrawlerInput {
  start_url: string;
  max_pages?: number;              // Default: 100
  max_depth?: number;              // Default: 3
  follow_external_links?: boolean; // Default: false
  check_resources?: boolean;       // Check images, CSS, JS (Default: true)
}

interface CrawledPage {
  url: string;
  status_code: number;
  load_time_ms: number;
  title?: string;
  meta_description?: string;
  h1_tags: string[];
  word_count: number;
  internal_links: number;
  external_links: number;
  broken_links: string[];
  missing_alt_text: number;
  has_canonical: boolean;
  has_schema: boolean;
  mobile_friendly: boolean;
  issues: Issue[];
}

interface Issue {
  severity: 'critical' | 'warning' | 'info';
  type: string;
  message: string;
  element?: string;
}
```

**Implementation Options**:
1. **Screaming Frog API** - $209/year (unlimited crawls)
2. **Sitebulb API** - $35/month
3. **Custom crawler** (Puppeteer + Cheerio)

**Recommended**: Custom crawler (full control, no ongoing costs)

**Engineering Effort**: 3-4 weeks
**Estimated Cost**: $15K-20K development

---

### SEO-009: backlink_checker

**Purpose**: Fetch comprehensive backlink data from Ahrefs/Moz

**Technical Specification**:

```typescript
interface BacklinkCheckerInput {
  domain: string;
  include_lost_links?: boolean;
  limit?: number;                  // Max backlinks to return
}

interface Backlink {
  source_url: string;
  source_domain: string;
  target_url: string;
  anchor_text: string;
  domain_rating: number;           // Ahrefs DR or Moz DA
  url_rating: number;
  link_type: 'dofollow' | 'nofollow';
  first_seen: string;
  last_seen: string;
  is_broken: boolean;
}

interface BacklinkProfile {
  domain: string;
  total_backlinks: number;
  referring_domains: number;
  domain_rating: number;
  backlinks: Backlink[];
  top_referring_domains: {
    domain: string;
    domain_rating: number;
    backlink_count: number;
  }[];
}
```

**API Provider Options**:
1. **Ahrefs API** - $500/month minimum (most comprehensive)
2. **Moz API** - $250/month (good for most use cases)
3. **Majestic API** - $50/month (cheaper but less data)

**Recommended**: Moz API ($250/month is acceptable for agency/SaaS use)

**Engineering Effort**: 2 weeks
**Estimated Cost**: $8K-10K development + $250/month

---

### ADS-001, ADS-002, ADS-003: Ads Platform APIs

**Purpose**: Direct API integration for real-time ads data

**Technical Specification** (Google Ads example):

```typescript
interface GoogleAdsApiInput {
  customer_id: string;
  date_range: {
    start_date: string;
    end_date: string;
  };
  metrics: string[];               // ['impressions', 'clicks', 'cost', 'conversions']
  breakdown?: 'campaign' | 'ad_group' | 'ad' | 'keyword';
}

interface GoogleAdsMetrics {
  id: string;
  name: string;
  impressions: number;
  clicks: number;
  cost_micros: number;             // Cost in micros (divide by 1M)
  conversions: number;
  cost_per_conversion: number;
  // ... additional metrics
}
```

**Implementation Requirements**:
- **Google Ads API**: Free, requires OAuth 2.0 authentication
- **Meta Ads API**: Free, requires Facebook Business verification
- **LinkedIn Ads API**: Free, requires LinkedIn Marketing Developer Program

**Engineering Effort**: 2-3 weeks per platform (6-9 weeks total)
**Estimated Cost**: $30K-45K development (all 3 platforms)

---

### DASH-001: data_connector

**Purpose**: Connect dashboards to live data sources (Ads APIs, GA4, etc.)

**Technical Specification**:

```typescript
interface DataConnectorInput {
  source: 'google_ads' | 'meta_ads' | 'linkedin_ads' | 'google_analytics' | 'custom';
  credentials: {
    // OAuth tokens or API keys
  };
  query: {
    metrics: string[];
    dimensions?: string[];
    filters?: Filter[];
    date_range: DateRange;
  };
  refresh_rate?: number;           // Seconds (for real-time dashboards)
}

interface DataConnectorOutput {
  data: Record<string, any>[];
  schema: {
    fields: {
      name: string;
      type: 'string' | 'number' | 'date' | 'boolean';
    }[];
  };
  last_updated: string;
  next_update?: string;            // If refresh_rate set
}
```

**Dependencies**: Requires ADS-001, ADS-002, ADS-003

**Engineering Effort**: 3 weeks (after Ads APIs complete)
**Estimated Cost**: $15K-18K development

---

## Priority P2 Tools (Medium Value)

### Chart Generation Tools (PRES-001, PRES-002, VIZ-001)

**Purpose**: Generate actual chart images (PNG/SVG) instead of text-based charts

**Technical Specification**:

```typescript
interface ChartGeneratorInput {
  chart_type: 'bar' | 'line' | 'pie' | 'scatter' | 'funnel' | 'gauge';
  data: {
    labels: string[];
    datasets: {
      label: string;
      data: number[];
      color?: string;
    }[];
  };
  options: {
    title?: string;
    width: number;
    height: number;
    format: 'png' | 'svg' | 'pdf';
    theme?: 'light' | 'dark';
  };
}

interface ChartGeneratorOutput {
  image_data: string;              // Base64 encoded image
  image_url?: string;              // If stored
  format: 'png' | 'svg' | 'pdf';
}
```

**Implementation Options**:
1. **QuickChart.io** - Free tier available, $40/month for production
2. **Chart.js + Puppeteer** - Custom solution, render client-side charts server-side
3. **PlotlyJS** - Node.js library for chart generation

**Recommended**: QuickChart.io (easiest) or custom Puppeteer solution (more control)

**Engineering Effort**: 2-3 weeks
**Estimated Cost**: $10K-12K development + $0-40/month

---

### Remaining P2 Tools

Due to space constraints, here's a summary table:

| Tool ID | Effort (weeks) | Cost (dev) | Monthly Cost | Notes |
|---------|----------------|------------|--------------|-------|
| SEO-004 | 1-2 | $5K-8K | $0 | Use PageSpeed Insights API (free) |
| SEO-005 | 1 | $3K-5K | $0 | Custom schema validator |
| SEO-006 | 2 | $8K-10K | $0 | Custom content analyzer |
| SEO-007 | 2-3 | $10K-12K | $50 | Scraping with proxies |
| SEO-010 | 1 | $3K-5K | $250 | Moz API wrapper |
| ADS-004 | 3-4 | $15K-20K | $0 | Complex attribution modeling |
| ADS-005 | 2 | $8K-10K | $0 | API wrapper for platform audience creation |
| ADS-006 | 2-3 | $10K-12K | $0 | CRM integration layer |
| DASH-002 | 2 | $8K-10K | $0 | React component library |
| COMP-001 | 2-3 | $10K-12K | $100 | Change detection + storage |
| COMP-002 | 2-3 | $10K-12K | $100 | Facebook Ad Library scraper |
| COMP-003 | 2 | $8K-10K | $250 | SEO API aggregator |
| ANLY-001 | 2-3 | $10K-12K | $0 | Data normalization layer |

**Total P2 Engineering**: ~30 weeks
**Total P2 Cost**: ~$108K-140K development + ~$750/month ongoing

---

## Priority P3 Tools (Low Priority)

These are nice-to-have optimizations but not critical for core functionality:

| Tool ID | Purpose | Estimated Effort | Estimated Cost |
|---------|---------|------------------|----------------|
| SEO-008 | ML content gap detection | 4-6 weeks | $20K-30K |
| SEO-011 | Broken link finder | 1-2 weeks | $5K-8K |
| SEO-012 | Outreach tracker | 2-3 weeks | $10K-12K |
| ADS-007 | Meta ad library scraper | 2 weeks | $8K-10K |
| ADS-008 | Video analyzer | 3-4 weeks | $15K-20K |
| ADS-009 | AI image generator | 4-6 weeks | $20K-30K |
| PRES-003 | Template library | 1 week | $3K-5K |
| VIZ-002 | Chart templates | 1 week | $3K-5K |
| VIZ-003 | Accessibility checker | 2 weeks | $8K-10K |
| DASH-003 | Template gallery | 1-2 weeks | $5K-8K |
| ANLY-002 | ML pattern detector | 4-6 weeks | $20K-30K |
| ANLY-003 | Scenario planner | 3-4 weeks | $15K-18K |

**Total P3 Engineering**: ~31-43 weeks
**Total P3 Cost**: ~$132K-186K

**Recommendation**: Defer P3 tools until P0-P1 tools are complete and ROI is validated

---

## Development Roadmap

### Phase 1: Critical GEO Tools (Weeks 1-6)

**Goal**: Enable GEO analysis functionality

**Deliverables**:
- ✅ GEO-001: run_multi_engine_test (Weeks 1-4)
- ✅ GEO-002: analyze_citations (Weeks 4-6, parallel with GEO-001 completion)

**Milestones**:
- Week 2: GEO-001 prototype working with ChatGPT
- Week 3: Add Perplexity and Gemini support
- Week 4: GEO-001 production-ready
- Week 5: GEO-002 prototype with citation analysis
- Week 6: GEO-002 production-ready, end-to-end GEO workflow tested

**Team**: 1-2 engineers
**Budget**: $30K-35K

---

### Phase 2: SEO Foundation (Weeks 7-12)

**Goal**: Enable comprehensive SEO analysis

**Deliverables**:
- ✅ SEO-001: keyword_research_api (Weeks 7-8)
- ✅ SEO-002: serp_analyzer (Weeks 8-9)
- ✅ SEO-003: crawler (Weeks 9-12)
- ✅ SEO-009: backlink_checker (Weeks 11-12, parallel)

**Milestones**:
- Week 8: Keyword research integrated with Moz API
- Week 9: SERP analysis working with SerpAPI
- Week 10: Basic crawler working (internal links, broken links)
- Week 11: Advanced crawler features (speed, mobile, schema)
- Week 12: Backlink analysis integrated, full SEO workflow complete

**Team**: 2 engineers
**Budget**: $50K-60K

---

### Phase 3: Ads Platform Integration (Weeks 13-18)

**Goal**: Real-time ads data and dashboard connectivity

**Deliverables**:
- ✅ ADS-001: google_ads_api (Weeks 13-15)
- ✅ ADS-002: meta_ads_api (Weeks 14-16, parallel start at week 14)
- ✅ ADS-003: linkedin_ads_api (Weeks 16-18)
- ✅ DASH-001: data_connector (Week 18, integrates all above)

**Milestones**:
- Week 14: Google Ads OAuth flow working
- Week 15: Google Ads metrics retrieval complete
- Week 16: Meta Ads integration complete
- Week 17: LinkedIn Ads integration complete
- Week 18: Unified data connector working with all platforms

**Team**: 2-3 engineers
**Budget**: $60K-75K

---

### Phase 4: Visualization & Polish (Weeks 19-22)

**Goal**: Enhanced presentation and dashboard output

**Deliverables**:
- ✅ PRES-001: slide_generator (Weeks 19-20)
- ✅ VIZ-001: chart_generator (Weeks 20-21)
- ✅ DASH-002: chart_library (Weeks 21-22)

**Milestones**:
- Week 20: PowerPoint generation working
- Week 21: Chart image generation working
- Week 22: Dashboard chart library complete

**Team**: 1-2 engineers
**Budget**: $25K-35K

---

### Total Phase 1-4 (P0 + P1 Tools)

**Timeline**: 22 weeks (~5.5 months)
**Team**: 2-3 engineers average
**Total Budget**: $165K-205K development
**Ongoing Costs**: ~$550/month (API subscriptions)

---

## Technical Architecture

### MCP Server Structure

```
mcp-servers/
├── marketing-tools/
│   ├── server.py                 # Main MCP server
│   ├── tools/
│   │   ├── geo/
│   │   │   ├── multi_engine_test.py
│   │   │   └── citation_analysis.py
│   │   ├── seo/
│   │   │   ├── keyword_research.py
│   │   │   ├── serp_analyzer.py
│   │   │   ├── crawler.py
│   │   │   └── backlink_checker.py
│   │   ├── ads/
│   │   │   ├── google_ads.py
│   │   │   ├── meta_ads.py
│   │   │   └── linkedin_ads.py
│   │   ├── dashboard/
│   │   │   └── data_connector.py
│   │   └── viz/
│   │       └── chart_generator.py
│   ├── utils/
│   │   ├── rate_limiter.py
│   │   ├── parallel_executor.py
│   │   └── cache.py
│   ├── config/
│   │   ├── api_keys.json        # Encrypted
│   │   └── rate_limits.json
│   └── tests/
│       └── ...
├── requirements.txt
├── docker-compose.yml
└── README.md
```

### Key Architectural Decisions

#### 1. Single MCP Server vs Multiple Servers

**Decision**: Single unified `marketing-tools` MCP server

**Rationale**:
- Easier to manage dependencies and shared utilities
- Shared rate limiting and caching across tools
- Simpler configuration for end users
- Can still organize tools into logical modules

**Alternative Considered**: Separate servers per category (seo-tools, ads-tools, etc.)
- Pro: More modular, easier to deploy individually
- Con: Duplicated code, harder to share utilities, more configuration overhead

#### 2. Caching Strategy

**Decision**: Redis-based caching with TTL

**Implementation**:
```python
# cache.py
import redis
import json
from typing import Optional

class MCPCache:
    def __init__(self):
        self.redis = redis.Redis(host='localhost', port=6379, db=0)

    def get(self, key: str) -> Optional[dict]:
        data = self.redis.get(key)
        return json.loads(data) if data else None

    def set(self, key: str, value: dict, ttl: int = 3600):
        self.redis.setex(key, ttl, json.dumps(value))

# Usage in tools
cache = MCPCache()

def keyword_research(keywords: list[str]) -> dict:
    cache_key = f"keywords:{','.join(sorted(keywords))}"

    # Try cache first
    cached = cache.get(cache_key)
    if cached:
        return cached

    # Fetch from API
    result = fetch_from_moz_api(keywords)

    # Cache for 24 hours (keyword metrics don't change frequently)
    cache.set(cache_key, result, ttl=86400)

    return result
```

**TTL Strategy**:
- Keyword metrics: 24 hours (daily updates sufficient)
- SERP results: 6 hours (more dynamic)
- Backlink data: 7 days (changes slowly)
- Ads data: No cache (real-time needed)
- GEO test results: 30 days (for comparison, not for fresh data)

#### 3. Rate Limiting

**Decision**: Token bucket algorithm with per-API limits

**Implementation**:
```python
# rate_limiter.py
import time
from collections import defaultdict

class RateLimiter:
    def __init__(self):
        self.buckets = defaultdict(lambda: {
            'tokens': 0,
            'last_update': time.time()
        })

    def allow(self, api_name: str, rate_limit: int, period: int = 60) -> bool:
        """
        Check if request is allowed

        Args:
            api_name: Name of API (e.g., 'moz', 'serpapi')
            rate_limit: Max requests per period
            period: Time period in seconds (default: 60)

        Returns:
            True if request allowed, False otherwise
        """
        bucket = self.buckets[api_name]
        now = time.time()

        # Refill tokens based on time elapsed
        elapsed = now - bucket['last_update']
        bucket['tokens'] = min(
            rate_limit,
            bucket['tokens'] + (elapsed / period) * rate_limit
        )
        bucket['last_update'] = now

        # Check if we have tokens
        if bucket['tokens'] >= 1:
            bucket['tokens'] -= 1
            return True
        else:
            return False

    def wait_time(self, api_name: str, rate_limit: int, period: int = 60) -> float:
        """Return seconds to wait before next request is allowed"""
        bucket = self.buckets[api_name]
        if bucket['tokens'] >= 1:
            return 0

        # Calculate wait time to get 1 token
        tokens_needed = 1 - bucket['tokens']
        return tokens_needed * (period / rate_limit)
```

**Rate Limits by API**:
```python
RATE_LIMITS = {
    'moz': {'limit': 10, 'period': 10},          # 10 requests per 10 seconds
    'serpapi': {'limit': 100, 'period': 86400},  # 100 requests per day (free tier)
    'ahrefs': {'limit': 500, 'period': 3600},    # 500 requests per hour
    'chatgpt': {'limit': 60, 'period': 60},      # 60 requests per minute
    'claude': {'limit': 50, 'period': 60},       # 50 requests per minute
}
```

#### 4. Parallel Execution

**Decision**: Use `asyncio` with `aiohttp` for parallel HTTP requests

**Implementation**:
```python
# parallel_executor.py
import asyncio
import aiohttp
from typing import List, Callable, Any

async def execute_parallel(
    tasks: List[dict],
    executor_func: Callable,
    max_concurrent: int = 50,
    timeout: int = 10
) -> List[Any]:
    """
    Execute tasks in parallel with concurrency limit

    Args:
        tasks: List of task configurations
        executor_func: Async function to execute each task
        max_concurrent: Max concurrent executions
        timeout: Timeout per task in seconds

    Returns:
        List of results
    """
    semaphore = asyncio.Semaphore(max_concurrent)

    async def execute_with_semaphore(task):
        async with semaphore:
            try:
                return await asyncio.wait_for(
                    executor_func(task),
                    timeout=timeout
                )
            except asyncio.TimeoutError:
                return {'error': 'Timeout', 'task': task}
            except Exception as e:
                return {'error': str(e), 'task': task}

    results = await asyncio.gather(
        *[execute_with_semaphore(task) for task in tasks],
        return_exceptions=True
    )

    return results

# Usage example
async def test_prompt_on_engine(task: dict) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.post(
            task['endpoint'],
            json={'prompt': task['prompt']},
            headers={'Authorization': f"Bearer {task['api_key']}"}
        ) as response:
            return await response.json()

# Execute 100 prompts across 3 engines in parallel
tasks = [
    {'prompt': p, 'endpoint': e, 'api_key': key}
    for p in prompts
    for e in engines
]

results = await execute_parallel(
    tasks,
    test_prompt_on_engine,
    max_concurrent=50
)
```

#### 5. Error Handling & Retries

**Decision**: Exponential backoff with jitter

**Implementation**:
```python
import random
import time

async def retry_with_backoff(
    func: Callable,
    max_retries: int = 3,
    base_delay: float = 1.0,
    max_delay: float = 16.0
):
    """
    Retry function with exponential backoff and jitter

    Args:
        func: Async function to retry
        max_retries: Maximum number of retries
        base_delay: Initial delay in seconds
        max_delay: Maximum delay in seconds
    """
    for attempt in range(max_retries + 1):
        try:
            return await func()
        except Exception as e:
            if attempt == max_retries:
                raise

            # Calculate delay with exponential backoff and jitter
            delay = min(
                base_delay * (2 ** attempt) + random.uniform(0, 1),
                max_delay
            )

            print(f"Attempt {attempt + 1} failed: {e}. Retrying in {delay:.2f}s...")
            await asyncio.sleep(delay)
```

---

## Resource Requirements

### Engineering Team

**Phase 1-2 (Weeks 1-12)**: GEO + SEO Tools
- **1 Senior Engineer** (API integrations, architecture)
- **1 Mid-Level Engineer** (tool implementations, testing)

**Phase 3 (Weeks 13-18)**: Ads Platform Integration
- **1 Senior Engineer** (OAuth flows, API integrations)
- **1 Mid-Level Engineer** (data connector, testing)
- **1 Junior Engineer** (documentation, test coverage)

**Phase 4 (Weeks 19-22)**: Visualization
- **1 Mid-Level Engineer** (chart generation, slide creation)

### Infrastructure

**Development Environment**:
- GitHub repository for MCP server code
- CI/CD pipeline (GitHub Actions)
- Staging environment (Docker Compose)
- Test API keys for all services

**Production Environment**:
- **Option A**: Self-hosted
  - 2-4 vCPU, 8GB RAM server
  - Redis instance (caching)
  - PostgreSQL (usage tracking, logs)
  - Cost: ~$50-100/month (AWS EC2/DigitalOcean)

- **Option B**: Serverless
  - AWS Lambda + API Gateway
  - ElastiCache (Redis)
  - RDS (PostgreSQL)
  - Cost: ~$100-200/month (pay-per-use)

**Recommended**: Start with Docker Compose locally, migrate to cloud when needed

### API Subscriptions

**Required**:
- Moz API: $250/month (or free tier)
- SerpAPI: $50/month
- ChatGPT API: Pay-per-use (~$50-200/month depending on usage)
- Anthropic API (Claude): Pay-per-use (~$50-150/month)
- Perplexity API: $20/month
- Gemini API: Free tier available

**Optional** (P2 tools):
- Ahrefs API: $500/month (or use Moz)
- QuickChart: $40/month (or custom solution)
- Proxies for scraping: $50-100/month

**Total Monthly**: $550-1,500/month depending on optional tools

---

## Testing Strategy

### Unit Testing

**Coverage Target**: 85%+

**Framework**: pytest

**Example Test**:
```python
# tests/test_keyword_research.py
import pytest
from tools.seo.keyword_research import keyword_research_api

@pytest.mark.asyncio
async def test_keyword_research_basic():
    result = await keyword_research_api({
        'keywords': ['seo tools', 'keyword research'],
        'location': 'US'
    })

    assert len(result['keywords']) == 2
    assert all(k['search_volume'] > 0 for k in result['keywords'])
    assert all(0 <= k['difficulty'] <= 100 for k in result['keywords'])

@pytest.mark.asyncio
async def test_keyword_research_with_related():
    result = await keyword_research_api({
        'keywords': ['seo tools'],
        'include_related': True
    })

    assert 'related_keywords' in result['keywords'][0]
    assert len(result['keywords'][0]['related_keywords']) > 0
```

### Integration Testing

**Coverage**: All API integrations

**Example Test**:
```python
# tests/integration/test_multi_engine.py
import pytest
from tools.geo.multi_engine_test import run_multi_engine_test

@pytest.mark.integration
@pytest.mark.asyncio
async def test_multi_engine_end_to_end():
    """Test full GEO workflow with real APIs"""
    result = await run_multi_engine_test({
        'prompts': [
            {'id': 'p1', 'text': 'best AI customer support software'},
            {'id': 'p2', 'text': 'how to automate customer support'}
        ],
        'engines': [
            {'name': 'chatgpt', 'model': 'gpt-4'},
            {'name': 'perplexity', 'model': 'sonar-medium'}
        ],
        'brand_info': {
            'brand_name': 'TestCorp',
            'domain': 'testcorp.com'
        }
    })

    assert len(result['results']) == 4  # 2 prompts × 2 engines
    assert all(r['response'] for r in result['results'])
    assert all(isinstance(r['latency_ms'], (int, float)) for r in result['results'])
```

### Load Testing

**Tool**: Locust or k6

**Scenarios**:
1. **GEO Load Test**: 100 prompts × 3 engines = 300 requests
   - Target: Complete in <90 seconds
   - Success rate: >95%

2. **SEO Crawler Load Test**: Crawl 100-page website
   - Target: Complete in <5 minutes
   - Find all critical issues

3. **Ads API Load Test**: Fetch data for 50 campaigns
   - Target: Complete in <30 seconds
   - No API errors

**Example Locust Test**:
```python
# tests/load/test_geo_load.py
from locust import User, task, between
import random

class GEOUser(User):
    wait_time = between(1, 3)

    @task
    def test_multi_engine(self):
        self.client.post("/tools/geo/multi_engine_test", json={
            'prompts': [
                {'id': f'p{i}', 'text': f'test prompt {i}'}
                for i in range(10)
            ],
            'engines': [
                {'name': 'chatgpt', 'model': 'gpt-4'}
            ]
        })

# Run: locust -f tests/load/test_geo_load.py --host=http://localhost:8000
```

---

## Deployment Plan

### Deployment Phases

#### Phase 1: Development Environment (Week 1)

**Setup**:
```bash
# Clone repo
git clone https://github.com/your-org/mcp-marketing-tools
cd mcp-marketing-tools

# Install dependencies
pip install -r requirements.txt

# Configure API keys
cp config/api_keys.example.json config/api_keys.json
# Edit api_keys.json with real keys

# Start Redis (for caching)
docker run -d -p 6379:6379 redis:7

# Start MCP server
python server.py --port 8000
```

**Validation**:
- Run test suite: `pytest tests/`
- Test manual tool invocation
- Verify all API keys work

#### Phase 2: Staging Environment (Week 12)

**Infrastructure**:
```yaml
# docker-compose.yml
version: '3.8'

services:
  mcp-server:
    build: .
    ports:
      - "8000:8000"
    environment:
      - REDIS_HOST=redis
      - POSTGRES_HOST=postgres
    depends_on:
      - redis
      - postgres
    volumes:
      - ./config:/app/config:ro

  redis:
    image: redis:7
    ports:
      - "6379:6379"

  postgres:
    image: postgres:15
    environment:
      POSTGRES_DB: mcp_tools
      POSTGRES_USER: mcp
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

**Deploy**:
```bash
# Build and start services
docker-compose up -d

# Run migrations
docker-compose exec mcp-server alembic upgrade head

# Run integration tests against staging
pytest tests/integration/ --staging
```

#### Phase 3: Production Deployment (Week 22)

**Option A: Self-Hosted (Docker)**
```bash
# On production server
git clone https://github.com/your-org/mcp-marketing-tools
cd mcp-marketing-tools

# Set production environment variables
export POSTGRES_PASSWORD=<secure-password>
export REDIS_PASSWORD=<secure-password>

# Deploy
docker-compose -f docker-compose.prod.yml up -d

# Configure nginx reverse proxy
# Configure SSL/TLS certificates (Let's Encrypt)
```

**Option B: Serverless (AWS Lambda)**
```yaml
# serverless.yml
service: mcp-marketing-tools

provider:
  name: aws
  runtime: python3.11
  region: us-east-1
  environment:
    REDIS_HOST: ${self:custom.redis.endpoint}
    POSTGRES_HOST: ${self:custom.postgres.endpoint}

functions:
  mcp-server:
    handler: server.handler
    timeout: 900  # 15 minutes max
    memorySize: 2048
    events:
      - http:
          path: /tools/{proxy+}
          method: ANY

custom:
  redis:
    endpoint: ${cf:mcp-tools-${self:provider.stage}.RedisEndpoint}
  postgres:
    endpoint: ${cf:mcp-tools-${self:provider.stage}.PostgresEndpoint}

resources:
  Resources:
    # ElastiCache Redis
    # RDS PostgreSQL
    # Security groups, etc.
```

### Rollout Strategy

**Week 22-23: Limited Beta**
- Deploy to production
- Enable for internal team only
- Monitor performance, errors
- Fix critical bugs

**Week 24-25: Expanded Beta**
- Enable for 10-20 beta users
- Collect feedback
- Monitor API costs
- Optimize performance bottlenecks

**Week 26+: General Availability**
- Public launch
- Full documentation published
- Support channels active
- Monitoring and alerting in place

---

## Monitoring & Observability

### Metrics to Track

**Performance Metrics**:
```python
from prometheus_client import Counter, Histogram, Gauge

# Request metrics
tool_requests = Counter(
    'mcp_tool_requests_total',
    'Total tool requests',
    ['tool_name', 'status']
)

tool_duration = Histogram(
    'mcp_tool_duration_seconds',
    'Tool execution duration',
    ['tool_name']
)

# API metrics
api_calls = Counter(
    'external_api_calls_total',
    'External API calls',
    ['api_name', 'status']
)

api_cost = Counter(
    'external_api_cost_usd',
    'API costs in USD',
    ['api_name']
)

# Cache metrics
cache_hits = Counter('cache_hits_total', 'Cache hits', ['tool_name'])
cache_misses = Counter('cache_misses_total', 'Cache misses', ['tool_name'])
```

**Alerting Rules**:
```yaml
groups:
  - name: mcp_tools
    rules:
      - alert: HighErrorRate
        expr: rate(mcp_tool_requests_total{status="error"}[5m]) > 0.05
        for: 5m
        annotations:
          summary: "High error rate detected"

      - alert: SlowToolExecution
        expr: histogram_quantile(0.95, mcp_tool_duration_seconds) > 30
        for: 10m
        annotations:
          summary: "95th percentile tool execution >30s"

      - alert: HighAPICost
        expr: increase(external_api_cost_usd[1h]) > 50
        annotations:
          summary: "API costs >$50/hour"
```

### Logging

**Structured Logging**:
```python
import structlog

logger = structlog.get_logger()

async def run_multi_engine_test(input_data):
    logger.info(
        "multi_engine_test_started",
        prompt_count=len(input_data['prompts']),
        engine_count=len(input_data['engines'])
    )

    try:
        results = await execute_tests(input_data)

        logger.info(
            "multi_engine_test_completed",
            total_tests=len(results),
            success_count=sum(1 for r in results if not r.get('error')),
            duration_ms=duration
        )

        return results

    except Exception as e:
        logger.error(
            "multi_engine_test_failed",
            error=str(e),
            exc_info=True
        )
        raise
```

---

## Cost Breakdown Summary

### Development Costs (One-Time)

| Phase | Duration | Team | Cost |
|-------|----------|------|------|
| Phase 1: GEO Tools | 6 weeks | 1-2 engineers | $30K-35K |
| Phase 2: SEO Tools | 6 weeks | 2 engineers | $50K-60K |
| Phase 3: Ads Integration | 6 weeks | 2-3 engineers | $60K-75K |
| Phase 4: Visualization | 4 weeks | 1-2 engineers | $25K-35K |
| **Total P0+P1** | **22 weeks** | **2-3 avg** | **$165K-205K** |

### Ongoing Costs (Monthly)

| Category | Service | Cost |
|----------|---------|------|
| **APIs** | Moz API | $0-250 |
| | SerpAPI | $50 |
| | ChatGPT API | $50-200 |
| | Claude API | $50-150 |
| | Perplexity API | $20 |
| | Gemini API | $0-50 |
| **Infrastructure** | Server/Hosting | $50-200 |
| | Redis/PostgreSQL | $0-50 |
| **Total Monthly** | | **$550-1,500** |

### ROI Analysis

**Assumptions**:
- Marketing agency with 20 clients
- Each client analyzed monthly
- Manual analysis: 8 hours per client = 160 hours/month
- Cost savings: 160 hours × $100/hour = $16,000/month
- Tool costs: $1,500/month
- **Net savings**: $14,500/month ($174K/year)
- **Payback period**: 1.2 months

---

## Success Metrics

### Technical Metrics

**P0 Tools (GEO)**:
- ✅ 300 prompts tested in <90 seconds (vs 14 minutes manual)
- ✅ 900 citations analyzed in <3 minutes (vs 45 minutes manual)
- ✅ Success rate >95%
- ✅ Cost per DEEP run <$2.50

**P1 Tools (SEO)**:
- ✅ Keyword research: 100 keywords in <30 seconds
- ✅ SERP analysis: 10 results analyzed in <10 seconds
- ✅ Crawler: 100 pages crawled in <5 minutes

**P1 Tools (Ads)**:
- ✅ Real-time data refresh <30 seconds
- ✅ Support 50+ concurrent campaigns
- ✅ 99.9% API uptime

### Business Metrics

**Adoption**:
- 80%+ of skills actively used within 3 months
- 50+ analyses run per week
- 90%+ user satisfaction

**Efficiency Gains**:
- 10x faster GEO analysis (4 hours → 25 minutes)
- 5x faster SEO audit (2 hours → 25 minutes)
- Real-time ads reporting (vs daily manual exports)

**Quality**:
- 95%+ accuracy on automated insights
- <5% false positives on issue detection
- Client satisfaction scores improve 20%+

---

## Next Steps

### Immediate Actions (This Week)

1. **Review & Approve Development Plan**
   - Confirm P0+P1 tool priorities
   - Approve $165K-205K budget
   - Confirm 22-week timeline

2. **Set Up Development Environment**
   - Create GitHub repository
   - Set up CI/CD pipeline
   - Provision staging infrastructure

3. **Acquire API Access**
   - Register for all required APIs
   - Obtain API keys and credentials
   - Test connectivity

### Week 1-2 Actions

1. **Hire/Assign Team**
   - 1 Senior Engineer (lead)
   - 1 Mid-Level Engineer

2. **Architecture Review**
   - Finalize technical architecture
   - Review MCP server structure
   - Set up development standards

3. **Begin Phase 1: GEO Tools**
   - Implement GEO-001 prototype
   - Set up testing framework
   - Begin documentation

---

## Appendix: Tool Comparison Matrix

[See separate detailed comparison spreadsheet]

Key highlights:
- **P0 tools**: 100% required for GEO functionality
- **P1 SEO tools**: 80% value from 20% effort (crawler is heavy but critical)
- **P1 Ads tools**: Highest ROI (eliminate manual exports entirely)
- **P2 tools**: Defer until P0+P1 validated
- **P3 tools**: Nice-to-have, consider after 6 months

---

**Document Version**: 1.0
**Last Updated**: 2024-01-15
**Next Review**: After Phase 1 completion (Week 6)
