# Data Visualization - Detailed Reference

This file contains complete chart code examples, text-based chart templates, and detailed visualization examples.

## Matplotlib Chart Examples

### Example 1: Bar Chart for Campaign ROAS

```python
import matplotlib.pyplot as plt
import json

# Load data
with open('/data/clients/{CLIENT_ID}/analyses/ads/ads-campaign-analysis-{timestamp}.json') as f:
    data = json.load(f)

# Extract chart data
campaigns = [c['campaign'] for c in data['findings']['top_campaigns']]
roas_values = [c['roas'] for c in data['findings']['top_campaigns']]

# Create chart
plt.figure(figsize=(10, 6))
bars = plt.barh(campaigns, roas_values, color='#0066CC')

# Highlight top performer
bars[0].set_color('#00CC88')

plt.xlabel('ROAS', fontsize=12)
plt.title('Top 5 Campaigns by ROAS', fontsize=14, fontweight='bold')
plt.grid(axis='x', alpha=0.3)

# Add value labels
for i, (campaign, roas) in enumerate(zip(campaigns, roas_values)):
    plt.text(roas + 0.1, i, f'{roas:.2f}', va='center')

plt.tight_layout()
output_file = '/docs/marketing/{CLIENT_ID}/charts/campaign-roas-bar-chart.png'
plt.savefig(output_file, dpi=300, bbox_inches='tight')
print(f"Chart saved: {output_file}")
```

### Example 2: Line Chart for Traffic Trend

```python
import matplotlib.pyplot as plt

# Sample data
months = ['2023-08', '2023-09', '2023-10', '2023-11', '2023-12', '2024-01']
organic_traffic = [8500, 9200, 9800, 10500, 11200, 12100]
paid_traffic = [5200, 5400, 5100, 5800, 6200, 6500]

# Create chart
fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(months, organic_traffic, marker='o', linewidth=2.5, markersize=8,
        color='#0066CC', label='Organic Traffic')
ax.plot(months, paid_traffic, marker='s', linewidth=2.5, markersize=8,
        color='#FF6B35', label='Paid Traffic')

ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('Visitors', fontsize=12)
ax.set_title('Traffic Growth: Organic vs Paid', fontsize=14, fontweight='bold')
ax.grid(True, alpha=0.3)
ax.legend(fontsize=11)

plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('/docs/marketing/{CLIENT_ID}/charts/traffic-trend-line-chart.png', dpi=300)
```

### Example 3: Pie Chart for Budget Allocation

```python
import matplotlib.pyplot as plt

# Budget data
channels = ['Paid Search', 'Paid Social', 'Content', 'SEO Tools']
budget = [50000, 30000, 20000, 5000]
colors = ['#0066CC', '#00CC88', '#FF6B35', '#6B7280']

# Create pie chart
fig, ax = plt.subplots(figsize=(10, 8))
wedges, texts, autotexts = ax.pie(budget, labels=channels, autopct='%1.1f%%',
                                    colors=colors, startangle=90, textprops={'fontsize': 11})

# Make percentage text bold
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')

ax.set_title('Marketing Budget Allocation', fontsize=14, fontweight='bold', pad=20)

plt.tight_layout()
plt.savefig('/docs/marketing/{CLIENT_ID}/charts/budget-allocation-pie-chart.png', dpi=300)
```

### Example 4: Multi-Bar Chart for Platform Comparison

```python
import matplotlib.pyplot as plt
import numpy as np

# Data for comparison
platforms = ['Google Ads', 'Meta Ads', 'LinkedIn Ads']
impressions = [125000, 95000, 42000]
clicks = [8500, 6200, 1800]
conversions = [450, 320, 95]

x = np.arange(len(platforms))
width = 0.25

fig, ax = plt.subplots(figsize=(12, 7))

bars1 = ax.bar(x - width, impressions, width, label='Impressions (K)', color='#0066CC')
bars2 = ax.bar(x, clicks, width, label='Clicks', color='#00CC88')
bars3 = ax.bar(x + width, conversions, width, label='Conversions', color='#FF6B35')

ax.set_xlabel('Platform', fontsize=12)
ax.set_ylabel('Count', fontsize=12)
ax.set_title('Platform Performance Comparison', fontsize=14, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(platforms)
ax.legend()
ax.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('/docs/marketing/{CLIENT_ID}/charts/platform-comparison-bars.png', dpi=300)
```

---

## Text-Based Chart Examples

### Bar Chart - Text

```
Google Ads Conversions by Campaign

Brand Search        ████████████████████ 180
Non-Brand Search    ███████████████ 125
Retargeting         ████████████ 95
Display             ██████ 45
Shopping            ████████ 65

0        50       100      150      200
                 Conversions
```

### Grouped Bar Chart - Text

```
ROAS by Platform - Current vs Target

               Current  Target
Google Ads     ████████ ██████████   (4.2 vs 5.0)
Meta Ads       ██████ ██████         (3.5 vs 3.5)
LinkedIn Ads   ███ ██████            (1.8 vs 3.5)

0       1       2      3     4      5      6
```

### Line Chart - Text

```
Monthly ROAS Trend (Jan-Jun 2024)

 5.0 |                               *
     |                          ----/
 4.0 |                     ----/
     |                ----/
 3.0 |           ----/
     |      ----/
 2.0 |------/
     |
 1.0 |
     +----------------------------------
      Jan  Feb  Mar  Apr  May  Jun

Trend: +150% improvement over 6 months
```

### Multi-Line Chart - Text

```
ROAS Trend by Platform

 5.0 |              ----*--Google Ads
 4.0 |         ----/
 3.0 |    ----/        *------Meta Ads
 2.0 |----/      ------/
 1.0 |    ------/--*--LinkedIn Ads
     +----------------------------
      Jan  Feb  Mar  Apr  May  Jun
```

### Pie Chart - Text

```
Marketing Budget Allocation

  Google Ads (50%)  ████████████████
  Meta Ads (30%)    ██████████
  LinkedIn Ads (10%) ███
  Other (10%)       ███

Total: $30,000/month
```

### Scatter Plot - Text

```
Ad Spend vs ROAS (Each point = 1 campaign)

ROAS
 6.0 |              *
     |
 4.0 |     *    *       *
     |       *     *
 2.0 |  *        *
     | *
 0.0 +---------------------------
     $0  $2K  $4K  $6K  $8K
          Monthly Spend

Pattern: Diminishing returns after $5K spend
```

### Bullet Chart - Text

```
Q1 Performance vs Target

Revenue
Target: $100K v
Current: $120K  ████████████████████████ 120%
[------------------------------------]
  0%         50%        100%       150%

Conversions
Target: 500 v
Current: 450   ██████████████████ 90%
[------------------------------------]
  0%         50%        100%       150%

ROAS
Target: 4.0 v
Current: 4.5    ██████████████████████ 112%
[------------------------------------]
  0%         50%        100%       150%
```

### Gauge Chart - Text

```
Marketing Health Score

         Poor    Fair   Good  Excellent
         +-------+------+------+
    0    25     50     75    100
         |       |   ^  |      |
                   68/100
         +-----------+

Status: FAIR - Room for improvement
```

### Funnel Chart - Text

```
Customer Journey Funnel

Impressions         ███████████████████████████████ 100,000 (100%)
                    v 2.5% CTR
Clicks              ████████████ 2,500 (2.5%)
                    v 40% Landing
Landing Page Views  █████ 1,000 (1.0%)
                    v 25% Sign Up
Sign Ups            ██ 250 (0.25%)
                    v 60% Purchase
Purchases           █ 150 (0.15%)

Conversion Rate: 0.15% (Impressions -> Purchase)
Biggest Drop-off: Clicks -> Landing Page (60% bounce)
```

### Waterfall Chart - Text

```
Revenue Impact Breakdown (Monthly)

$140K |                              +-----+
      |                              |     |$135K
$120K |                +------++-----+Final|
      |                |+$28K ||+$8K ||     |
$100K |    +------+    |(GEO) ||(Ads)||     |
      |    |$96K  |    |      ||     ||     |
 $80K |    |Base  |    +------++-----++-----+
      |    |      |
 $60K |    +------+
      +-------------------------------------------
         Current  +GEO   +Ads   +SEO   Total

Breakdown: GEO adds $28K, Ads optimization adds $8K
```

### Heatmap/Matrix - Text

```
Campaign Performance Matrix
(Green=Good, Yellow=Fair, Red=Poor)

                 CTR    CPC    Conv Rate  ROAS
Brand Search     1.8%G  $2.5Y  8.5%G      4.8G
Non-Brand        1.2%Y  $1.9G  5.2%Y      4.2G
Retargeting      1.5%G  $2.1G  7.8%G      5.1G
Display          0.5%R  $3.8R  2.1%R      1.8R
Cold Audience    0.6%R  $4.2R  1.8%R      1.2R

Summary: Display and Cold Audience underperforming across all metrics
```

### Gantt Chart - Text

```
90-Day Implementation Roadmap

Task                    Feb        Mar        Apr
----------------------+----------+----------+----------
Ads Reallocation      ####------+----------+----------
SEO Technical Fixes   ##########+----------+----------
GEO Content (Wave 1)  --########+----------+----------
GEO Content (Wave 2)  ----------+########--+----------
Creative Refresh      ----------+--####----+----------
Results Analysis      ----------+----------+--####----
                      ----------+----------+----------
                      Week 1-4   Week 5-8   Week 9-12

Milestones: * Quick wins complete (Week 2)  * First results (Week 6)  * Final review (Week 12)
```

---

## Unicode Box Drawing Characters Reference

```
Box Drawing:
- | + / \ _ =

Lines and Arrows:
-> <- v ^

Blocks:
# = * .

Graph Characters:
* o + x

Status:
[G] Good  [Y] Fair  [R] Poor
```

---

## Common Visualization Mistakes

### Mistake 1: Wrong Chart Type
**Problem**: Using pie chart for 12 categories
**Solution**: Use bar chart instead

### Mistake 2: Missing Context
**Problem**: Chart shows "$50K revenue" with no context
**Solution**: Add comparison (vs last month, vs target, vs competitor)

### Mistake 3: Too Much Data
**Problem**: Cramming 30 data points into one chart
**Solution**: Show top 10, or break into multiple charts

### Mistake 4: Misleading Scale
**Problem**: Truncated Y-axis makes 5% change look like 500%
**Solution**: Start at zero or clearly annotate

### Mistake 5: Unclear Labels
**Problem**: Axis labeled "Performance" (too vague)
**Solution**: "Revenue ($K)" or "Conversion Rate (%)"
