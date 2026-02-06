---
name: geo-prompt-generation
description: Generate targeted test prompts to evaluate brand visibility across AI engines based on company value data, user types, question families, and funnel stages. Use after geo-company-value to create the prompt set for multi-engine testing.
metadata:
  author: castor
  version: "1.0"
  domain: geo
  execution-modes: light, deep
---

# GEO Prompt Generation

## Purpose

Generate targeted test prompts to evaluate brand visibility across AI engines based on company value data, user types, question families, and funnel stages.

## Prerequisites

**Required Input**: Company value data from `geo-company-value` skill
**Input File**: `/data/geo/company-value-{company_name}-{mode}.json`

## Execution Modes

### LIGHT Mode (10-20 prompts, 2-3 minutes)
- **Coverage**: Basic sampling across dimensions
- **Total Prompts**: 10-20

### DEEP Mode (80-100 prompts, 10-15 minutes)
- **Coverage**: Comprehensive coverage of all combinations
- **Total Prompts**: 80-100

## Prompt Taxonomy

### Dimension 1: Question Families

1. **Informational** - "What is...", "How does...", "Explain...", "Define..."
2. **Comparison** - "Best [category] for [use case]", "[X] vs [Y]", "Top [solutions]"
3. **Problem-Solution** - "How to solve [pain point]", "Fix [problem]", "Reduce [negative outcome]"
4. **Recommendation** - "Which [tool] for [specific scenario]", "Recommend [solution]"
5. **Exploratory** - "Options for...", "Alternatives to...", "Ways to...", "Strategies for..."

### Dimension 2: User Types (From ICP)

Extract from company value data. Each user type includes persona_name, role, company_size, and industry.

### Dimension 3: Funnel Stages

1. **Awareness** - User does not know solution exists, researching the problem
2. **Consideration** - User knows solutions exist, evaluating approaches
3. **Decision** - User is comparing specific vendors, ready to purchase
4. **Retention** - Existing users, advanced features, optimization queries

## LIGHT Mode Generation Strategy

### Formula
```
Core Prompts = 2 question types x 2 user types x 2 funnel stages = 8 prompts
High-Value Additions = 5-10 strategic prompts
Total = 13-18 prompts
```

### Step-by-Step Process

**Step 1: Load Company Data**
```
Read: /data/geo/company-value-{company}-light.json
Extract:
- Top 2 ICP personas
- Top 5 pain points
- Top 3 services
- Top 2 competitors (if available)
```

**Step 2: Select Dimensions**
```
Question Families: Pick 2
- Comparison (always include)
- Problem-Solution OR Recommendation

User Types: Pick 2
- Primary persona
- Secondary persona

Funnel Stages: Pick 2
- Consideration (always include)
- Decision OR Awareness
```

**Step 3: Generate Core Matrix**

Create 2x2x2 = 8 core prompts from all combinations.

**Step 4: Add High-Value Variations**

Add 5-10 strategic prompts targeting:
- Specific pain points from company data
- Competitor mentions
- Long-tail specific queries
- Industry-specific angles

**Step 5: Structure Output**

```json
{
  "prompts": [
    {
      "prompt_id": "prompt_001",
      "text": "Best AI customer support tools for SaaS support teams",
      "question_family": "comparison",
      "user_type": "Head of Support",
      "funnel_stage": "consideration",
      "expected_visibility": "HIGH",
      "target_features": ["AI automation", "ticket routing"],
      "competitor_mentions_expected": ["Zendesk", "Intercom"],
      "strategic_value": "high"
    }
  ],
  "metadata": {
    "mode": "LIGHT",
    "total_prompts": 15,
    "coverage": {
      "question_families": 2,
      "user_types": 2,
      "funnel_stages": 2
    }
  }
}
```

**Output**: `/data/geo/prompts-{company}-light.json`

## DEEP Mode Generation Strategy

### Formula
```
Core Matrix = 5 question types x 4 user types x 4 funnel stages = 80 prompts
High-Value Additions = 15-20 strategic prompts
Total = 95-100 prompts
```

### Step-by-Step Process

**Step 1: Load Company Data**
```
Read: /data/geo/company-value-{company}-deep.json
Extract:
- All 3-5 ICP personas
- All pain points (categorized by severity)
- All services and features
- All competitors
- Geographic markets
- Industry verticals
```

**Step 2: Generate Full Dimension Coverage**

Use all 5 question families, 4+ user types (use ICP personas; if < 4, create variants by company size, role level, or industry vertical), and all 4 funnel stages.

**Step 3: Generate Core 80-Prompt Matrix**

Systematic combinations of all dimensions. See `references/workflow-detail.md` for example prompts by question family.

**Step 4: Add Strategic High-Value Prompts (15-20)**

Categories: Competitor-Focused, Long-Tail Specific, Feature-Specific, Budget-Conscious, Industry-Specific. See `references/workflow-detail.md` for examples.

**Step 5: Optimize and Diversify**

- **Remove Duplicates**: Check for semantic similarity (if >80% similar, keep only the more specific version)
- **Add Variations**: For critical queries, create natural language variants
- **Geographic Variations**: If company serves multiple regions, add region-specific prompts

**Step 6: Prioritize and Tag**

Mark each prompt with strategic metadata including priority level (P1 = must appear, P2 = should appear, P3 = nice to have).

```json
{
  "prompt_id": "prompt_045",
  "text": "How to reduce support ticket volume by 50% with AI",
  "question_family": "problem-solution",
  "user_type": "Head of Support",
  "funnel_stage": "consideration",
  "expected_visibility": "MEDIUM",
  "target_pain_point": "High ticket volume",
  "target_features": ["AI automation", "ticket routing"],
  "competitor_mentions_expected": ["Zendesk"],
  "strategic_value": "high",
  "priority": "P1",
  "search_volume_estimate": "medium",
  "difficulty": "medium"
}
```

**Step 7: Structure Final Output**

**Output**: `/data/geo/prompts-{company}-deep.json`

See `references/workflow-detail.md` for full DEEP output schema.

## Prompt Quality Guidelines

### Good Prompt Characteristics
- **Specific**: "Best AI support tools for SaaS companies" vs "Good support software"
- **Natural Language**: How people actually search
- **Contextual**: Includes persona context (role, company size, industry)
- **Actionable**: Implies user has a goal or problem
- **Realistic**: Real queries people would ask AI engines

### Bad Prompt Examples
- "Your brand is the best" (Not a real query)
- "Support tools" (Too vague)
- "ZXQKW customer service AI" (Unnatural, keyword-stuffed)
- "Tell me about [YourBrand]" (Too direct, unrealistic)

## Validation Checks

Before saving output:

1. **Minimum Count**: LIGHT >= 10, DEEP >= 80
2. **No Duplicates**: Check for identical or near-identical prompts
3. **Coverage**: All question families represented
4. **Persona Alignment**: All ICP personas have dedicated prompts
5. **Brand Mention**: < 10% of prompts should mention brand directly
6. **Competitor Balance**: If competitors mentioned, balanced across top competitors

## Error Handling

**If company data is incomplete**:
- Use generic personas for missing ICP data
- Focus on industry-standard pain points
- Generate fewer prompts (60-70 for DEEP instead of 95)
- Flag in metadata: `"data_quality": "incomplete"`

**If no competitors identified**:
- Skip competitor comparison prompts
- Focus on general market queries
- Use "best [category]" queries instead

## Agent Workflow

```
1. Load company value data from previous step
2. Determine mode (LIGHT or DEEP)
3. Execute generation steps:
   [LIGHT]
   - Select 2x2x2 dimensions
   - Generate 8 core prompts
   - Add 5-10 strategic prompts

   [DEEP]
   - Generate 5x4x4 = 80 core matrix
   - Add 15-20 strategic prompts
   - Optimize and deduplicate
   - Tag and prioritize
4. Validate output
5. Save JSON to /data/geo/
6. Provide summary (e.g., "Generated 95 prompts across 5 question types")
7. Pass to next skill (geo-multi-engine-testing)
```

## Next Skill

Once complete, prompts feed into:
**geo-multi-engine-testing** for execution across AI engines
