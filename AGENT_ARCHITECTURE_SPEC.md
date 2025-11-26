# Agent Architecture Specification: Environments & Sessions

## Overview

This specification defines the architecture for multi-tenant marketing agent deployment where:
- **Environments** = Company/client workspaces (persistent, shared context)
- **Sessions** = Individual agent conversations (ephemeral, session-specific state)

---

## Table of Contents

1. [Core Concepts](#core-concepts)
2. [Environment Specification](#environment-specification)
3. [Session Specification](#session-specification)
4. [Data Flow & Interaction](#data-flow--interaction)
5. [Technical Implementation](#technical-implementation)
6. [Visualization Component Library](#visualization-component-library)
7. [API Specification](#api-specification)

---

## Core Concepts

### Environment
**Definition**: A persistent workspace for a specific company/client containing all shared context and historical data.

**Lifecycle**: Long-lived (months to years)

**Scope**: Company-wide
- All sessions within an environment share the same context
- All agents (SEO, GEO, Ads, etc.) access the same environment data
- Historical analyses, recommendations, and learnings accumulate

**Analogy**: GitHub Repository (persistent, shared, versioned)

### Session
**Definition**: An individual agent conversation or task execution within an environment.

**Lifecycle**: Short-lived (minutes to hours)
- Created for a specific user request or workflow
- May be ephemeral (single interaction) or persistent (multi-turn conversation)
- Terminated when task is complete or conversation ends

**Scope**: Conversation-specific
- Session-specific context (current task, conversation history)
- References environment data but doesn't modify it directly
- Can spawn sub-sessions for parallel agent execution

**Analogy**: GitHub Pull Request (temporary, task-focused, references repo)

### Relationship
```
Environment (1) ─── contains ──→ Sessions (many)
                │
                └── shared context
                    ├── Company profile
                    ├── Brand guidelines
                    ├── Marketing goals
                    ├── Historical analyses
                    └── Recommendations

Session ─── references ──→ Environment (read)
       └── updates ────→ Environment (write on completion)
```

---

## Environment Specification

### Environment Structure

```
/environments/
├── {environment-id}/
│   ├── metadata.json              # Environment configuration
│   ├── context/                   # Shared context (read by all sessions)
│   │   ├── company-profile.json
│   │   ├── brand-guidelines.json
│   │   ├── marketing-goals.json
│   │   ├── competitors.json
│   │   └── industry-data.json
│   ├── knowledge-base/            # Accumulated learnings
│   │   ├── analyses/              # Historical analysis results
│   │   │   ├── seo/
│   │   │   │   └── {analysis-id}.json
│   │   │   ├── geo/
│   │   │   ├── ads/
│   │   │   └── competitive/
│   │   ├── recommendations/       # Past recommendations with outcomes
│   │   │   └── {recommendation-id}.json
│   │   └── insights/              # Extracted insights and patterns
│   │       └── {insight-id}.json
│   ├── assets/                    # Shared resources
│   │   ├── raw-data/              # Uploaded CSV, JSON exports
│   │   ├── charts/                # Generated visualizations
│   │   └── documents/             # Reports, presentations
│   ├── sessions/                  # Session records
│   │   └── {session-id}/
│   │       ├── session.json       # Session metadata
│   │       ├── conversation.jsonl # Conversation log
│   │       ├── state.json         # Session state
│   │       └── outputs/           # Session-specific outputs
│   └── changelog.jsonl            # Environment change log
```

### Environment Metadata Schema

**File**: `/environments/{environment-id}/metadata.json`

```json
{
  "environment_id": "acme-corp-prod",
  "environment_name": "Acme Corporation - Production",
  "environment_type": "production",
  "created_at": "2024-01-10T09:00:00Z",
  "updated_at": "2024-01-24T15:30:00Z",

  "company": {
    "name": "Acme Corporation",
    "domain": "acmecorp.com",
    "industry": "B2B SaaS",
    "size": "50-500 employees",
    "markets": ["North America", "Europe"]
  },

  "configuration": {
    "default_analysis_mode": "COMPREHENSIVE",
    "auto_update_context": true,
    "session_retention_days": 90,
    "max_concurrent_sessions": 10,
    "enabled_agents": [
      "seo-analyst",
      "geo-optimizer",
      "ads-analyst",
      "presentation-designer",
      "dashboard-creator",
      "content-strategist",
      "competitor-analyst"
    ]
  },

  "access_control": {
    "owners": ["user-123", "user-456"],
    "editors": ["user-789"],
    "viewers": ["team-marketing"],
    "api_access": true,
    "webhook_url": "https://acmecorp.com/webhooks/marketing-agent"
  },

  "integrations": {
    "google_ads": {
      "enabled": true,
      "account_id": "123-456-7890",
      "last_sync": "2024-01-24T10:00:00Z"
    },
    "google_analytics": {
      "enabled": true,
      "property_id": "GA-12345678",
      "last_sync": "2024-01-24T12:00:00Z"
    },
    "moz": {
      "enabled": false
    }
  },

  "statistics": {
    "total_sessions": 156,
    "total_analyses": 342,
    "active_sessions": 2,
    "last_activity": "2024-01-24T15:28:00Z"
  }
}
```

### Context Files

#### Company Profile
**File**: `/environments/{env-id}/context/company-profile.json`

```json
{
  "last_updated": "2024-01-20T10:00:00Z",
  "version": 3,

  "company_info": {
    "name": "Acme Corporation",
    "website": "https://acmecorp.com",
    "industry": "B2B SaaS",
    "founded": "2018",
    "description": "Cloud analytics platform for marketing teams"
  },

  "value_propositions": [
    "Real-time marketing analytics across all channels",
    "AI-powered insights and recommendations",
    "Cross-channel attribution modeling"
  ],

  "ideal_customer_profile": {
    "company_size": "50-500 employees",
    "revenue_range": "$10M-$100M ARR",
    "departments": ["Marketing", "Growth", "Analytics"],
    "pain_points": [
      "Data silos across marketing tools",
      "Slow manual reporting (20+ hours/week)",
      "No clear attribution model"
    ],
    "buying_personas": [
      {
        "role": "CMO",
        "priorities": ["ROI visibility", "Team efficiency"],
        "objections": ["Integration complexity"]
      }
    ]
  },

  "competitors": [
    {
      "name": "Competitor A",
      "url": "https://competitora.com",
      "positioning": "Enterprise-focused",
      "strengths": ["Brand recognition", "Enterprise features"],
      "weaknesses": ["Complex setup", "Expensive"],
      "last_analyzed": "2024-01-15T00:00:00Z"
    }
  ]
}
```

#### Marketing Goals
**File**: `/environments/{env-id}/context/marketing-goals.json`

```json
{
  "last_updated": "2024-01-15T14:30:00Z",
  "fiscal_year": "2024",

  "objectives": [
    {
      "objective_id": "obj-001",
      "goal": "Increase organic traffic",
      "target": "50% growth in 6 months",
      "baseline": 10000,
      "target_value": 15000,
      "unit": "monthly visitors",
      "priority": "high",
      "owner": "SEO Manager",
      "deadline": "2024-06-30",
      "status": "in_progress",
      "progress": 0.32
    }
  ],

  "kpis": [
    {
      "kpi_id": "kpi-001",
      "metric": "Organic Traffic",
      "current": 10000,
      "target": 15000,
      "period": "monthly",
      "trend": "up",
      "last_measured": "2024-01-24T00:00:00Z"
    }
  ],

  "budget": {
    "total_monthly": 105000,
    "currency": "USD",
    "allocation": {
      "paid_search": 50000,
      "paid_social": 30000,
      "content": 20000,
      "tools": 5000
    }
  }
}
```

### Knowledge Base Structure

#### Analysis Record
**File**: `/environments/{env-id}/knowledge-base/analyses/seo/{analysis-id}.json`

```json
{
  "analysis_id": "seo-audit-20240115-143022",
  "type": "seo",
  "subtype": "technical-audit",
  "created_at": "2024-01-15T14:30:22Z",
  "created_by_session": "session-abc123",
  "agent": "seo-analyst",
  "execution_mode": "COMPREHENSIVE",

  "inputs": {
    "website": "https://acmecorp.com",
    "pages_analyzed": 50
  },

  "findings": {
    "overall_score": 68,
    "issues": {
      "critical": 4,
      "high": 8,
      "medium": 12,
      "low": 5
    },
    "details": {...}
  },

  "recommendations": [
    {
      "recommendation_id": "rec-001",
      "priority": "high",
      "category": "technical-seo",
      "issue": "Slow page load time",
      "recommendation": "Optimize images with lazy loading",
      "expected_impact": "+15% organic traffic",
      "effort": "2 weeks",
      "status": "implemented",
      "implementation_date": "2024-01-20",
      "actual_impact": "+12% organic traffic"
    }
  ],

  "metadata": {
    "execution_time_ms": 45000,
    "skill_files_used": [".claude/approaches/seo/technical-audit.md"],
    "tools_used": ["WebFetch", "Bash"]
  }
}
```

#### Recommendation Tracking
**File**: `/environments/{env-id}/knowledge-base/recommendations/{recommendation-id}.json`

```json
{
  "recommendation_id": "rec-001",
  "source_analysis": "seo-audit-20240115-143022",
  "created_at": "2024-01-15T14:30:22Z",

  "recommendation": {
    "category": "technical-seo",
    "priority": "high",
    "issue": "Slow page load time (4.2s desktop)",
    "recommendation": "Optimize images with lazy loading and WebP format",
    "expected_impact": "+15% organic traffic",
    "effort_estimate": "2 weeks"
  },

  "lifecycle": {
    "status": "implemented",
    "assigned_to": "Engineering Team",
    "assigned_date": "2024-01-16T09:00:00Z",
    "implementation_started": "2024-01-17T10:00:00Z",
    "implementation_completed": "2024-01-20T16:00:00Z",
    "verification_date": "2024-01-24T12:00:00Z"
  },

  "outcomes": {
    "actual_impact": "+12% organic traffic",
    "measured_at": "2024-01-24T12:00:00Z",
    "measurement_method": "Google Analytics comparison (30 days before vs after)",
    "additional_benefits": [
      "Improved Core Web Vitals score",
      "Reduced bounce rate by 3%"
    ],
    "lessons_learned": "Image optimization had bigger impact than expected on mobile"
  },

  "related_recommendations": ["rec-002", "rec-003"]
}
```

#### Insight Extraction
**File**: `/environments/{env-id}/knowledge-base/insights/{insight-id}.json`

```json
{
  "insight_id": "insight-001",
  "type": "pattern",
  "created_at": "2024-01-24T10:00:00Z",
  "confidence": 0.85,

  "insight": {
    "title": "Competitor comparison keywords have 2x higher ROAS",
    "description": "Analysis of 5 ad campaigns shows that keywords comparing Acme to competitors consistently achieve ROAS of 3.8 vs 1.9 for generic keywords",
    "category": "advertising",
    "tags": ["paid-search", "competitor-comparison", "roas-optimization"]
  },

  "evidence": {
    "source_analyses": [
      "ads-campaign-analysis-20240112-140000",
      "ads-campaign-analysis-20240118-093000"
    ],
    "data_points": 22,
    "observation_period": "90 days",
    "statistical_significance": 0.95
  },

  "recommendations": [
    "Increase budget allocation to competitor comparison keywords by 30%",
    "Create more competitor comparison landing pages",
    "Develop content comparing Acme features to Competitor A and B"
  ],

  "applied": true,
  "application_date": "2024-01-22T00:00:00Z",
  "impact_measurement": {
    "expected": "+20% overall ROAS",
    "actual": "+18% overall ROAS",
    "measured_at": "2024-02-10T00:00:00Z"
  }
}
```

---

## Session Specification

### Session Structure

```
/environments/{environment-id}/sessions/{session-id}/
├── session.json           # Session metadata
├── conversation.jsonl     # Multi-turn conversation log
├── state.json            # Current session state
├── context.json          # Session-specific context
├── outputs/              # Session outputs
│   ├── analyses/         # Analysis results (before committing to knowledge-base)
│   ├── visualizations/   # Generated charts/tables for display
│   └── artifacts/        # Temporary files
└── logs/                 # Session execution logs
    ├── agent-calls.jsonl
    ├── tool-calls.jsonl
    └── errors.jsonl
```

### Session Metadata Schema

**File**: `/environments/{env-id}/sessions/{session-id}/session.json`

```json
{
  "session_id": "session-abc123",
  "environment_id": "acme-corp-prod",

  "lifecycle": {
    "status": "active",
    "created_at": "2024-01-24T14:00:00Z",
    "updated_at": "2024-01-24T14:15:32Z",
    "expires_at": "2024-01-24T18:00:00Z",
    "terminated_at": null
  },

  "session_type": "interactive",
  "session_mode": "conversational",

  "user": {
    "user_id": "user-123",
    "username": "sarah@acmecorp.com",
    "role": "marketing_manager"
  },

  "agent": {
    "primary_agent": "seo-analyst",
    "delegated_agents": ["competitor-analyst"],
    "execution_mode": "COMPREHENSIVE"
  },

  "task": {
    "task_type": "analysis",
    "task_description": "Perform SEO audit and competitive analysis",
    "expected_duration_minutes": 30,
    "priority": "normal"
  },

  "statistics": {
    "total_messages": 12,
    "agent_calls": 3,
    "tool_calls": 45,
    "analyses_generated": 2,
    "files_created": 3,
    "api_calls": 67,
    "total_cost_usd": 2.34
  },

  "parent_session": null,
  "child_sessions": ["session-def456", "session-ghi789"]
}
```

### Session Types

| Type | Description | Lifecycle | Use Case |
|------|-------------|-----------|----------|
| **interactive** | Multi-turn conversation | Hours | User chatting with agent |
| **batch** | Single execution | Minutes | Scheduled analysis |
| **workflow** | Multi-step process | Hours | Complex multi-agent workflow |
| **api** | API-triggered | Seconds | External system integration |

### Session Modes

| Mode | Description | Agent Behavior |
|------|-------------|----------------|
| **conversational** | Back-and-forth dialog | Asks clarifying questions |
| **autonomous** | Execute and report | Minimal user interaction |
| **collaborative** | Step-by-step with user | Confirms each step |

### Session State Schema

**File**: `/environments/{env-id}/sessions/{session-id}/state.json`

```json
{
  "current_step": "analyzing_competitors",
  "progress": 0.65,

  "workflow": {
    "total_steps": 5,
    "completed_steps": 3,
    "current_step": 4,
    "steps": [
      {
        "step_id": 1,
        "name": "Load context",
        "status": "completed",
        "started_at": "2024-01-24T14:00:00Z",
        "completed_at": "2024-01-24T14:00:02Z"
      },
      {
        "step_id": 2,
        "name": "Run SEO audit",
        "status": "completed",
        "started_at": "2024-01-24T14:00:02Z",
        "completed_at": "2024-01-24T14:05:30Z"
      },
      {
        "step_id": 3,
        "name": "Identify competitors",
        "status": "completed",
        "started_at": "2024-01-24T14:05:30Z",
        "completed_at": "2024-01-24T14:06:15Z"
      },
      {
        "step_id": 4,
        "name": "Analyze competitors",
        "status": "in_progress",
        "started_at": "2024-01-24T14:06:15Z",
        "progress": 0.4
      },
      {
        "step_id": 5,
        "name": "Generate recommendations",
        "status": "pending"
      }
    ]
  },

  "active_tasks": [
    {
      "task_id": "task-001",
      "agent": "competitor-analyst",
      "description": "Analyzing Competitor A website",
      "progress": 0.6,
      "started_at": "2024-01-24T14:10:00Z"
    }
  ],

  "pending_actions": [
    {
      "action": "user_confirmation",
      "message": "Found 8 critical SEO issues. Should I create detailed fix plan?",
      "options": ["yes", "no", "show_issues_first"]
    }
  ],

  "variables": {
    "competitors_found": 5,
    "seo_score": 68,
    "priority_issues": 4,
    "estimated_time_remaining_minutes": 10
  }
}
```

### Conversation Log

**File**: `/environments/{env-id}/sessions/{session-id}/conversation.jsonl`

```jsonl
{"timestamp": "2024-01-24T14:00:00Z", "role": "user", "content": "Run a comprehensive SEO audit and compare us to our top 3 competitors", "message_id": "msg-001"}
{"timestamp": "2024-01-24T14:00:01Z", "role": "assistant", "content": "I'll run a comprehensive SEO audit for acmecorp.com and analyze your top 3 competitors. This will take approximately 20-30 minutes.", "message_id": "msg-002", "metadata": {"agents_to_delegate": ["seo-analyst", "competitor-analyst"]}}
{"timestamp": "2024-01-24T14:00:02Z", "role": "system", "event": "agent_delegated", "agent": "seo-analyst", "task": "Technical SEO audit"}
{"timestamp": "2024-01-24T14:05:30Z", "role": "assistant", "content": "SEO audit complete. Found 12 issues (4 critical). Now analyzing competitors...", "message_id": "msg-003", "metadata": {"analysis_id": "seo-audit-20240124-140530", "visualization": "seo-score-card"}}
{"timestamp": "2024-01-24T14:10:00Z", "role": "assistant", "content": "Competitor analysis in progress (2 of 3 complete)...", "message_id": "msg-004", "metadata": {"progress": 0.67, "visualization": "competitor-progress-bar"}}
```

---

## Data Flow & Interaction

### Session Creation Flow

```
1. User requests new analysis
   ↓
2. System creates session
   - Generate session_id
   - Load environment context
   - Initialize session state
   ↓
3. Session reads environment context
   - company-profile.json
   - marketing-goals.json
   - brand-guidelines.json
   - Previous analyses (if relevant)
   ↓
4. Agent executes task
   - Uses environment context
   - Generates session-specific outputs
   - Updates session state in real-time
   ↓
5. Session completes
   - Commit outputs to environment knowledge-base
   - Update environment context (if needed)
   - Archive session
```

### Environment Update Flow

```
Session generates recommendation
   ↓
User approves recommendation
   ↓
Recommendation added to environment knowledge-base
   ↓
Track implementation status
   ↓
Measure outcome
   ↓
Update recommendation with results
   ↓
Extract insight if pattern detected
   ↓
Update environment context if significant
```

### Multi-Session Coordination

**Scenario**: User asks for complete marketing analysis

```
Session-001 (Master)
   ├── Delegates to Session-002 (SEO Analyst)
   ├── Delegates to Session-003 (Ads Analyst)
   ├── Delegates to Session-004 (GEO Optimizer)
   └── Delegates to Session-005 (Competitor Analyst)

All sessions read same environment context
   ↓
Execute in parallel
   ↓
Return results to Session-001
   ↓
Session-001 synthesizes results
   ↓
Commit all outputs to environment knowledge-base
```

---

## Technical Implementation

### Database Schema (if using PostgreSQL/MongoDB)

#### Environments Table

```sql
CREATE TABLE environments (
    environment_id VARCHAR(100) PRIMARY KEY,
    environment_name VARCHAR(255) NOT NULL,
    environment_type VARCHAR(50) NOT NULL, -- 'production', 'staging', 'development'
    company_name VARCHAR(255) NOT NULL,
    company_domain VARCHAR(255),
    industry VARCHAR(100),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    configuration JSONB,
    access_control JSONB,
    integrations JSONB,
    statistics JSONB,
    status VARCHAR(50) DEFAULT 'active', -- 'active', 'archived', 'deleted'

    INDEX idx_company_domain (company_domain),
    INDEX idx_status (status),
    INDEX idx_created_at (created_at)
);
```

#### Sessions Table

```sql
CREATE TABLE sessions (
    session_id VARCHAR(100) PRIMARY KEY,
    environment_id VARCHAR(100) NOT NULL REFERENCES environments(environment_id),
    session_type VARCHAR(50) NOT NULL, -- 'interactive', 'batch', 'workflow', 'api'
    session_mode VARCHAR(50) NOT NULL, -- 'conversational', 'autonomous', 'collaborative'
    status VARCHAR(50) NOT NULL, -- 'active', 'completed', 'failed', 'expired'

    user_id VARCHAR(100),
    primary_agent VARCHAR(100),

    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    expires_at TIMESTAMP,
    terminated_at TIMESTAMP,

    task JSONB,
    state JSONB,
    statistics JSONB,

    parent_session_id VARCHAR(100) REFERENCES sessions(session_id),

    INDEX idx_environment_id (environment_id),
    INDEX idx_status (status),
    INDEX idx_user_id (user_id),
    INDEX idx_created_at (created_at),
    INDEX idx_parent_session (parent_session_id)
);
```

#### Analyses Table

```sql
CREATE TABLE analyses (
    analysis_id VARCHAR(100) PRIMARY KEY,
    environment_id VARCHAR(100) NOT NULL REFERENCES environments(environment_id),
    session_id VARCHAR(100) REFERENCES sessions(session_id),

    analysis_type VARCHAR(50) NOT NULL, -- 'seo', 'geo', 'ads', etc.
    analysis_subtype VARCHAR(50),

    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    agent VARCHAR(100),
    execution_mode VARCHAR(50),

    inputs JSONB,
    findings JSONB,
    recommendations JSONB,
    metadata JSONB,

    INDEX idx_environment_id (environment_id),
    INDEX idx_session_id (session_id),
    INDEX idx_analysis_type (analysis_type),
    INDEX idx_created_at (created_at)
);
```

### File-based Alternative

If using file-based storage (current approach):

```python
# Environment management
class Environment:
    def __init__(self, environment_id: str):
        self.environment_id = environment_id
        self.base_path = f"/environments/{environment_id}"

    def load_context(self, context_type: str):
        """Load shared context (company-profile, marketing-goals, etc.)"""
        path = f"{self.base_path}/context/{context_type}.json"
        return json.load(open(path))

    def get_analyses(self, analysis_type: str = None, since: datetime = None):
        """Get historical analyses"""
        path = f"{self.base_path}/knowledge-base/analyses/"
        if analysis_type:
            path += f"{analysis_type}/"
        # Return filtered analyses

    def commit_analysis(self, session_id: str, analysis: dict):
        """Commit session analysis to environment knowledge-base"""
        analysis_id = analysis['analysis_id']
        analysis_type = analysis['type']
        path = f"{self.base_path}/knowledge-base/analyses/{analysis_type}/{analysis_id}.json"
        json.dump(analysis, open(path, 'w'), indent=2)

        # Update changelog
        self._log_change(f"Analysis {analysis_id} added by session {session_id}")

class Session:
    def __init__(self, session_id: str, environment_id: str):
        self.session_id = session_id
        self.environment = Environment(environment_id)
        self.base_path = f"/environments/{environment_id}/sessions/{session_id}"

    def load_environment_context(self):
        """Load shared environment context"""
        return {
            'company_profile': self.environment.load_context('company-profile'),
            'marketing_goals': self.environment.load_context('marketing-goals'),
            'brand_guidelines': self.environment.load_context('brand-guidelines'),
        }

    def update_state(self, state: dict):
        """Update session state"""
        path = f"{self.base_path}/state.json"
        json.dump(state, open(path, 'w'), indent=2)

    def log_message(self, role: str, content: str, metadata: dict = None):
        """Append to conversation log"""
        path = f"{self.base_path}/conversation.jsonl"
        entry = {
            'timestamp': datetime.now().isoformat(),
            'role': role,
            'content': content,
            'metadata': metadata
        }
        with open(path, 'a') as f:
            f.write(json.dumps(entry) + '\n')

    def save_visualization(self, viz_id: str, viz_data: dict):
        """Save visualization for display"""
        path = f"{self.base_path}/outputs/visualizations/{viz_id}.json"
        json.dump(viz_data, open(path, 'w'), indent=2)
```

### API Endpoints

```python
# Environment Management
POST   /api/environments                    # Create environment
GET    /api/environments/{env_id}           # Get environment details
PUT    /api/environments/{env_id}           # Update environment
DELETE /api/environments/{env_id}           # Archive environment
GET    /api/environments/{env_id}/context   # Get all context
PUT    /api/environments/{env_id}/context/{type}  # Update specific context

# Session Management
POST   /api/environments/{env_id}/sessions  # Create session
GET    /api/sessions/{session_id}           # Get session details
PUT    /api/sessions/{session_id}/state     # Update session state
DELETE /api/sessions/{session_id}           # Terminate session
GET    /api/sessions/{session_id}/conversation  # Get conversation log
POST   /api/sessions/{session_id}/messages  # Send message to session

# Analysis Management
GET    /api/environments/{env_id}/analyses  # List analyses
GET    /api/analyses/{analysis_id}          # Get specific analysis
POST   /api/environments/{env_id}/analyses  # Create analysis (from session)

# Knowledge Base
GET    /api/environments/{env_id}/insights  # Get extracted insights
GET    /api/environments/{env_id}/recommendations  # Get recommendations
PUT    /api/recommendations/{rec_id}        # Update recommendation status
```

---

## Visualization Component Library

### Overview

All visualizations are **text-based** (ASCII/Unicode) for terminal display and web rendering.

**Design Principles**:
- ✅ Render in terminal (Claude Code interface)
- ✅ Render in web (HTML/CSS conversion)
- ✅ Copy-paste friendly (plain text)
- ✅ Accessible (screen readers can parse)
- ✅ Responsive (adapt to terminal width)

---

### 1. Data Tables

#### Component: DataTable

**Use Cases**: Campaign performance, keyword rankings, competitor comparison

**Example**:
```
┌────────────────────┬──────────┬─────────┬──────────┬──────────┐
│ Campaign           │ Spend    │ Conv.   │ CPA      │ ROAS     │
├────────────────────┼──────────┼─────────┼──────────┼──────────┤
│ Brand Search       │ $12,450  │ 180     │ $69.17   │ 4.2  ⭐  │
│ Competitor Compare │ $8,320   │ 125     │ $66.56   │ 3.8      │
│ Generic Keywords   │ $18,750  │ 95      │ $197.37  │ 1.7  ⚠️  │
│ Retargeting        │ $6,200   │ 85      │ $72.94   │ 3.5      │
└────────────────────┴──────────┴─────────┴──────────┴──────────┘

Total: $45,720  |  Conversions: 485  |  Avg ROAS: 3.3
```

**Features**:
- ✅ Box drawing characters (┌ ─ ┐ │ ├ ┤ └ ┴ ┘)
- ✅ Column alignment (left for text, right for numbers)
- ✅ Visual indicators (⭐ ⚠️ ❌ ✓)
- ✅ Summary row at bottom
- ✅ Sortable columns (arrows ↑ ↓)
- ✅ Highlight rows (different background colors)

**Variants**:
- Compact table (single line borders)
- Zebra striping (alternating row colors)
- Expandable rows (click to show details)
- Frozen header (scrollable body)

---

### 2. Bar Charts (Horizontal)

#### Component: HorizontalBarChart

**Use Cases**: Campaign comparison, keyword difficulty, ROAS by platform

**Example**:
```
Top 5 Campaigns by ROAS

Retargeting     ████████████████████████████  8.6  ($285 spent)
Brand Search    ████████████████████████      8.3  ($425 spent)
Pricing Intent  ███████████████████           5.3  ($340 spent)
Demo Intent     ██████████████████            5.2  ($290 spent)
Competitor Comp ███████████████               3.8  ($360 spent)

0    1    2    3    4    5    6    7    8    9   10
                        ROAS
```

**Features**:
- ✅ Unicode block characters (█ ▓ ▒ ░ for different intensities)
- ✅ Value labels at end of bars
- ✅ Axis labels and scale
- ✅ Color coding (high = green, medium = yellow, low = red)
- ✅ Inline metadata (spend shown in parentheses)

**Variants**:
- Stacked bars (multiple values per category)
- Grouped bars (side-by-side comparison)
- Sparkbars (mini inline bars: Trend: ▂▃▅▇▆▄▂)

---

### 3. Bar Charts (Vertical)

#### Component: VerticalBarChart

**Use Cases**: Monthly trends, weekly performance, time-series data

**Example**:
```
Organic Traffic Growth (Last 6 Months)

15K ┤                           ███
    │                       ███ ███
12K ┤                   ███ ███ ███
    │               ███ ███ ███ ███
 9K ┤           ███ ███ ███ ███ ███
    │       ███ ███ ███ ███ ███ ███
 6K ┤   ███ ███ ███ ███ ███ ███ ███
    │   ███ ███ ███ ███ ███ ███ ███
 3K ┤   ███ ███ ███ ███ ███ ███ ███
    └───┴───┴───┴───┴───┴───┴───┴──
      Aug Sep Oct Nov Dec Jan

Target: 15K  |  Current: 12.1K  |  Progress: 81% ✓
```

**Features**:
- ✅ Y-axis with scale markers (┤)
- ✅ X-axis labels
- ✅ Grid lines (optional)
- ✅ Target line indicator
- ✅ Summary metrics below

---

### 4. Line Charts

#### Component: LineChart

**Use Cases**: Traffic trends, ranking changes over time, budget pacing

**Example**:
```
SEO Ranking Position (Last 30 Days)

Position
   1 ┤
   5 ┤  ●───●
  10 ┤        ●───●───●
  15 ┤                  ╲
  20 ┤                   ●───●
  25 ┤                         ╲
  30 ┤                          ●─────●
     └─────┬─────┬─────┬─────┬─────┬─────
         Dec 25  Jan 1  Jan 8 Jan15 Jan22

Keyword: "marketing analytics software"
Current: Position 8  |  Best: Position 5  |  Trend: ↑ Improving
```

**Features**:
- ✅ Line drawing with ─ │ ╲ ╱ ●
- ✅ Data points marked (●)
- ✅ Axis labels with dates
- ✅ Trend indicators
- ✅ Multiple lines (different symbols: ● ■ ▲)

**Variants**:
- Area chart (filled below line with ▓▒░)
- Multi-line comparison (Organic: ●─● vs Paid: ■─■)
- Sparkline (mini inline: ▁▂▃▅▇▆▄▂)

---

### 5. Pie Charts (Donut Charts)

#### Component: PieChart

**Use Cases**: Budget allocation, traffic sources, sentiment distribution

**Example**:
```
Marketing Budget Allocation

        ╭─────────────╮
     ╭──┤ Paid Search ├──╮
    │   ╰─────────────╯   │
    │      ███████         │  Paid Search:  $50K (48%)
    │    ███████████       │  Paid Social:  $30K (29%)
    │   ███████████████    │  Content:      $20K (19%)
    │    ██████╱╱██████    │  SEO Tools:    $5K  (5%)
    │     ███╱╱╱╱╱████     │
     ╰────╱╱╱╱╱╱╱╱────╯    Total: $105K/month

Legend: ███ Paid Search  ▓▓▓ Paid Social  ▒▒▒ Content  ░░░ Tools
```

**Features**:
- ✅ Circular representation with Unicode
- ✅ Segment labels
- ✅ Percentage and absolute values
- ✅ Legend with color mapping
- ✅ Total summary

**Alternative (Text-based)**:
```
Budget Allocation

Paid Search    ████████████████████████████████████████████████  48%  $50K
Paid Social    ██████████████████████████████                    29%  $30K
Content        ███████████████████████                           19%  $20K
SEO Tools      ██████                                             5%  $5K
               └────────────────────────────────────────────────┘
               0%          25%          50%          75%        100%
```

---

### 6. Progress Bars

#### Component: ProgressBar

**Use Cases**: Goal completion, task progress, session status

**Example**:
```
Monthly Objectives Progress

Organic Traffic Growth
Target: 15,000 visitors  |  Current: 12,100  |  81% complete
[████████████████████████████████░░░░░░░░] 81%  ✓ On track

MQL Generation
Target: 500 MQLs  |  Current: 320  |  64% complete
[██████████████████████████░░░░░░░░░░░░░░] 64%  ⚠️ Behind

ROAS Improvement
Target: 4.0  |  Current: 2.8  |  70% complete
[██████████████████████████████░░░░░░░░░░] 70%  ⚠️ Needs attention
```

**Features**:
- ✅ Filled segments (█) vs empty (░)
- ✅ Percentage label
- ✅ Status indicators (✓ ⚠️ ❌)
- ✅ Current vs target values
- ✅ Color coding (green/yellow/red zones)

**Variants**:
- Circular progress: ◔ ◑ ◕ ●
- Mini progress: [▰▰▰▱▱] 60%
- Stepped progress: ①──②──③──④──⑤

---

### 7. Gauges/Meters

#### Component: Gauge

**Use Cases**: SEO score, performance rating, health indicators

**Example**:
```
SEO Health Score

      Poor        Fair         Good        Excellent
        ├───────────┼───────────┼───────────┤
        0          40          70         100
                            ▲
                           68

Overall SEO Score: 68/100 (Good)

Technical SEO:    ████████████░░░░░░░░  62/100  Fair
Content Quality:  ██████████████████░░  80/100  Excellent
Backlinks:        ██████████░░░░░░░░░░  50/100  Poor
Mobile:           ███████████████░░░░░  75/100  Good
```

**Features**:
- ✅ Scale with zones (Poor/Fair/Good/Excellent)
- ✅ Pointer (▲ ▼ ►)
- ✅ Numeric score
- ✅ Category breakdown
- ✅ Color zones

**Variants**:
- Speedometer style
- Thermometer (vertical)
- Battery indicator: [████████░░] 80%

---

### 8. Heatmaps

#### Component: Heatmap

**Use Cases**: Ranking distribution, sentiment by topic, performance matrix

**Example**:
```
Keyword Ranking Distribution (Position Heatmap)

              Week 1  Week 2  Week 3  Week 4
Keyword 1       ██      ██      ▓▓      ▒▒   (improving: 8→5)
Keyword 2       ░░      ░░      ░░      ░░   (stable: 25-27)
Keyword 3       ▓▓      ██      ██      ██   (excellent: 3-5)
Keyword 4       ▒▒      ▓▓      ██      ██   (improving: 12→4)
Keyword 5       ██      ▓▓      ▓▓      ▒▒   (declining: 5→10)

Legend: ██ Top 5  ▓▓ 6-10  ▒▒ 11-20  ░░ 21+
```

**Features**:
- ✅ Intensity gradients (██ ▓▓ ▒▒ ░░)
- ✅ Row/column labels
- ✅ Color legend
- ✅ Trend annotations
- ✅ Compact grid format

**Use Cases**:
- Time-based performance
- Multi-dimensional comparison
- Correlation matrix

---

### 9. Network Graphs

#### Component: NetworkGraph

**Use Cases**: Competitive landscape, topic relationships, citation network

**Example**:
```
Competitive Landscape Map

                    Enterprise Tier
                          │
        Competitor A ─────┼───── Competitor B
             │            │            │
             │     ┌──────┴──────┐     │
             │     │   Market    │     │
             └─────┤   Leader    ├─────┘
                   │   (You)     │
                   └──────┬──────┘
                          │
            ┌─────────────┼─────────────┐
            │             │             │
      Competitor C   Competitor D   Competitor E
         (SMB)         (Mid-market)    (Niche)

Legend:
  ─── Direct competition
  ··· Indirect overlap
  Size = Market share
```

**Features**:
- ✅ Node representation
- ✅ Edge connections (─ ─ ─, ···)
- ✅ Hierarchical layout
- ✅ Labels and annotations
- ✅ Legend

**Variants**:
- Tree diagram (hierarchical)
- Mind map (radial)
- Flow diagram (directional →)

---

### 10. Sparklines

#### Component: Sparkline

**Use Cases**: Inline trends, mini charts in tables, dashboard KPIs

**Example**:
```
Key Metrics Dashboard

Organic Traffic     12,100   Trend: ▁▂▃▅▇▆▇  (+18% vs last month)
Paid Conversions       485   Trend: ▄▅▅▆▆▇▇  (+12% vs last month)
ROAS                   2.8   Trend: ▂▃▃▄▃▃▄  (+8% vs last month)
Bounce Rate           42%    Trend: ▇▆▅▄▃▃▂  (-15% vs last month) ✓
Avg Session Time     3:45    Trend: ▃▃▄▅▅▆▇  (+22% vs last month)
```

**Features**:
- ✅ Compact (single line)
- ✅ 8 levels of height (▁▂▃▄▅▆▇█)
- ✅ Inline with metrics
- ✅ Trend direction visible at glance
- ✅ Minimal space usage

**Variants**:
- Line sparkline: ╱╲╱─
- Bar sparkline: ▁▂▃▅▇
- Win/loss: ▄▄▅█▅▄▃ (W) vs ▆▅▄▃▂▁ (L)

---

### 11. Funnel Charts

#### Component: FunnelChart

**Use Cases**: Conversion funnels, sales pipeline, user journey

**Example**:
```
Marketing Funnel

Website Visitors        ████████████████████████████████  10,000  (100%)
                        └──────────────────────┐
Lead Magnet Downloads   ████████████████████            3,500   (35%)
                        └────────────────┐
MQL (Marketing Qual)    ████████████              1,200   (12%)
                        └──────────┐
SQL (Sales Qual)        ████████            850   (8.5%)
                        └──────┐
Opportunities           █████        320   (3.2%)
                        └────┐
Customers               ███    95   (0.95%)

Conversion Rate: 0.95%  |  Biggest Drop: Visitors→Downloads (65% drop)
```

**Features**:
- ✅ Tapering width (shows drop-off)
- ✅ Percentage and absolute numbers
- ✅ Conversion rate between stages
- ✅ Highlight biggest drop-off
- ✅ Summary metrics

---

### 12. Comparison Matrix

#### Component: ComparisonMatrix

**Use Cases**: Feature comparison, competitor analysis, option evaluation

**Example**:
```
Competitor Feature Comparison

                      Acme   Comp A  Comp B  Comp C
Real-time Analytics    ✓       ✓      ✓       ✗
AI Insights            ✓       ✗      ✓       ✗
Multi-channel Attrib   ✓       ✓      ✗       ✗
API Access             ✓       ✓      ✓       ✓
White Label            ✓       ✗      ✗       ✓
Mobile App             ✓       ✓      ✗       ✗
Price/month         $399    $699    $299    $499

Score (out of 7)       7       5       4       3
                      ⭐      ─       ─       ─
```

**Features**:
- ✅ Checkmarks (✓) and crosses (✗)
- ✅ Row headers (features)
- ✅ Column headers (competitors)
- ✅ Summary row (total score)
- ✅ Visual winner indicator (⭐)

**Variants**:
- Traffic light (🟢 🟡 🔴)
- Star ratings (⭐⭐⭐⭐⭐)
- Numeric scores (1-10)

---

### 13. Timelines

#### Component: Timeline

**Use Cases**: Recommendation tracking, campaign history, project milestones

**Example**:
```
SEO Optimization Timeline

2024-01-10  ●  SEO Audit Completed
            │  Found 12 critical issues
            │
2024-01-15  ●  Recommendations Approved
            │  Budget allocated: $15K
            │
2024-01-20  ●─────● Image Optimization (DONE)
            │       Impact: +12% traffic
            │
2024-01-22  ●─────● Meta Tags Fixed (DONE)
            │       Impact: +5% CTR
            │
2024-01-24  ●──────────────────●  Content Expansion (IN PROGRESS)
            │                     Expected completion: Feb 10
            │
2024-02-01  ○  Schema Markup (PLANNED)
            │
2024-02-15  ○  Backlink Campaign (PLANNED)

Legend: ● Completed  ● In Progress  ○ Planned
```

**Features**:
- ✅ Vertical timeline with dates
- ✅ Event markers (● ○)
- ✅ Status indicators
- ✅ Duration bars (─────)
- ✅ Annotations
- ✅ Legend

**Variants**:
- Horizontal timeline
- Gantt chart style
- Milestone markers

---

### 14. Status Cards/KPI Cards

#### Component: KPICard

**Use Cases**: Dashboard metrics, summary stats, key indicators

**Example**:
```
╔════════════════════════════════════╗
║  Organic Traffic                   ║
║  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  ║
║                                    ║
║         12,100 visitors            ║
║                                    ║
║         ↑ 18%  vs last month       ║
║         ▁▂▃▅▇▆▇  (7-day trend)     ║
║                                    ║
║  Target: 15,000  |  81% to goal    ║
╚════════════════════════════════════╝
```

**Features**:
- ✅ Box borders (╔ ═ ╗ ║ ╚ ╝)
- ✅ Large numeric display
- ✅ Trend indicator (↑ ↓ →)
- ✅ Sparkline
- ✅ Goal progress
- ✅ Visual emphasis

**Variants**:
- Compact card (single line)
- Multi-metric card (grid of values)
- Colored backgrounds (status-based)

---

### 15. Scatter Plots

#### Component: ScatterPlot

**Use Cases**: Keyword difficulty vs volume, cost vs ROAS, positioning map

**Example**:
```
Keyword Opportunity Map (Difficulty vs Search Volume)

Volume
  10K ┤                                      ● keyword-3
      │                                      (high volume, low diff)
   5K ┤              ● keyword-1
      │              (balanced)       ● keyword-2
   2K ┤     ● keyword-5               (high volume, high diff)
      │
   1K ┤  ● keyword-4
      │  (low volume, low diff)
      └──────┬──────┬──────┬──────┬──────┬──────
            10     20     30     40     50     60
                    Keyword Difficulty

Quadrants:
  Top-Left:  Low Diff, High Volume (BEST)  ← keyword-3
  Top-Right: High Diff, High Volume (COMPETITIVE)  ← keyword-2
  Bottom-Left: Low Diff, Low Volume (EASY WINS)  ← keyword-4, 5
  Bottom-Right: High Diff, Low Volume (AVOID)
```

**Features**:
- ✅ X and Y axes with scales
- ✅ Data points (● ■ ▲)
- ✅ Point labels
- ✅ Quadrant lines (optional)
- ✅ Legend and annotations

---

### 16. Tree Maps (Text-based)

#### Component: TreeMap

**Use Cases**: Budget allocation, traffic sources breakdown, hierarchical data

**Example**:
```
Traffic Source Breakdown

┌─────────────────────────────────────────────────┐
│ Direct (35%)                                    │
│ ████████████████████                            │
├─────────────────────────┬───────────────────────┤
│ Organic Search (28%)    │ Paid Search (22%)     │
│ ██████████████          │ ███████████           │
├─────────────┬───────────┼───────────┬───────────┤
│ Social (8%) │ Email (5%)│ Referral  │ Other     │
│ ████        │ ███       │ (1.5%)    │ (0.5%)    │
└─────────────┴───────────┴───────────┴───────────┘

Total Sessions: 45,320
```

**Features**:
- ✅ Nested rectangles
- ✅ Size proportional to value
- ✅ Percentage labels
- ✅ Hierarchical grouping

---

### 17. Bullet Graphs

#### Component: BulletGraph

**Use Cases**: Performance vs target, KPI tracking with ranges

**Example**:
```
Q1 Marketing Performance vs Target

Organic Traffic
Poor    Fair     Good    Excellent
├───────┼────────┼────────┤
│░░░░░░░│▓▓▓▓▓▓▓▓│████████│▒▒▒▒▒▒▒▒│
├───────┼────────┼────────┤
 5K     10K     15K     20K
Target: 15K  |  Actual: 12.1K  |  81% ✓

ROAS
├───────┼────────┼────────┤
│░░░░░░░│▓▓▓▓▓▓▓▓│██████  │▒▒▒▒▒▒▒▒│
├───────┼────────┼────────┤
 1.0     2.0     4.0     6.0
Target: 4.0  |  Actual: 2.8  |  70% ⚠️
```

**Features**:
- ✅ Performance zones (poor/fair/good/excellent)
- ✅ Target marker (│)
- ✅ Actual performance bar (█)
- ✅ Quantitative scale
- ✅ Status indicator

---

## Visualization Component Specification

### JSON Schema for Visualizations

All visualizations are generated as JSON and rendered by component library:

```json
{
  "visualization_id": "viz-001",
  "type": "bar_chart_horizontal",
  "title": "Top 5 Campaigns by ROAS",
  "created_at": "2024-01-24T14:15:00Z",

  "data": {
    "categories": ["Retargeting", "Brand Search", "Pricing Intent", "Demo Intent", "Competitor Comp"],
    "values": [8.6, 8.3, 5.3, 5.2, 3.8],
    "metadata": [
      {"spend": 285},
      {"spend": 425},
      {"spend": 340},
      {"spend": 290},
      {"spend": 360}
    ]
  },

  "config": {
    "max_value": 10,
    "bar_character": "█",
    "empty_character": " ",
    "show_values": true,
    "show_scale": true,
    "color_scheme": "gradient",
    "width": 50
  },

  "render": {
    "ascii": "...",  # Rendered ASCII version
    "html": "...",   # HTML version for web
    "markdown": "..." # Markdown version
  }
}
```

### Component Library Structure

```python
# Python implementation

class VisualizationLibrary:
    """Text-based visualization library for marketing agent"""

    @staticmethod
    def render_table(data: list[dict], columns: list[str], **kwargs) -> str:
        """Render data table with box drawing characters"""
        pass

    @staticmethod
    def render_bar_chart_horizontal(categories: list, values: list, **kwargs) -> str:
        """Render horizontal bar chart"""
        pass

    @staticmethod
    def render_line_chart(dates: list, values: list, **kwargs) -> str:
        """Render line chart with axis"""
        pass

    @staticmethod
    def render_progress_bar(current: float, target: float, **kwargs) -> str:
        """Render progress bar"""
        pass

    @staticmethod
    def render_gauge(value: float, max_value: float, zones: dict, **kwargs) -> str:
        """Render gauge/meter"""
        pass

    @staticmethod
    def render_sparkline(values: list[float], **kwargs) -> str:
        """Render mini inline sparkline"""
        pass

    @staticmethod
    def render_kpi_card(title: str, value: Any, trend: float, **kwargs) -> str:
        """Render KPI card"""
        pass

# Usage
viz = VisualizationLibrary()

table = viz.render_table(
    data=campaign_data,
    columns=['Campaign', 'Spend', 'Conversions', 'ROAS'],
    highlight_top=1,
    add_summary=True
)

print(table)
```

---

## Summary

### Environment vs Session

| Aspect | Environment | Session |
|--------|-------------|---------|
| **Lifecycle** | Long-lived (months/years) | Short-lived (minutes/hours) |
| **Scope** | Company-wide | Conversation-specific |
| **Storage** | `/environments/{env-id}/` | `/environments/{env-id}/sessions/{session-id}/` |
| **Context** | Shared (all sessions) | Private (single session) |
| **Updates** | Incremental (knowledge accumulation) | Transient (state updates) |
| **Persistence** | Permanent | Ephemeral or archived |

### Visualization Types (17 total)

1. **Data Table** - Campaign performance, rankings
2. **Horizontal Bar Chart** - Comparisons, ROAS
3. **Vertical Bar Chart** - Time series, trends
4. **Line Chart** - Traffic, rankings over time
5. **Pie Chart** - Budget, traffic sources
6. **Progress Bar** - Goals, completion
7. **Gauge/Meter** - Scores, ratings
8. **Heatmap** - Distribution, performance matrix
9. **Network Graph** - Competitive landscape
10. **Sparkline** - Inline mini trends
11. **Funnel Chart** - Conversion funnels
12. **Comparison Matrix** - Feature comparison
13. **Timeline** - Project history, milestones
14. **KPI Card** - Dashboard metrics
15. **Scatter Plot** - Positioning, opportunity map
16. **Tree Map** - Hierarchical breakdown
17. **Bullet Graph** - Performance vs target

All use **ASCII/Unicode characters** for terminal and web rendering.

---

**Next Steps**:
1. Implement Environment and Session classes
2. Build visualization component library (Python)
3. Update agent prompts to use environment context
4. Create visualization rendering in agent responses
