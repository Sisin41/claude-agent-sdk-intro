# Dashboard Creation - Detailed Reference

This file contains full code examples, templates, and layout diagrams for the dashboard-creation skill.

## Layout Diagrams

### Light Mode Layout

```
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
```

### Deep Mode Layout

```
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

## Widget Type 1: KPI Card

### HTML/CSS Example

```html
<div class="kpi-card">
  <div class="kpi-header">
    <span class="kpi-title">Total Revenue</span>
    <span class="kpi-trend positive">↑ 12%</span>
  </div>
  <div class="kpi-value">$135,000</div>
  <div class="kpi-subtitle">vs last month: $120,500</div>
  <div class="kpi-sparkline">
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
.kpi-trend.positive { color: #28a745; font-weight: bold; }
.kpi-trend.negative { color: #dc3545; }
</style>
```

### React Component

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

## Widget Type 2: Alert/Status Indicator

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
.alert-icon { font-size: 24px; margin-right: 15px; }
</style>
```

---

## Widget Type 3: Progress Bar/Goal Tracker

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

## Widget Type 4: Comparison Table

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
.comparison-table { width: 100%; border-collapse: collapse; background: white; }
.comparison-table th {
  background-color: #f8f9fa; padding: 12px; text-align: left;
  font-weight: 600; border-bottom: 2px solid #dee2e6;
}
.comparison-table td { padding: 12px; border-bottom: 1px solid #dee2e6; }
.row-excellent { background-color: #d4edda; }
.row-good { background-color: #fff3cd; }
.row-poor { background-color: #f8d7da; }
.metric-excellent { color: #28a745; font-weight: bold; }
.metric-poor { color: #dc3545; font-weight: bold; }
</style>
```

---

## Widget Type 5: Chart Widget (Chart.js)

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
    plugins: { legend: { position: 'top' }, title: { display: false } },
    scales: {
      y: { beginAtZero: true, title: { display: true, text: 'ROAS' } }
    }
  }
});
</script>
```

---

## Full Light Mode HTML Dashboard Template

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Marketing Performance Dashboard - AcmeCorp</title>
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;
      background-color: #f5f5f5; padding: 20px;
    }
    .dashboard-header {
      background: white; padding: 20px 30px; border-radius: 8px;
      margin-bottom: 20px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .dashboard-header h1 { font-size: 28px; color: #333; }
    .dashboard-subtitle { color: #666; margin-top: 5px; }
    .kpi-grid {
      display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 20px; margin-bottom: 20px;
    }
    .kpi-card {
      background: white; border-radius: 8px; padding: 20px;
      box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .kpi-title { font-size: 14px; color: #666; text-transform: uppercase; letter-spacing: 0.5px; }
    .kpi-value { font-size: 36px; font-weight: bold; color: #333; margin: 10px 0; }
    .kpi-change { font-size: 14px; font-weight: 600; }
    .kpi-change.positive { color: #28a745; }
    .kpi-change.negative { color: #dc3545; }
    .charts-grid {
      display: grid; grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
      gap: 20px; margin-bottom: 20px;
    }
    .chart-card {
      background: white; border-radius: 8px; padding: 20px;
      box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .chart-card h3 { margin-bottom: 15px; color: #333; }
    .table-card {
      background: white; border-radius: 8px; padding: 20px;
      box-shadow: 0 2px 4px rgba(0,0,0,0.1); overflow-x: auto;
    }
    table { width: 100%; border-collapse: collapse; }
    th, td { padding: 12px; text-align: left; border-bottom: 1px solid #eee; }
    th { background-color: #f8f9fa; font-weight: 600; }
    .badge { padding: 4px 8px; border-radius: 4px; font-size: 12px; font-weight: 600; }
    .badge-success { background-color: #d4edda; color: #155724; }
    .badge-danger { background-color: #f8d7da; color: #721c24; }

    @media (max-width: 768px) {
      .kpi-grid { grid-template-columns: repeat(2, 1fr); }
      .charts-grid { grid-template-columns: 1fr; }
      .kpi-value { font-size: 24px; }
      table { font-size: 12px; }
      th, td { padding: 8px; }
    }
    @media (max-width: 480px) {
      .kpi-grid { grid-template-columns: 1fr; }
      .dashboard-header h1 { font-size: 20px; }
      .kpi-value { font-size: 20px; }
    }
  </style>
</head>
<body>
  <div class="dashboard-header">
    <h1>Marketing Performance Dashboard</h1>
    <p class="dashboard-subtitle">AcmeCorp - January 2024</p>
  </div>

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

  <div class="table-card">
    <h3>Top Campaigns</h3>
    <table>
      <thead>
        <tr>
          <th>Campaign</th><th>Platform</th><th>Spend</th>
          <th>Conversions</th><th>ROAS</th><th>Status</th>
        </tr>
      </thead>
      <tbody>
        <!-- Populate from data -->
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
        datasets: [{ label: 'ROAS', data: [4.2, 3.5, 1.8], backgroundColor: ['#007bff', '#28a745', '#ffc107'] }]
      },
      options: {
        responsive: true,
        plugins: { legend: { display: false } },
        scales: { y: { beginAtZero: true, title: { display: true, text: 'ROAS' } } }
      }
    });

    // Revenue Trend Chart
    const ctxRevenue = document.getElementById('revenueTrend').getContext('2d');
    new Chart(ctxRevenue, {
      type: 'line',
      data: {
        labels: ['Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Jan'],
        datasets: [{
          label: 'Revenue', data: [96000, 105000, 112000, 118000, 125000, 135000],
          borderColor: '#28a745', backgroundColor: 'rgba(40, 167, 69, 0.1)', tension: 0.4, fill: true
        }]
      },
      options: {
        responsive: true,
        plugins: { legend: { display: false } },
        scales: { y: { beginAtZero: true, ticks: { callback: function(value) { return '$' + (value/1000) + 'K'; } } } }
      }
    });
  </script>
</body>
</html>
```

---

## Deep Mode React Dashboard Example

```jsx
import React, { useState } from 'react';
import { Line, Bar, Doughnut } from 'react-chartjs-2';

const MarketingDashboard = () => {
  const [dateRange, setDateRange] = useState('30days');
  const [platform, setPlatform] = useState('all');

  const filteredData = filterData(rawData, { dateRange, platform });

  return (
    <div className="dashboard">
      <Header />
      <Filters
        dateRange={dateRange} setDateRange={setDateRange}
        platform={platform} setPlatform={setPlatform}
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

## Real-Time Data Updates

### Polling Approach

```javascript
useEffect(() => {
  const fetchData = async () => {
    const response = await fetch('/api/dashboard-data');
    const data = await response.json();
    setDashboardData(data);
  };
  fetchData();
  const interval = setInterval(fetchData, 30000);
  return () => clearInterval(interval);
}, []);
```

### WebSocket Approach

```javascript
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

## Export Functionality

```javascript
import html2canvas from 'html2canvas';
import jsPDF from 'jspdf';

const exportDashboardToPDF = async () => {
  const dashboard = document.getElementById('dashboard');
  const canvas = await html2canvas(dashboard, { scale: 2, logging: false, useCORS: true });
  const imgData = canvas.toDataURL('image/png');
  const pdf = new jsPDF('p', 'mm', 'a4');
  const imgWidth = 210;
  const imgHeight = (canvas.height * imgWidth) / canvas.width;
  pdf.addImage(imgData, 'PNG', 0, 0, imgWidth, imgHeight);
  pdf.save('marketing-dashboard.pdf');
};
```
