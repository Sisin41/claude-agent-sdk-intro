# Agent Chaining Patterns

Common multi-agent workflow patterns for the orchestrator.

## Pattern 1: Analysis → Strategy → Execution

```
GEO Analysis → SEO Analysis → Competitor Analysis
     ↓
Content Strategy
     ↓
Content Generation → Social Posts → Email Campaigns
```

**Use Case**: Complete marketing workflow from research to content
**Duration**: 2-4 hours
**Checkpoints**: After each analysis, before content generation

## Pattern 2: Light Scan → Deep Dive

```
GEO Analysis (LIGHT)
     ↓ (discovers high-value opportunity)
GEO Analysis (DEEP - focused on that area)
     ↓
Content Strategy (targeting that opportunity)
     ↓
Content Generation
```

**Use Case**: Initial scan reveals something worth deeper investigation
**Duration**: 1-2 hours
**Checkpoints**: After LIGHT results, after DEEP results

## Pattern 3: Parallel Analysis → Synthesis

```
┌─ GEO Analysis ────────┐
├─ SEO Analysis ────────┤
├─ Competitor Analysis ─┤ → Data Synthesis → Content Strategy
└─ Ads Analysis ────────┘
```

**Use Case**: Comprehensive market understanding before strategy
**Duration**: 1-1.5 hours
**Checkpoints**: After all parallel analyses complete, before synthesis

## Pattern 4: Audit Mode (Standard)

```
┌─ GEO LIGHT ──┐
│               ├──→ Content Gen LIGHT ──→ Report Builder
└─ SEO LIGHT ──┘
```

**Use Case**: Quick 360-degree snapshot for a company
**Duration**: 15-25 minutes
**Checkpoints**: After report generation

## Pattern 5: Multi-Company Batch Audit

```
Company A ──→ [Pattern 4]
Company B ──→ [Pattern 4]     (all parallel)
Company C ──→ [Pattern 4]
```

**Use Case**: Audit multiple companies simultaneously
**Duration**: Same as single audit (parallelism)
**Checkpoints**: After all companies complete

## Pattern 6: Iterative Content

```
Content Strategy
     ↓
Content Generation (batch 1)
     ↓ ✋ Review
Content Generation (batch 2 - adjusted)
     ↓ ✋ Review
Content Generation (batch 3)
```

**Use Case**: Large content creation with quality checkpoints
**Duration**: 3-5 hours
**Checkpoints**: After each batch

## Recommended Next Steps Matrix

| Completed Work | Recommended Next |
|----------------|------------------|
| GEO + SEO + Competitor analysis | Content Strategy |
| Content Strategy | Content Generation |
| All analyses + strategy + content | Dashboard |
| Executive-level insights | Presentation |
| Initial LIGHT scan | DEEP scan of top opportunity |
| Completed audit | Ongoing monitoring schedule |
