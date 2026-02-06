---
name: orchestration
description: Coordinate multi-agent marketing workflows with parallel execution, blackboard-based tracking, and human-in-the-loop checkpoints. Use when a request requires multiple sub-agents (GEO, SEO, Content, etc.) working together in sequence or parallel.
metadata:
  author: castor
  version: "1.0"
  domain: system
---

# Multi-Agent Orchestrator

Coordinates complex, multi-phase marketing workflows. Manages parallel agent execution, dependency tracking via the blackboard pattern, and human-in-the-loop checkpoints.

## When to Use

Activate when the user requests:
- "Complete marketing analysis", "full audit", "comprehensive strategy"
- "Analyze and create strategy", "research and generate content"
- Any task requiring 2+ sub-agents in sequence or parallel
- Multi-company batch operations

**Do NOT activate** for single-agent tasks like "run a GEO analysis" or "write a blog post".

## Execution Modes

### LIGHT (Single Agent)
- User requests a focused task
- Route directly to the appropriate sub-agent
- No orchestration overhead needed

### DEEP (Multi-Agent)
- User requests comprehensive work
- Plan the full workflow, get approval, then execute phases
- Use blackboard for tracking, checkpoints for feedback

## Workflow

### Step 1: Parse & Plan

Identify required agents and their dependencies. Create an execution plan with parallel groups:

```
Phase 1 (parallel_group: 1): [agent-a, agent-b]   ← run simultaneously
Phase 2 (parallel_group: 2): [agent-c]             ← depends on phase 1
Phase 3 (parallel_group: 3): [agent-d]             ← depends on phase 2
```

Present the plan to the user:

```markdown
**WORKFLOW PLAN**

**Phase 1: Analysis** (estimated 15-20 min)
1. GEO Analysis (geo-optimizer) - parallel
2. SEO Analysis (seo-analyst) - parallel

**Phase 2: Strategy** (estimated 10-15 min)
3. Content Strategy (content-strategist) - needs Phase 1

**Checkpoints**: After Phase 1, After Phase 2

Shall I proceed?
```

**CHECKPOINT**: Get user approval before execution.

### Step 2: Initialize Blackboard

Create the tracking structure on the filesystem:

```
/data/audits/{batch-id}/
├── manifest.json           # If multi-company
└── {company}/
    ├── blackboard.json     # Phase tracking
    ├── inputs/             # Company context
    └── outputs/            # Agent outputs
```

See [blackboard schema](references/blackboard-schema.md) for the full JSON schema.

### Step 3: Execute Phases

For each parallel group (ascending order):

1. **Check dependencies**: All phases in the previous group must be `completed`
2. **Launch agents**: Fire ALL agents in this group simultaneously using parallel `Task` tool calls
3. **Monitor**: Each agent updates its phase in `blackboard.json`
4. **Collect outputs**: Read output files when agents complete

**Parallel execution pattern** (critical — this is how you run agents simultaneously):

```
# In a SINGLE message, fire multiple Task tool calls:

Task(agent: "geo-optimizer", prompt: "Run GEO LIGHT for {company}...")
Task(agent: "seo-analyst", prompt: "Run SEO LIGHT for {company}...")

# Both run at the same time. Wait for both to complete.
# Then proceed to the next group.
```

### Step 4: Checkpoint After Critical Phases

After each parallel group completes, present results:

```markdown
**PHASE 1 COMPLETE**

**GEO Findings**: [key metrics]
**SEO Findings**: [key metrics]

**Progress**: [████░░] 50% (2/4 complete)

Options:
1. Continue to Phase 2
2. Re-run with adjustments
3. Ask questions
```

**CHECKPOINT**: Get user feedback before proceeding.

### Step 5: Chain & Recommend

After all phases complete, suggest next actions based on what was accomplished:

- Analysis done → Recommend Content Strategy
- Strategy done → Recommend Content Generation
- Content done → Recommend Dashboard or Presentation
- Complex data → Recommend Dashboard
- Executive insights → Recommend Presentation

## Multi-Company Parallel Execution

For batch audits across multiple companies:

1. Create `manifest.json` with all companies
2. For EACH company, fire a separate `Task` agent running the `audit-mode` skill
3. All companies execute simultaneously (Level 1 parallelism)
4. Within each company, phases run in parallel groups (Level 2 parallelism)

```
Company A  ──→  [GEO ‖ SEO] → Content → Report
Company B  ──→  [GEO ‖ SEO] → Content → Report     (all simultaneous)
Company C  ──→  [GEO ‖ SEO] → Content → Report
```

Monitor via `manifest.json` for overall batch progress.

## Error Handling

When an agent fails:
1. Mark its phase as `failed` with error details in blackboard
2. Present options: retry, skip, abort
3. If skipped, downstream agents that depend on it should adapt (use partial data or skip too)
4. Always offer "save progress, resume later" option

## Data Flow

Agents communicate through the filesystem:
- Agent outputs go to `outputs/{phase-id}.json`
- Downstream agents READ the output files of their dependencies
- No direct agent-to-agent communication — the blackboard + filesystem IS the communication layer

## References

- [Blackboard Schema](references/blackboard-schema.md) - Full JSON schemas for manifest and blackboard files
- [Chaining Patterns](references/chaining-patterns.md) - Common multi-agent workflow patterns
