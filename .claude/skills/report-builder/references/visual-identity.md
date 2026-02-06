# Visual Identity — Beaverstudio.ai Reports

## Royal Tactician — "Whimsical Hi-Bit Desktop OS"

Brand: **Beaverstudio.ai**
Logo background: `#b4c2e5`
Style: Pixel-art inspired, retro desktop OS, playful and geometric

## Fonts (Google Fonts)

```html
<link href="https://fonts.googleapis.com/css2?family=DotGothic16&family=IBM+Plex+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
```

| Role | Font | Weight(s) | Usage |
|------|------|-----------|-------|
| Body / UI | DotGothic16 | 400 | All interface text, labels, buttons, paragraphs |
| Data / Stats | IBM Plex Mono | 400, 500, 600, 700 | Numbers, timestamps, counters, code, scores |

## Color Palette

### Core Ink & Paper

| Token | Hex | Role |
|-------|-----|------|
| `--color-cloud` | `#F0F4F8` | App background, window content fill |
| `--color-paper` | `#FFFFFF` | Card surfaces, input backgrounds |
| `--color-vellum` | `#FFF9F0` | Warm chat panels, user messages |
| `--color-ink` | `#2D323E` | Primary text, borders, window frames |
| `--color-ink-light` | `#4A5568` | Secondary text, descriptions |
| `--color-shadow` | `#BCCCDC` | Geometric shadows, dividers, disabled states |
| `--color-brand-bg` | `#b4c2e5` | Logo background, brand tint |

### Semantic Accents (The Magic Five)

| Token | Hex | Role | Window/Section |
|-------|-----|------|----------------|
| `--color-royal` | `#4D8AF0` | Primary action, links | Agents, GEO section |
| `--color-lavender` | `#9D7FEA` | AI/magic actions | Sessions, AI processing |
| `--color-growth` | `#57B886` | Success, ROI | Analytics, SEO section |
| `--color-gold` | `#F2C94C` | Budget, premium | Files, Content section |
| `--color-coral` | `#E85D75` | Errors, warnings | Settings, Alerts |

### Chart Palette (ordered)

`#4D8AF0`, `#57B886`, `#9D7FEA`, `#F2C94C`, `#E85D75`

## Geometry Rules

| Property | Value | Notes |
|----------|-------|-------|
| Border Radius | `1px` | Sharp, retro, geometric — NO rounded corners |
| Border Weight | 1px (cards) / 2px (windows, emphasis) | Ink-on-paper feel |
| Geometric Shadow | `Npx Npx 0 <color>` | NO blur ever. Cards: 2-3px. Windows: 4px accent color |
| Spacing | 4, 6, 8, 12, 16, 24, 32px scale | Prefer gap over margin |

## Component Classes

### Windows (Report Sections)

Each report section renders as an OS "window" with a colored title bar.

```css
.window {
  background: var(--color-paper);
  border: 2px solid var(--color-ink);
  border-radius: 1px;
}
.window-titlebar {
  padding: 8px 12px;
  color: white;
  font-weight: bold;
  display: flex;
  align-items: center;
  gap: 8px;
  text-shadow: 1px 1px 0 rgba(0,0,0,0.3);
}
/* Window dots: 10x10px squares with 2px white border */
.window-dot { width: 10px; height: 10px; border: 2px solid white; display: inline-block; }
```

Window themes by section:

| Section | Title Bar Gradient | Shadow Color |
|---------|-------------------|--------------|
| GEO Analysis | `#4D8AF0 -> #6BA3FF` | `#4D8AF0` |
| SEO Analysis | `#57B886 -> #6ECF9A` | `#57B886` |
| Content | `#F2C94C -> #FFE066` | `#F2C94C` |
| Action Plan | `#9D7FEA -> #B794F6` | `#9D7FEA` |
| Executive Summary | `#E85D75 -> #FF7A8F` | `#E85D75` |

### Score Cards (Retro Game Stats)

```css
.score-card {
  background: var(--color-paper);
  border: 2px solid var(--color-ink);
  border-radius: 1px;
  padding: 16px;
  box-shadow: 2px 2px 0 var(--color-shadow);
  text-align: center;
}
.score-card .value {
  font-family: 'IBM Plex Mono', monospace;
  font-size: 2rem;
  font-weight: 700;
}
.score-card .label {
  font-family: 'DotGothic16', sans-serif;
  color: var(--color-ink-light);
  font-size: 0.85rem;
}
```

Color score thresholds:
- `>25%`: `--color-growth` (green)
- `10-25%`: `--color-gold` (yellow)
- `<10%`: `--color-coral` (red)

### Pixel Progress Bars

```css
.pixel-bar-track {
  background: var(--color-cloud);
  border: 2px solid var(--color-ink);
  border-radius: 1px;
  height: 24px;
  overflow: hidden;
}
.pixel-bar-fill {
  height: 100%;
  /* Stepped pixel effect via repeating gradient */
  background-image: repeating-linear-gradient(
    90deg,
    currentColor 0px,
    currentColor 8px,
    transparent 8px,
    transparent 10px
  );
}
```

### Mechanical Buttons

```css
.btn {
  font-family: 'DotGothic16', sans-serif;
  border: 2px solid var(--color-ink);
  border-radius: 1px;
  padding: 6px 16px;
  box-shadow: 0 2px 0 var(--color-ink);
  cursor: pointer;
  transition: all 0.05s;
}
.btn:active {
  transform: translateY(2px);
  box-shadow: none;
}
.btn-primary { background: #4D8AF0; color: white; }
.btn-magic { background: #9D7FEA; color: white; }
.btn-success { background: #57B886; color: white; }
.btn-danger { background: #E85D75; color: white; }
```

### Status Badges

```css
.badge { font-family: 'DotGothic16'; font-size: 0.75rem; padding: 2px 8px; border: 1px solid; border-radius: 1px; }
.badge-success { background: #ECFDF5; border-color: #57B886; color: #57B886; }
.badge-warning { background: #FFFBEB; border-color: #F2C94C; color: #B7931E; }
.badge-danger { background: #FEF2F2; border-color: #E85D75; color: #E85D75; }
.badge-magic { background: #F5F3FF; border-color: #9D7FEA; color: #9D7FEA; }
.badge-info { background: #EBF4FF; border-color: #4D8AF0; color: #4D8AF0; }
```

### Tags (Keywords)

```css
.tag {
  font-family: 'IBM Plex Mono', monospace;
  font-size: 0.7rem;
  background: var(--color-cloud);
  border: 1px solid var(--color-shadow);
  border-radius: 1px;
  padding: 2px 6px;
  color: var(--color-ink-light);
}
```

## Desktop Background

Reports sit on an animated gradient desktop:

```css
.desktop-bg {
  background: linear-gradient(135deg, #667eea, #764ba2, #f093fb, #f5576c, #4facfe);
  background-size: 400% 400%;
  animation: gradient-shift 15s ease infinite;
  min-height: 100vh;
  position: relative;
}
/* Pixel grid overlay */
.desktop-bg::before {
  content: '';
  position: absolute;
  inset: 0;
  background-image:
    linear-gradient(rgba(255,255,255,0.06) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255,255,255,0.06) 1px, transparent 1px);
  background-size: 48px 48px;
  pointer-events: none;
}
```

## Taskbar

```css
.taskbar {
  position: fixed;
  bottom: 0;
  width: 100%;
  height: 48px;
  background: linear-gradient(180deg, #3D4452, #2D323E);
  border-top: 2px solid #4A5568;
  display: flex;
  align-items: center;
  padding: 0 12px;
  z-index: 100;
}
```

## Animations

| Name | Duration | Use |
|------|----------|-----|
| `gradient-shift` | 15s infinite | Desktop background |
| `float` | 1s ease-in-out infinite | Decorative elements hover |
| `sparkle` | 2s ease-in-out infinite | Decorative stars |
| `typing-cursor` | 0.8s step-end infinite | AI processing indicator |
| `pixel-fill` | 0.6s ease-out | Progress bar fill on load |

## Design Principles

1. **Square Everything** — `border-radius: 1px`. No rounded corners anywhere.
2. **Geometric Shadows** — No blur, no spread. Always `Npx Npx 0 <color>`.
3. **Mechanical Buttons** — 2px bottom shadow, disappears + translates on press.
4. **Color = Identity** — Every window/section has an assigned accent from the five-color palette.
5. **Paper & Ink** — Content on white cards over cool gray. Text is soft charcoal, never pure black.
6. **Playful Pixel Spirit** — Decorative pixel elements (sparkles, hearts, clouds) scattered throughout.

## Wireframe Reference

See [wireframe-report.html](../assets/wireframe-report.html) for a live example of the complete report styling.
