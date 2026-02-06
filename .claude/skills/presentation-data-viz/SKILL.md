---
name: presentation-data-viz
description: Create compelling, accurate data visualizations for marketing presentations, dashboards, and reports. Use when selecting chart types, generating matplotlib/Chart.js charts, or applying visualization best practices to analysis data.
metadata:
  author: castor
  version: "1.0"
  domain: presentation
  execution-modes: light, deep
---

# Data Visualization for Marketing

## Purpose

Create compelling, accurate data visualizations for marketing presentations, dashboards, and reports using appropriate chart types, design principles, and storytelling techniques.

## When to Use This Skill

- Creating charts for presentations (with presentation-creation skill)
- Building dashboards (with dashboard-creation skill)
- Visualizing analysis results (GEO, SEO, Ads data)
- Communicating complex data to stakeholders
- Comparing performance metrics

## Chart Generation with Python (matplotlib)

### Load Source Data

```python
# Load analysis files for visualization
seo_data = Read(f"/data/clients/{CLIENT_ID}/analyses/seo/seo-audit-{timestamp}.json")
ads_data = Read(f"/data/clients/{CLIENT_ID}/analyses/ads/ads-campaign-analysis-{timestamp}.json")
```

### Generate Charts as PNG Images

Use Bash to run Python scripts with matplotlib. Save charts to `/docs/marketing/{CLIENT_ID}/charts/`.

**Directory setup**: `mkdir -p /docs/marketing/{client-id}/charts`

**Naming convention**: `{chart-type}-{metric}-{timestamp}.png`

### Matplotlib Style Configuration

```python
plt.style.use('seaborn-v0_8-darkgrid')
plt.rcParams['font.size'] = 11
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['xtick.labelsize'] = 10
plt.rcParams['ytick.labelsize'] = 10
plt.rcParams['legend.fontsize'] = 11
plt.rcParams['figure.dpi'] = 100
plt.rcParams['savefig.dpi'] = 300
```

Use brand colors from `brand-guidelines.json` when available.

See `references/workflow-detail.md` for complete matplotlib chart examples (bar, line, pie, multi-bar).

## Visualization Types & When to Use

### 1. Bar Chart (Horizontal or Vertical)
**Best For**: Comparing values across categories (3-12 categories)
**Use Cases**: Platform performance, month-over-month metrics, campaign rankings
**Avoid**: More than 15 categories, showing trends over time

### 2. Grouped Bar Chart
**Best For**: Comparing multiple metrics across categories
**Use Cases**: Current vs target ROAS by platform, year-over-year by channel

### 3. Line Chart
**Best For**: Showing trends over time (5+ data points)
**Use Cases**: Performance over weeks/months, growth trends, before/after comparisons

### 4. Multi-Line Chart
**Best For**: Comparing trends across multiple series
**Use Cases**: ROAS trend by platform, traffic by source over time

### 5. Pie Chart (Use Sparingly)
**Best For**: Showing proportions of a whole (3-5 categories only)
**Use Cases**: Budget allocation, traffic sources, conversion breakdown
**Avoid**: More than 5 categories, similar-sized slices, precise comparison needed

### 6. Stacked Bar Chart
**Best For**: Part-to-whole comparisons across categories
**Use Cases**: Conversions by source and campaign type

### 7. Histogram
**Best For**: Showing frequency distribution
**Use Cases**: CPA distribution across campaigns, customer age distribution

### 8. Scatter Plot
**Best For**: Showing relationship between two variables
**Use Cases**: CPC vs Conversion Rate, Ad Spend vs ROAS

### 9. Bullet Chart
**Best For**: Showing performance against targets
**Use Cases**: Q1 metrics vs goals, KPI target tracking

### 10. Funnel Chart
**Best For**: Showing drop-off through stages
**Use Cases**: Customer journey (impressions -> clicks -> conversions -> purchases)

### 11. Waterfall Chart
**Best For**: Showing cumulative effect of sequential changes
**Use Cases**: Revenue impact breakdown by initiative

### 12. Heatmap/Matrix
**Best For**: Comparing two dimensions with color coding
**Use Cases**: Campaign performance matrix (CTR, CPC, Conv Rate, ROAS by campaign)

### 13. Gantt Chart (Simplified)
**Best For**: Project timelines and roadmaps
**Use Cases**: 90-day implementation roadmap with milestones

## Chart Selection Quick Reference

```
"How do things compare?"          -> Bar Chart
"How has it changed over time?"   -> Line Chart
"What's the composition?"         -> Stacked Bar / Pie
"What's the relationship?"        -> Scatter Plot
"How does it perform vs goal?"    -> Bullet Chart
"What's the distribution?"        -> Histogram
"What's the flow/process?"        -> Funnel
```

## Visualization Best Practices

### Rule 1: One Chart = One Insight
Keep each chart focused on a single question. Don't cram multiple dimensions into one visualization.

### Rule 2: Use Color Purposefully

**Semantic Colors**:
- Green (#28a745): Positive, success, above target
- Red (#dc3545): Negative, failure, below target
- Yellow (#ffc107): Warning, caution, neutral
- Blue (#007bff): Informational, emphasis

**Category Colors**: Use distinct, contrasting colors for categories. Limit to 5-6 colors max. Use consistently across all charts.

**Accessibility**: High contrast, don't rely solely on color (use patterns and labels too).

### Rule 3: Label Clearly

Required labels for every chart:
1. Chart title (what is being shown)
2. Axis labels (X and Y)
3. Units (dollars, percent, count)
4. Data values (on or near bars/points)
5. Legend (if multiple series)
6. Data source/date (footer)

### Rule 4: Maintain Consistent Scale
Use the same Y-axis range when comparing related charts. Exception: vastly different ranges may use logarithmic scale (clearly noted).

### Rule 5: Start Y-Axis at Zero (Usually)
Truncated axes make small changes look dramatic. Exception: stock prices, temperature, and similar data where truncation is standard (clearly labeled).

### Rule 6: Order Matters
- Descending order for rankings (highest to lowest)
- Chronological for time-based data
- Never random order

### Rule 7: Add Annotations for Context
Annotate outliers ("Campaign paused mid-month"), inflection points ("Algorithm change"), targets ("Industry average"), and key events ("Black Friday").

### Rule 8: Avoid Chart Junk
No 3D effects, excessive gridlines, decorative images, unnecessary borders, or redundant legends. Keep flat/2D, minimal gridlines, essential colors only.

### Rule 9: Every Chart Tells a Story
Each chart should answer three questions:
1. **What**: What is this showing?
2. **So What**: Why does it matter?
3. **Now What**: What action should be taken?

## Platform-Specific Considerations

### For Presentations
- Larger fonts (18pt+ for labels)
- High contrast colors
- Simple charts (bar, line only)
- Minimal data points
- Titles visible from 10 feet away

### For Dashboards
- Real-time data support
- Interactive elements
- Multiple small charts (overview)
- Color-coded status indicators
- Drill-down capability

### For Reports
- Detailed axes and labels
- Data source citations
- Multiple series OK
- More complexity acceptable
- Print-friendly colors (avoid neon)

## Text-Based Charts (Markdown/ASCII)

Use text-based charts for markdown presentations, email reports, and terminal dashboards. See `references/workflow-detail.md` for Unicode box drawing characters and text chart templates.

## Validation Checklist

Before finalizing any data visualization:
- Chart type appropriate for data?
- Title clear and descriptive?
- Axes labeled with units?
- Data values shown or easily readable?
- Colors used purposefully and accessibly?
- Scale consistent and not misleading?
- Legend included (if needed)?
- Annotations for key points?
- Source and date noted?
- Chart tells a clear story?
- Action/recommendation clear?

## Agent Workflow

```
1. Read this skill file
2. Receive data to visualize (from analysis skills)
3. Determine:
   - What question does this data answer?
   - Who is the audience?
   - What format is needed? (presentation, dashboard, report)
4. Select appropriate chart type
5. Create visualization following best practices
6. Add labels, colors, annotations
7. Validate using checklist
8. Output in requested format (PNG, markdown, ASCII)
```

## Integration with Other Skills

**Used by**:
- `presentation-creation` skill for charts in presentations
- `dashboard-creation` skill for dashboard widgets
- All analysis skills (GEO, SEO, Ads) for visualizing results
