# Data Workspace

This directory contains the file-based workspace for the marketing agent system.

## Structure

```
/data/
├── clients/          # Client-specific workspaces
├── templates/        # Analysis templates and schemas
└── scripts/          # Python analysis utilities
```

## Example Client Workspace

See `/data/clients/acme-corp/` for a complete example workspace including:

- **Context files** (company-profile.json, marketing-goals.json, brand-guidelines.json)
- **Analysis files** (SEO audit, ads analysis, competitive analysis)
- **History files** (conversation-log.jsonl, analysis-timeline.json)
- **Raw data** (Google Ads export CSV)

## Documentation

See `WORKSPACE_CONVENTIONS.md` in the project root for complete documentation on:

- Directory structure and naming conventions
- File schemas for all analysis types
- Workspace management rules
- Agent-specific usage patterns
- Best practices

## Getting Started

To create a new client workspace:

```bash
# Use the client ID (e.g., "acme-corp")
CLIENT_ID="your-client-slug"

# Create workspace structure
mkdir -p /data/clients/${CLIENT_ID}/{analyses/{geo,seo,ads,competitive,content},context,history,raw-data,temp}

# Initialize context files
# (See templates/ directory for JSON schemas)
```

## Scripts Directory

The `/data/scripts/` directory will contain Python utilities for:

- **seo/** - Keyword clustering, content analysis, backlink scoring
- **ads/** - Campaign metrics, A/B test significance, attribution modeling
- **geo/** - Citation clustering, sentiment analysis
- **viz/** - Chart generation with matplotlib/plotly

*Note: Scripts to be developed alongside MCP tools implementation.*
