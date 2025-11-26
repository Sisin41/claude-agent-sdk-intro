# GEO Prompt Generation

## Purpose
Generate targeted test prompts to evaluate brand visibility across AI engines based on company value data, user types, question families, and funnel stages.

---

## Prerequisites
**Required Input**: Company value data from `company-value-identification.md`
**Input File**: `/data/geo/company-value-{company_name}-{mode}.json`

---

## Execution Modes

### LIGHT Mode (10-20 prompts, 2-3 minutes)
**Coverage**: Basic sampling across dimensions
**Total Prompts**: 10-20

### DEEP Mode (80-100 prompts, 10-15 minutes)
**Coverage**: Comprehensive coverage of all combinations
**Total Prompts**: 80-100

---

## Prompt Taxonomy

### Dimension 1: Question Families

```
1. Informational
   - "What is..."
   - "How does..."
   - "Explain..."
   - "Define..."
   - Format: Educational, awareness-building

2. Comparison
   - "Best [category] for [use case]"
   - "[X] vs [Y]"
   - "Top [solutions]"
   - "Compare [options]"
   - Format: Evaluation, consideration stage

3. Problem-Solution
   - "How to solve [pain point]"
   - "Fix [problem]"
   - "Reduce [negative outcome]"
   - "Improve [metric]"
   - Format: Solution-focused, action-oriented

4. Recommendation
   - "Which [tool] for [specific scenario]"
   - "Recommend [solution] for [context]"
   - "Should I use [X] or [Y]"
   - Format: Decision support, buying stage

5. Exploratory
   - "Options for..."
   - "Alternatives to..."
   - "Ways to..."
   - "Strategies for..."
   - Format: Discovery, research phase
```

---

### Dimension 2: User Types (From ICP)

Extract from company value data:
```json
{
  "user_types": [
    {
      "persona_name": "Head of Support",
      "role": "Head of Customer Support",
      "company_size": "SMB",
      "industry": "SaaS"
    },
    {
      "persona_name": "VP of CX",
      "role": "VP of Customer Experience",
      "company_size": "Enterprise",
      "industry": "E-commerce"
    }
  ]
}
```

---

### Dimension 3: Funnel Stages

```
1. Awareness
   - User doesn't know solution exists
   - Researching the problem
   - Educational queries
   - Example: "What is AI customer support?"

2. Consideration
   - User knows solutions exist
   - Evaluating different approaches
   - Comparison queries
   - Example: "Best AI customer support tools"

3. Decision
   - User is comparing specific vendors
   - Ready to purchase
   - Detailed comparison queries
   - Example: "Zendesk vs Intercom vs [YourBrand]"

4. Retention
   - Existing users
   - Advanced features
   - Optimization queries
   - Example: "Advanced analytics in [YourBrand]"
```

---

## LIGHT Mode Generation Strategy

### Goal
Ensure basic coverage across all dimensions with 10-20 prompts

### Formula
```
Core Prompts = 2 question types × 2 user types × 2 funnel stages = 8 prompts
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

Create 2×2×2 = 8 core prompts:

```
Example Matrix:
Q1 (Comparison) × User1 (Head of Support) × Stage1 (Consideration)
→ "Best AI customer support tools for SaaS support teams"

Q1 (Comparison) × User1 (Head of Support) × Stage2 (Decision)
→ "Compare Zendesk vs Intercom for mid-size SaaS companies"

Q1 (Comparison) × User2 (VP of CX) × Stage1 (Consideration)
→ "Top customer experience platforms with AI automation"

... (continue for all 8 combinations)
```

**Step 4: Add High-Value Variations**

Add 5-10 strategic prompts targeting:
- Specific pain points from company data
- Competitor mentions
- Long-tail specific queries
- Industry-specific angles

```
Example High-Value Prompts:
1. "How to reduce support ticket volume by 50%" (pain point)
2. "Alternatives to Zendesk for growing SaaS companies" (competitor + persona)
3. "AI automation for customer support in e-commerce" (industry angle)
4. "[YourBrand] vs [Competitor] pricing" (direct comparison)
5. "Customer support AI tools under $500/month" (budget-conscious)
```

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
      "expected_visibility": "HIGH",  // Should brand appear?
      "target_features": ["AI automation", "ticket routing"],
      "competitor_mentions_expected": ["Zendesk", "Intercom"],
      "strategic_value": "high"  // high, medium, low
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

**Time**: 2-3 minutes

---

## DEEP Mode Generation Strategy

### Goal
Comprehensive coverage of all dimensions with 80-100 prompts

### Formula
```
Core Matrix = 5 question types × 4 user types × 4 funnel stages = 80 prompts
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

**Question Families** (5 types):
- Informational
- Comparison
- Problem-Solution
- Recommendation
- Exploratory

**User Types** (4 personas minimum):
- Use all ICP personas from company data
- If < 4 personas, create variants:
  - By company size (SMB, Mid-market, Enterprise)
  - By role level (Manager, Director, VP, C-Level)
  - By industry vertical

**Funnel Stages** (4 stages):
- Awareness
- Consideration
- Decision
- Retention

**Step 3: Generate Core 80-Prompt Matrix**

Create systematic combinations:

```python
# Pseudo-code for generation logic:
for question_family in ["informational", "comparison", "problem-solution", "recommendation", "exploratory"]:
    for user_type in icp_personas:
        for funnel_stage in ["awareness", "consideration", "decision", "retention"]:
            prompt = generate_prompt(question_family, user_type, funnel_stage, company_data)
            prompts.append(prompt)

# Result: 5 × 4 × 4 = 80 core prompts
```

**Example Prompts by Question Family**:

**1. Informational (16 prompts - 4 personas × 4 stages)**:
```
Awareness:
- "What is AI-powered customer support automation?"
- "How does AI ticket routing work?"
- "Explain sentiment analysis in customer support"

Consideration:
- "How AI customer support differs from traditional help desk"
- "Benefits of AI automation in support teams"

Decision:
- "How [YourBrand] AI routing compares to rule-based systems"

Retention:
- "Advanced features in [YourBrand] for enterprise customers"
```

**2. Comparison (16 prompts)**:
```
Awareness:
- "AI customer support vs traditional support software"
- "Chatbots vs AI support automation"

Consideration:
- "Best AI customer support tools for SaaS companies"
- "Top 10 customer support platforms with AI"
- "AI support automation tools comparison 2024"

Decision:
- "Zendesk vs Intercom vs [YourBrand]"
- "Compare [YourBrand] and Freshdesk for enterprise"
- "[YourBrand] vs [Competitor] pricing and features"

Retention:
- "Advanced AI support tools for scaling enterprises"
```

**3. Problem-Solution (16 prompts)**:
```
Each targeting specific pain points from company data:
- "How to reduce customer support ticket volume by 50%"
- "Fix slow customer support response times"
- "Reduce support costs without sacrificing quality"
- "Automate repetitive customer support tasks"
- "Eliminate support ticket backlog"
- "Improve customer satisfaction scores with AI"
- "Scale customer support without hiring more agents"
```

**4. Recommendation (16 prompts)**:
```
Persona-specific scenarios:
- "Which AI support tool for 100-person SaaS company?"
- "Recommend customer support automation for startups"
- "Best support platform for scaling from 10 to 100 agents"
- "AI customer support for e-commerce with 50K monthly orders"
- "Support automation tool for B2B SaaS with enterprise clients"
```

**5. Exploratory (16 prompts)**:
```
- "Alternatives to hiring more support agents"
- "Options for automating customer support workflows"
- "Ways to improve support team efficiency"
- "Strategies for reducing customer churn through better support"
- "Customer support automation options for remote teams"
```

**Step 4: Add Strategic High-Value Prompts (15-20)**

**Competitor-Focused**:
```
- "Alternatives to Zendesk for growing SaaS companies"
- "Why companies switch from Intercom to [YourBrand]"
- "Zendesk competitors with better AI automation"
- "Cheaper alternatives to enterprise support platforms"
```

**Long-Tail Specific**:
```
- "AI customer support for Shopify stores"
- "Support automation for subscription-based businesses"
- "Customer service AI for healthcare compliance"
- "GDPR-compliant AI support tools for European companies"
```

**Feature-Specific**:
```
- "AI sentiment analysis for customer support tickets"
- "Automatic ticket prioritization software"
- "AI-powered knowledge base for support teams"
- "Support analytics and reporting tools with AI"
```

**Budget-Conscious**:
```
- "Best AI customer support tools under $500/month"
- "Free AI customer support automation tools"
- "ROI of AI customer support automation"
```

**Industry-Specific** (if applicable):
```
- "Customer support automation for SaaS companies"
- "AI support tools for e-commerce businesses"
- "Healthcare customer service automation with compliance"
```

**Step 5: Optimize and Diversify**

**Remove Duplicates**:
```
Check for semantic similarity:
- "Best AI support tools" vs "Top AI customer service platforms"
- If >80% similar, keep only the more specific version
```

**Add Variations**:
```
For critical queries, create natural language variants:
- "Best AI customer support tools for SaaS"
- "What is the best AI-powered customer support software for SaaS companies?"
- "Top AI customer service automation platforms for SaaS businesses"
```

**Geographic Variations** (if company serves multiple regions):
```
- "Best AI customer support tools in Europe"
- "AI support automation for UK businesses"
- "Customer service AI platforms for APAC"
```

**Step 6: Prioritize and Tag**

Mark each prompt with strategic metadata:

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
  "priority": "P1",  // P1 = must appear, P2 = should appear, P3 = nice to have
  "search_volume_estimate": "medium",  // Based on research if available
  "difficulty": "medium"  // Competitive difficulty
}
```

**Step 7: Structure Final Output**

```json
{
  "prompts": [
    { ... },  // 95-100 prompts
  ],
  "metadata": {
    "mode": "DEEP",
    "total_prompts": 95,
    "coverage": {
      "question_families": 5,
      "user_types": 4,
      "funnel_stages": 4,
      "core_matrix_prompts": 80,
      "strategic_prompts": 15
    },
    "breakdown_by_type": {
      "informational": 20,
      "comparison": 25,
      "problem-solution": 20,
      "recommendation": 20,
      "exploratory": 10
    },
    "breakdown_by_priority": {
      "P1_high_priority": 30,
      "P2_medium_priority": 40,
      "P3_low_priority": 25
    }
  },
  "source_data": {
    "company_value_file": "/data/geo/company-value-acme-deep.json",
    "personas_used": 4,
    "pain_points_referenced": 7,
    "competitors_mentioned": ["Zendesk", "Intercom", "Freshdesk"]
  },
  "generated_at": "2024-01-15T11:00:00Z",
  "time_taken_seconds": 180
}
```

**Output**: `/data/geo/prompts-{company}-deep.json`

**Time**: 10-15 minutes

---

## Prompt Quality Guidelines

### Good Prompt Characteristics
✅ **Specific**: "Best AI support tools for SaaS companies" vs "Good support software"
✅ **Natural Language**: How people actually search
✅ **Contextual**: Includes persona context (role, company size, industry)
✅ **Actionable**: Implies user has a goal or problem
✅ **Realistic**: Real queries people would ask AI engines

### Bad Prompt Examples
❌ "Your brand is the best" (Not a real query)
❌ "Support tools" (Too vague)
❌ "ZXQKW customer service AI" (Unnatural, keyword-stuffed)
❌ "Tell me about [YourBrand]" (Too direct, unrealistic)

---

## Validation Checks

Before saving output:

1. **Minimum Count**: LIGHT ≥10, DEEP ≥80
2. **No Duplicates**: Check for identical or near-identical prompts
3. **Coverage**: All question families represented
4. **Persona Alignment**: All ICP personas have dedicated prompts
5. **Brand Mention**: < 10% of prompts should mention brand directly
6. **Competitor Balance**: If competitors mentioned, balanced across top competitors

---

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

---

## Usage Example

**Agent Workflow**:
```
1. Read this skill file
2. Load company value data from previous step
3. Determine mode (LIGHT or DEEP)
4. Execute generation steps:
   [LIGHT]
   - Select 2×2×2 dimensions
   - Generate 8 core prompts
   - Add 5-10 strategic prompts

   [DEEP]
   - Generate 5×4×4 = 80 core matrix
   - Add 15-20 strategic prompts
   - Optimize and deduplicate
   - Tag and prioritize
5. Validate output
6. Save JSON to /data/geo/
7. Provide summary to user (e.g., "Generated 95 prompts across 5 question types")
8. Pass to next skill (multi-engine-testing.md)
```

---

## Next Skill
Once complete, prompts feed into:
→ **`multi-engine-testing.md`** for execution across AI engines

---

## MCP Tools Needed

**Current**: Built-in tools sufficient (Read, Write)

**Future Enhancement** (optional):
- `mcp__GEO__prompt_optimizer` - Validate prompt quality, suggest improvements
- `mcp__GEO__search_volume_lookup` - Get search volume estimates for prompts
