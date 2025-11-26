# Main Agent (Castor) - Complete Definition

## 📍 Location

**Main Agent Prompt**: `.claude/output-styles/personal-assistant.md`
**Sub-Agents Config**: `marketing_agent.py` (lines 111-780)

---

## 🎯 Main Agent: Castor (The Orchestrator)

### **File**: `.claude/output-styles/personal-assistant.md`

```markdown
---
name: Personal Assistant
description: A personal assistant that helps you with... everything.
---

# Role

You are Castor, a personal assistant for the user. Your goal is to help the
user maximize their potential and achieve their goals. You do this by providing
them with the information and tools they need to succeed.

## Communication Style

You must always refer to yourself as Castor!

## Subagents

You have access to the following specialized marketing subagents:

- **geo-optimizer**: Expert in Generative Engine Optimization (GEO). Analyzes
  brand visibility in AI search engines (ChatGPT, Perplexity, Gemini), identifies
  citation opportunities, and creates optimization strategies.

- **seo-analyst**: Expert in Search Engine Optimization (SEO). Performs keyword
  research, technical audits, competitor analysis, and content optimization.

- **ads-analyst**: Expert in advertising analytics across platforms (Google Ads,
  Meta Ads, LinkedIn). Analyzes campaign performance and provides optimization
  recommendations.

- **competitor-analyst**: Expert in competitive analysis and market intelligence.
  Researches competitors, analyzes strategies, and identifies market gaps.

- **dashboard-creator**: Expert in building marketing dashboards and data
  visualizations. Creates interactive dashboards with real-time metrics and KPI
  tracking.

- **presentation-designer**: Expert in creating professional marketing
  presentations. Generates slide decks with data visualizations and compelling
  narratives.

- **content-strategist**: Expert in developing comprehensive content strategies.
  Creates content calendars, topic clusters, and multi-channel campaign plans.

- **content-writer**: Expert in generating high-quality content in parallel.
  Creates blog posts, social media content, emails, and marketing materials while
  integrating insights from all prior analyses.

### Subagent Usage

**MANDATORY:** Leverage these subagents for any tasks that require specialized
marketing expertise.

**MANDATORY:** These subagents can work independently of each other. You can
delegate tasks to them at the same time with parallel Task tool usage. You do not
need to wait for a response from one subagent before delegating to another. Bias
towards delegating tasks in parallel when possible.
```

---

## 🏗️ Architecture Overview

### **Layer 1: Main Agent (Castor)**
- **Location**: `.claude/output-styles/personal-assistant.md`
- **Role**: Orchestrator and delegator
- **Personality**: Personal assistant, helpful, refers to self as "Castor"
- **Primary Job**: Listen to user, delegate to appropriate sub-agents
- **Tools Available**: All tools + Task (for delegation)

### **Layer 2: Sub-Agents (8 Specialists)**
- **Location**: `marketing_agent.py` (AgentDefinition objects)
- **Role**: Domain experts in specific marketing areas
- **Delegation**: Called via Task tool by main agent
- **Each Has**:
  - Description (one-liner)
  - Prompt (detailed instructions)
  - Tools (specific tools for their domain)
  - Model (usually "sonnet")

### **Layer 3: Approaches (Detailed Workflows)**
- **Location**: `.claude/approaches/{domain}/*.md`
- **Role**: Step-by-step execution instructions
- **Loaded By**: Sub-agents when needed
- **Content**: Detailed processes, templates, examples

### **Layer 4: Tools**
- **Programmatic Tools**: `marketing_tools.py` (for token efficiency)
- **MCP Tools**: Future parallel execution engines
- **Built-in Tools**: Read, Write, WebSearch, etc.

---

## 📊 Complete Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    USER INTERACTION                         │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│  LAYER 1: MAIN AGENT (Castor)                               │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │
│  File: .claude/output-styles/personal-assistant.md          │
│  Role: Orchestrator & Delegator                             │
│  Says: "I'm Castor, your personal marketing assistant!"     │
│  Decides: Which sub-agent(s) to delegate to                 │
│  Tools: All tools + Task (for delegation)                   │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      │ Delegates via Task tool
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│  LAYER 2: SUB-AGENTS (8 Specialists)                        │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │
│  File: marketing_agent.py (AgentDefinition objects)         │
│                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │ geo-optimizer│  │ seo-analyst  │  │ ads-analyst  │     │
│  │  (line 111)  │  │  (line 204)  │  │  (line 272)  │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
│                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │presentation- │  │ dashboard-   │  │  content-    │     │
│  │  designer    │  │  creator     │  │  strategist  │     │
│  │  (line 345)  │  │  (line 425)  │  │  (line 511)  │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
│                                                              │
│  ┌──────────────┐  ┌──────────────┐                        │
│  │ competitor-  │  │  content-    │                        │
│  │  analyst     │  │  writer      │                        │
│  │  (line 580)  │  │  (line 647)  │                        │
│  └──────────────┘  └──────────────┘                        │
│                                                              │
│  Each has: description, prompt, tools, model                │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      │ Loads detailed workflows
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│  LAYER 3: APPROACHES (Detailed Workflows)                   │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │
│  Location: .claude/approaches/{domain}/*.md                 │
│                                                              │
│  GEO (5 files):                                             │
│    • company-value-identification.md                        │
│    • prompt-generation.md                                   │
│    • multi-engine-testing.md                                │
│    • citation-analysis.md                                   │
│    • strategy-synthesis.md                                  │
│                                                              │
│  SEO (4 files):                                             │
│    • keyword-research.md                                    │
│    • technical-audit.md                                     │
│    • content-optimization.md                                │
│    • backlink-analysis.md                                   │
│                                                              │
│  Ads (3 files):                                             │
│    • campaign-analysis.md                                   │
│    • audience-insights.md                                   │
│    • creative-optimization.md                               │
│                                                              │
│  + 7 more files for other domains                          │
│                                                              │
│  Each contains: step-by-step processes, templates, examples │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      │ Uses tools
                      │
                      ▼
┌─────────────────────────────────────────────────────────────┐
│  LAYER 4: TOOLS                                             │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │
│                                                              │
│  Programmatic Tools (marketing_tools.py):                   │
│    • query_chatgpt() - Search-enabled ChatGPT              │
│    • query_perplexity() - Live web search                  │
│    • query_gemini() - Google Search grounding              │
│    • fetch_backlink_data() - SEO backlinks                 │
│    • read_analytics_file() - Analytics aggregation         │
│                                                              │
│  Built-in Tools:                                            │
│    • Read, Write, Edit, MultiEdit                          │
│    • Grep, Glob                                             │
│    • WebSearch, WebFetch                                    │
│    • Bash (for Python/data analysis)                       │
│    • TodoWrite (task tracking)                              │
│    • code_execution (for programmatic tools)                │
│                                                              │
│  MCP Tools (future):                                        │
│    • run_multi_engine_test (parallel execution)            │
│    • analyze_citations (parallel LLM analysis)             │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔄 Interaction Flow Example

**User asks**: "Run a deep GEO analysis for Acme Corp"

```
1. USER → Castor (Main Agent)
   Input: "Run a deep GEO analysis for Acme Corp"

2. Castor reads request
   - Identifies this needs GEO expertise
   - Decision: Delegate to geo-optimizer sub-agent

3. Castor → geo-optimizer (via Task tool)
   Delegation: "Perform DEEP GEO analysis for Acme Corp"

4. geo-optimizer receives task
   - Reads its prompt (line 111 in marketing_agent.py)
   - Sees it should load approach files for workflows
   - Creates TodoWrite task list

5. geo-optimizer → Loads approaches
   - Reads: company-value-identification.md
   - Reads: prompt-generation.md
   - Reads: multi-engine-testing.md (sees programmatic approach!)
   - Reads: citation-analysis.md
   - Reads: strategy-synthesis.md

6. geo-optimizer → Executes workflow
   - Step 1: Company research (WebSearch, WebFetch)
   - Step 2: Generate 100 prompts
   - Step 3: Run tests (uses programmatic tools!)
     - Writes Python code
     - Calls query_chatgpt(), query_perplexity(), query_gemini()
     - Processes 300 queries in code
     - Returns aggregated insights (98% token savings!)
   - Step 4: Analyze citations (programmatically)
   - Step 5: Create strategy report

7. geo-optimizer → Castor
   Returns: Complete GEO analysis report

8. Castor → USER
   Presents: Analysis findings and recommendations
```

---

## 🎭 Key Characteristics

### **Main Agent (Castor)**:
- **Personality**: Personal assistant, helpful, friendly
- **Name**: Always refers to self as "Castor"
- **Primary Skill**: Delegation and orchestration
- **Knowledge**: Knows which sub-agent to use for what
- **Parallel Execution**: Can delegate to multiple sub-agents at once

### **Sub-Agents**:
- **Personality**: Domain experts (serious, professional)
- **Names**: Refer to themselves as "Castor's {domain} specialist"
- **Primary Skill**: Deep expertise in specific marketing domain
- **Knowledge**: Detailed workflows and best practices
- **Execution**: Follow approach files step-by-step

---

## 📝 Important Notes

### **Where Things Are Defined**:

| Component | Location | Purpose |
|-----------|----------|---------|
| **Main agent persona** | `.claude/output-styles/personal-assistant.md` | Castor's personality, subagent list |
| **Sub-agent configs** | `marketing_agent.py` (AgentDefinition) | Technical configuration |
| **Sub-agent prompts** | `marketing_agent.py` (prompt field) | Detailed instructions |
| **Approach workflows** | `.claude/approaches/{domain}/*.md` | Step-by-step execution guides |
| **Programmatic tools** | `marketing_tools.py` | Token-efficient tools |
| **Orphaned docs** | `.claude/agents/*.md` | ⚠️ NOT USED (duplicate content) |

### **The Disconnect We Found**:
- `.claude/agents/*.md` files have similar content to sub-agent prompts
- BUT they're NOT being used (orphaned!)
- Main agent uses `.claude/output-styles/personal-assistant.md` instead
- Sub-agents use prompts from `marketing_agent.py`

---

## 🎯 Summary

**Main Agent (Castor)**:
- Lives in: `.claude/output-styles/personal-assistant.md`
- Role: Personal assistant and orchestrator
- Says: "I'm Castor!"
- Does: Listens, delegates to specialists

**Sub-Agents (8 specialists)**:
- Live in: `marketing_agent.py` (Python code)
- Role: Domain experts
- Say: "I'm Castor's {domain} specialist"
- Do: Execute detailed marketing workflows

**Approaches (19 workflow files)**:
- Live in: `.claude/approaches/{domain}/*.md`
- Role: Step-by-step guides
- Content: Detailed processes, templates, examples
- Used by: Sub-agents when executing tasks

---

**Want to see any specific part in more detail?** 🚀
