# Marketing Dashboard Creation

## Purpose
Create interactive marketing dashboards to monitor real-time performance, track KPIs, visualize trends, and provide at-a-glance insights for marketing teams and executives.

---

## Execution Modes

### SIMPLE Mode (15-20 minutes)
**Goal**: Create basic static dashboard with key metrics
**Scope**: 5-10 KPI cards + 2-3 simple charts
**Output**: Single-page HTML dashboard (no backend required)

### COMPREHENSIVE Mode (45-60 minutes)
**Goal**: Create interactive dashboard with multiple sections and drill-down capability
**Scope**: 15-25 widgets, multiple pages, interactive filters
**Output**: React-based dashboard with modular components

---

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

---

## Dashboard Types

### Type 1: Executive Overview Dashboard
```
Purpose: High-level performance at-a-glance
Audience: C-level, busy executives
Update Frequency: Daily or weekly
Key Features:
- Overall health score
- Top 3-5 KPIs
- Week-over-week trends
- Red flags / alerts
- Quick action items
```

### Type 2: Campaign Performance Dashboard
```
Purpose: Monitor active campaign metrics
Audience: Marketing managers, campaign teams
Update Frequency: Real-time or hourly
Key Features:
- Campaign-level metrics
- Platform comparison
- Budget pacing
- Conversion funnel
- Creative performance
```

### Type 3: Channel Analytics Dashboard
```
Purpose: Deep-dive into specific channels (SEO, Paid, GEO)
Audience: Channel specialists
Update Frequency: Daily
Key Features:
- Channel-specific metrics
- Trend analysis
- Competitive benchmarking
- Optimization opportunities
- Historical comparisons
```

### Type 4: Client Reporting Dashboard
```
Purpose: Transparent performance reporting for clients
Audience: External clients, stakeholders
Update Frequency: Weekly or monthly
Key Features:
- Client-specific branding
- ROI highlights
- Goal tracking
- Visual storytelling
- Export functionality
```

---

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

**Dashboard Layout Planning**:

```
SIMPLE Mode Layout:
┌─────────────────────────────────────────┐
│  HEADER: Marketing Performance         │
│  Date Range: Jan 1-31, 2024             │
├─────────────────────────────────────────┤
│ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐   │
│ │ KPI1 │ │ KPI2 │ │ KPI3 │ │ KPI4 │   │
│ └──────┘ └──────┘ └──────┘ └──────┘   │
├─────────────────────────────────────────┤
│ ┌────────────────┐ ┌────────────────┐  │
│ │  Chart 1:      │ │  Chart 2:      │  │
│ │  ROAS Trend    │ │  Traffic by    │  │
│ │                │ │  Source        │  │
│ └────────────────┘ └────────────────┘  │
├─────────────────────────────────────────┤
│ ┌──────────────────────────────────┐   │
│ │  Table: Top Campaigns            │   │
│ └──────────────────────────────────┘   │
└─────────────────────────────────────────┘

COMPREHENSIVE Mode Layout:
┌─────────────────────────────────────────┐
│  HEADER + NAVIGATION TABS               │
│  [Overview] [Paid] [SEO] [GEO] [Goals]  │
├─────────────────────────────────────────┤
│  FILTERS: Date Range | Platform | ...  │
├─────────────────────────────────────────┤
│ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐│
│ │KPI 1│ │KPI 2│ │KPI 3│ │KPI 4│ │KPI 5││
│ └─────┘ └─────┘ └─────┘ └─────┘ └─────┘│
├─────────────────────────────────────────┤
│ ┌─────────────┐ ┌─────────────┐        │
│ │  Chart 1    │ │  Chart 2    │        │
│ └─────────────┘ └─────────────┘        │
│ ┌─────────────┐ ┌─────────────┐        │
│ │  Chart 3    │ │  Chart 4    │        │
│ └─────────────┘ └─────────────┘        │
├─────────────────────────────────────────┤
│ ┌──────────────────────────────────┐   │
│ │  Data Table (sortable, filterable) │   │
│ └──────────────────────────────────┘   │
└─────────────────────────────────────────┘
```

---

### Step 2: Load and Prepare Data

**Data Loading**:

```javascript
// Read data from analysis files
const geoData = JSON.parse(readFile('/data/geo/strategy-synthesis-acme-deep.json'));
const adsData = JSON.parse(readFile('/data/ads/campaign-analysis-acme-deep.json'));
const seoData = JSON.parse(readFile('/data/seo/tech-audit-acme-comprehensive.json'));

// Extract key metrics
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
    topPerformers: adsData.campaigns
      .sort((a, b) => b.roas - a.roas)
      .slice(0, 10)
  }
};
```

---

### Step 3: Create Widget Components

#### Widget Type 1: KPI Card

**Purpose**: Display single metric with trend

**HTML/CSS Example**:
```html
<div class="kpi-card">
  <div class="kpi-header">
    <span class="kpi-title">Total Revenue</span>
    <span class="kpi-trend positive">↑ 12%</span>
  </div>
  <div class="kpi-value">$135,000</div>
  <div class="kpi-subtitle">vs last month: $120,500</div>
  <div class="kpi-sparkline">
    <!-- Mini trend chart -->
    <svg>...</svg>
  </div>
</div>

<style>
.kpi-card {
  background: white;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}
.kpi-value {
  font-size: 32px;
  font-weight: bold;
  color: #333;
  margin: 10px 0;
}
.kpi-trend.positive {
  color: #28a745;
  font-weight: bold;
}
.kpi-trend.negative {
  color: #dc3545;
}
</style>
```

**React Component Example**:
```jsx
const KPICard = ({ title, value, change, changePercent, subtitle, trend }) => {
  const trendClass = change >= 0 ? 'positive' : 'negative';
  const trendIcon = change >= 0 ? '↑' : '↓';

  return (
    <div className="kpi-card">
      <div className="kpi-header">
        <span className="kpi-title">{title}</span>
        <span className={`kpi-trend ${trendClass}`}>
          {trendIcon} {Math.abs(changePercent)}%
        </span>
      </div>
      <div className="kpi-value">{value}</div>
      <div className="kpi-subtitle">{subtitle}</div>
      {trend && <Sparkline data={trend} />}
    </div>
  );
};

// Usage:
<KPICard
  title="Total Revenue"
  value="$135,000"
  change={14500}
  changePercent={12}
  subtitle="vs last month: $120,500"
  trend={[96, 105, 112, 120, 135]}
/>
```

---

#### Widget Type 2: Alert/Status Indicator

**Purpose**: Highlight issues or wins

**Example**:
```html
<div class="alert alert-danger">
  <span class="alert-icon">⚠️</span>
  <div class="alert-content">
    <strong>Budget Alert:</strong> LinkedIn campaign exceeding budget by 15% ($750)
    <button class="alert-action">View Campaign</button>
  </div>
</div>

<div class="alert alert-success">
  <span class="alert-icon">✅</span>
  <div class="alert-content">
    <strong>Win:</strong> Google Ads ROAS increased 23% this week (4.2 → 5.2)
  </div>
</div>

<style>
.alert {
  padding: 15px;
  border-radius: 6px;
  margin-bottom: 15px;
  display: flex;
  align-items: center;
}
.alert-danger {
  background-color: #f8d7da;
  border-left: 4px solid #dc3545;
}
.alert-success {
  background-color: #d4edda;
  border-left: 4px solid #28a745;
}
.alert-icon {
  font-size: 24px;
  margin-right: 15px;
}
</style>
```

---

#### Widget Type 3: Progress Bar/Goal Tracker

**Purpose**: Show progress toward goals

**Example**:
```html
<div class="goal-tracker">
  <div class="goal-header">
    <span class="goal-title">Q1 Revenue Goal</span>
    <span class="goal-percentage">78% Complete</span>
  </div>
  <div class="progress-bar">
    <div class="progress-fill" style="width: 78%"></div>
  </div>
  <div class="goal-details">
    $312,000 of $400,000 target
    <span class="goal-remaining">$88,000 remaining</span>
  </div>
</div>

<style>
.progress-bar {
  height: 20px;
  background-color: #e9ecef;
  border-radius: 10px;
  overflow: hidden;
  margin: 10px 0;
}
.progress-fill {
  height: 100%;
  background: linear-gradient(90deg, #28a745, #20c997);
  transition: width 0.3s ease;
}
</style>
```

---

#### Widget Type 4: Comparison Table

**Purpose**: Compare metrics across categories

**Example**:
```html
<table class="comparison-table">
  <thead>
    <tr>
      <th>Platform</th>
      <th>Spend</th>
      <th>Conversions</th>
      <th>CPA</th>
      <th>ROAS</th>
      <th>Status</th>
    </tr>
  </thead>
  <tbody>
    <tr class="row-excellent">
      <td><strong>Google Ads</strong></td>
      <td>$15,000</td>
      <td>450</td>
      <td>$33.33</td>
      <td class="metric-excellent">4.2</td>
      <td><span class="badge badge-success">Excellent</span></td>
    </tr>
    <tr class="row-good">
      <td><strong>Meta Ads</strong></td>
      <td>$10,000</td>
      <td>320</td>
      <td>$31.25</td>
      <td class="metric-good">3.5</td>
      <td><span class="badge badge-success">Good</span></td>
    </tr>
    <tr class="row-poor">
      <td><strong>LinkedIn Ads</strong></td>
      <td>$5,000</td>
      <td>80</td>
      <td>$62.50</td>
      <td class="metric-poor">1.8</td>
      <td><span class="badge badge-danger">Poor</span></td>
    </tr>
  </tbody>
</table>

<style>
.comparison-table {
  width: 100%;
  border-collapse: collapse;
  background: white;
}
.comparison-table th {
  background-color: #f8f9fa;
  padding: 12px;
  text-align: left;
  font-weight: 600;
  border-bottom: 2px solid #dee2e6;
}
.comparison-table td {
  padding: 12px;
  border-bottom: 1px solid #dee2e6;
}
.row-excellent { background-color: #d4edda; }
.row-good { background-color: #fff3cd; }
.row-poor { background-color: #f8d7da; }
.metric-excellent { color: #28a745; font-weight: bold; }
.metric-poor { color: #dc3545; font-weight: bold; }
</style>
```

---

#### Widget Type 5: Chart Widget

**Using Chart.js for interactive charts**:

```html
<div class="chart-widget">
  <div class="chart-header">
    <h3>ROAS Trend - Last 90 Days</h3>
    <select class="chart-filter">
      <option>All Platforms</option>
      <option>Google Ads</option>
      <option>Meta Ads</option>
    </select>
  </div>
  <canvas id="roasTrendChart"></canvas>
</div>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
const ctx = document.getElementById('roasTrendChart').getContext('2d');
const roasTrendChart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    datasets: [{
      label: 'Google Ads',
      data: [2.8, 3.2, 3.5, 3.9, 4.1, 4.2],
      borderColor: '#007bff',
      backgroundColor: 'rgba(0, 123, 255, 0.1)',
      tension: 0.4
    }, {
      label: 'Meta Ads',
      data: [2.5, 2.8, 3.0, 3.2, 3.4, 3.5],
      borderColor: '#28a745',
      backgroundColor: 'rgba(40, 167, 69, 0.1)',
      tension: 0.4
    }]
  },
  options: {
    responsive: true,
    plugins: {
      legend: {
        position: 'top',
      },
      title: {
        display: false
      }
    },
    scales: {
      y: {
        beginAtZero: true,
        title: {
          display: true,
          text: 'ROAS'
        }
      }
    }
  }
});
</script>
```

---

### Step 4: Build Complete Dashboard

**SIMPLE Mode - Static HTML Dashboard**:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Marketing Performance Dashboard - AcmeCorp</title>
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }
    body {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;
      background-color: #f5f5f5;
      padding: 20px;
    }
    .dashboard-header {
      background: white;
      padding: 20px 30px;
      border-radius: 8px;
      margin-bottom: 20px;
      box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .dashboard-header h1 {
      font-size: 28px;
      color: #333;
    }
    .dashboard-subtitle {
      color: #666;
      margin-top: 5px;
    }
    .kpi-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 20px;
      margin-bottom: 20px;
    }
    .kpi-card {
      background: white;
      border-radius: 8px;
      padding: 20px;
      box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .kpi-title {
      font-size: 14px;
      color: #666;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }
    .kpi-value {
      font-size: 36px;
      font-weight: bold;
      color: #333;
      margin: 10px 0;
    }
    .kpi-change {
      font-size: 14px;
      font-weight: 600;
    }
    .kpi-change.positive {
      color: #28a745;
    }
    .kpi-change.negative {
      color: #dc3545;
    }
    .charts-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
      gap: 20px;
      margin-bottom: 20px;
    }
    .chart-card {
      background: white;
      border-radius: 8px;
      padding: 20px;
      box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .chart-card h3 {
      margin-bottom: 15px;
      color: #333;
    }
    .table-card {
      background: white;
      border-radius: 8px;
      padding: 20px;
      box-shadow: 0 2px 4px rgba(0,0,0,0.1);
      overflow-x: auto;
    }
    table {
      width: 100%;
      border-collapse: collapse;
    }
    th, td {
      padding: 12px;
      text-align: left;
      border-bottom: 1px solid #eee;
    }
    th {
      background-color: #f8f9fa;
      font-weight: 600;
    }
    .badge {
      padding: 4px 8px;
      border-radius: 4px;
      font-size: 12px;
      font-weight: 600;
    }
    .badge-success {
      background-color: #d4edda;
      color: #155724;
    }
    .badge-danger {
      background-color: #f8d7da;
      color: #721c24;
    }
  </style>
</head>
<body>
  <div class="dashboard-header">
    <h1>📊 Marketing Performance Dashboard</h1>
    <p class="dashboard-subtitle">AcmeCorp - January 2024</p>
  </div>

  <!-- KPI Cards -->
  <div class="kpi-grid">
    <div class="kpi-card">
      <div class="kpi-title">Total Revenue</div>
      <div class="kpi-value">$135,000</div>
      <div class="kpi-change positive">↑ 12% vs last month</div>
    </div>
    <div class="kpi-card">
      <div class="kpi-title">Overall ROAS</div>
      <div class="kpi-value">4.2</div>
      <div class="kpi-change positive">↑ 31% vs last month</div>
    </div>
    <div class="kpi-card">
      <div class="kpi-title">Conversions</div>
      <div class="kpi-value">850</div>
      <div class="kpi-change positive">↑ 22% vs last month</div>
    </div>
    <div class="kpi-card">
      <div class="kpi-title">Cost Per Acquisition</div>
      <div class="kpi-value">$35</div>
      <div class="kpi-change positive">↓ 18% vs last month</div>
    </div>
  </div>

  <!-- Charts -->
  <div class="charts-grid">
    <div class="chart-card">
      <h3>ROAS by Platform</h3>
      <canvas id="roasByPlatform"></canvas>
    </div>
    <div class="chart-card">
      <h3>Monthly Revenue Trend</h3>
      <canvas id="revenueTrend"></canvas>
    </div>
  </div>

  <!-- Campaign Table -->
  <div class="table-card">
    <h3>Top Campaigns</h3>
    <table>
      <thead>
        <tr>
          <th>Campaign</th>
          <th>Platform</th>
          <th>Spend</th>
          <th>Conversions</th>
          <th>ROAS</th>
          <th>Status</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Brand Search</strong></td>
          <td>Google Ads</td>
          <td>$8,000</td>
          <td>180</td>
          <td>5.8</td>
          <td><span class="badge badge-success">Excellent</span></td>
        </tr>
        <tr>
          <td><strong>Retargeting</strong></td>
          <td>Meta Ads</td>
          <td>$3,500</td>
          <td>95</td>
          <td>4.5</td>
          <td><span class="badge badge-success">Excellent</span></td>
        </tr>
        <tr>
          <td><strong>Non-Brand Search</strong></td>
          <td>Google Ads</td>
          <td>$5,000</td>
          <td>85</td>
          <td>3.8</td>
          <td><span class="badge badge-success">Good</span></td>
        </tr>
        <tr>
          <td><strong>Cold Audience</strong></td>
          <td>LinkedIn Ads</td>
          <td>$2,500</td>
          <td>12</td>
          <td>0.6</td>
          <td><span class="badge badge-danger">Poor</span></td>
        </tr>
      </tbody>
    </table>
  </div>

  <script>
    // ROAS by Platform Chart
    const ctxPlatform = document.getElementById('roasByPlatform').getContext('2d');
    new Chart(ctxPlatform, {
      type: 'bar',
      data: {
        labels: ['Google Ads', 'Meta Ads', 'LinkedIn Ads'],
        datasets: [{
          label: 'ROAS',
          data: [4.2, 3.5, 1.8],
          backgroundColor: ['#007bff', '#28a745', '#ffc107']
        }]
      },
      options: {
        responsive: true,
        plugins: {
          legend: { display: false }
        },
        scales: {
          y: {
            beginAtZero: true,
            title: {
              display: true,
              text: 'ROAS'
            }
          }
        }
      }
    });

    // Revenue Trend Chart
    const ctxRevenue = document.getElementById('revenueTrend').getContext('2d');
    new Chart(ctxRevenue, {
      type: 'line',
      data: {
        labels: ['Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Jan'],
        datasets: [{
          label: 'Revenue',
          data: [96000, 105000, 112000, 118000, 125000, 135000],
          borderColor: '#28a745',
          backgroundColor: 'rgba(40, 167, 69, 0.1)',
          tension: 0.4,
          fill: true
        }]
      },
      options: {
        responsive: true,
        plugins: {
          legend: { display: false }
        },
        scales: {
          y: {
            beginAtZero: true,
            ticks: {
              callback: function(value) {
                return '$' + (value/1000) + 'K';
              }
            }
          }
        }
      }
    });
  </script>
</body>
</html>
```

---

### Step 5: Add Interactivity (COMPREHENSIVE Mode)

**React Dashboard with Filters**:

```jsx
import React, { useState } from 'react';
import { Line, Bar, Doughnut } from 'react-chartjs-2';

const MarketingDashboard = () => {
  const [dateRange, setDateRange] = useState('30days');
  const [platform, setPlatform] = useState('all');

  // Filter data based on selections
  const filteredData = filterData(rawData, { dateRange, platform });

  return (
    <div className="dashboard">
      <Header />

      <Filters
        dateRange={dateRange}
        setDateRange={setDateRange}
        platform={platform}
        setPlatform={setPlatform}
      />

      <KPIGrid data={filteredData.kpis} />

      <div className="charts-grid">
        <ChartCard title="ROAS Trend">
          <Line data={filteredData.roasTrend} options={lineOptions} />
        </ChartCard>

        <ChartCard title="Platform Comparison">
          <Bar data={filteredData.platformComp} options={barOptions} />
        </ChartCard>

        <ChartCard title="Budget Allocation">
          <Doughnut data={filteredData.budgetAlloc} options={doughnutOptions} />
        </ChartCard>

        <ChartCard title="Conversion Funnel">
          <FunnelChart data={filteredData.funnel} />
        </ChartCard>
      </div>

      <CampaignTable data={filteredData.campaigns} />

      <AlertsSection alerts={filteredData.alerts} />
    </div>
  );
};

const Filters = ({ dateRange, setDateRange, platform, setPlatform }) => (
  <div className="filters">
    <select value={dateRange} onChange={(e) => setDateRange(e.target.value)}>
      <option value="7days">Last 7 Days</option>
      <option value="30days">Last 30 Days</option>
      <option value="90days">Last 90 Days</option>
      <option value="custom">Custom Range</option>
    </select>

    <select value={platform} onChange={(e) => setPlatform(e.target.value)}>
      <option value="all">All Platforms</option>
      <option value="google">Google Ads</option>
      <option value="meta">Meta Ads</option>
      <option value="linkedin">LinkedIn Ads</option>
    </select>
  </div>
);
```

---

### Step 6: Add Export Functionality

**Export to PDF/Image**:

```javascript
// Using html2canvas and jsPDF
import html2canvas from 'html2canvas';
import jsPDF from 'jspdf';

const exportDashboardToPDF = async () => {
  const dashboard = document.getElementById('dashboard');

  const canvas = await html2canvas(dashboard, {
    scale: 2,
    logging: false,
    useCORS: true
  });

  const imgData = canvas.toDataURL('image/png');
  const pdf = new jsPDF('p', 'mm', 'a4');

  const imgWidth = 210; // A4 width in mm
  const imgHeight = (canvas.height * imgWidth) / canvas.width;

  pdf.addImage(imgData, 'PNG', 0, 0, imgWidth, imgHeight);
  pdf.save('marketing-dashboard.pdf');
};

// Export button
<button onClick={exportDashboardToPDF} className="export-btn">
  📥 Export as PDF
</button>
```

---

### Step 7: Responsive Design

**Mobile-Friendly CSS**:

```css
/* Mobile Responsiveness */
@media (max-width: 768px) {
  .kpi-grid {
    grid-template-columns: repeat(2, 1fr);
  }

  .charts-grid {
    grid-template-columns: 1fr;
  }

  .kpi-value {
    font-size: 24px;
  }

  table {
    font-size: 12px;
  }

  th, td {
    padding: 8px;
  }
}

@media (max-width: 480px) {
  .kpi-grid {
    grid-template-columns: 1fr;
  }

  .dashboard-header h1 {
    font-size: 20px;
  }

  .kpi-value {
    font-size: 20px;
  }
}
```

---

### Step 8: Real-Time Data Updates

**Using WebSocket or Polling**:

```javascript
// Polling approach (every 30 seconds)
useEffect(() => {
  const fetchData = async () => {
    const response = await fetch('/api/dashboard-data');
    const data = await response.json();
    setDashboardData(data);
  };

  // Initial fetch
  fetchData();

  // Set up polling
  const interval = setInterval(fetchData, 30000); // 30 seconds

  return () => clearInterval(interval);
}, []);

// WebSocket approach (real-time)
useEffect(() => {
  const ws = new WebSocket('wss://your-server.com/dashboard');

  ws.onmessage = (event) => {
    const data = JSON.parse(event.data);
    setDashboardData(data);
  };

  return () => ws.close();
}, []);
```

---

### Step 9: Output Generation

**Output Files**:

```
/output/dashboards/{company}-marketing-dashboard.html
  - Self-contained HTML file with inline CSS and JS
  - Can be opened directly in browser
  - No dependencies required

/output/dashboards/{company}-dashboard-react/
  - Full React project structure
  - src/components/KPICard.jsx
  - src/components/ChartWidget.jsx
  - src/App.jsx
  - package.json
  - README.md with setup instructions
```

---

## Validation Checks

```
✓ All KPIs displayed with correct values
✓ Charts render correctly and show accurate data
✓ Responsive design works on mobile/tablet/desktop
✓ Colors follow brand guidelines
✓ Data sources are cited
✓ Export functionality works (if included)
✓ Filters update dashboard correctly (COMPREHENSIVE mode)
✓ No broken links or missing images
✓ Loading states handled gracefully
✓ Accessibility (screen reader friendly, color contrast)
```

---

## Usage Example

**Agent Workflow**:
```
1. Read this skill file
2. Load data from analysis files (/data/)
3. Determine dashboard type (Executive, Campaign, Channel, Client)
4. Determine mode (SIMPLE or COMPREHENSIVE)
5. Use TodoWrite to track creation:
   [ ] Define scope and layout
   [ ] Load and prepare data
   [ ] Create KPI cards
   [ ] Create charts
   [ ] Build tables
   [ ] Add interactivity (COMPREHENSIVE)
   [ ] Test responsiveness
   [ ] Export functionality
   [ ] Validation
   [ ] Output generation
6. Build dashboard (HTML or React)
7. Save to /output/dashboards/
8. Provide summary and instructions
```

---

## Integration with Other Skills

**Requires data from**:
- All analysis skills (GEO, SEO, Ads, Competitor)
- **data-visualization.md** - For chart guidance

**Outputs used by**:
- Marketing teams for daily monitoring
- Executives for performance overview
- Clients for transparency and reporting

---

## MCP Tools Needed

**Current**: Built-in tools sufficient for static dashboards

**Future Enhancement**:
- `mcp__Dashboard__data_connector` - Connect to live data sources (Google Ads API, Meta Ads API, etc.)
- `mcp__Dashboard__chart_library` - Pre-built chart components
- `mcp__Dashboard__template_gallery` - Ready-made dashboard templates
