---
name: report-builder
description: Build branded, self-contained HTML audit reports in the Royal Tactician "Whimsical Hi-Bit Desktop OS" visual style. Reads JSON data from the audit pipeline and renders a polished Beaverstudio.ai report with window-based sections, pixel-art charts, and retro game-style score cards. Use after audit-mode analyses are complete.
metadata:
  author: castor
  version: "2.0"
  domain: system
  brand: beaverstudio.ai
---

# Report Builder

Generates branded, self-contained HTML reports in the **Royal Tactician** visual style — a whimsical hi-bit desktop OS aesthetic for Beaverstudio.ai.

## When to Use

- After `audit-mode` completes all analysis phases
- When the user requests a formatted report from existing analysis data
- When wrapping any set of analysis JSONs into a presentable deliverable

## Input

Read the following files from the audit workspace:

```
/data/audits/{batch-id}/{company}/
├── inputs/
│   └── company-profile.json
└── outputs/
    ├── geo-light.json       # GEO analysis results
    ├── seo-light.json       # SEO analysis results
    └── content-light.json   # Content recommendations
```

Any of the output files may be missing (partial audit). Adapt the report accordingly.

## Output

Write a single self-contained HTML file:

```
/data/audits/{batch-id}/{company}/outputs/report.html
```

The HTML must be fully self-contained — Google Fonts link is the only external dependency. Opens correctly in any browser.

## Visual Style: Royal Tactician

Follow [visual identity](references/visual-identity.md) exactly. Key rules:

- **Fonts**: DotGothic16 (UI text) + IBM Plex Mono (data/numbers)
- **Colors**: Paper & Ink palette with the Magic Five accents (royal blue, lavender, green, gold, coral)
- **Geometry**: `border-radius: 1px` everywhere. Geometric shadows `Npx Npx 0 <color>` — NO blur.
- **Layout**: Each section is a "window" with colored title bar and window dots
- **Charts**: Pixel-style bar charts with stepped fills (repeating-linear-gradient)
- **Score cards**: Retro game health-bar style with mono font numbers
- **Buttons**: Mechanical key feel (2px bottom shadow, translateY on active)
- **Background**: Animated gradient desktop with pixel grid overlay
- **Taskbar**: Fixed bottom bar with start button, window tabs, system tray LEDs, clock
- **Decorations**: Pixel clouds, sparkles, hearts scattered on desktop
- **Cursors**: Custom pixel-art arrow (default) and pixel hand (pointer)

See [wireframe-report.html](assets/wireframe-report.html) for the complete reference implementation.

## Report Structure

### 1. Desktop Background + Main Window Frame

The entire report sits inside a "main window" on an animated gradient desktop:

```html
<div class="desktop-bg">
  <div class="main-window">
    <div class="main-window-titlebar">
      <span class="window-dots"><!-- close, min, max --></span>
      <span>audit-report.html — Beaverstudio.ai Marketing Audit</span>
    </div>
    <div class="main-window-content">
      <!-- All report sections here -->
    </div>
  </div>
</div>
```

### 2. Header

Beaver avatar (placeholder for logo), company name in IBM Plex Mono, audit metadata, "Powered by Beaverstudio.ai" badge.

### 3. Executive Summary Window (`window-coral`)

- Title bar: `executive_summary.exe`
- "Quick Assessment" ribbon with health label badge (STRONG / MODERATE / WEAK)
- 3-5 sentence synthesis of all findings

### 4. GEO + SEO Side by Side (two-column grid)

**GEO Window** (`window-royal`):
- Title bar: `geo_analysis.log`
- Score cards per engine with pixel health bars (green >25%, yellow 10-25%, red <10%)
- Pixel bar chart for brand mentions per engine
- Opportunities list with impact badges

**SEO Window** (`window-growth`):
- Title bar: `seo_analysis.log`
- Score cards (authority, indexed pages, issues count)
- Keyword opportunities table with volume and position badges
- Technical issues with severity badges
- Quick wins list

### 5. Content Recommendations Window (`window-gold`)

- Title bar: `content_recommendations.txt`
- Content cards with priority pips (numbered squares)
- Each card: title, type badge, keyword tags, two-column GEO/SEO angle boxes
- Impact indicators

### 6. Action Plan Window (`window-lavender`)

- Title bar: `action_plan.todo`
- Three priority tiers: This Week (coral), This Month (gold), This Quarter (royal)
- Numbered action items with left-color border and description + context

### 7. Footer

Beaver stamp, generation timestamp, confidentiality notice, audit ID in mono font.

### 8. Taskbar (fixed bottom)

Start button (rainbow border), window tabs, system tray with green/blue/gold LEDs, live clock.

## Chart Rendering

Use **CSS pixel-art style** for all data visualization. No SVG needed, no JS libraries:

- **Pixel bar charts**: `repeating-linear-gradient` creates stepped pixel effect
- **Health bars**: 8px tall bars with stepped fill inside score cards
- **Score cards**: Large IBM Plex Mono numbers with DotGothic16 labels
- **Tables**: 2px bordered, cloud-colored headers, hover highlights
- **Badges**: 1px border-radius, semantic colors, DotGothic16 font

## Adaptation for Missing Data

If some analysis files are missing:
- Skip that section window entirely
- Note in Executive Summary: "Note: {analysis} was not available for this audit"
- Adjust Action Plan to only reference available data
- If both GEO and SEO are missing, render as single column instead of two-col
- Still produce a valid, well-styled report

## References

- [Visual Identity](references/visual-identity.md) — Full color palette, typography, component CSS
- [Wireframe Report](assets/wireframe-report.html) — Complete reference implementation with sample data
