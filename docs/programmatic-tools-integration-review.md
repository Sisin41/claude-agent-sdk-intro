# Programmatic Tool Calling Integration Review

**Date**: 2025-11-26
**Purpose**: Comprehensive review of GEO system to ensure programmatic tool calling is properly integrated

---

## Executive Summary

✅ **What's Working**:
- `marketing_tools.py`: 5 programmatic tools defined and ready
- `marketing_agent.py`: Code execution enabled with beta header
- `multi-engine-testing.md`: Fully updated with DEEP mode programmatic approach

⚠️ **What Needs Updating**:
- `citation-analysis.md`: Add programmatic approach for large-scale analysis
- `geo-optimizer agent prompt`: Add guidance on when to use programmatic vs MCP

---

## Detailed Analysis

### 1. ✅ multi-engine-testing.md - COMPLETE

**Status**: Already updated with full programmatic support

**What's Included**:
- LIGHT mode (10-20 prompts): Use MCP tool `run_multi_engine_test`
- DEEP mode (50-100 prompts): Use programmatic Python with `query_chatgpt()`, `query_perplexity()`, `query_gemini()`
- Full code example (lines 48-143)
- Token savings breakdown: 80K → 1.5K tokens (98% reduction)
- Decision matrix for when to use each approach

**Key Section** (lines 27-187):
```markdown
### DEEP Mode (Programmatic Approach) ⚡ RECOMMENDED
**Prompts**: 50-100
**Engines**: 3 (ChatGPT + Perplexity + Gemini)
**Total Tests**: 150-300
**Expected Time**: 2-5 minutes
**Token Usage**: ~1,500 tokens (150x savings!)
**Approach**: Use programmatic tool calling (code execution)
```

**Verdict**: ✅ No changes needed

---

### 2. ⚠️ citation-analysis.md - NEEDS UPDATE

**Status**: Currently uses MCP tool which cannot be called programmatically

**Current Implementation**:
- Uses `mcp__MarketingTools__analyze_citations` MCP tool (mentioned throughout)
- Works for LIGHT mode (30-60 citations)
- Does NOT scale to DEEP mode (150-300 citations) efficiently

**Problem**:
- MCP tool processes each citation individually, loads all results to context
- For 300 citations with detailed analysis: ~50K+ tokens
- Cannot be called from code execution

**Solution Needed**:
Add programmatic approach section similar to multi-engine-testing.md:

```markdown
### DEEP Mode (Programmatic Approach) ⚡ RECOMMENDED

For large-scale citation analysis (150+ citations), use programmatic Python:

```python
# Process citations in code execution
import json

# Load test results
test_results = [...]  # From multi-engine-testing output

# Extract all citations programmatically
all_citations = []
for result in test_results:
    for citation in result['citations']:
        all_citations.append({
            'url': citation['url'],
            'context': result['response'][0:200],  # First 200 chars
            'engine': result['engine'],
            'prompt_id': result['prompt_id']
        })

# Analyze programmatically (no LLM needed for basic analysis)
brand_cited = [c for c in all_citations if 'propel.io' in c['url'].lower()]
competitor_cited = [c for c in all_citations if any(comp in c['url'].lower() for comp in competitors)]

# Domain clustering
from collections import Counter
domain_counts = Counter(c['url'].split('/')[2] for c in all_citations)
top_domains = domain_counts.most_common(20)

# Return only aggregated insights (not 50K tokens of raw data!)
print(json.dumps({
    "total_citations": len(all_citations),
    "brand_citations": len(brand_cited),
    "competitor_citations": len(competitor_cited),
    "top_cited_domains": top_domains,
    "citation_gaps": identify_missing_citations(all_citations, target_brand)
}, indent=2))
```

**Token Savings**:
- Traditional (MCP): 300 citations × 150 tokens = 45K tokens
- Programmatic: Aggregated insights only = 800 tokens
- Savings: 98% reduction
```

**Where to Insert**: After current "Step 2: Run Citation Analysis" section (around line 215)

**Verdict**: ⚠️ Needs update - add programmatic approach for DEEP mode

---

### 3. ⚠️ geo-optimizer Agent Prompt - NEEDS UPDATE

**Status**: Mentions MCP tools but doesn't mention programmatic capabilities

**Current Issues**:

**Line 131-134** - Execution modes mention time but not approach:
```python
**Execution Modes:**
- **LIGHT**: Quick scan (10-20 prompts, 2 engines, basic analysis) - ~5 min
- **DEEP**: Comprehensive (50-100 prompts, all engines, detailed analysis) - ~15-20 min
```

**Line 158-161** - Lists MCP tools but doesn't clarify they're for LIGHT mode only:
```python
**Custom Tools** (when MCP server is configured):
- mcp__MarketingTools__run_multi_engine_test: Execute prompts across AI engines in parallel
- mcp__MarketingTools__analyze_citations: LLM-powered parallel citation analysis
- mcp__MarketingTools__competitor_visibility: Compare brand vs competitors
```

**Line 167** - Suggests MCP tools as fallback, but doesn't mention programmatic approach:
```python
- If MCP tools unavailable, use WebSearch/WebFetch as alternatives
```

**Solution Needed**:

1. Update execution modes to mention approach:
```python
**Execution Modes:**
- **LIGHT**: Quick scan (10-20 prompts, 2 engines, MCP tools) - ~5 min
- **DEEP**: Comprehensive (50-100 prompts, 3 engines, programmatic code execution) - ~5-8 min
  - 150x more efficient with programmatic approach (98% token savings)
  - Use code_execution to call query_chatgpt(), query_perplexity(), query_gemini()
```

2. Add programmatic tools section:
```python
**Programmatic Tools** (for DEEP mode - called from code execution):
- query_chatgpt(prompt): Query ChatGPT programmatically
- query_perplexity(prompt): Query Perplexity programmatically
- query_gemini(prompt): Query Gemini programmatically
- Use these in Python code to batch process 50-100 prompts efficiently

**MCP Tools** (for LIGHT mode - direct tool calls):
- mcp__MarketingTools__run_multi_engine_test: Small-scale testing (10-20 prompts)
- mcp__MarketingTools__analyze_citations: Small-scale citation analysis (30-60 citations)
```

3. Add workflow guidance:
```python
**Workflow:**
...
3. Determine execution mode (ask user if unclear: "light" or "deep"?)
   - LIGHT: Use MCP tools for direct execution
   - DEEP: Use code_execution with programmatic tools for efficiency
4. Use TodoWrite to create task list for transparency
5. Follow approach workflows step-by-step
   - For DEEP mode: Write Python code that calls programmatic tools
   - For LIGHT mode: Use MCP tools directly
```

**Verdict**: ⚠️ Needs update - add programmatic tool guidance

---

### 4. ✅ company-value-identification.md - NO CHANGES NEEDED

**Status**: Uses WebSearch/WebFetch which are sufficient

**Why No Changes**:
- This step does NOT involve multi-engine testing or citation processing
- Uses built-in WebSearch/WebFetch for research
- No large-scale data processing that would benefit from programmatic approach
- Works perfectly as-is

**Verdict**: ✅ No changes needed

---

### 5. ✅ prompt-generation.md - NO CHANGES NEEDED

**Status**: Uses Read/Write which are sufficient

**Why No Changes**:
- Generates prompts from company data (pure logic)
- No external API calls needed
- No large-scale data processing
- Works perfectly as-is

**Verdict**: ✅ No changes needed

---

### 6. ✅ strategy-synthesis.md - NO CHANGES NEEDED

**Status**: Uses Read/Write/Edit which are sufficient

**Why No Changes**:
- Aggregates existing analysis data
- Creates strategic report
- No external API calls needed
- Works perfectly as-is

**Verdict**: ✅ No changes needed

---

## Implementation Priority

### Priority 1: citation-analysis.md
**Why**: Critical for DEEP mode to scale efficiently
**Impact**: HIGH - enables processing 300+ citations with 98% token savings
**Effort**: MEDIUM - ~100 lines, following multi-engine-testing pattern

### Priority 2: geo-optimizer agent prompt
**Why**: Ensures agent knows when and how to use programmatic approach
**Impact**: HIGH - without this, agent won't leverage programmatic tools properly
**Effort**: LOW - ~30 lines of guidance updates

---

## Token Efficiency Impact

### Current State (without programmatic approach for citation analysis):
- Multi-engine testing (100 prompts × 3 engines): 80K tokens → 1.5K tokens (✅ implemented)
- Citation analysis (300 citations): 45K tokens → 45K tokens (⚠️ not optimized)

### Future State (with full programmatic integration):
- Multi-engine testing: 1.5K tokens (✅)
- Citation analysis: 800 tokens (⚠️ needs implementation)
- **Total savings**: 80K + 45K → 1.5K + 800 = ~98% overall token reduction

---

## Next Steps

1. **Update citation-analysis.md**
   - Add DEEP mode programmatic approach section (after line 215)
   - Include Python code example for citation processing
   - Add token savings breakdown
   - Update decision matrix (LIGHT vs DEEP)

2. **Update geo-optimizer agent prompt**
   - Update execution modes (lines 131-134)
   - Add programmatic tools section
   - Update workflow guidance (line 147-157)
   - Clarify MCP vs programmatic approach

3. **Testing**
   - Test DEEP mode multi-engine testing with real prompts
   - Validate programmatic citation analysis works
   - Ensure agent selects correct approach based on mode

---

## Decision Matrix Reference

| Scenario | Mode | Approach | Tools | Why |
|----------|------|----------|-------|-----|
| 10-20 prompts | LIGHT | MCP Direct | run_multi_engine_test | Simple, fast, fits in context |
| 50-100 prompts | DEEP | Programmatic | query_chatgpt/perplexity/gemini | 98% token savings |
| 30-60 citations | LIGHT | MCP Direct | analyze_citations | LLM analysis useful |
| 150-300 citations | DEEP | Programmatic | Python code | Efficient aggregation |

---

## Key Insights

1. **Programmatic tool calling is essential for DEEP mode** - without it, token costs are prohibitive
2. **MCP tools remain valuable for LIGHT mode** - easier for quick tests
3. **Hybrid approach is correct** - different tools for different scales
4. **Agent needs explicit guidance** - must know when to use which approach
5. **Citation analysis needs same treatment** - currently only multi-engine-testing has programmatic support

---

## References

- Programmatic tool calling docs: https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling
- marketing_tools.py: Lines 1-317 (programmatic tool definitions)
- marketing_agent.py: Lines 27-830 (agent configuration)
- multi-engine-testing.md: Lines 27-187 (DEEP mode implementation)
