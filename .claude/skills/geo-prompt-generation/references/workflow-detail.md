# GEO Prompt Generation - Detailed Reference

This file contains detailed examples, prompt templates, and extended output schemas referenced by the main SKILL.md.

## LIGHT Mode Example Matrix

```
Q1 (Comparison) x User1 (Head of Support) x Stage1 (Consideration)
-> "Best AI customer support tools for SaaS support teams"

Q1 (Comparison) x User1 (Head of Support) x Stage2 (Decision)
-> "Compare Zendesk vs Intercom for mid-size SaaS companies"

Q1 (Comparison) x User2 (VP of CX) x Stage1 (Consideration)
-> "Top customer experience platforms with AI automation"

Q1 (Comparison) x User2 (VP of CX) x Stage2 (Decision)
-> "Best CX platforms for enterprise e-commerce"

Q2 (Problem-Solution) x User1 (Head of Support) x Stage1 (Consideration)
-> "How to reduce support ticket volume in SaaS companies"

Q2 (Problem-Solution) x User1 (Head of Support) x Stage2 (Decision)
-> "AI automation to eliminate support ticket backlog"

Q2 (Problem-Solution) x User2 (VP of CX) x Stage1 (Consideration)
-> "Strategies to improve customer experience at scale"

Q2 (Problem-Solution) x User2 (VP of CX) x Stage2 (Decision)
-> "Enterprise CX automation solutions comparison"
```

## LIGHT Mode High-Value Prompt Examples

```
1. "How to reduce support ticket volume by 50%" (pain point)
2. "Alternatives to Zendesk for growing SaaS companies" (competitor + persona)
3. "AI automation for customer support in e-commerce" (industry angle)
4. "[YourBrand] vs [Competitor] pricing" (direct comparison)
5. "Customer support AI tools under $500/month" (budget-conscious)
```

## DEEP Mode Example Prompts by Question Family

### 1. Informational (16 prompts - 4 personas x 4 stages)

**Awareness**:
- "What is AI-powered customer support automation?"
- "How does AI ticket routing work?"
- "Explain sentiment analysis in customer support"

**Consideration**:
- "How AI customer support differs from traditional help desk"
- "Benefits of AI automation in support teams"

**Decision**:
- "How [YourBrand] AI routing compares to rule-based systems"

**Retention**:
- "Advanced features in [YourBrand] for enterprise customers"

### 2. Comparison (16 prompts)

**Awareness**:
- "AI customer support vs traditional support software"
- "Chatbots vs AI support automation"

**Consideration**:
- "Best AI customer support tools for SaaS companies"
- "Top 10 customer support platforms with AI"
- "AI support automation tools comparison 2024"

**Decision**:
- "Zendesk vs Intercom vs [YourBrand]"
- "Compare [YourBrand] and Freshdesk for enterprise"
- "[YourBrand] vs [Competitor] pricing and features"

**Retention**:
- "Advanced AI support tools for scaling enterprises"

### 3. Problem-Solution (16 prompts)

Each targeting specific pain points from company data:
- "How to reduce customer support ticket volume by 50%"
- "Fix slow customer support response times"
- "Reduce support costs without sacrificing quality"
- "Automate repetitive customer support tasks"
- "Eliminate support ticket backlog"
- "Improve customer satisfaction scores with AI"
- "Scale customer support without hiring more agents"

### 4. Recommendation (16 prompts)

Persona-specific scenarios:
- "Which AI support tool for 100-person SaaS company?"
- "Recommend customer support automation for startups"
- "Best support platform for scaling from 10 to 100 agents"
- "AI customer support for e-commerce with 50K monthly orders"
- "Support automation tool for B2B SaaS with enterprise clients"

### 5. Exploratory (16 prompts)

- "Alternatives to hiring more support agents"
- "Options for automating customer support workflows"
- "Ways to improve support team efficiency"
- "Strategies for reducing customer churn through better support"
- "Customer support automation options for remote teams"

## Strategic High-Value Prompts (DEEP Mode, 15-20)

### Competitor-Focused
- "Alternatives to Zendesk for growing SaaS companies"
- "Why companies switch from Intercom to [YourBrand]"
- "Zendesk competitors with better AI automation"
- "Cheaper alternatives to enterprise support platforms"

### Long-Tail Specific
- "AI customer support for Shopify stores"
- "Support automation for subscription-based businesses"
- "Customer service AI for healthcare compliance"
- "GDPR-compliant AI support tools for European companies"

### Feature-Specific
- "AI sentiment analysis for customer support tickets"
- "Automatic ticket prioritization software"
- "AI-powered knowledge base for support teams"
- "Support analytics and reporting tools with AI"

### Budget-Conscious
- "Best AI customer support tools under $500/month"
- "Free AI customer support automation tools"
- "ROI of AI customer support automation"

### Industry-Specific
- "Customer support automation for SaaS companies"
- "AI support tools for e-commerce businesses"
- "Healthcare customer service automation with compliance"

## DEEP Mode Full Output Schema

```json
{
  "prompts": [
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

## Prompt Generation Pseudo-Code (DEEP)

```python
for question_family in ["informational", "comparison", "problem-solution", "recommendation", "exploratory"]:
    for user_type in icp_personas:
        for funnel_stage in ["awareness", "consideration", "decision", "retention"]:
            prompt = generate_prompt(question_family, user_type, funnel_stage, company_data)
            prompts.append(prompt)

# Result: 5 x 4 x 4 = 80 core prompts
```
