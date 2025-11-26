# Workspace Structure and Naming Conventions

## Overview

The marketing agent system uses a **file-based workspace** for persistent storage of analyses, client context, and conversation history. This enables stateful behavior without requiring a database while maintaining clear organization and easy debugging.

---

## Directory Structure

### Root Workspace Layout

```
/data/
├── clients/               # Client-specific workspaces
│   ├── {client-id}/      # Individual client workspace
│   │   ├── analyses/     # All completed analyses
│   │   ├── context/      # Client profile and persistent context
│   │   ├── history/      # Conversation and interaction logs
│   │   ├── raw-data/     # Source data files (CSV, JSON exports)
│   │   └── temp/         # Temporary processing files
│   └── ...
├── templates/            # Analysis templates and schemas
└── scripts/              # Python analysis utilities

/docs/
└── marketing/            # Generated reports and presentations
    └── {client-id}/      # Client-specific documentation
```

### Client Workspace Structure

```
/data/clients/{client-id}/
├── analyses/
│   ├── geo/
│   │   ├── geo-analysis-YYYY-MM-DD-HHMMSS.json
│   │   ├── geo-citation-analysis-YYYY-MM-DD-HHMMSS.json
│   │   └── geo-strategy-YYYY-MM-DD-HHMMSS.json
│   ├── seo/
│   │   ├── seo-audit-YYYY-MM-DD-HHMMSS.json
│   │   ├── seo-keyword-research-YYYY-MM-DD-HHMMSS.json
│   │   ├── seo-content-optimization-YYYY-MM-DD-HHMMSS.json
│   │   └── seo-backlink-analysis-YYYY-MM-DD-HHMMSS.json
│   ├── ads/
│   │   ├── ads-campaign-analysis-YYYY-MM-DD-HHMMSS.json
│   │   ├── ads-audience-insights-YYYY-MM-DD-HHMMSS.json
│   │   └── ads-creative-optimization-YYYY-MM-DD-HHMMSS.json
│   ├── competitive/
│   │   └── competitor-analysis-YYYY-MM-DD-HHMMSS.json
│   └── content/
│       └── content-strategy-YYYY-MM-DD-HHMMSS.json
│
├── context/
│   ├── company-profile.json          # Company info, ICP, positioning
│   ├── marketing-goals.json          # Objectives, KPIs, targets
│   ├── brand-guidelines.json         # Voice, messaging, visual identity
│   └── previous-recommendations.json # Track what was suggested
│
├── history/
│   ├── conversation-log.jsonl        # All user interactions (JSONL format)
│   └── analysis-timeline.json        # Chronological list of all analyses
│
├── raw-data/
│   ├── google-ads-export-YYYY-MM-DD.csv
│   ├── google-analytics-YYYY-MM-DD.csv
│   ├── keyword-data-YYYY-MM-DD.json
│   └── ...
│
└── temp/
    └── [auto-cleaned temporary files]
```

---

## Naming Conventions

### Client IDs

**Format**: `{company-slug}` or `{company-slug}-{project}`

**Rules**:
- Lowercase letters, numbers, hyphens only
- No spaces or special characters
- Maximum 50 characters
- Must be URL-safe

**Examples**:
- ✅ `acme-corp`
- ✅ `techstartup-2024-relaunch`
- ✅ `saas-company-b2b`
- ❌ `Acme Corp` (has space and uppercase)
- ❌ `tech@startup` (invalid character)

---

### Analysis Files

**Format**: `{analysis-type}-{analysis-name}-{timestamp}.json`

**Components**:
- `{analysis-type}`: Category (geo, seo, ads, competitive, content)
- `{analysis-name}`: Specific analysis (audit, keyword-research, campaign-analysis)
- `{timestamp}`: `YYYY-MM-DD-HHMMSS` format

**Rules**:
- All lowercase with hyphens
- Timestamp is required (enables versioning and history)
- Must be valid JSON format
- Saved to appropriate subdirectory in `/analyses/`

**Examples**:
```
/data/clients/acme-corp/analyses/seo/seo-audit-2024-01-15-143022.json
/data/clients/acme-corp/analyses/geo/geo-analysis-2024-01-20-091545.json
/data/clients/acme-corp/analyses/ads/ads-campaign-analysis-2024-01-22-160033.json
```

---

### Context Files

**Format**: `{context-type}.json` (no timestamp, always overwritten)

**Available Context Types**:
- `company-profile.json` - Core company information
- `marketing-goals.json` - Current objectives and KPIs
- `brand-guidelines.json` - Messaging and identity
- `previous-recommendations.json` - Historical suggestions

**Rules**:
- Fixed filenames (no timestamps)
- Always in `/context/` directory
- Updated incrementally (agents can Read → Edit → Write)
- Must maintain JSON schema consistency

---

### History Files

**Conversation Log Format**: `conversation-log.jsonl` (JSONL - JSON Lines)

**Structure**:
```jsonl
{"timestamp": "2024-01-15T14:30:22Z", "role": "user", "content": "Run SEO audit", "session_id": "sess-001"}
{"timestamp": "2024-01-15T14:31:45Z", "role": "assistant", "content": "...", "analysis_id": "seo-audit-2024-01-15-143022", "agent": "seo-analyst"}
{"timestamp": "2024-01-15T15:22:10Z", "role": "user", "content": "Now compare to competitors", "session_id": "sess-001"}
```

**Analysis Timeline Format**: `analysis-timeline.json`

**Structure**:
```json
{
  "client_id": "acme-corp",
  "analyses": [
    {
      "analysis_id": "seo-audit-2024-01-15-143022",
      "type": "seo",
      "subtype": "audit",
      "timestamp": "2024-01-15T14:30:22Z",
      "agent": "seo-analyst",
      "status": "completed",
      "file_path": "/data/clients/acme-corp/analyses/seo/seo-audit-2024-01-15-143022.json",
      "summary": "Technical SEO audit identified 12 issues..."
    }
  ]
}
```

---

### Raw Data Files

**Format**: `{source}-{export-type}-{date}.{ext}`

**Examples**:
```
google-ads-export-2024-01-15.csv
google-analytics-2024-01-15.csv
keyword-data-2024-01-20.json
meta-ads-performance-2024-01-22.csv
```

**Rules**:
- Include source platform/tool name
- Include export date (YYYY-MM-DD)
- Preserve original file extension (.csv, .json, .xlsx)
- Stored in `/raw-data/` directory

---

## File Schemas

### Company Profile Schema

**File**: `/data/clients/{client-id}/context/company-profile.json`

```json
{
  "client_id": "acme-corp",
  "company_name": "Acme Corporation",
  "industry": "B2B SaaS",
  "website": "https://acmecorp.com",
  "description": "Cloud analytics platform for marketing teams",

  "value_propositions": [
    "Real-time marketing analytics",
    "AI-powered insights",
    "Cross-channel attribution"
  ],

  "ideal_customer_profile": {
    "company_size": "50-500 employees",
    "departments": ["Marketing", "Growth", "Analytics"],
    "pain_points": [
      "Data silos across marketing tools",
      "Slow manual reporting",
      "No clear attribution model"
    ],
    "buying_personas": [
      {"role": "CMO", "priorities": ["ROI", "Team efficiency"]},
      {"role": "Marketing Analyst", "priorities": ["Data accuracy", "Ease of use"]}
    ]
  },

  "competitors": [
    {"name": "Competitor A", "url": "https://competitora.com"},
    {"name": "Competitor B", "url": "https://competitorb.com"}
  ],

  "positioning": "The only analytics platform built specifically for modern marketing teams",

  "last_updated": "2024-01-15T14:30:22Z"
}
```

---

### Marketing Goals Schema

**File**: `/data/clients/{client-id}/context/marketing-goals.json`

```json
{
  "client_id": "acme-corp",

  "objectives": [
    {
      "goal": "Increase organic traffic",
      "target": "50% growth in 6 months",
      "current_baseline": "10,000 monthly visitors",
      "priority": "high"
    },
    {
      "goal": "Improve ROAS on paid ads",
      "target": "4.0 ROAS",
      "current_baseline": "2.5 ROAS",
      "priority": "medium"
    }
  ],

  "kpis": [
    {"metric": "Organic Traffic", "current": 10000, "target": 15000, "period": "monthly"},
    {"metric": "MQLs", "current": 500, "target": 800, "period": "monthly"},
    {"metric": "ROAS", "current": 2.5, "target": 4.0, "period": "overall"}
  ],

  "budget": {
    "paid_search": 50000,
    "paid_social": 30000,
    "content": 20000,
    "seo_tools": 5000,
    "period": "monthly",
    "currency": "USD"
  },

  "last_updated": "2024-01-15T14:30:22Z"
}
```

---

### Analysis File Schema (Generic)

**All analysis files follow this base structure:**

```json
{
  "analysis_id": "seo-audit-2024-01-15-143022",
  "client_id": "acme-corp",
  "analysis_type": "seo",
  "analysis_subtype": "audit",
  "timestamp": "2024-01-15T14:30:22Z",
  "agent": "seo-analyst",
  "execution_mode": "COMPREHENSIVE",
  "duration_seconds": 240,

  "inputs": {
    "website": "https://acmecorp.com",
    "pages_analyzed": 50,
    "parameters": {}
  },

  "findings": {
    // Analysis-specific findings
  },

  "recommendations": [
    {
      "priority": "high",
      "category": "technical-seo",
      "issue": "Slow page load time",
      "recommendation": "Optimize images and implement lazy loading",
      "expected_impact": "+15% organic traffic",
      "effort": "2 weeks"
    }
  ],

  "metrics": {
    // Analysis-specific metrics
  },

  "metadata": {
    "skill_files_used": [
      ".claude/approaches/seo/technical-audit.md"
    ],
    "mcp_tools_used": [],
    "data_sources": [
      "WebFetch: https://acmecorp.com",
      "WebSearch: 'acmecorp site speed'"
    ]
  }
}
```

---

## Workspace Management Rules

### Creating a New Client Workspace

**Agent Behavior**:
1. Check if `/data/clients/{client-id}/` exists
2. If not, create full directory structure
3. Initialize `company-profile.json` with minimal data
4. Create empty `analysis-timeline.json`
5. Create empty `conversation-log.jsonl`

**Example Bash command**:
```bash
mkdir -p /data/clients/acme-corp/{analyses/{geo,seo,ads,competitive,content},context,history,raw-data,temp}
```

---

### Reading Previous Analyses

**Agent Workflow**:

1. **Find recent analysis**:
   ```bash
   # Get most recent SEO audit
   ls -t /data/clients/acme-corp/analyses/seo/seo-audit-*.json | head -1
   ```

2. **Read analysis-timeline.json** for summary of all past work:
   ```python
   Read("/data/clients/acme-corp/history/analysis-timeline.json")
   ```

3. **Load specific analysis** when needed:
   ```python
   Read("/data/clients/acme-corp/analyses/seo/seo-audit-2024-01-15-143022.json")
   ```

**When to Load Context**:
- **Always load** `company-profile.json` at start of any analysis
- **Load** `marketing-goals.json` for strategic analyses
- **Load** `previous-recommendations.json` to avoid repeating suggestions
- **Check** `analysis-timeline.json` to see what's been done recently

---

### Writing New Analyses

**Agent Workflow**:

1. **Generate timestamp**:
   ```bash
   timestamp=$(date +"%Y-%m-%d-%H%M%S")
   ```

2. **Create analysis file**:
   ```python
   Write(
       file_path=f"/data/clients/{client_id}/analyses/seo/seo-audit-{timestamp}.json",
       content=json.dumps(analysis_data, indent=2)
   )
   ```

3. **Update analysis-timeline.json**:
   ```python
   # Read current timeline
   timeline = Read("/data/clients/{client_id}/history/analysis-timeline.json")

   # Append new analysis
   timeline["analyses"].append({
       "analysis_id": f"seo-audit-{timestamp}",
       "type": "seo",
       "timestamp": timestamp,
       ...
   })

   # Write back
   Write("/data/clients/{client_id}/history/analysis-timeline.json", timeline)
   ```

4. **Log to conversation history**:
   ```bash
   echo '{"timestamp":"...","role":"assistant","analysis_id":"..."}' >> /data/clients/acme-corp/history/conversation-log.jsonl
   ```

---

### Updating Context Files

**Incremental Update Pattern**:

```python
# 1. Read existing context
company_profile = Read("/data/clients/acme-corp/context/company-profile.json")

# 2. Update specific fields
company_profile["competitors"].append({
    "name": "New Competitor C",
    "url": "https://competitorc.com"
})
company_profile["last_updated"] = current_timestamp()

# 3. Write back
Write("/data/clients/acme-corp/context/company-profile.json", company_profile)
```

**Never Overwrite Without Reading First** - Always preserve existing context.

---

## Data Analysis with Bash Tool

### Using Python for Data Processing

With the Bash tool enabled, agents can now perform advanced data analysis:

**Example: Statistical Analysis of Campaign Data**

```python
Bash("""
python3 << 'EOF'
import pandas as pd
import json

# Read raw campaign data
df = pd.read_csv('/data/clients/acme-corp/raw-data/google-ads-export-2024-01-15.csv')

# Calculate metrics
analysis = {
    "total_spend": float(df['spend'].sum()),
    "total_conversions": int(df['conversions'].sum()),
    "avg_roas": float(df['roas'].mean()),
    "campaigns_analyzed": len(df),
    "top_performers": df.nlargest(5, 'roas')[['campaign', 'roas']].to_dict('records')
}

# Write analysis
with open('/data/clients/acme-corp/analyses/ads/ads-campaign-analysis-2024-01-15-160033.json', 'w') as f:
    json.dump(analysis, f, indent=2)

print(json.dumps(analysis, indent=2))
EOF
""")
```

**Example: Chart Generation**

```python
Bash("""
python3 << 'EOF'
import matplotlib.pyplot as plt
import pandas as pd
import json

# Read data
with open('/data/clients/acme-corp/analyses/ads/ads-campaign-analysis-2024-01-15-160033.json') as f:
    data = json.load(f)

# Create chart
platforms = [item['campaign'] for item in data['top_performers']]
roas_values = [item['roas'] for item in data['top_performers']]

plt.figure(figsize=(10, 6))
plt.bar(platforms, roas_values)
plt.title('Top 5 Campaigns by ROAS')
plt.xlabel('Campaign')
plt.ylabel('ROAS')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Save chart
plt.savefig('/docs/marketing/acme-corp/campaign-roas-chart.png', dpi=300)
print("Chart saved to /docs/marketing/acme-corp/campaign-roas-chart.png")
EOF
""")
```

---

## Agent-Specific Workspace Usage

### GEO Optimizer

**Writes to**:
- `/data/clients/{id}/analyses/geo/geo-analysis-{timestamp}.json`
- `/data/clients/{id}/analyses/geo/geo-citation-analysis-{timestamp}.json`

**Reads from**:
- `/data/clients/{id}/context/company-profile.json` (for value props, ICP)
- Previous GEO analyses for trend comparison

**Uses Bash for**:
- Citation clustering and statistical analysis
- Sentiment scoring of AI responses
- Multi-engine test result aggregation

---

### SEO Analyst

**Writes to**:
- `/data/clients/{id}/analyses/seo/seo-audit-{timestamp}.json`
- `/data/clients/{id}/analyses/seo/seo-keyword-research-{timestamp}.json`

**Reads from**:
- `/data/clients/{id}/context/company-profile.json`
- `/data/clients/{id}/raw-data/keyword-data-*.json`

**Uses Bash for**:
- Keyword clustering algorithms
- Statistical significance testing
- Traffic forecasting calculations

---

### Ads Analyst

**Writes to**:
- `/data/clients/{id}/analyses/ads/ads-campaign-analysis-{timestamp}.json`
- `/data/clients/{id}/analyses/ads/ads-audience-insights-{timestamp}.json`

**Reads from**:
- `/data/clients/{id}/context/marketing-goals.json` (for ROAS targets)
- `/data/clients/{id}/raw-data/google-ads-export-*.csv`

**Uses Bash for**:
- A/B test statistical significance
- Multi-touch attribution modeling
- Campaign performance forecasting

---

### Presentation Designer

**Writes to**:
- `/docs/marketing/{id}/{name}-presentation.md`
- `/docs/marketing/{id}/charts/*.png` (chart images)

**Reads from**:
- Any analysis files to create presentations
- `/data/clients/{id}/context/brand-guidelines.json`

**Uses Bash for**:
- Chart generation with matplotlib
- Converting markdown to HTML/PDF

---

### Dashboard Creator

**Writes to**:
- `/dashboard/{id}/dashboard.html`
- `/dashboard/{id}/components/*.jsx`

**Reads from**:
- Multiple analysis files for dashboard data
- `/data/clients/{id}/context/marketing-goals.json`

**Uses Bash for**:
- Data aggregation from multiple sources
- JSON generation for dashboard data feeds

---

## Best Practices

### 1. Always Check for Existing Workspace

Before any analysis, check if client workspace exists:

```python
# Check if workspace exists
import os
workspace_path = f"/data/clients/{client_id}"
if not os.path.exists(workspace_path):
    # Create workspace structure
    Bash(f"mkdir -p {workspace_path}/{{analyses/{{geo,seo,ads,competitive,content}},context,history,raw-data,temp}}")
```

### 2. Load Context Early

At the start of every analysis:

```python
# Load company profile
company_profile = Read(f"/data/clients/{client_id}/context/company-profile.json")

# Load marketing goals if doing strategic work
goals = Read(f"/data/clients/{client_id}/context/marketing-goals.json")
```

### 3. Update Analysis Timeline

After completing any analysis:

```python
# Update timeline
timeline = Read(f"/data/clients/{client_id}/history/analysis-timeline.json")
timeline["analyses"].append({...})
Write(f"/data/clients/{client_id}/history/analysis-timeline.json", timeline)
```

### 4. Use Consistent Timestamps

Always use `YYYY-MM-DD-HHMMSS` format:

```bash
timestamp=$(date +"%Y-%m-%d-%H%M%S")
```

### 5. Validate JSON Before Writing

Ensure all JSON is valid before writing to files:

```python
import json
# Validate
json.dumps(analysis_data)  # Will raise error if invalid
# Then write
Write(file_path, json.dumps(analysis_data, indent=2))
```

### 6. Clean Temp Files

Periodically clean temporary processing files:

```bash
# Remove temp files older than 1 day
find /data/clients/*/temp -type f -mtime +1 -delete
```

### 7. Separate Raw Data from Analyses

- **Raw data** = Unprocessed exports (CSV, JSON from platforms)
- **Analyses** = Processed insights with recommendations

Never modify raw data files. Always create new analysis files.

---

## File Retention and Cleanup

### Retention Policies

| File Type | Retention | Cleanup Rule |
|-----------|-----------|--------------|
| Context files | Forever | Never delete |
| Analysis files | 12 months | Archive after 12 months |
| Conversation logs | 6 months | Archive after 6 months |
| Raw data files | 3 months | Delete after 3 months |
| Temp files | 1 day | Auto-delete daily |

### Archive Strategy

```bash
# Archive old analyses to compressed format
tar -czf /data/archives/acme-corp-analyses-2023.tar.gz \
  /data/clients/acme-corp/analyses/
```

---

## Security and Isolation

### Client Isolation Rules

1. **Never read files from other client workspaces**
2. **Always validate client_id before file operations**
3. **Use absolute paths** (not relative)
4. **No symlinks between client directories**

### Sensitive Data

- Do **NOT** store API keys or credentials in workspace files
- Do **NOT** commit workspace files to git (add `/data/clients/` to `.gitignore`)
- **Sanitize** data before logging to conversation history

---

## Migration from Stateless to File-Based

### For Existing Analyses

If you have existing analysis outputs that didn't use this structure:

1. Create client workspace
2. Move analysis to appropriate directory with timestamp
3. Create `company-profile.json` from analysis content
4. Initialize `analysis-timeline.json` with migrated analyses

---

## Summary

**Key Takeaways**:

✅ **Client workspaces** organized under `/data/clients/{client-id}/`
✅ **Timestamped analysis files** enable version history
✅ **Context files** provide persistent client information
✅ **Consistent naming** with `{type}-{name}-{timestamp}.json` format
✅ **Bash tool** enables Python for statistical analysis and chart generation
✅ **Analysis timeline** tracks all completed work
✅ **Separation** between raw data and processed analyses

This structure provides stateful behavior without a database while maintaining simplicity, debuggability, and scalability.
