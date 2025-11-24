# Current Agent System Status Quo

**Date**: November 24, 2025
**Purpose**: Document what actually exists in the agent system vs. what's been specified

---

## System Architecture (What Actually Exists)

### Components Built

1. **Master Agent (Kaya)** - `/marketing_agent.py`
   - Personal assistant role
   - Has access to 7 specialized sub-agents
   - Can delegate tasks using the `Task` tool
   - Configured with "Personal Assistant" output style

2. **7 Specialized Sub-Agents** - Defined in `/marketing_agent.py`
   - `geo-optimizer`: GEO analysis expert
   - `seo-analyst`: SEO expert
   - `ads-analyst`: Advertising analytics expert
   - `presentation-designer`: Creates presentations
   - `dashboard-creator`: Builds dashboards
   - `content-strategist`: Content strategy
   - `competitor-analyst`: Competitive intelligence

3. **17 Skill Workflows** - Markdown files in `.claude/skills/`
   - Detailed step-by-step instructions for complex tasks
   - Examples: `multi-engine-testing.md`, `technical-audit.md`, `campaign-analysis.md`
   - Contains workflow logic, file paths, validation rules

4. **File-based Workspace** - `/data/clients/{client-id}/` structure
   - Persistent storage for client data
   - Context files: `company-profile.json`, `marketing-goals.json`, `brand-guidelines.json`
   - Analysis files: Timestamped JSON outputs
   - History tracking: `analysis-timeline.json`

5. **CLI Interface** - `cli_tools.py`
   - Rich terminal UI with colored panels
   - Message parsing and display
   - User input handling

6. **Logging Hook** - `.claude/hooks/log_agent_actions.py`
   - Extracts tool calls from transcripts
   - Saves to `/logs/{timestamp}_{session_id}.log`
   - Runs on "Stop" event (when agent finishes)

### Tools Available to Agents

**Master Agent Tools**:
```python
['Read', 'Write', 'Edit', 'MultiEdit', 'Grep', 'Glob', 'Task', 'TodoWrite',
 'WebSearch', 'WebFetch', 'Bash']
```

**Sub-Agent Tools** (typical):
```python
['Read', 'Write', 'Edit', 'MultiEdit', 'Grep', 'Glob', 'TodoWrite',
 'WebSearch', 'WebFetch']
```

**Data Analysis Sub-Agents** (geo, seo, ads):
```python
# Same as above + Bash for Python/pandas/matplotlib
```

### MCP Tools Status

**Specified but NOT Implemented**:
- ❌ `mcp__MarketingTools__run_multi_engine_test` (GEO-001)
- ❌ `mcp__MarketingTools__analyze_citations` (GEO-002)
- ❌ `mcp__MarketingTools__competitor_visibility` (GEO-003)
- ❌ All other 30 MCP tools in the roadmap

**TypeScript Implementation Exists** (but not connected):
- ✅ `/mcp-servers/marketing-tools/src/tools/geo/multiEngineTest.ts` (459 lines)
- ✅ `/mcp-servers/marketing-tools/src/tools/geo/analyzeCitations.ts` (418 lines)
- ⚠️ These are standalone - not integrated with the agent system
- ⚠️ No MCP server running to provide these tools

---

## Current Agent Interaction Flow

### What Happens When User Talks to Kaya

**Step 1: User Input**
```
User: "Run a deep GEO analysis for Acme Corp"
```

**Step 2: Master Agent Processes Request**
- Kaya receives the request
- Decides to delegate to `geo-optimizer` sub-agent
- Uses `Task` tool to spawn sub-agent

**Step 3: Sub-Agent Execution**
- `geo-optimizer` loads skill file: `multi-engine-testing.md`
- Executes workflow steps using available tools
- May use: Read, Write, WebSearch, WebFetch, TodoWrite

**Step 4: Sub-Agent Uses TodoWrite (Behind the Scenes)**
The agent DOES use TodoWrite internally:
```python
TodoWrite(todos=[
  {"content": "Load company profile", "status": "in_progress"},
  {"content": "Generate test prompts", "status": "pending"},
  {"content": "Run multi-engine tests", "status": "pending"},
  {"content": "Analyze citations", "status": "pending"},
  {"content": "Generate report", "status": "pending"}
])
```

**BUT** → User sees nothing! No progress bars, no task list, no visualization.

**Step 5: Tool Calls Happen Silently**
- Agent calls Read, Write, WebSearch, etc.
- Each tool executes and returns results
- User sees text messages like "Tool Use" panels, but no semantic understanding

**Step 6: Agent Returns Final Result**
- After all work is done (could be 5-20 minutes)
- Returns final text response to Kaya
- Kaya shows user the result

**Step 7: Logging (Post-Execution)**
- After agent stops, hook runs: `log_agent_actions.py`
- Extracts all tool calls to `/logs/` file
- User never sees this log

---

## What the User Actually Sees

### Current UX Flow Example

**Scenario**: User asks for SEO audit

```
┌─────────────────────────────────────┐
│ User Prompt                         │
│ "Analyze the SEO for acmecorp.com"  │
└─────────────────────────────────────┘

┌─────────────────────────────────────┐
│ Assistant                           │
│ "I'll analyze the SEO for           │
│ acmecorp.com. Let me delegate this  │
│ to my SEO specialist."              │
└─────────────────────────────────────┘

┌─────────────────────────────────────┐
│ Tool Use                            │
│ Tool: <Task>                        │
│ {                                   │
│   "subagent_type": "seo-analyst",   │
│   "prompt": "Run comprehensive SEO  │
│   audit for acmecorp.com",          │
│   "description": "SEO audit"        │
│ }                                   │
└─────────────────────────────────────┘

[5-10 minute wait - USER SEES NOTHING]

┌─────────────────────────────────────┐
│ Tool Result                         │
│ {                                   │
│   "success": true,                  │
│   "data": {                         │
│     "overall_health_score": 68,     │
│     "critical_issues": [...],       │
│     "recommendations": [...]        │
│   }                                 │
│ }                                   │
└─────────────────────────────────────┘

┌─────────────────────────────────────┐
│ Assistant                           │
│ "SEO audit complete! I found 3      │
│ critical issues and 12 high         │
│ priority items..."                  │
└─────────────────────────────────────┘
```

### Problems with Current UX

1. **No Progress Visibility**
   - User has no idea what's happening during the 5-10 minute wait
   - No way to know if system is working or stuck
   - No indication of which step the agent is on

2. **No Real-Time Updates**
   - TodoWrite tool exists but output is invisible
   - Can't see "Loading company profile..." → "Analyzing homepage..." → "Checking mobile friendliness..."

3. **Raw JSON Dumps**
   - Tool results show as massive JSON blobs
   - Hard to parse visually
   - No formatted tables, charts, or structured output

4. **No Sub-Agent Transparency**
   - When Kaya delegates to sub-agent, user sees Task tool call
   - But during sub-agent execution, it's a black box
   - Can't see the sub-agent's thought process or tool usage

5. **No Visualizations**
   - No progress bars: `[████████░░░░] 67%`
   - No status tables showing issue counts
   - No charts or graphs for data
   - Everything is text

---

## What Currently Works Well

### ✅ Functional Aspects

1. **Agent Delegation** - Task tool successfully spawns sub-agents
2. **File Persistence** - Client workspace saves analysis results
3. **Skill Workflows** - Detailed markdown workflows guide agents
4. **Tool Usage** - All base tools (Read, Write, WebSearch, etc.) work correctly
5. **Context Loading** - Agents successfully load client context files
6. **Multi-Step Workflows** - Agents can execute complex 10+ step processes
7. **Bash for Data Analysis** - Agents can run Python for calculations, pandas, etc.

### ✅ What's Well-Designed

1. **Workspace Structure** - Clean `/data/clients/{id}/` hierarchy
2. **Naming Conventions** - Timestamped files with clear naming
3. **History Tracking** - `analysis-timeline.json` tracks all analyses
4. **Skill Documentation** - Extremely detailed workflow instructions
5. **Agent Prompts** - Well-crafted prompts with clear expertise areas
6. **Logging System** - Comprehensive tool call logging (even if hidden)

---

## Concrete Example: GEO Analysis Flow

### Current Reality (What Actually Happens)

**User Request**:
```
"Run a deep GEO analysis for our AI customer support platform"
```

**What User Sees**:
```
Kaya: "I'll run a comprehensive GEO analysis. Let me delegate to my GEO specialist."

[Tool Use: Task - geo-optimizer]

[15 minute black box - no feedback]

[Tool Result: Giant JSON blob with 300 test results]

Kaya: "Analysis complete! Brand mentioned in 16.8% of AI engine responses.
Top engine was Perplexity at 28%. Full report saved to /data/clients/..."
```

### What's Actually Happening Behind the Scenes

While user waits in the dark, the agent is doing:

```python
# Step 1: Load context (5 seconds)
Read("/data/clients/acme/context/company-profile.json")
# User sees: Nothing

# Step 2: Load skill workflow (2 seconds)
Read(".claude/skills/geo/company-value-identification.md")
# User sees: Nothing

# Step 3: Extract value props (30 seconds)
WebSearch("Acme Corp AI customer support platform features")
WebFetch("https://acmecorp.com/about")
# User sees: Nothing, maybe "Tool Use: WebSearch" panel

# Step 4: Generate prompts (60 seconds)
# Internal logic to create 100 test prompts
TodoWrite([
  {"content": "Generate test prompts", "status": "in_progress"},
  ...
])
# User sees: NOTHING - TodoWrite is invisible

# Step 5: Multi-engine testing (10 minutes)
# Falls back to manual WebSearch since MCP tool doesn't exist
for prompt in prompts:
    WebSearch(prompt)
    WebFetch(top_results)
# User sees: 100 "Tool Use: WebSearch" panels flying by

# Step 6: Aggregate results (30 seconds)
Bash("python3 << EOF\nimport pandas as pd\n...")
# User sees: "Tool Use: Bash" with code

# Step 7: Save analysis (5 seconds)
Write("/data/clients/acme/analyses/geo/geo-deep-2025-11-24.json", results)
# User sees: "Tool Use: Write"

# Total: 15 minutes of agent work
# User experience: Confusion and boredom
```

### Current Tool Call Display

What the user actually sees during execution:

```
┌─────────────────────────────────────┐
│ Tool Use                            │
│ Tool: <WebSearch>                   │
│ {                                   │
│   "query": "best AI customer        │
│   support tools for SaaS 2024"      │
│ }                                   │
└─────────────────────────────────────┘

┌─────────────────────────────────────┐
│ Tool Result                         │
│ {                                   │
│   "results": [                      │
│     {                               │
│       "title": "10 Best AI...",     │
│       "url": "https://...",         │
│       "snippet": "..."              │
│     }                               │
│   ]                                 │
│ }                                   │
└─────────────────────────────────────┘
```

Repeated 100 times with no context or progress indication.

---

## What the Skill Files Expect vs. Reality

### Example: `multi-engine-testing.md`

**Skill File Says**:
```markdown
**Progress Tracking**:
```
Show real-time progress:
[████████████████░░░░] 70% (210/300)

By engine:
ChatGPT:    [████████████████████] 100/100 ✓ (42s)
Perplexity: [████████████████████] 100/100 ✓ (38s)
Gemini:     [██████░░░░░░░░░░░░░░] 10/100 ⏳ (in progress)
```
```

**Reality**:
- ❌ No progress bars rendered
- ❌ No per-engine status
- ❌ These are just instructions in markdown, not implemented features

**Skill File Says**:
```markdown
Use TodoWrite to plan analysis steps
```

**Reality**:
- ✅ Agent DOES call TodoWrite
- ❌ User never sees the todo list
- ❌ No UI to display task progress

---

## Terminal Display (cli_tools.py)

### What's Implemented

```python
def print_rich_message(type, message, console):
    """
    Prints message in colored panel with border

    Types:
    - "user": Yellow border, user prompt
    - "assistant": Green border, agent response
    - "tool_use": Blue border, shows tool name + input
    - "tool_result": Magenta border, shows tool output
    - "system": Cyan border, system messages
    """
```

### What's Displayed

1. **User Prompts** - Yellow panel with user input
2. **Assistant Messages** - Green panel with text responses
3. **Tool Use Blocks** - Blue panel showing tool name and JSON input
4. **Tool Results** - Magenta panel showing JSON output
5. **System Messages** - Cyan panel for compaction, etc.

### What's NOT Displayed

1. ❌ Todo list from TodoWrite calls
2. ❌ Progress bars or percentages
3. ❌ Formatted tables (beyond Rich table in stats)
4. ❌ Charts or visualizations
5. ❌ Sub-agent "thinking" or planning
6. ❌ Real-time task status updates
7. ❌ Hierarchical view of agent → sub-agent → tool calls

---

## Visualization Specifications vs. Reality

### In AGENT_ARCHITECTURE_SPEC.md (Specified)

17 visualization types were designed:
1. Progress Bars
2. Status Tables
3. Metric Cards
4. Timeline Views
5. Tree Structures
6. Comparison Tables
7. Bar Charts (ASCII)
8. Line Charts (ASCII)
9. Pie Charts (ASCII)
10. Network Graphs
11. Gantt Charts
12. Error/Warning Boxes
13. Code Blocks
14. File Trees
15. Interactive Tables
16. Sparklines
17. ASCII Art Logos

### Reality

- ❌ NONE of these are implemented
- ❌ No rendering library exists
- ❌ No component to convert data → visualization
- ✅ Only basic Rich panels exist (colored boxes with text)

### Example Specification vs. Reality

**Spec Said**:
```
┌─────────────────────────────────┐
│ 🔄 SEO Audit Progress           │
│ [████████░░░░] 67% (6/9)        │
│ ✓ Crawlability                  │
│ ✓ Page Speed                    │
│ ⟳ Mobile-Friendliness...        │
│ ○ Schema Markup                 │
└─────────────────────────────────┘
```

**Reality Shows**:
```
┌─────────────────────────────────┐
│ Tool Use                        │
│ Tool: <TodoWrite>               │
│ {                               │
│   "todos": [                    │
│     {"content": "Crawlability", │
│      "status": "completed"},    │
│     ...                         │
│   ]                             │
│ }                               │
└─────────────────────────────────┘
```
→ And user doesn't even see this, it's hidden!

---

## MCP Tools: Spec vs. Implementation

### Specified in Skills (Expected to Exist)

From `multi-engine-testing.md`:
```python
# Expected MCP tool call
results = await mcp__MarketingTools__run_multi_engine_test({
    "prompts": loaded_prompts,
    "engines": configured_engines,
    "max_concurrent": 50,
})
```

### Reality

1. **TypeScript Implementation EXISTS** - `multiEngineTest.ts` (459 lines)
   - ✅ Full implementation with Zod validation
   - ✅ Parallel execution with p-limit
   - ✅ Citation extraction
   - ✅ Brand mention detection
   - ❌ BUT: No MCP server running
   - ❌ NOT connected to agent system
   - ❌ Agents can't actually call it

2. **What Agents Do Instead** - Fallback to manual method
   - Use WebSearch for each prompt (slow, sequential)
   - Parse results manually
   - Takes 40-60 minutes instead of 90 seconds

3. **Impact**:
   - **With MCP tool** (if connected): 300 tests in 90 seconds
   - **Without MCP tool** (current): 100 tests in 40 minutes
   - **Performance loss**: 26x slower

---

## Data Flow: What Works

### Client Workspace (Works Perfectly)

```
/data/clients/acme-corp/
├── context/
│   ├── company-profile.json        ✓ Loaded by agents
│   ├── marketing-goals.json        ✓ Guides analysis
│   └── brand-guidelines.json       ✓ Used for presentations
├── analyses/
│   ├── geo/
│   │   └── geo-deep-2025-11-24-143022.json  ✓ Saved after analysis
│   ├── seo/
│   │   └── seo-audit-2025-11-24-150033.json ✓ Timestamped
│   └── competitive/
│       └── competitor-analysis-2025-11-24.json
├── history/
│   └── analysis-timeline.json      ✓ Updated on each run
└── raw-data/
    ├── google-ads-export-2025-11.csv
    └── keyword-data-semrush.json
```

### What Agents Do With Files

1. **Read context** at start of every analysis ✓
2. **Load skill workflows** for step-by-step instructions ✓
3. **Save results** to timestamped JSON files ✓
4. **Update timeline** to track analysis history ✓
5. **Generate reports** to `/docs/marketing/` ✓

### File Loading Example (Works)

```python
# Agent executes this successfully
context = Read("/data/clients/acme/context/company-profile.json")

# Extracts data
company_name = context["company"]["name"]  # "Acme Corp"
website = context["company"]["website"]    # "acmecorp.com"
competitors = context["competitors"]       # ["Zendesk", "Intercom"]

# Uses context in analysis
# ... continues workflow
```

---

## Summary: What's Built vs. What's Needed

### ✅ What's Actually Built (Working)

| Component | Status | Notes |
|-----------|--------|-------|
| Master agent (Kaya) | ✅ Working | Delegates successfully |
| 7 sub-agents | ✅ Working | Execute tasks correctly |
| 17 skill workflows | ✅ Working | Detailed instructions exist |
| File workspace | ✅ Working | Persistent storage works |
| Base tools | ✅ Working | Read, Write, WebSearch, etc. |
| TodoWrite tool | ✅ Working | Agents use it (invisibly) |
| Bash for analysis | ✅ Working | Python/pandas/matplotlib |
| Agent delegation | ✅ Working | Task tool spawns sub-agents |
| Context loading | ✅ Working | Loads client data correctly |
| Analysis saving | ✅ Working | Timestamped JSON outputs |
| History tracking | ✅ Working | Timeline logs all analyses |
| Logging hook | ✅ Working | Saves tool calls to /logs/ |

### ❌ What's Specified But NOT Implemented

| Component | Status | Impact |
|-----------|--------|--------|
| Progress bars | ❌ Not implemented | User has no feedback |
| TodoWrite visibility | ❌ Hidden from user | Can't see task progress |
| Visualization library | ❌ Not implemented | No charts, tables, graphs |
| Real-time updates | ❌ Not implemented | Black box execution |
| MCP tool integration | ❌ Not connected | 26x slower fallback |
| Sub-agent transparency | ❌ Not implemented | Can't see sub-agent work |
| Formatted tables | ❌ Not implemented | Raw JSON dumps |
| Status indicators | ❌ Not implemented | No ✓ ⟳ ○ symbols |
| Event streaming | ❌ Not implemented | No real-time UI updates |
| Component library | ❌ Not implemented | No reusable viz components |

### 🔨 What Needs to Be Built

1. **Visualization Rendering Layer**
   - Python library to generate ASCII/Unicode visualizations
   - Functions: `render_progress_bar()`, `render_table()`, `render_chart()`
   - Emit to stdout or special message type

2. **Real-Time Event System**
   - Hook into TodoWrite tool calls
   - Stream events when tasks update
   - Websocket or SSE for web UI

3. **MCP Server Connection**
   - Start marketing-tools MCP server
   - Configure in `mcp_servers` dict
   - Enable fast parallel execution

4. **Frontend Components** (for web app)
   - React components to render each visualization type
   - Event subscription to agent progress
   - Hierarchical view: User → Kaya → Sub-Agent → Tools

5. **Message Type Extensions**
   - New message type: `VisualizationMessage`
   - Carries structured data + render instructions
   - CLI and web UI both consume it

---

## Comparison: Current vs. Desired

### Current: Silent Black Box

```
User: "Run deep GEO analysis"
Kaya: "Starting analysis..."

[15 minutes of silence]

Kaya: "Done! Results: {giant JSON blob}"
```

**User Experience**: Frustrating, unclear, boring

### Desired: Transparent Real-Time Progress

```
User: "Run deep GEO analysis"
Kaya: "I'll run a comprehensive GEO analysis for Acme Corp."

┌─────────────────────────────────────────┐
│ 🎯 Delegating to GEO Optimizer          │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│ 📋 GEO Analysis Plan                    │
│ [██░░░░░░░░] 20% (1/5)                  │
│ ✓ Load company context                  │
│ ⟳ Identifying value propositions...     │
│ ○ Generate test prompts                 │
│ ○ Run multi-engine tests                │
│ ○ Analyze citations                     │
└─────────────────────────────────────────┘

[30 seconds later]

┌─────────────────────────────────────────┐
│ 📋 GEO Analysis Plan                    │
│ [████░░░░░░] 40% (2/5)                  │
│ ✓ Load company context                  │
│ ✓ Identifying value propositions        │
│ ⟳ Generating test prompts...            │
│ ○ Run multi-engine tests                │
│ ○ Analyze citations                     │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│ 💡 Value Props Identified                │
│ • AI-powered ticket deflection          │
│ • 24/7 automated support                │
│ • Seamless human handoff                │
│ • 60% reduction in support costs        │
└─────────────────────────────────────────┘

[2 minutes later]

┌─────────────────────────────────────────┐
│ 🚀 Running Multi-Engine Tests           │
│ [████████████████░░░░] 80% (240/300)    │
│                                         │
│ ChatGPT:    [████████████████████] 100% │
│ Perplexity: [████████████████████] 100% │
│ Gemini:     [████████░░░░░░░░░░░] 40%   │
└─────────────────────────────────────────┘

[5 minutes later]

┌─────────────────────────────────────────┐
│ ✅ Analysis Complete                     │
│                                         │
│ Brand Visibility: 16.8%                 │
│ Tests Run: 300                          │
│ Engines: 3                              │
│ Duration: 7m 23s                        │
└─────────────────────────────────────────┘

┌──────────────────────────────────────────┐
│ 📊 Results by Engine                     │
├────────────┬──────────┬──────────────────┤
│ Engine     │ Mentions │ Visibility Rate  │
├────────────┼──────────┼──────────────────┤
│ Perplexity │ 28       │ 28.0% 🔥         │
│ ChatGPT    │ 12       │ 12.0%            │
│ Gemini     │ 8        │ 8.0%             │
├────────────┼──────────┼──────────────────┤
│ TOTAL      │ 48       │ 16.8%            │
└────────────┴──────────┴──────────────────┘

Kaya: "Analysis complete! Your brand has the highest visibility
on Perplexity (28%). I recommend focusing GEO optimization efforts
there. Full report saved to /data/clients/acme/analyses/geo/..."
```

**User Experience**: Engaging, transparent, informative

---

## Technical Gap Analysis

### Gap 1: TodoWrite Output Not Visible

**Problem**: TodoWrite tool exists but user can't see it

**Current**:
```python
# Agent calls this
TodoWrite([
  {"content": "Load context", "status": "completed"},
  {"content": "Generate prompts", "status": "in_progress"}
])

# Returns success to agent
# User sees: NOTHING
```

**Needed**:
```python
# When TodoWrite is called, emit visualization event
event = VisualizationEvent(
  type="todo_list",
  data={
    "todos": [...]
  }
)

# CLI renders:
# ┌─────────────────────┐
# │ [██░░░░] 33% (1/3)  │
# │ ✓ Load context      │
# │ ⟳ Generate prompts  │
# │ ○ Run tests         │
# └─────────────────────┘

# Web UI subscribes to event and updates React component
```

### Gap 2: No Real-Time Event Streaming

**Problem**: No way to send intermediate updates to UI

**Current**:
- Agent runs from start to finish
- Only final result returned
- No intermediate communication

**Needed**:
- Event emitter in agent execution loop
- Hooks on tool calls to broadcast events
- WebSocket connection to stream to web UI
- CLI polls for events and renders

### Gap 3: No Visualization Rendering

**Problem**: No code to convert data → ASCII art

**Current**:
- Raw JSON displayed
- No formatting logic

**Needed**:
```python
# visualization.py
class VisualizationRenderer:
    @staticmethod
    def render_progress_bar(current, total, width=20):
        filled = int((current / total) * width)
        bar = "█" * filled + "░" * (width - filled)
        percent = int((current / total) * 100)
        return f"[{bar}] {percent}% ({current}/{total})"

    @staticmethod
    def render_table(data, headers):
        # Generate: ┌─┬─┐\n│X│Y│\n└─┴─┘
        pass

    @staticmethod
    def render_status_icon(status):
        icons = {
            "completed": "✓",
            "in_progress": "⟳",
            "pending": "○",
            "failed": "✗"
        }
        return icons.get(status, "○")
```

### Gap 4: MCP Tools Not Connected

**Problem**: TypeScript MCP tools exist but not usable

**Current**:
- Tools implemented in `/mcp-servers/marketing-tools/src/`
- No MCP server running
- Not configured in `marketing_agent.py`

**Needed**:
1. Build TypeScript: `cd mcp-servers/marketing-tools && npm run build`
2. Configure server:
```python
mcp_servers = {
    "MarketingTools": {
        "command": "node",
        "args": ["mcp-servers/marketing-tools/dist/index.js"]
    }
}
```
3. Agent can now call: `mcp__MarketingTools__run_multi_engine_test(...)`

### Gap 5: Sub-Agent Work Not Visible

**Problem**: When sub-agent executes, user sees nothing

**Current Flow**:
```
User → Kaya → [Task tool spawn] → Sub-Agent runs → [Black box] → Result
```

**Needed**:
- Sub-agent tool calls visible in UI
- Hierarchical display showing:
  - Kaya (master)
    - → SEO Analyst (sub-agent)
      - → WebFetch(acmecorp.com)
      - → TodoWrite([...])
      - → Bash(python analysis)
- Collapsible/expandable sections

---

## Concrete Action Items to Close Gaps

### Phase 1: Make TodoWrite Visible (Quick Win)

**Estimated Time**: 4-6 hours

1. **Modify cli_tools.py** to detect TodoWrite in tool results
2. **Add render function** to display todo list with progress bar
3. **Test** with existing agent workflows

**Expected Result**: User sees task progress when agent uses TodoWrite

### Phase 2: Build Visualization Library

**Estimated Time**: 2-3 days

1. Create `/viz/renderer.py`
2. Implement 5 core visualization types:
   - Progress bars
   - Tables
   - Status indicators
   - Metric cards
   - Charts (basic ASCII)
3. Write tests for each renderer

**Expected Result**: Reusable functions to convert data → ASCII/Unicode art

### Phase 3: Connect MCP Tools

**Estimated Time**: 1 day

1. Build TypeScript MCP server
2. Add to `mcp_servers` config
3. Test that agents can call `mcp__MarketingTools__*` tools
4. Benchmark performance improvement

**Expected Result**: 26x faster GEO analysis (90 seconds vs 40 minutes)

### Phase 4: Real-Time Events (Web UI)

**Estimated Time**: 1-2 weeks

1. Design event schema (TodoUpdate, ToolCall, Progress, etc.)
2. Hook into agent execution to emit events
3. WebSocket server to stream events
4. React components to subscribe and render
5. Hierarchical agent → sub-agent → tool view

**Expected Result**: Live updating web UI showing agent progress

---

## Files to Reference

### Key Implementation Files

- `marketing_agent.py:32-610` - Agent definitions and configuration
- `cli_tools.py:45-218` - Current terminal display logic
- `.claude/output-styles/personal-assistant.md` - Master agent prompt
- `.claude/skills/geo/multi-engine-testing.md` - GEO workflow
- `.claude/skills/seo/technical-audit.md` - SEO workflow
- `.claude/hooks/log_agent_actions.py` - Tool call logging

### MCP Implementation (Exists but Not Connected)

- `mcp-servers/marketing-tools/src/tools/geo/multiEngineTest.ts:317-416`
- `mcp-servers/marketing-tools/src/tools/geo/analyzeCitations.ts:359-458`
- `mcp-servers/marketing-tools/src/utils/logger.ts:49-114`

### Specifications (Design Docs)

- `AGENT_ARCHITECTURE_SPEC.md` - Visualization specs (overcomplicated)
- `MCP_DEVELOPMENT_FRAMEWORK.md` - MCP tool standards
- `MCP_TOOLS_COMPREHENSIVE_PLAN.md` - Roadmap for 33 tools

---

## Conclusion

### What Works

The agent system is **functionally complete**:
- ✅ Agents delegate and execute tasks correctly
- ✅ File workspace persists data properly
- ✅ Skills guide complex multi-step workflows
- ✅ All base tools work (Read, Write, WebSearch, etc.)
- ✅ Agents can run Python for data analysis

### What's Missing

The **user experience layer** is absent:
- ❌ No progress visibility
- ❌ No real-time updates
- ❌ No visualizations rendered
- ❌ TodoWrite output hidden
- ❌ Sub-agent work invisible
- ❌ MCP tools not connected (26x slower fallback)

### Bottom Line

**The engine runs perfectly. The dashboard is blank.**

We have a powerful multi-agent system executing complex marketing workflows behind the scenes, but users are staring at a black box waiting for JSON to appear.

The next phase is building the **visualization and event streaming layer** so users can see what Kaya and her team are actually doing.
