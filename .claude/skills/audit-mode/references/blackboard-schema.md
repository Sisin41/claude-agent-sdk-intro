# Blackboard Schema

The blackboard is the coordination layer for multi-agent audit execution. Each company being audited gets its own blackboard file on the filesystem.

## File Location

```
/data/audits/{batch-id}/
├── manifest.json                    # Batch-level tracking (multi-company)
├── {company-slug}/
│   ├── blackboard.json              # Per-company phase tracking
│   ├── inputs/
│   │   └── company-profile.json     # Company context
│   └── outputs/
│       ├── geo-light.json           # GEO analysis output
│       ├── seo-light.json           # SEO analysis output
│       ├── content-light.json       # Content generation output
│       └── report.html              # Final branded report
```

## manifest.json (Batch Tracker)

```json
{
  "batch_id": "batch-20260206-143000",
  "created_at": "2026-02-06T14:30:00Z",
  "updated_at": "2026-02-06T14:45:00Z",
  "status": "in_progress",
  "companies": [
    {
      "slug": "acme-corp",
      "domain": "acme.com",
      "status": "completed",
      "blackboard": "acme-corp/blackboard.json"
    },
    {
      "slug": "competitor-a",
      "domain": "competitor-a.com",
      "status": "in_progress",
      "blackboard": "competitor-a/blackboard.json"
    }
  ],
  "totals": {
    "total": 2,
    "completed": 1,
    "in_progress": 1,
    "pending": 0,
    "failed": 0
  }
}
```

## blackboard.json (Per-Company Tracker)

```json
{
  "audit_id": "audit-acme-20260206-143000",
  "batch_id": "batch-20260206-143000",
  "company": {
    "name": "Acme Corp",
    "slug": "acme-corp",
    "domain": "acme.com"
  },
  "status": "in_progress",
  "created_at": "2026-02-06T14:30:00Z",
  "updated_at": "2026-02-06T14:42:00Z",
  "phases": [
    {
      "id": "geo-light",
      "skill": "geo-strategy-synthesis",
      "mode": "light",
      "parallel_group": 1,
      "depends_on": [],
      "status": "completed",
      "output_path": "outputs/geo-light.json",
      "started_at": "2026-02-06T14:30:05Z",
      "completed_at": "2026-02-06T14:35:12Z",
      "duration_seconds": 307,
      "error": null
    },
    {
      "id": "seo-light",
      "skill": "seo-keyword-research",
      "mode": "light",
      "parallel_group": 1,
      "depends_on": [],
      "status": "completed",
      "output_path": "outputs/seo-light.json",
      "started_at": "2026-02-06T14:30:05Z",
      "completed_at": "2026-02-06T14:36:48Z",
      "duration_seconds": 403,
      "error": null
    },
    {
      "id": "content-gen-light",
      "skill": "content-blog-writer",
      "mode": "light",
      "parallel_group": 2,
      "depends_on": ["geo-light", "seo-light"],
      "status": "in_progress",
      "output_path": null,
      "started_at": "2026-02-06T14:36:50Z",
      "completed_at": null,
      "duration_seconds": null,
      "error": null
    },
    {
      "id": "report",
      "skill": "report-builder",
      "mode": "standard",
      "parallel_group": 3,
      "depends_on": ["geo-light", "seo-light", "content-gen-light"],
      "status": "pending",
      "output_path": null,
      "started_at": null,
      "completed_at": null,
      "duration_seconds": null,
      "error": null
    }
  ]
}
```

## Status Values

| Status | Meaning |
|--------|---------|
| `pending` | Not yet started, waiting for dependencies |
| `in_progress` | Currently executing |
| `completed` | Finished successfully, output available |
| `failed` | Execution failed, see `error` field |
| `skipped` | Skipped by user or orchestrator decision |

## Parallel Groups

Phases in the same `parallel_group` number execute simultaneously. Groups execute in ascending order. A group only starts when all phases in the previous group are `completed` (or `skipped`).

```
Group 1: [geo-light, seo-light]     ← run in parallel
Group 2: [content-gen-light]         ← waits for group 1
Group 3: [report]                    ← waits for group 2
```

## Reading the Blackboard

Agents should:
1. Read `blackboard.json` at the start of their execution
2. Check that their dependencies are `completed`
3. Update their own phase status to `in_progress`
4. On completion, update status to `completed` and set `output_path`
5. On failure, update status to `failed` and set `error`

## Multi-Company Parallel Execution

When auditing multiple companies simultaneously:
1. The orchestrator creates a batch with `manifest.json`
2. For each company, it fires a separate `Task` agent (audit-mode skill)
3. Each company's audit runs independently with its own blackboard
4. The orchestrator monitors `manifest.json` for overall progress
5. All company audits can run their internal phases in parallel too

This creates a two-level parallelism:
- **Level 1**: Multiple companies audited simultaneously
- **Level 2**: Within each company, GEO + SEO run in parallel
