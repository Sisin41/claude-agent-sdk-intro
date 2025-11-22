# Data Visualization for Marketing

## Purpose
Create compelling, accurate data visualizations for marketing presentations, dashboards, and reports using appropriate chart types, design principles, and storytelling techniques.

---

## When to Use This Skill

- Creating charts for presentations (from presentation-creation.md)
- Building dashboards (from dashboard-creation.md)
- Visualizing analysis results (GEO, SEO, Ads data)
- Communicating complex data to stakeholders
- Comparing performance metrics

---

## Visualization Types & Use Cases

### 1. Comparison Charts

#### Bar Chart (Horizontal or Vertical)
**Best For**: Comparing values across categories

**Use Cases**:
- Platform performance (Google Ads vs Meta Ads vs LinkedIn)
- Month-over-month metrics
- Campaign rankings
- Audience segment performance

**Example (Text-Based)**:
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

**When to Use**:
- ✅ Comparing 3-12 categories
- ✅ Clear winner/loser needed
- ✅ Exact values important

**When NOT to Use**:
- ❌ More than 15 categories (too crowded)
- ❌ Showing trends over time (use line chart)

---

#### Grouped Bar Chart
**Best For**: Comparing multiple metrics across categories

**Example (Text-Based)**:
```
ROAS by Platform - Current vs Target

               Current  Target
Google Ads     ████████ ██████████   (4.2 vs 5.0)
Meta Ads       ██████ ██████         (3.5 vs 3.5)
LinkedIn Ads   ███ ██████            (1.8 vs 3.5)

0       1       2      3     4      5      6
```

---

### 2. Trend Charts

#### Line Chart
**Best For**: Showing trends over time

**Use Cases**:
- Performance over weeks/months
- Growth trends
- Before/after comparisons
- Seasonal patterns

**Example (Text-Based)**:
```
Monthly ROAS Trend (Jan-Jun 2024)

 5.0 ┤                               ●
     │                          ╭────╯
 4.0 ┤                     ╭────╯
     │                ╭────╯
 3.0 ┤           ╭────╯
     │      ╭────╯
 2.0 ┤──────╯
     │
 1.0 ┤
     └──────────────────────────────────
      Jan  Feb  Mar  Apr  May  Jun

Trend: +150% improvement over 6 months
```

**When to Use**:
- ✅ Time series data
- ✅ Showing momentum/trajectory
- ✅ Multiple data points (5+)

---

#### Multi-Line Chart
**Best For**: Comparing trends across multiple series

**Example**:
```
ROAS Trend by Platform

 5.0 ┤              ╭──●──Google Ads
 4.0 ┤         ╭────╯
 3.0 ┤    ╭────╯        ●──────Meta Ads
 2.0 ┤────╯      ╭──────╯
 1.0 ┤    ╭──────╯──●──LinkedIn Ads
     └────────────────────────────
      Jan  Feb  Mar  Apr  May  Jun
```

---

### 3. Part-to-Whole Charts

#### Pie Chart
**Best For**: Showing proportions of a whole (use sparingly!)

**Use Cases**:
- Budget allocation
- Traffic sources
- Conversion breakdown

**Example (Text-Based)**:
```
Marketing Budget Allocation

  Google Ads (50%)  ████████████████
  Meta Ads (30%)    ██████████
  LinkedIn Ads (10%) ███
  Other (10%)       ███

Total: $30,000/month
```

**When to Use**:
- ✅ 3-5 categories only
- ✅ Percentages add to 100%
- ✅ One category is dominant (>50%)

**When NOT to Use**:
- ❌ More than 5 categories (too cluttered)
- ❌ Similar-sized slices (hard to compare)
- ❌ Precise comparison needed (use bar chart)

---

#### Stacked Bar Chart
**Best For**: Part-to-whole comparisons across categories

**Example**:
```
Conversions by Source & Campaign Type

Google   [Brand: 45%  ][Non-Brand: 35%][Display: 20%]
         ████████████████████████████████████████████ 200

Meta     [Retarget: 60%    ][Cold: 40%        ]
         ████████████████████████████████████  150

LinkedIn [Sponsored: 70%      ][InMail: 30%]
         ███████████████████████████  80

Legend: Brand | Non-Brand | Display | Retarget | Cold | Sponsored | InMail
```

---

### 4. Distribution Charts

#### Histogram
**Best For**: Showing frequency distribution

**Use Cases**:
- CPA distribution across campaigns
- Customer age distribution
- Page load time distribution

**Example**:
```
CPA Distribution Across All Campaigns

Frequency
   15 ┤     █
      │     █
   10 ┤     █
      │  █  █  █
    5 ┤  █  █  █
      │  █  █  █  █
    0 ┴──────────────
       $0 $30 $60 $90 $120
          Cost Per Acquisition

Most campaigns: $30-60 CPA range
```

---

### 5. Correlation Charts

#### Scatter Plot
**Best For**: Showing relationship between two variables

**Use Cases**:
- CPC vs Conversion Rate
- Ad spend vs ROAS
- Audience size vs CPA

**Example**:
```
Ad Spend vs ROAS (Each point = 1 campaign)

ROAS
 6.0 ┤              ●
     │
 4.0 ┤     ●    ●       ●
     │       ●     ●
 2.0 ┤  ●        ●
     │ ●
 0.0 ┴───────────────────────
     $0  $2K  $4K  $6K  $8K
          Monthly Spend

Pattern: Diminishing returns after $5K spend
```

---

### 6. Performance Comparison

#### Bullet Chart
**Best For**: Showing performance against targets

**Example**:
```
Q1 Performance vs Target

Revenue
Target: $100K ▼
Current: $120K  ████████████████████████ 120%
[────────────────────────────────────]
  0%         50%        100%       150%

Conversions
Target: 500 ▼
Current: 450   ██████████████████ 90%
[────────────────────────────────────]
  0%         50%        100%       150%

ROAS
Target: 4.0 ▼
Current: 4.5    ██████████████████████ 112%
[────────────────────────────────────]
  0%         50%        100%       150%
```

---

#### Gauge Chart (Speedometer)
**Best For**: Single metric performance

**Example**:
```
Marketing Health Score

         Poor    Fair   Good  Excellent
         ├───────┼──────┼──────┤
    0    25     50     75    100
         │       │   ▲  │      │
                   68/100
         └───────────╯

Status: FAIR - Room for improvement
```

---

### 7. Ranking Charts

#### Waterfall Chart
**Best For**: Showing cumulative effect of sequential changes

**Example**:
```
Revenue Impact Breakdown (Monthly)

$140K ┤                              ┌─────┐
      │                              │     │$135K
$120K ┤                ┌──────┐┌─────┤Final│
      │                │+$28K ││+$8K ││     │
$100K ┤    ┌──────┐    │(GEO) ││(Ads)││     │
      │    │$96K  │    │      ││     ││     │
 $80K ┤    │Base  │    └──────┘└─────┘└─────┘
      │    │      │       ↑      ↑       ↑
 $60K ┤    └──────┘
      └────────────────────────────────────
         Current  +GEO   +Ads   +SEO   Total

Breakdown: GEO adds $28K, Ads optimization adds $8K
```

---

### 8. Comparison Matrix

#### Heatmap/Table
**Best For**: Comparing two dimensions with color coding

**Example**:
```
Campaign Performance Matrix
(Color: 🟢 Green=Good, 🟡 Yellow=Fair, 🔴 Red=Poor)

                 CTR    CPC    Conv Rate  ROAS
Brand Search     🟢1.8%  🟡$2.5  🟢8.5%     🟢4.8
Non-Brand        🟡1.2%  🟢$1.9  🟡5.2%     🟢4.2
Retargeting      🟢1.5%  🟢$2.1  🟢7.8%     🟢5.1
Display          🔴0.5%  🔴$3.8  🔴2.1%     🔴1.8
Cold Audience    🔴0.6%  🔴$4.2  🔴1.8%     🔴1.2

Summary: Display and Cold Audience underperforming across all metrics
```

---

### 9. Funnel Charts

#### Conversion Funnel
**Best For**: Showing drop-off through stages

**Example**:
```
Customer Journey Funnel

Impressions         ███████████████████████████████ 100,000 (100%)
                    ↓ 2.5% CTR
Clicks              ████████████ 2,500 (2.5%)
                    ↓ 40% Landing
Landing Page Views  █████ 1,000 (1.0%)
                    ↓ 25% Sign Up
Sign Ups            ██ 250 (0.25%)
                    ↓ 60% Purchase
Purchases           █ 150 (0.15%)

Conversion Rate: 0.15% (Impressions → Purchase)
Biggest Drop-off: Clicks → Landing Page (60% bounce)
```

---

### 10. Timeline/Roadmap

#### Gantt Chart (Simplified)
**Best For**: Project timelines and roadmaps

**Example**:
```
90-Day Implementation Roadmap

Task                    Feb        Mar        Apr
──────────────────────┼──────────┼──────────┼──────────
Ads Reallocation      ████──────┼──────────┼──────────
SEO Technical Fixes   ██████████┼──────────┼──────────
GEO Content (Wave 1)  ──████████┼──────────┼──────────
GEO Content (Wave 2)  ──────────┼████████──┼──────────
Creative Refresh      ──────────┼──████────┼──────────
Results Analysis      ──────────┼──────────┼──████────
                      ──────────┼──────────┼──────────
                      Week 1-4   Week 5-8   Week 9-12

Milestones: ● Quick wins complete (Week 2) ● First results (Week 6) ● Final review (Week 12)
```

---

## Data Visualization Best Practices

### Rule 1: Choose the Right Chart Type

```
Question to Ask → Chart Type

"How do things compare?" → Bar Chart
"How has it changed over time?" → Line Chart
"What's the composition?" → Stacked Bar / Pie
"What's the relationship?" → Scatter Plot
"How does it perform vs goal?" → Bullet Chart
"What's the distribution?" → Histogram
"What's the flow/process?" → Funnel
```

### Rule 2: Simplify, Simplify, Simplify

**Good**:
```
Q1 Revenue by Channel

Google   ████████████ $48K
Meta     ████████ $32K
LinkedIn ████ $16K
```

**Bad** (too complex):
```
Q1 Revenue by Channel with Breakdown by Month and Sub-Channel
Including Projected vs Actual with Historical Comparison

[Extremely cluttered multi-dimensional chart]
```

**Guideline**: One chart = one insight

---

### Rule 3: Use Color Purposefully

#### Color Coding System

```
Semantic Colors:
🟢 Green (#28a745): Positive, success, above target, growth
🔴 Red (#dc3545): Negative, failure, below target, decline
🟡 Yellow (#ffc107): Warning, caution, neutral
🔵 Blue (#007bff): Informational, neutral, emphasis

Category Colors:
Use distinct, contrasting colors for different categories
- Google: Blue
- Meta: Navy/Dark Blue
- LinkedIn: Teal
```

#### Color Accessibility

```
✓ Use high contrast (readable for colorblind users)
✓ Don't rely solely on color (use patterns, labels too)
✓ Limit to 5-6 colors max per chart
✓ Use color consistently across all charts
```

---

### Rule 4: Label Clearly

**Required Labels**:
```
1. Chart title (what is being shown)
2. Axis labels (X and Y)
3. Units (dollars, percent, count)
4. Data values (on or near bars/points)
5. Legend (if multiple series)
6. Data source/date (footer)
```

**Example**:
```
[TITLE] ROAS by Platform - January 2024

ROAS
 5.0 ┤
     │        4.8
 4.0 ┤      ████
     │      ████   3.5
 3.0 ┤      ████  ████
     │      ████  ████   1.8
 2.0 ┤      ████  ████  ████
     │      ████  ████  ████
 1.0 ┤      ████  ████  ████
     │      ████  ████  ████
   0 ┴──────────────────────
        Google Meta LinkedIn
        [AXIS LABEL] Platform

[FOOTER] Data Source: Ads Manager Reports, Jan 1-31 2024
```

---

### Rule 5: Maintain Consistent Scale

**Good** (Consistent Y-axis):
```
Chart 1: Revenue ($0 - $100K)
Chart 2: Revenue ($0 - $100K)  ← Same scale
Easy to compare!
```

**Bad** (Inconsistent scale):
```
Chart 1: Revenue ($0 - $100K)
Chart 2: Revenue ($0 - $50K)   ← Different scale
Visually misleading!
```

**Exception**: When ranges are vastly different, use logarithmic scale or dual axes (but note clearly!)

---

### Rule 6: Start Y-Axis at Zero (Usually)

**Good**:
```
Conversions

 200 ┤          ████
     │          ████
 100 ┤    ████  ████
     │    ████  ████
   0 ┴─────────────────
       Jan    Feb

Accurate visual representation
```

**Misleading** (Truncated Y-axis):
```
Conversions

 110 ┤          ████
     │          ████
 100 ┤    ████  ████
     │    ████  ████
  90 ┴─────────────────
       Jan    Feb

Looks like 4x growth, actually only 10% growth!
```

**Exception**: When showing small changes in large numbers (e.g., stock prices, temperature), truncated axis is acceptable if clearly labeled.

---

### Rule 7: Order Matters

**For Bar Charts**:
```
✓ Descending order (highest to lowest) - shows ranking
✓ Ascending order (lowest to highest) - shows progression
✓ Chronological (if time-based)
✓ Alphabetical (if no other logic)

✗ Random order - confusing
```

**Example**:
```
GOOD (Descending - shows best performers first):

Platform ROAS
Google   ████████ 4.8
Meta     ██████ 3.5
LinkedIn ███ 1.8

BAD (Random):
LinkedIn ███ 1.8
Google   ████████ 4.8
Meta     ██████ 3.5
```

---

### Rule 8: Use Annotations Wisely

**Add annotations for**:
```
- Outliers ("Campaign paused mid-month")
- Inflection points ("Algorithm change")
- Targets/benchmarks ("Industry average")
- Key events ("Black Friday")
```

**Example**:
```
Monthly Revenue

$150K ┤                     ╭─●← New campaign launched
      │                ╭────╯
$100K ┤           ╭────╯
      │      ╭────╯
 $50K ┤──────╯
      │          ▲
      │          Site downtime (3 days)
      └──────────────────────────────
        Jan  Feb  Mar  Apr  May
```

---

### Rule 9: Avoid Chart Junk

**Chart Junk** = Unnecessary visual elements that distract

**Examples of Chart Junk**:
```
✗ 3D effects (distort perception)
✗ Too many gridlines
✗ Decorative images
✗ Excessive colors
✗ Unnecessary borders/boxes
✗ Redundant legends
```

**Keep it Clean**:
```
✓ Flat/2D charts
✓ Minimal gridlines (only if helpful)
✓ No decorations
✓ Essential colors only
✓ Remove unnecessary borders
```

---

### Rule 10: Tell a Story

**Every Chart Should Answer**:
1. **What**: What is this showing?
2. **So What**: Why does it matter?
3. **Now What**: What action should be taken?

**Example**:
```
[CHART] Google Ads ROAS: 4.8 (vs target 4.0)

[TITLE] Google Ads Outperforming Target by 20%

ROAS
 5.0 ┤      ────● Actual: 4.8
     │     /
 4.0 ┤────●  Target: 4.0
     │
 3.0 ┤
     └──────────────────
       Target  Actual

[SO WHAT] Exceeding ROAS target by 20% = $12K extra revenue/month

[NOW WHAT] Recommendation: Increase Google Ads budget by 30% to capture more conversions
```

---

## Creating Text-Based Charts

**When to Use Text-Based Charts**:
- Markdown presentations
- Quick data visualization in documents
- Email reports
- Terminal/CLI dashboards
- Accessibility (screen reader friendly)

### Unicode Box Drawing Characters

```
Box Drawing:
─ ━ │ ┃ ┌ ┐ └ ┘ ├ ┤ ┬ ┴ ┼

Lines and Arrows:
→ ← ↑ ↓ ↔ ↕

Blocks:
█ ▓ ▒ ░ ▀ ▄ ■ □

Graph Characters:
● ○ ◆ ◇ ▲ △ ▼ ▽

Checkmarks and Status:
✓ ✗ ✅ ❌ ⚠

Symbols:
🟢 🟡 🔴 🔵 📈 📉 💰 🎯
```

### Text Chart Templates

#### Simple Bar Chart Template:
```
Metric Name

Category 1   ████████ 80
Category 2   ██████ 60
Category 3   ████ 40
Category 4   ██ 20

0    20   40   60   80  100
```

#### Line Chart Template:
```
Metric Over Time

100 ┤            ●
    │         ╭──╯
 75 ┤      ╭──╯
    │   ╭──╯
 50 ┤───╯
    └────────────────
     Q1  Q2  Q3  Q4
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

---

## Platform-Specific Considerations

### For Presentations
```
- Larger fonts (18pt+ for labels)
- High contrast colors
- Simple charts (bar, line only)
- Minimal data points per chart
- Clear titles visible from 10 feet away
```

### For Dashboards
```
- Real-time data
- Interactive elements
- Multiple small charts (overview)
- Color-coded status indicators
- Drill-down capability
```

### For Reports
```
- Detailed axes and labels
- Data source citations
- Multiple series OK
- Can be more complex
- Print-friendly colors (avoid neon)
```

---

## Validation Checklist

Before finalizing any data visualization:

```
✓ Chart type appropriate for data?
✓ Title clear and descriptive?
✓ Axes labeled with units?
✓ Data values shown or easily readable?
✓ Colors used purposefully and accessibly?
✓ Scale consistent and not misleading?
✓ Legend included (if needed)?
✓ Annotations for key points?
✓ Source and date noted?
✓ Chart tells a clear story?
✓ Action/recommendation clear?
```

---

## Usage Example

**Agent Workflow**:
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
8. Output in requested format (markdown, ASCII, etc.)
```

---

## Integration with Other Skills

**Used by**:
- **presentation-creation.md** - For charts in presentations
- **dashboard-creation.md** - For dashboard widgets
- All analysis skills (GEO, SEO, Ads) - For visualizing results

---

## MCP Tools Needed

**Current**: Built-in text generation sufficient for ASCII/Unicode charts

**Future Enhancement**:
- `mcp__Viz__chart_generator` - Generate actual PNG/SVG chart images
- `mcp__Viz__chart_templates` - Pre-built chart templates library
- `mcp__Viz__accessibility_checker` - Validate color contrast and screen reader compatibility
