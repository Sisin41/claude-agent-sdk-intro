---
name: dashboard-creation
description: Create interactive marketing dashboards to monitor real-time performance, track KPIs, visualize trends, and provide at-a-glance insights. Use when building HTML or React-based dashboards from analysis data for marketing teams, executives, or clients.
metadata:
  author: castor
  version: "1.0"
  domain: dashboard
  execution-modes: light, deep
---

# Marketing Dashboard Creation

## Purpose

Create interactive marketing dashboards to monitor real-time performance, track KPIs, visualize trends, and provide at-a-glance insights for marketing teams and executives.

## Execution Modes

### Light Mode (15-20 minutes)
**Goal**: Create basic static dashboard with key metrics
**Scope**: 5-10 KPI cards + 2-3 simple charts
**Output**: Single-page HTML dashboard (no backend required)

### Deep Mode (45-60 minutes)
**Goal**: Create interactive dashboard with multiple sections and drill-down capability
**Scope**: 15-25 widgets, multiple pages, interactive filters
**Output**: React-based dashboard with modular components

## Prerequisites

**Required Input**:
- Data source (JSON files from analysis skills OR CSV exports)
- Dashboard purpose (real-time monitoring, executive overview, campaign tracking)
- Target audience (marketing team, executives, clients)
- Update frequency (real-time, daily, weekly)

**Optional**:
- Brand colors and logo
- Historical data for trends
- Benchmark data for comparisons

## Dashboard Types

### Type 1: Executive Overview Dashboard
- **Audience**: C-level, busy executives
- **Update Frequency**: Daily or weekly
- **Features**: Overall health score, top 3-5 KPIs, week-over-week trends, red flags/alerts, quick action items

### Type 2: Campaign Performance Dashboard
- **Audience**: Marketing managers, campaign teams
- **Update Frequency**: Real-time or hourly
- **Features**: Campaign-level metrics, platform comparison, budget pacing, conversion funnel, creative performance

### Type 3: Channel Analytics Dashboard
- **Audience**: Channel specialists
- **Update Frequency**: Daily
- **Features**: Channel-specific metrics, trend analysis, competitive benchmarking, optimization opportunities

### Type 4: Client Reporting Dashboard
- **Audience**: External clients, stakeholders
- **Update Frequency**: Weekly or monthly
- **Features**: Client-specific branding, ROI highlights, goal tracking, visual storytelling, export functionality

## Workflow Steps

### Step 1: Define Dashboard Scope & Layout

**Identify Key Metrics**:

```
Primary KPIs (Always visible):
1. Overall Performance Score (0-100)
2. Monthly Revenue / ROAS
3. Total Conversions
4. Cost Per Acquisition
5. Month-over-Month Growth

Secondary Metrics (By category):
- Paid Ads: CTR, CPC, Impression Share
- SEO: Organic Traffic, Rankings, Backlinks
- GEO: AI Visibility %, Citation Quality
- Content: Engagement, Shares, Time on Page
```

**Layout**: Use grid-based layouts. Light mode uses a single page with KPI cards row, two-column chart grid, and a data table. Deep mode adds navigation tabs, filters, and multiple chart grids. See `references/workflow-detail.md` for full layout diagrams.

### Step 2: Load and Prepare Data

Read data from analysis files using direct file operations:

```javascript
// Read data files directly
const geoData = JSON.parse(readFile('/data/geo/strategy-synthesis-acme-deep.json'));
const adsData = JSON.parse(readFile('/data/ads/campaign-analysis-acme-deep.json'));
const seoData = JSON.parse(readFile('/data/seo/tech-audit-acme-comprehensive.json'));

// Extract key metrics into dashboardData object
const dashboardData = {
  overview: {
    totalRevenue: adsData.overall_performance.revenue,
    totalSpend: adsData.overall_performance.spend,
    roas: adsData.overall_performance.roas,
    conversions: adsData.overall_performance.conversions,
    healthScore: calculateOverallHealth([geoData, adsData, seoData])
  },
  trends: {
    revenueByMonth: extractTrend(adsData, 'revenue'),
    roasByPlatform: extractPlatformMetrics(adsData, 'roas')
  },
  campaigns: {
    topPerformers: adsData.campaigns.sort((a, b) => b.roas - a.roas).slice(0, 10)
  }
};
```

### Step 3: Create Widget Components

The dashboard uses 5 core widget types:

1. **KPI Card** - Display single metric with trend indicator and sparkline
2. **Alert/Status Indicator** - Highlight issues (red) or wins (green) with action buttons
3. **Progress Bar/Goal Tracker** - Show progress toward goals with percentage
4. **Comparison Table** - Compare metrics across categories with color-coded status badges
5. **Chart Widget** - Interactive charts using Chart.js (line, bar, doughnut, etc.)

See `references/workflow-detail.md` for complete HTML/CSS/React code for each widget type.

### Step 4: Build Complete Dashboard

**Light Mode** - Generate a self-contained HTML file with:
- Inline CSS (responsive grid layout)
- Chart.js CDN for charts
- KPI cards grid, charts grid, and campaign table
- No external dependencies

**Deep Mode** - Generate a React-based dashboard with:
- Modular component architecture (KPICard, ChartWidget, CampaignTable, etc.)
- Interactive filters (date range, platform)
- Navigation tabs (Overview, Paid, SEO, GEO, Goals)
- State management for filter interactions

See `references/workflow-detail.md` for full HTML template and React component examples.

### Step 5: Add Interactivity (Deep Mode)

- Date range filters (7 days, 30 days, 90 days, custom)
- Platform filters (All, Google Ads, Meta Ads, LinkedIn Ads)
- Sortable/filterable data tables
- Drill-down capability from KPI cards to detail views

### Step 6: Add Export Functionality

Use html2canvas and jsPDF for PDF/image export:

```javascript
const exportDashboardToPDF = async () => {
  const dashboard = document.getElementById('dashboard');
  const canvas = await html2canvas(dashboard, { scale: 2, useCORS: true });
  const imgData = canvas.toDataURL('image/png');
  const pdf = new jsPDF('p', 'mm', 'a4');
  const imgWidth = 210;
  const imgHeight = (canvas.height * imgWidth) / canvas.width;
  pdf.addImage(imgData, 'PNG', 0, 0, imgWidth, imgHeight);
  pdf.save('marketing-dashboard.pdf');
};
```

### Step 7: Responsive Design

Apply mobile-friendly CSS breakpoints:
- **Desktop** (default): Full grid layout
- **Tablet** (max-width: 768px): 2-column KPI grid, single-column charts
- **Mobile** (max-width: 480px): Single-column everything, reduced font sizes

### Step 8: Real-Time Data Updates (Deep Mode)

Use polling (every 30 seconds via `setInterval`) or WebSocket connections for live data. Include cleanup in React `useEffect` return.

### Step 9: Output Generation

```
Light Mode:
/output/dashboards/{company}-marketing-dashboard.html
  - Self-contained HTML with inline CSS and JS
  - Opens directly in browser, no dependencies

Deep Mode:
/output/dashboards/{company}-dashboard-react/
  - src/components/KPICard.jsx
  - src/components/ChartWidget.jsx
  - src/App.jsx
  - package.json
  - README.md with setup instructions
```

## Validation Checks

```
- All KPIs displayed with correct values
- Charts render correctly and show accurate data
- Responsive design works on mobile/tablet/desktop
- Colors follow brand guidelines
- Data sources are cited
- Export functionality works (if included)
- Filters update dashboard correctly (Deep mode)
- No broken links or missing images
- Loading states handled gracefully
- Accessibility (screen reader friendly, color contrast)
```

## Agent Workflow

```
1. Read this skill file
2. Load data from analysis files (/data/)
3. Determine dashboard type (Executive, Campaign, Channel, Client)
4. Determine mode (Light or Deep)
5. Track creation with TodoWrite:
   [ ] Define scope and layout
   [ ] Load and prepare data
   [ ] Create KPI cards
   [ ] Create charts
   [ ] Build tables
   [ ] Add interactivity (Deep)
   [ ] Test responsiveness
   [ ] Export functionality
   [ ] Validation
   [ ] Output generation
6. Build dashboard (HTML or React)
7. Save to /output/dashboards/
8. Provide summary and instructions
```

## Integration with Other Skills

**Requires data from**:
- All analysis skills (GEO, SEO, Ads, Competitor)
- `presentation-data-viz` skill for chart guidance

**Outputs used by**:
- Marketing teams for daily monitoring
- Executives for performance overview
- Clients for transparency and reporting
