# Visualization Implementation Plan

**Created**: November 24, 2025
**Purpose**: Two-track plan for making agent progress visible in both CLI (ASCII) and Web App (React chat interface)

---

## Overview

We have a fully functional agent system where agents use TodoWrite and execute complex workflows, but users can't see any progress. We need to make the agent's work visible through inline chat visualizations.

**Two Implementation Tracks**:
1. **Track 1: ASCII/Terminal** - Quick win to test with current CLI agent
2. **Track 2: Web App Chat** - Production-ready chat interface with real-time updates

---

# Track 1: ASCII/Terminal Implementation

## Goal
Make the CLI agent show real-time progress using ASCII/Unicode visualizations in the terminal, using the existing Rich library.

## Timeline
**Estimated**: 1-2 days

---

## Phase 1A: Intercept TodoWrite Output

### Current State
```python
# Agent calls TodoWrite
TodoWrite([
  {"content": "Load context", "status": "completed"},
  {"content": "Generate prompts", "status": "in_progress"}
])

# Tool returns success
# User sees: NOTHING
```

### Implementation

**File**: `cli_tools.py`

**Add new message parser**:
```python
def parse_and_print_message(message: Message, console: Console):
    # ... existing code ...

    elif isinstance(message, UserMessage):
        for block in message.content:
            if isinstance(block, ToolResultBlock):
                # Check if this is a TodoWrite result
                if block.tool_use_id and is_todo_write_result(block):
                    render_todo_visualization(block.content, console)
                else:
                    formatted_content = format_tool_result(block.content)
                    print_rich_message("tool_result", formatted_content, console)

def is_todo_write_result(block: ToolResultBlock) -> bool:
    """Check if tool result is from TodoWrite"""
    # TodoWrite returns structure like: [{"type": "text", "text": "..."}]
    # We need to detect this pattern
    try:
        if isinstance(block.content, list):
            for item in block.content:
                if isinstance(item, dict) and "todos" in str(item):
                    return True
    except:
        pass
    return False

def render_todo_visualization(content, console: Console):
    """Render TodoWrite data as progress visualization"""
    # Extract todos from content
    todos = extract_todos(content)

    if not todos:
        return

    # Calculate progress
    total = len(todos)
    completed = sum(1 for t in todos if t.get("status") == "completed")
    in_progress_count = sum(1 for t in todos if t.get("status") == "in_progress")

    # Build visualization
    lines = []
    lines.append(render_progress_bar(completed, total, width=20))
    lines.append("")

    for todo in todos:
        status = todo.get("status", "pending")
        content = todo.get("content", "")
        active_form = todo.get("activeForm", content)

        # Choose display text based on status
        display_text = active_form if status == "in_progress" else content

        icon = get_status_icon(status)
        lines.append(f"{icon} {display_text}")

    visualization = "\n".join(lines)

    # Print in a special panel
    panel = Panel(
        visualization,
        title="📋 Task Progress",
        border_style="cyan",
        title_align="left"
    )
    console.print(panel, end="\n\n")
```

**Add helper functions**:
```python
def render_progress_bar(current: int, total: int, width: int = 20) -> str:
    """Render ASCII progress bar"""
    if total == 0:
        return "[" + "░" * width + "] 0%"

    filled = int((current / total) * width)
    bar = "█" * filled + "░" * (width - filled)
    percent = int((current / total) * 100)

    return f"[{bar}] {percent}% ({current}/{total})"

def get_status_icon(status: str) -> str:
    """Get icon for todo status"""
    icons = {
        "completed": "✓",
        "in_progress": "⟳",
        "pending": "○",
        "failed": "✗"
    }
    return icons.get(status, "○")

def extract_todos(content) -> list:
    """Extract todos array from ToolResultBlock content"""
    # TodoWrite returns: [{"type": "text", "text": "Success"}]
    # But we need to hook earlier to get the actual todos
    # This is a limitation - we may need to modify the SDK

    # For now, we can parse from tool_use input instead of result
    # (see next section)
    pass
```

### Problem: Tool Results Don't Contain Todo Data

**Issue**: TodoWrite returns generic success message, not the actual todos.

**Solution**: Intercept the **tool_use** (input) instead of tool_result (output)

**Modified approach**:
```python
# In parse_and_print_message
elif isinstance(message, AssistantMessage):
    for block in message.content:
        if isinstance(block, TextBlock):
            print_rich_message("assistant", block.text, console)
        elif isinstance(block, ToolUseBlock):
            # Check if this is TodoWrite
            if block.name == "TodoWrite":
                render_todo_visualization_from_input(block.input, console)
            else:
                print_rich_message("tool_use", f"Tool: <{block.name}> \n\n {block.input}", console)

def render_todo_visualization_from_input(tool_input: dict, console: Console):
    """Render TodoWrite visualization from tool input"""
    todos = tool_input.get("todos", [])

    if not todos:
        return

    # Calculate progress
    total = len(todos)
    completed = sum(1 for t in todos if t.get("status") == "completed")

    # Build visualization (same as above)
    lines = []
    lines.append(render_progress_bar(completed, total, width=20))
    lines.append("")

    for todo in todos:
        status = todo.get("status", "pending")
        content = todo.get("content", "")
        active_form = todo.get("activeForm", content)

        display_text = active_form if status == "in_progress" else content
        icon = get_status_icon(status)
        lines.append(f"{icon} {display_text}")

    visualization = "\n".join(lines)

    panel = Panel(
        visualization,
        title="📋 Task Progress",
        border_style="cyan",
        title_align="left"
    )
    console.print(panel, end="\n\n")
```

---

## Phase 1B: Add Table Rendering

### Use Case
When agents analyze data and want to show results in table format.

### Implementation

**Add to cli_tools.py**:
```python
from rich.table import Table

def render_table_from_data(data: dict, console: Console):
    """
    Render data table in chat.

    Expected format:
    {
        "type": "table",
        "title": "Results by Engine",
        "headers": ["Engine", "Mentions", "Visibility Rate"],
        "rows": [
            ["Perplexity", "28", "28.0%"],
            ["ChatGPT", "12", "12.0%"],
            ["Gemini", "8", "8.0%"]
        ]
    }
    """
    table = Table(
        title=data.get("title", ""),
        show_header=True,
        header_style="bold cyan"
    )

    # Add columns
    for header in data.get("headers", []):
        table.add_column(header)

    # Add rows
    for row in data.get("rows", []):
        table.add_row(*[str(cell) for cell in row])

    console.print(table, end="\n\n")
```

**Agent usage**:
```python
# Agent could emit a special message with table data
# For now, agents would need to format tables manually in text
# Future: Add a "RenderTable" tool
```

---

## Phase 1C: Add Metric Cards

### Use Case
Show key metrics prominently (like "Brand Visibility: 16.8%")

### Implementation

```python
def render_metric_card(data: dict, console: Console):
    """
    Render metric card.

    Expected format:
    {
        "type": "metric_card",
        "label": "Brand Visibility",
        "value": "16.8%",
        "trend": "up",  # optional: "up", "down", "neutral"
        "context": "Across 3 AI engines"  # optional
    }
    """
    label = data.get("label", "")
    value = data.get("value", "")
    trend = data.get("trend")
    context = data.get("context", "")

    # Trend icon
    trend_icon = ""
    if trend == "up":
        trend_icon = "📈"
    elif trend == "down":
        trend_icon = "📉"

    # Build card
    lines = [
        f"[bold cyan]{label}[/bold cyan]",
        f"[bold green]{value}[/bold green] {trend_icon}",
    ]

    if context:
        lines.append(f"[dim]{context}[/dim]")

    panel = Panel(
        "\n".join(lines),
        border_style="green",
        padding=(0, 2)
    )

    console.print(panel, end="\n\n")
```

---

## Phase 1D: Enhanced Tool Call Display

### Goal
Make tool calls more readable and less verbose.

### Current
```
┌─────────────────────────────────────┐
│ Tool Use                            │
│ Tool: <WebSearch>                   │
│ {                                   │
│   "query": "best AI customer        │
│   support tools SaaS 2024"          │
│ }                                   │
└─────────────────────────────────────┘
```

### Improved
```
┌─────────────────────────────────────┐
│ 🔍 Web Search                       │
│ "best AI customer support tools     │
│  SaaS 2024"                         │
└─────────────────────────────────────┘
```

### Implementation

```python
def render_tool_use_compact(block: ToolUseBlock, console: Console):
    """Render tool use in compact format"""
    tool_name = block.name
    tool_input = block.input

    # Tool-specific formatting
    if tool_name == "WebSearch":
        query = tool_input.get("query", "")
        message = f'🔍 [bold blue]Web Search[/bold blue]\n"{query}"'

    elif tool_name == "WebFetch":
        url = tool_input.get("url", "")
        message = f'📄 [bold blue]Fetching[/bold blue]\n{url}'

    elif tool_name == "Read":
        file_path = tool_input.get("file_path", "")
        message = f'📖 [bold blue]Reading[/bold blue]\n{file_path}'

    elif tool_name == "Write":
        file_path = tool_input.get("file_path", "")
        message = f'💾 [bold blue]Writing[/bold blue]\n{file_path}'

    elif tool_name == "Bash":
        command = tool_input.get("command", "")[:100]  # Truncate long commands
        message = f'⚡ [bold blue]Running[/bold blue]\n{command}...'

    elif tool_name == "Task":
        subagent = tool_input.get("subagent_type", "")
        description = tool_input.get("description", "")
        message = f'🤝 [bold blue]Delegating to {subagent}[/bold blue]\n{description}'

    else:
        # Default format
        message = f'🔧 [bold blue]{tool_name}[/bold blue]\n{json.dumps(tool_input, indent=2)}'

    panel = Panel(
        message,
        border_style="blue",
        padding=(0, 1)
    )
    console.print(panel, end="\n\n")
```

---

## Phase 1E: Sub-Agent Progress Tracking

### Goal
When Kaya delegates to a sub-agent, show nested progress.

### Visualization
```
┌─────────────────────────────────────┐
│ Kaya                                │
│ I'll delegate this to my SEO        │
│ specialist.                         │
└─────────────────────────────────────┘

┌─────────────────────────────────────┐
│ 🤝 Delegating to seo-analyst        │
│ Task: SEO audit for acmecorp.com    │
└─────────────────────────────────────┘

  ┌───────────────────────────────────┐
  │ 📋 SEO Analyst Progress           │
  │ [████████░░] 80% (8/10)           │
  │ ✓ Homepage analysis               │
  │ ✓ Core pages check                │
  │ ⟳ Page speed analysis...          │
  └───────────────────────────────────┘
  ↑ Indented to show it's sub-agent
```

### Implementation

**Challenge**: Sub-agent runs in separate process, so we can't directly intercept its TodoWrite calls in the CLI.

**Solutions**:

1. **Option A**: Parse sub-agent output and detect TodoWrite patterns
2. **Option B**: Sub-agent returns progress in final response
3. **Option C**: Use SDK streaming (if available) to get intermediate messages

For now, we can at least show **when delegation happens** clearly.

---

## Testing Track 1

### Test Cases

1. **Test TodoWrite Rendering**
```bash
# Run agent with a task that uses TodoWrite
python marketing_agent.py

User: "Run a quick GEO analysis for Acme Corp"

# Expected: See progress bars update as agent works
```

2. **Test Tool Call Formatting**
```bash
# Expected: Compact, readable tool calls instead of verbose JSON
```

3. **Test Table Display** (future)
```bash
# When agent generates analysis results
# Expected: Nice formatted tables
```

### Success Criteria

- ✅ TodoWrite calls show as progress bars in chat
- ✅ Tool calls are compact and readable
- ✅ User can follow agent's progress in real-time
- ✅ No more 15-minute black box waits

---

# Track 2: Web App Chat Implementation

## Goal
Build a production chat interface where agents' work is visible through real-time chat messages with rich visualizations.

## Timeline
**Estimated**: 2-3 weeks

---

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                     Web Frontend                        │
│  ┌──────────────────────────────────────────────────┐  │
│  │  Chat Interface (React)                          │  │
│  │  - Message stream                                │  │
│  │  - Progress visualizations                       │  │
│  │  - Sub-agent hierarchical view                   │  │
│  └──────────────────────────────────────────────────┘  │
│                        ↕ WebSocket                      │
├─────────────────────────────────────────────────────────┤
│                  Backend Server (FastAPI)               │
│  ┌──────────────────────────────────────────────────┐  │
│  │  Event Stream Manager                            │  │
│  │  - Intercept agent messages                      │  │
│  │  - Broadcast to WebSocket                        │  │
│  │  - Handle TodoWrite events                       │  │
│  └──────────────────────────────────────────────────┘  │
│                        ↕                                │
│  ┌──────────────────────────────────────────────────┐  │
│  │  Claude Agent SDK                                │  │
│  │  - Kaya (master agent)                           │  │
│  │  - 7 sub-agents                                  │  │
│  │  - Tools (Read, Write, TodoWrite, etc.)          │  │
│  └──────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────┘
```

---

## Phase 2A: Message Type System

### Define Message Types

**File**: `backend/types/messages.py`

```python
from typing import Literal, Optional, List, Dict, Any
from pydantic import BaseModel
from datetime import datetime

class ChatMessage(BaseModel):
    """Base chat message"""
    id: str
    timestamp: datetime
    type: Literal["user", "assistant", "system", "progress", "tool_call", "visualization"]

class UserMessage(ChatMessage):
    """Message from user"""
    type: Literal["user"] = "user"
    content: str

class AssistantMessage(ChatMessage):
    """Message from assistant (text response)"""
    type: Literal["assistant"] = "assistant"
    content: str
    agent: str  # "kaya" or sub-agent name

class ProgressMessage(ChatMessage):
    """Progress update (TodoWrite visualization)"""
    type: Literal["progress"] = "progress"
    agent: str
    todos: List[Dict[str, Any]]
    progress_percent: int

class ToolCallMessage(ChatMessage):
    """Tool call notification"""
    type: Literal["tool_call"] = "tool_call"
    agent: str
    tool_name: str
    tool_input: Dict[str, Any]
    compact_display: str  # Pre-formatted for display

class VisualizationMessage(ChatMessage):
    """Rich visualization (table, chart, metric card)"""
    type: Literal["visualization"] = "visualization"
    viz_type: Literal["table", "metric_card", "chart", "list"]
    data: Dict[str, Any]

class SystemMessage(ChatMessage):
    """System notification"""
    type: Literal["system"] = "system"
    content: str
    severity: Literal["info", "warning", "error"] = "info"
```

---

## Phase 2B: Event Stream Manager

### Backend Service

**File**: `backend/services/agent_event_stream.py`

```python
from claude_agent_sdk import ClaudeSDKClient, Message, AssistantMessage, ToolUseBlock
from typing import AsyncIterator, Callable
import asyncio

class AgentEventStream:
    """
    Wraps Claude Agent SDK to intercept and broadcast events.
    """

    def __init__(self):
        self.subscribers: List[Callable] = []

    def subscribe(self, callback: Callable):
        """Subscribe to agent events"""
        self.subscribers.append(callback)

    def unsubscribe(self, callback: Callable):
        """Unsubscribe from events"""
        self.subscribers.remove(callback)

    async def broadcast(self, message: ChatMessage):
        """Broadcast message to all subscribers"""
        for callback in self.subscribers:
            await callback(message)

    async def run_agent_with_streaming(
        self,
        client: ClaudeSDKClient,
        user_prompt: str,
        session_id: str
    ) -> AsyncIterator[ChatMessage]:
        """
        Run agent and yield chat messages in real-time.
        """

        # Send user message
        user_msg = UserMessage(
            id=f"user_{session_id}_{timestamp()}",
            timestamp=datetime.now(),
            content=user_prompt
        )
        yield user_msg

        # Query agent
        await client.query(user_prompt)

        # Stream responses
        async for message in client.receive_response():
            # Convert SDK message to chat message(s)
            chat_messages = self.convert_sdk_message(message, session_id)

            for chat_msg in chat_messages:
                yield chat_msg

    def convert_sdk_message(
        self,
        sdk_message: Message,
        session_id: str
    ) -> List[ChatMessage]:
        """
        Convert SDK message to chat message(s).
        """
        messages = []

        if isinstance(sdk_message, AssistantMessage):
            for block in sdk_message.content:
                if isinstance(block, TextBlock):
                    # Regular text response
                    messages.append(AssistantMessage(
                        id=f"asst_{session_id}_{timestamp()}",
                        timestamp=datetime.now(),
                        content=block.text,
                        agent="kaya"  # Detect actual agent from context
                    ))

                elif isinstance(block, ToolUseBlock):
                    # Check if TodoWrite
                    if block.name == "TodoWrite":
                        messages.append(self.create_progress_message(
                            block.input,
                            session_id
                        ))
                    else:
                        messages.append(self.create_tool_call_message(
                            block,
                            session_id
                        ))

        return messages

    def create_progress_message(
        self,
        tool_input: dict,
        session_id: str
    ) -> ProgressMessage:
        """Create progress message from TodoWrite input"""
        todos = tool_input.get("todos", [])
        total = len(todos)
        completed = sum(1 for t in todos if t.get("status") == "completed")
        progress_percent = int((completed / total * 100)) if total > 0 else 0

        return ProgressMessage(
            id=f"progress_{session_id}_{timestamp()}",
            timestamp=datetime.now(),
            agent="kaya",  # Detect actual agent
            todos=todos,
            progress_percent=progress_percent
        )

    def create_tool_call_message(
        self,
        tool_block: ToolUseBlock,
        session_id: str
    ) -> ToolCallMessage:
        """Create tool call message"""

        # Generate compact display
        compact = self.format_tool_compact(
            tool_block.name,
            tool_block.input
        )

        return ToolCallMessage(
            id=f"tool_{session_id}_{timestamp()}",
            timestamp=datetime.now(),
            agent="kaya",
            tool_name=tool_block.name,
            tool_input=tool_block.input,
            compact_display=compact
        )

    def format_tool_compact(self, tool_name: str, tool_input: dict) -> str:
        """Format tool call compactly"""
        if tool_name == "WebSearch":
            return f'🔍 Searching: "{tool_input.get("query", "")}"'
        elif tool_name == "Task":
            subagent = tool_input.get("subagent_type", "")
            desc = tool_input.get("description", "")
            return f'🤝 Delegating to {subagent}: {desc}'
        elif tool_name == "Read":
            return f'📖 Reading: {tool_input.get("file_path", "")}'
        elif tool_name == "Write":
            return f'💾 Writing: {tool_input.get("file_path", "")}'
        else:
            return f'🔧 {tool_name}'
```

---

## Phase 2C: WebSocket Server

### FastAPI WebSocket Endpoint

**File**: `backend/api/websocket.py`

```python
from fastapi import WebSocket, WebSocketDisconnect
from typing import Dict
import json

class ConnectionManager:
    """Manage WebSocket connections"""

    def __init__(self):
        self.active_connections: Dict[str, WebSocket] = {}

    async def connect(self, session_id: str, websocket: WebSocket):
        await websocket.accept()
        self.active_connections[session_id] = websocket

    def disconnect(self, session_id: str):
        if session_id in self.active_connections:
            del self.active_connections[session_id]

    async def send_message(self, session_id: str, message: ChatMessage):
        if session_id in self.active_connections:
            websocket = self.active_connections[session_id]
            await websocket.send_text(message.model_dump_json())

manager = ConnectionManager()

@app.websocket("/ws/{session_id}")
async def websocket_endpoint(websocket: WebSocket, session_id: str):
    await manager.connect(session_id, websocket)

    try:
        while True:
            # Receive user messages
            data = await websocket.receive_text()
            user_input = json.loads(data)

            # Run agent with streaming
            event_stream = AgentEventStream()

            async for message in event_stream.run_agent_with_streaming(
                client=agent_client,
                user_prompt=user_input["content"],
                session_id=session_id
            ):
                # Send message to client
                await manager.send_message(session_id, message)

    except WebSocketDisconnect:
        manager.disconnect(session_id)
```

---

## Phase 2D: React Chat Interface

### Chat Component

**File**: `frontend/src/components/Chat.tsx`

```typescript
import React, { useState, useEffect, useRef } from 'react';
import { ChatMessage, ProgressMessage, ToolCallMessage } from '../types/messages';
import MessageRenderer from './MessageRenderer';
import ProgressCard from './visualizations/ProgressCard';
import ToolCallCard from './visualizations/ToolCallCard';

export default function Chat({ sessionId }: { sessionId: string }) {
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [input, setInput] = useState('');
  const ws = useRef<WebSocket | null>(null);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    // Connect to WebSocket
    ws.current = new WebSocket(`ws://localhost:8000/ws/${sessionId}`);

    ws.current.onmessage = (event) => {
      const message: ChatMessage = JSON.parse(event.data);

      // Update or append message
      setMessages(prev => {
        // If this is a progress update, replace previous progress message
        if (message.type === 'progress') {
          const lastProgressIdx = prev.findLastIndex(m => m.type === 'progress');
          if (lastProgressIdx !== -1) {
            const updated = [...prev];
            updated[lastProgressIdx] = message;
            return updated;
          }
        }

        return [...prev, message];
      });
    };

    return () => {
      ws.current?.close();
    };
  }, [sessionId]);

  useEffect(() => {
    // Auto-scroll to bottom
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  const sendMessage = () => {
    if (!input.trim()) return;

    ws.current?.send(JSON.stringify({
      content: input
    }));

    setInput('');
  };

  return (
    <div className="flex flex-col h-screen bg-gray-50">
      {/* Messages */}
      <div className="flex-1 overflow-y-auto p-4 space-y-4">
        {messages.map((message) => (
          <MessageRenderer key={message.id} message={message} />
        ))}
        <div ref={messagesEndRef} />
      </div>

      {/* Input */}
      <div className="border-t bg-white p-4">
        <div className="flex gap-2">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyPress={(e) => e.key === 'Enter' && sendMessage()}
            placeholder="Ask Kaya anything..."
            className="flex-1 border rounded-lg px-4 py-2"
          />
          <button
            onClick={sendMessage}
            className="bg-blue-600 text-white px-6 py-2 rounded-lg hover:bg-blue-700"
          >
            Send
          </button>
        </div>
      </div>
    </div>
  );
}
```

### Message Renderer

**File**: `frontend/src/components/MessageRenderer.tsx`

```typescript
import React from 'react';
import { ChatMessage } from '../types/messages';
import ProgressCard from './visualizations/ProgressCard';
import ToolCallCard from './visualizations/ToolCallCard';
import TableCard from './visualizations/TableCard';
import MetricCard from './visualizations/MetricCard';

export default function MessageRenderer({ message }: { message: ChatMessage }) {
  switch (message.type) {
    case 'user':
      return (
        <div className="flex justify-end">
          <div className="bg-blue-600 text-white rounded-lg px-4 py-2 max-w-2xl">
            {message.content}
          </div>
        </div>
      );

    case 'assistant':
      return (
        <div className="flex justify-start">
          <div className="bg-white border rounded-lg px-4 py-2 max-w-2xl shadow-sm">
            <div className="text-xs text-gray-500 mb-1">{message.agent}</div>
            <div className="prose prose-sm">{message.content}</div>
          </div>
        </div>
      );

    case 'progress':
      return <ProgressCard message={message} />;

    case 'tool_call':
      return <ToolCallCard message={message} />;

    case 'visualization':
      if (message.viz_type === 'table') {
        return <TableCard data={message.data} />;
      } else if (message.viz_type === 'metric_card') {
        return <MetricCard data={message.data} />;
      }
      return null;

    case 'system':
      return (
        <div className="flex justify-center">
          <div className="bg-gray-100 text-gray-600 rounded-lg px-3 py-1 text-sm">
            {message.content}
          </div>
        </div>
      );

    default:
      return null;
  }
}
```

### Progress Card Component

**File**: `frontend/src/components/visualizations/ProgressCard.tsx`

```typescript
import React from 'react';
import { ProgressMessage } from '../../types/messages';

export default function ProgressCard({ message }: { message: ProgressMessage }) {
  const { todos, progress_percent, agent } = message;

  return (
    <div className="flex justify-start">
      <div className="bg-cyan-50 border border-cyan-200 rounded-lg px-4 py-3 max-w-2xl">
        <div className="flex items-center gap-2 mb-2">
          <span className="text-lg">📋</span>
          <span className="font-medium text-cyan-900">
            {agent} Progress
          </span>
        </div>

        {/* Progress Bar */}
        <div className="mb-3">
          <div className="flex items-center gap-2 mb-1">
            <div className="flex-1 bg-gray-200 rounded-full h-2">
              <div
                className="bg-cyan-600 h-2 rounded-full transition-all duration-300"
                style={{ width: `${progress_percent}%` }}
              />
            </div>
            <span className="text-sm font-medium text-cyan-900">
              {progress_percent}%
            </span>
          </div>
        </div>

        {/* Todo List */}
        <div className="space-y-1">
          {todos.map((todo, idx) => (
            <div key={idx} className="flex items-start gap-2 text-sm">
              <span className="text-base">
                {todo.status === 'completed' ? '✓' :
                 todo.status === 'in_progress' ? '⟳' : '○'}
              </span>
              <span className={
                todo.status === 'completed' ? 'text-gray-500' :
                todo.status === 'in_progress' ? 'text-cyan-900 font-medium' :
                'text-gray-600'
              }>
                {todo.status === 'in_progress' ? todo.activeForm : todo.content}
              </span>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
```

### Tool Call Card Component

**File**: `frontend/src/components/visualizations/ToolCallCard.tsx`

```typescript
import React, { useState } from 'react';
import { ToolCallMessage } from '../../types/messages';

export default function ToolCallCard({ message }: { message: ToolCallMessage }) {
  const [expanded, setExpanded] = useState(false);

  return (
    <div className="flex justify-start">
      <div className="bg-blue-50 border border-blue-200 rounded-lg px-4 py-2 max-w-2xl">
        <div
          className="flex items-center gap-2 cursor-pointer"
          onClick={() => setExpanded(!expanded)}
        >
          <span className="text-sm text-blue-900">
            {message.compact_display}
          </span>
          {expanded && (
            <span className="text-xs text-blue-600 ml-auto">▼</span>
          )}
        </div>

        {expanded && (
          <pre className="mt-2 text-xs bg-blue-100 p-2 rounded overflow-x-auto">
            {JSON.stringify(message.tool_input, null, 2)}
          </pre>
        )}
      </div>
    </div>
  );
}
```

### Table Card Component

**File**: `frontend/src/components/visualizations/TableCard.tsx`

```typescript
import React from 'react';

interface TableData {
  title?: string;
  headers: string[];
  rows: (string | number)[][];
}

export default function TableCard({ data }: { data: TableData }) {
  return (
    <div className="flex justify-start">
      <div className="bg-white border rounded-lg px-4 py-3 max-w-4xl shadow-sm overflow-x-auto">
        {data.title && (
          <h3 className="font-medium text-gray-900 mb-2">{data.title}</h3>
        )}

        <table className="min-w-full divide-y divide-gray-200">
          <thead className="bg-gray-50">
            <tr>
              {data.headers.map((header, idx) => (
                <th
                  key={idx}
                  className="px-4 py-2 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
                >
                  {header}
                </th>
              ))}
            </tr>
          </thead>
          <tbody className="bg-white divide-y divide-gray-200">
            {data.rows.map((row, rowIdx) => (
              <tr key={rowIdx}>
                {row.map((cell, cellIdx) => (
                  <td
                    key={cellIdx}
                    className="px-4 py-2 text-sm text-gray-900"
                  >
                    {cell}
                  </td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
```

---

## Phase 2E: Agent Modifications to Emit Visualizations

### Add Visualization Helper

**File**: `backend/utils/agent_viz_helpers.py`

```python
def emit_table(title: str, headers: list, rows: list) -> str:
    """
    Helper for agents to emit table data.
    Returns a special formatted string that backend will parse.
    """
    table_data = {
        "type": "visualization",
        "viz_type": "table",
        "data": {
            "title": title,
            "headers": headers,
            "rows": rows
        }
    }

    # Return as special marker that backend will detect
    return f"[VISUALIZATION]{json.dumps(table_data)}[/VISUALIZATION]"

def emit_metric_card(label: str, value: str, trend: str = None, context: str = None) -> str:
    """Helper for agents to emit metric cards"""
    metric_data = {
        "type": "visualization",
        "viz_type": "metric_card",
        "data": {
            "label": label,
            "value": value,
            "trend": trend,
            "context": context
        }
    }

    return f"[VISUALIZATION]{json.dumps(metric_data)}[/VISUALIZATION]"
```

### Modify Agent Prompts to Use Helpers

Agents can now include visualizations in their text responses:

```python
# Example in seo-analyst agent response
response = f"""
SEO Audit Complete!

{emit_metric_card("Overall Health Score", "68/100", trend="down", context="Needs improvement")}

{emit_table(
    title="Issues by Priority",
    headers=["Priority", "Count", "Est. Fix Time"],
    rows=[
        ["Critical", "3", "2 hours"],
        ["High", "12", "1 day"],
        ["Medium", "18", "3 days"]
    ]
)}

Top Issue: robots.txt blocking blog content
"""
```

Backend parses `[VISUALIZATION]...[/VISUALIZATION]` markers and converts to VisualizationMessage.

---

## Testing Track 2

### Test Cases

1. **Chat Flow Test**
```typescript
// Send message
ws.send({ content: "Run GEO analysis" })

// Expect sequence:
// 1. UserMessage
// 2. AssistantMessage ("I'll run GEO analysis...")
// 3. ToolCallMessage (Delegation)
// 4. ProgressMessage (0%)
// 5. ProgressMessage (20%) - updates previous
// 6. ProgressMessage (40%)
// ... progress updates
// 10. AssistantMessage (Final result with tables)
```

2. **Progress Update Test**
```typescript
// Verify progress messages replace previous ones
// Not append new ones each time
```

3. **Visualization Rendering Test**
```typescript
// Verify tables render correctly
// Verify metric cards display properly
// Verify tool calls are compact
```

### Success Criteria

- ✅ Chat messages appear in real-time
- ✅ Progress bars update smoothly (replace, not append)
- ✅ Sub-agent work is visible
- ✅ Tables and metrics render inline in chat
- ✅ Tool calls are compact and expandable
- ✅ No lag or stuttering in UI
- ✅ Works with multiple concurrent sessions

---

# Deployment Checklist

## Prerequisites

### 1. MCP Tools (Critical for Performance)

**Status**: TypeScript implementation exists, not connected

**Action Items**:
```bash
# Build MCP server
cd mcp-servers/marketing-tools
npm install
npm run build

# Test MCP server standalone
node dist/index.js

# Configure in marketing_agent.py
mcp_servers = {
    "MarketingTools": {
        "command": "node",
        "args": ["mcp-servers/marketing-tools/dist/index.js"]
    }
}
```

**Impact**: 26x performance improvement (90 seconds vs 40 minutes for deep GEO analysis)

**Priority**: P0 - Must have before launch

---

### 2. Python Visualization Library (For Track 1)

**Status**: Not implemented

**Action Items**:
```bash
# Create visualization module
mkdir -p backend/viz
touch backend/viz/__init__.py
touch backend/viz/renderers.py

# Implement core renderers:
# - render_progress_bar()
# - render_table()
# - render_status_icon()
# - format_tool_compact()
```

**Testing**:
```python
# Unit tests
pytest backend/viz/test_renderers.py
```

**Priority**: P0 - Needed for Track 1 (CLI)

---

### 3. Backend API (For Track 2)

**Status**: Not implemented

**Tech Stack**:
- FastAPI (Python web framework)
- WebSocket support
- Claude Agent SDK integration

**Action Items**:
```bash
# Setup project
mkdir -p backend/{api,services,types,utils}

# Install dependencies
pip install fastapi uvicorn websockets pydantic

# Implement:
# - backend/api/websocket.py (WebSocket endpoint)
# - backend/services/agent_event_stream.py (Event streaming)
# - backend/types/messages.py (Message types)
```

**Testing**:
```bash
# Run server
uvicorn backend.main:app --reload

# Test WebSocket connection
wscat -c ws://localhost:8000/ws/test-session
```

**Priority**: P0 - Core of Track 2

---

### 4. Frontend (For Track 2)

**Status**: Not implemented

**Tech Stack**:
- React + TypeScript
- Tailwind CSS
- WebSocket client

**Action Items**:
```bash
# Setup project
npx create-react-app frontend --template typescript
cd frontend

# Install dependencies
npm install tailwindcss autoprefixer postcss

# Implement components:
# - src/components/Chat.tsx
# - src/components/MessageRenderer.tsx
# - src/components/visualizations/ProgressCard.tsx
# - src/components/visualizations/ToolCallCard.tsx
# - src/components/visualizations/TableCard.tsx
# - src/components/visualizations/MetricCard.tsx
```

**Testing**:
```bash
npm start
# Test at http://localhost:3000
```

**Priority**: P0 - User-facing interface

---

### 5. Database (For Session Persistence)

**Status**: Not needed immediately (file-based works)

**Future**: PostgreSQL for multi-user, session history, analytics

**Priority**: P2 - Nice to have

---

## Environment Setup

### Development Environment

```bash
# Clone repo
git clone <repo>
cd claude-agent-sdk-intro

# Python environment
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt

# Node environment (MCP tools)
cd mcp-servers/marketing-tools
npm install

# Frontend
cd frontend
npm install

# Environment variables
cp .env.example .env
# Set: ANTHROPIC_API_KEY, OPENAI_API_KEY, PERPLEXITY_API_KEY, etc.
```

### Production Environment

**Infrastructure Needs**:
- Web server (Nginx/Apache for frontend)
- Application server (Uvicorn/Gunicorn for FastAPI)
- Process manager (Supervisor/PM2)
- SSL certificate (Let's Encrypt)
- Domain name

**Deployment**:
```bash
# Build frontend
cd frontend
npm run build

# Serve static files with Nginx
# Backend runs on :8000
# Nginx proxies /ws to backend WebSocket
```

---

## Launch Phases

### Phase 0: MCP Tools (Week 1)

**Goal**: Connect existing TypeScript MCP tools

**Tasks**:
- Build marketing-tools MCP server
- Configure in marketing_agent.py
- Test GEO-001 and GEO-002
- Benchmark performance

**Success**: Deep GEO analysis runs in <2 minutes

---

### Phase 1: CLI Improvements (Week 1-2)

**Goal**: Make CLI agent progress visible

**Tasks**:
- Implement TodoWrite visualization in cli_tools.py
- Add compact tool call formatting
- Test with all 7 sub-agents

**Success**: Users see real-time progress in terminal

---

### Phase 2: Backend (Week 2-3)

**Goal**: Build WebSocket event streaming

**Tasks**:
- Implement FastAPI server
- Create AgentEventStream service
- Define message types
- Test WebSocket connection

**Success**: Backend streams agent events via WebSocket

---

### Phase 3: Frontend (Week 3-4)

**Goal**: Build React chat interface

**Tasks**:
- Create chat UI components
- Implement message renderers
- Build visualization components
- Connect to WebSocket

**Success**: Chat interface displays agent work in real-time

---

### Phase 4: Integration Testing (Week 4)

**Goal**: End-to-end testing

**Tasks**:
- Test all agent workflows in web UI
- Performance testing (concurrent users)
- Bug fixes
- Polish UI/UX

**Success**: All 7 sub-agents work smoothly in web UI

---

### Phase 5: Production Deployment (Week 5)

**Goal**: Deploy to production

**Tasks**:
- Setup production infrastructure
- Configure domain and SSL
- Deploy backend and frontend
- Monitoring and logging
- Documentation

**Success**: Live at production URL

---

## Success Metrics

### Performance Metrics

- [ ] Deep GEO analysis completes in <2 minutes (with MCP tools)
- [ ] Web UI responds to user input in <100ms
- [ ] Progress updates stream with <500ms latency
- [ ] Supports 10+ concurrent users without degradation

### User Experience Metrics

- [ ] No more 15-minute "black box" waits
- [ ] Users can see task progress at all times
- [ ] Tool calls are readable and non-intrusive
- [ ] Sub-agent work is visible but not overwhelming
- [ ] Visualizations render correctly (tables, progress, metrics)

### Functional Metrics

- [ ] All 7 sub-agents work in web UI
- [ ] TodoWrite visualization works for all agents
- [ ] File workspace persists correctly
- [ ] Analysis results save to correct locations
- [ ] Error handling doesn't crash the UI

---

## Open Questions

1. **Authentication**: Do we need user authentication? Multi-tenancy?
2. **Session Persistence**: Save chat history to database or just files?
3. **Analytics**: Track usage, performance, error rates?
4. **Scaling**: How many concurrent users do we expect?
5. **Mobile**: Does chat UI need to work on mobile?

---

## Current Gaps Summary

| Component | Track 1 (CLI) | Track 2 (Web) | Priority |
|-----------|---------------|---------------|----------|
| MCP Tools Connected | ✅ Need | ✅ Need | P0 |
| TodoWrite Visibility | ✅ Need | ✅ Need | P0 |
| Viz Renderers (Python) | ✅ Need | ⚠️ Optional | P0 |
| Backend API | ❌ Not needed | ✅ Need | P0 |
| WebSocket | ❌ Not needed | ✅ Need | P0 |
| Frontend | ❌ Not needed | ✅ Need | P0 |
| Message Types | ❌ Not needed | ✅ Need | P0 |
| Event Stream Service | ❌ Not needed | ✅ Need | P0 |
| Chat Components | ❌ Not needed | ✅ Need | P0 |
| Progress Cards | ❌ Not needed | ✅ Need | P0 |
| Tool Call Cards | ❌ Not needed | ✅ Need | P0 |
| Table Renderer | ✅ Need | ✅ Need | P1 |
| Metric Cards | ⚠️ Nice to have | ✅ Need | P1 |

---

## Estimated Timeline

### Track 1 Only (CLI)
- **Week 1**: MCP tools + TodoWrite viz = Working CLI with progress
- **Effort**: 1 developer, 1 week

### Track 2 (Web App)
- **Week 1-2**: Backend (FastAPI + WebSocket + Event streaming)
- **Week 3-4**: Frontend (React + Components + Integration)
- **Week 5**: Testing + Deployment
- **Effort**: 2 developers, 5 weeks

### Parallel Approach
- Dev 1: MCP tools + Backend
- Dev 2: CLI viz + Frontend
- **Total**: 4 weeks with 2 devs

---

## Next Immediate Steps

1. **Connect MCP Tools** (2-4 hours)
   ```bash
   cd mcp-servers/marketing-tools
   npm run build
   # Configure in marketing_agent.py
   # Test performance improvement
   ```

2. **Implement TodoWrite Viz in CLI** (4-6 hours)
   ```python
   # Modify cli_tools.py
   # Add render_todo_visualization_from_input()
   # Test with GEO analysis
   ```

3. **Decision Point**: Track 1 only or both?
   - If Track 1: Polish CLI, ship in 1 week
   - If Track 2: Start backend development, ship in 4-5 weeks

4. **Create Project Plan** (if Track 2)
   - Sprint planning
   - Task breakdown
   - Developer assignment
   - Milestone definitions
