---
name: presentation-creation
description: Create professional marketing presentations from analysis data with compelling narratives, data visualizations, and actionable recommendations. Use when building executive summaries, detailed analyses, or pitch decks from GEO, SEO, Ads, and Competitor data.
metadata:
  author: castor
  version: "1.0"
  domain: presentation
  execution-modes: light, deep
---

# Marketing Presentation Creation

## Purpose

Create professional marketing presentations from analysis data (GEO, SEO, Ads, Competitor analysis) with compelling narratives, data visualizations, and actionable recommendations in various formats.

## Execution Modes

### Light Mode (10-15 minutes)
**Goal**: Create concise executive summary presentation (5-10 slides)
**Scope**: High-level findings and top recommendations
**Output**: Executive-ready slide deck in markdown format

### Deep Mode (30-45 minutes)
**Goal**: Create detailed analysis presentation (20-40 slides)
**Scope**: In-depth findings, visualizations, supporting data, implementation roadmap
**Output**: Full presentation deck with detailed appendix

## Prerequisites

**Required Input**:
- Analysis data from skills (GEO, SEO, Ads, Competitor)
  - JSON files from /data/geo/, /data/seo/, /data/ads/, etc.
- Presentation objective (inform, persuade, recommend)
- Target audience (executives, marketing team, board)

**Optional**:
- Brand colors and logo
- Company background information
- Specific formatting requirements

## Presentation Formats

### Format 1: Executive Summary (5-10 slides)
- **Audience**: C-level, busy executives
- **Duration**: 5-10 minute read
- **Structure**: Title -> Executive Summary -> Key Findings (2-3 slides) -> Recommendations (1-2) -> Next Steps

### Format 2: Detailed Analysis (20-30 slides)
- **Audience**: Marketing team, stakeholders
- **Duration**: 20-30 minute presentation
- **Structure**: Title + Agenda -> Executive Summary -> Methodology -> Detailed Findings (10-15) -> Competitive Analysis (3-5) -> Recommendations (3-5) -> Implementation Roadmap (2-3) -> Appendix

### Format 3: Pitch Deck (10-15 slides)
- **Audience**: Clients, prospects, investors
- **Duration**: 15-20 minute presentation
- **Structure**: Title + Hook -> Problem Statement -> Current Situation -> Solution/Recommendation -> Results/Proof -> Implementation Plan -> Investment Required -> Expected ROI -> Next Steps

## Workflow Steps

### Step 1: Data Collection & Review

Load all relevant data files and extract key metrics:

```
Read all relevant data files:
- GEO analysis: /data/geo/*-{company}-*.json
- SEO analysis: /data/seo/*-{company}-*.json
- Ads analysis: /data/ads/*-{company}-*.json
- Competitor analysis: /data/competitor/*-{company}-*.json

Extract key metrics:
- Overall performance scores
- Top opportunities
- Critical issues
- Recommendations
- Projected impact
```

### Step 2: Determine Narrative Arc

Select narrative based on format and audience:

**Executive Summary**: Situation -> Problem -> Solution -> Impact
**Detailed Analysis**: Context -> Deep Dive -> Insights -> Roadmap
**Pitch Deck**: Problem -> Agitate -> Solution -> Proof -> Close

### Step 3: Create Slide Outline

Build a structured outline mapping each slide's title, key content, and supporting data. Each slide should have:
- A clear, specific title (states the insight, not just the topic)
- One sentence summary
- 3-5 supporting bullets (concise, data-driven)
- An insight/so-what statement
- Optional visual/chart placeholder

### Step 4: Create Data Visualizations

For each slide with data, create the appropriate visualization type:

1. **Performance Scorecard** - Table with category scores, status indicators, and benchmarks
2. **Opportunity Matrix** - Impact vs Effort quadrant chart
3. **Trend Chart** - Line chart showing metric movement over time
4. **Before/After Comparison** - Side-by-side current vs projected metrics
5. **Waterfall Chart** - Cumulative revenue impact breakdown

See `references/workflow-detail.md` for full visualization examples.

### Step 5: Write Slide Content

**Best Practice Structure**:
```markdown
## Slide Title (Clear, Specific - states the insight)

**One Sentence Summary** (tells the main point immediately)

Supporting Points:
- Bullet 1 (concise, data-driven)
- Bullet 2 (action-oriented)
- Bullet 3 (specific, not vague)

**Insight/So What**: Why this matters (1 sentence)
```

**Good**: "Google Ads Outperforming Other Platforms by 2.3x" with specific ROAS, CPA, and conversion data per platform.

**Bad**: "Platform Performance" with vague bullets like "Google is good." No data, no clear recommendation.

### Step 6: Build Presentation (Markdown Format)

Output the full presentation in markdown with slide separators (`---`). Include:
- Title slide with company name, topic, and date
- Executive summary with metrics table
- Individual findings slides with data and recommendations
- Implementation roadmap with monthly milestones
- ROI slide with investment/return table
- Next steps with action items and decision required
- Appendix with data sources

See `references/workflow-detail.md` for a complete Light Mode example presentation.

### Step 7: Add Design Guidance

Include design notes for implementation:
- **Colors**: Brand colors primary, semantic accents (green=positive, red=negative, yellow=warning, blue=info)
- **Typography**: Titles 32-36pt bold, body 18-24pt regular, captions 14-16pt light, sans-serif fonts
- **Layout**: Max 5 bullets per slide, max 15 words per bullet, 30-40% white space
- **Charts**: Simple, clear, large fonts, consistent colors, always label axes and cite sources

### Step 8: Create Variants (Deep Mode)

Generate multiple presentation versions for different audiences:
- **C-Level** (5 slides, 5 min): Focus on ROI, risk, decision required
- **Marketing Team** (25 slides, 30 min): Tactical execution, methodology, granular data
- **Board/Investor** (10 slides, 15 min): Strategic positioning, competitive advantage

### Step 9: Output Generation

Save in multiple formats:

```
Format 1 (Primary): /output/presentations/{company}-{topic}-{date}.md
  - Markdown, easy to edit, version control friendly
  - Convert to slides using Marp, reveal.js

Format 2 (PowerPoint-Ready): /output/presentations/{company}-{topic}-{date}-pptx-structure.md
  - Slide-by-slide with title, content, visual placeholder, speaker notes
```

### Step 10: Quality Checks

```
- Data Accuracy: All numbers match source data, calculations correct, projections realistic
- Narrative Flow: Logical progression, each slide builds on previous, clear beginning/middle/end
- Visual Clarity: Charts readable, colors consistent, text concise, no overcrowded slides
- Actionability: Clear recommendations, specific next steps, ownership assignable, timeline realistic
- Audience Appropriateness: Right detail level, appropriate tone, matches time constraints
```

## Validation Checks

1. **Slide Count**: Light 5-10 slides, Deep 20-40 slides
2. **Data Citations**: All data points sourced from analysis files
3. **Visualizations**: At least 3-5 charts/tables included
4. **Recommendations**: Specific, actionable, prioritized
5. **ROI Calculation**: Present and realistic
6. **Next Steps**: Clear and time-bound

## Agent Workflow

```
1. Read this skill file
2. Load analysis data from /data/ directories
3. Determine presentation format (Executive, Detailed, Pitch)
4. Determine mode (Light or Deep)
5. Track creation with TodoWrite:
   [ ] Data collection
   [ ] Narrative planning
   [ ] Slide outline
   [ ] Data visualizations
   [ ] Content writing
   [ ] Design guidance
   [ ] Quality check
   [ ] Output generation
6. Build presentation in markdown
7. Save to /output/presentations/
8. Provide summary with format, slide count, audience, duration, key slides, and output files
```

## Integration with Other Skills

**Requires data from**:
- All analysis skills (GEO, SEO, Ads, Competitor)
- `presentation-data-viz` skill for creating compelling charts

**Feeds into**:
- Client/stakeholder meetings
- Strategy planning sessions
- Board presentations
