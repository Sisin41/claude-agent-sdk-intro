# Visual Identity — Castor AI Reports

Standard brand identity for all generated reports.

## Color Palette

| Role | Hex | Usage |
|------|-----|-------|
| Primary | `#1a1a2e` | Headers, dark backgrounds |
| Secondary | `#16213e` | Section backgrounds, cards |
| Accent | `#0f3460` | Interactive elements, links |
| Highlight | `#e94560` | CTAs, alerts, important badges |
| Success | `#06d6a0` | Positive scores, green indicators |
| Warning | `#ffd166` | Moderate scores, yellow indicators |
| Danger | `#ef476f` | Low scores, red indicators, critical issues |
| Text Primary | `#eaeaea` | Body text on dark backgrounds |
| Text Secondary | `#a0a0b0` | Supporting text, captions |
| Background | `#0d1117` | Page background |
| Card BG | `#161b22` | Card/section backgrounds |
| Border | `#30363d` | Borders, dividers |

## Typography

```css
font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;

/* Headings */
h1 { font-size: 2rem; font-weight: 700; color: #eaeaea; }
h2 { font-size: 1.5rem; font-weight: 600; color: #eaeaea; border-bottom: 2px solid #e94560; padding-bottom: 8px; }
h3 { font-size: 1.15rem; font-weight: 600; color: #a0a0b0; }

/* Body */
body { font-size: 0.95rem; line-height: 1.6; color: #eaeaea; }
```

## Base HTML Template

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{{company_name}} — Marketing Audit Report</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      background: #0d1117;
      color: #eaeaea;
      line-height: 1.6;
      padding: 0;
    }
    .container { max-width: 900px; margin: 0 auto; padding: 40px 24px; }

    /* Header */
    .report-header {
      text-align: center;
      padding: 48px 24px;
      background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
      border-radius: 12px;
      margin-bottom: 32px;
    }
    .report-header h1 { font-size: 2rem; margin-bottom: 8px; }
    .report-header .subtitle { color: #a0a0b0; font-size: 1.1rem; }
    .report-header .date { color: #a0a0b0; font-size: 0.85rem; margin-top: 12px; }
    .report-header .badge {
      display: inline-block;
      margin-top: 16px;
      padding: 4px 16px;
      background: #e94560;
      color: white;
      border-radius: 20px;
      font-size: 0.75rem;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 1px;
    }

    /* Sections */
    .section {
      background: #161b22;
      border: 1px solid #30363d;
      border-radius: 12px;
      padding: 28px;
      margin-bottom: 24px;
    }
    .section h2 {
      font-size: 1.35rem;
      border-bottom: 2px solid #e94560;
      padding-bottom: 8px;
      margin-bottom: 20px;
    }

    /* Score Cards */
    .score-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 16px;
      margin: 16px 0;
    }
    .score-card {
      background: #0d1117;
      border: 1px solid #30363d;
      border-radius: 8px;
      padding: 20px;
      text-align: center;
    }
    .score-card .value {
      font-size: 2.2rem;
      font-weight: 700;
      margin: 8px 0;
    }
    .score-card .label { color: #a0a0b0; font-size: 0.85rem; }
    .score-card .trend { font-size: 0.8rem; margin-top: 4px; }
    .score-green .value { color: #06d6a0; }
    .score-yellow .value { color: #ffd166; }
    .score-red .value { color: #ef476f; }

    /* Bar Charts */
    .bar-chart { margin: 12px 0; }
    .bar-row {
      display: flex;
      align-items: center;
      margin: 8px 0;
    }
    .bar-label { width: 120px; font-size: 0.85rem; color: #a0a0b0; }
    .bar-track {
      flex: 1;
      height: 28px;
      background: #0d1117;
      border-radius: 4px;
      overflow: hidden;
      position: relative;
    }
    .bar-fill {
      height: 100%;
      border-radius: 4px;
      display: flex;
      align-items: center;
      padding-left: 8px;
      font-size: 0.8rem;
      font-weight: 600;
      color: white;
      min-width: fit-content;
    }

    /* Tables */
    table {
      width: 100%;
      border-collapse: collapse;
      margin: 12px 0;
    }
    th, td {
      padding: 10px 12px;
      text-align: left;
      border-bottom: 1px solid #30363d;
      font-size: 0.9rem;
    }
    th {
      color: #a0a0b0;
      font-weight: 600;
      font-size: 0.8rem;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }

    /* Badges */
    .badge-high { background: #ef476f22; color: #ef476f; padding: 2px 10px; border-radius: 12px; font-size: 0.75rem; font-weight: 600; }
    .badge-medium { background: #ffd16622; color: #ffd166; padding: 2px 10px; border-radius: 12px; font-size: 0.75rem; font-weight: 600; }
    .badge-low { background: #06d6a022; color: #06d6a0; padding: 2px 10px; border-radius: 12px; font-size: 0.75rem; font-weight: 600; }
    .badge-type { background: #0f346022; color: #5fa8d3; padding: 2px 10px; border-radius: 12px; font-size: 0.75rem; font-weight: 600; }

    /* Tags */
    .tag {
      display: inline-block;
      background: #30363d;
      color: #a0a0b0;
      padding: 2px 8px;
      border-radius: 4px;
      font-size: 0.75rem;
      margin: 2px;
    }

    /* Content Cards */
    .content-card {
      background: #0d1117;
      border: 1px solid #30363d;
      border-radius: 8px;
      padding: 20px;
      margin: 12px 0;
    }
    .content-card .card-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 12px;
    }
    .content-card .priority {
      background: #e94560;
      color: white;
      width: 28px;
      height: 28px;
      border-radius: 50%;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      font-size: 0.85rem;
      font-weight: 700;
      margin-right: 12px;
    }

    /* Action Plan */
    .action-plan { list-style: none; padding: 0; }
    .action-plan li {
      padding: 12px 16px;
      margin: 8px 0;
      background: #0d1117;
      border-left: 3px solid #e94560;
      border-radius: 0 8px 8px 0;
      font-size: 0.9rem;
    }
    .action-plan .priority-label {
      font-weight: 600;
      color: #e94560;
      font-size: 0.8rem;
      text-transform: uppercase;
      margin-bottom: 4px;
    }

    /* Footer */
    .report-footer {
      text-align: center;
      padding: 32px;
      color: #a0a0b0;
      font-size: 0.8rem;
      border-top: 1px solid #30363d;
      margin-top: 40px;
    }

    /* Utility */
    .text-muted { color: #a0a0b0; }
    .text-small { font-size: 0.85rem; }
    .mt-16 { margin-top: 16px; }
    .mb-16 { margin-bottom: 16px; }
    .note {
      background: #ffd16610;
      border-left: 3px solid #ffd166;
      padding: 12px 16px;
      border-radius: 0 8px 8px 0;
      font-size: 0.85rem;
      color: #ffd166;
      margin: 12px 0;
    }
  </style>
</head>
<body>
  <div class="container">
    <!-- Report sections go here -->
  </div>
</body>
</html>
```

## Component Examples

### Score Card
```html
<div class="score-card score-red">
  <div class="label">ChatGPT Visibility</div>
  <div class="value">12%</div>
  <div class="trend text-muted">Below benchmark (25%)</div>
</div>
```

### Bar Chart Row
```html
<div class="bar-row">
  <div class="bar-label">ChatGPT</div>
  <div class="bar-track">
    <div class="bar-fill" style="width: 23%; background: #ef476f;">23%</div>
  </div>
</div>
```

### Impact Badge
```html
<span class="badge-high">High Impact</span>
<span class="badge-medium">Medium</span>
<span class="badge-low">Low</span>
```

### Keyword Tag
```html
<span class="tag">project management</span>
<span class="tag">team collaboration</span>
```
