# Web App Development Brief
## Building the Marketing Agent Chat Interface

**Date**: November 24, 2025
**From**: AI Engineering Team (Agent System)
**To**: Web Development Team
**Purpose**: Build production chat interface with real-time agent progress visualization

---

## Executive Summary

We've built a fully functional multi-agent marketing system with **7 specialized agents** that execute complex workflows flawlessly. However, users currently experience 5-20 minute "black boxes" with zero feedback.

**The CLI Sprint Success**: We implemented real-time visualization in the terminal that makes agent progress visible through:
- Progress bars showing task completion
- Compact tool call formatting
- Status icons for task states
- All visualizations inline in chat

**Your Mission**: Build a web chat interface that displays these same visualizations in a modern React UI with WebSocket streaming.

---

## What's Already Built (Agent System)

### Core Components ✅

**1. Master Agent (Kaya)**
- Personal assistant that orchestrates 7 sub-agents
- Delegates tasks using the `Task` tool
- File: `/marketing_agent.py`

**2. Seven Specialized Sub-Agents**
- `geo-optimizer`: Generative Engine Optimization
- `seo-analyst`: Search Engine Optimization
- `ads-analyst`: Advertising Analytics
- `presentation-designer`: Creates slide decks
- `dashboard-creator`: Builds dashboards
- `content-strategist`: Content planning
- `competitor-analyst`: Competitive intelligence

**3. TodoWrite Tool**
- Agents use this to track progress internally
- Contains: task list, status (pending/in_progress/completed), active form
- **This is what we visualize!**

**4. File Workspace**
- `/data/clients/{client-id}/` structure
- Persistent storage for analyses, context, history

**5. CLI Visualization (Just Completed)**
- Real-time progress bars
- Compact tool formatting
- Status icons (✓ ⟳ ○)
- File: `/cli_tools.py` (reference implementation)

---

## CLI Implementation (Your Reference)

### What We Built

```python
# cli_tools.py - KEY FUNCTIONS

def render_progress_bar(current: int, total: int, width: int = 20) -> str:
    """Generates: [████████░░] 80% (4/5)"""
    filled = int((current / total) * width)
    bar = "█" * filled + "░" * (width - filled)
    percent = int((current / total) * 100)
    return f"[{bar}] {percent}% ({current}/{total})"


def get_status_icon(status: str) -> str:
    """Returns: ✓ ⟳ ○ ✗ based on status"""
    icons = {
        "completed": "✓",
        "in_progress": "⟳",
        "pending": "○",
        "failed": "✗"
    }
    return icons.get(status, "○")


def render_todo_visualization(tool_input: dict, console: Console):
    """Main visualization function"""
    todos = tool_input.get("todos", [])
    total = len(todos)
    completed = sum(1 for t in todos if t.get("status") == "completed")

    lines = [render_progress_bar(completed, total, width=20), ""]

    for todo in todos:
        status = todo.get("status", "pending")
        content = todo.get("content", "")
        active_form = todo.get("activeForm", content)
        display_text = active_form if status == "in_progress" else content
        icon = get_status_icon(status)
        lines.append(f"{icon} {display_text}")

    # Renders in cyan panel titled "📋 Task Progress"
```

### Terminal Output Example

```
┌─────────────────────────────────┐
│ User Prompt                     │
│ Run a deep GEO analysis         │
└─────────────────────────────────┘

┌─────────────────────────────────┐
│ Assistant                       │
│ I'll run a comprehensive GEO    │
│ analysis. Let me delegate to my │
│ GEO specialist.                 │
└─────────────────────────────────┘

┌─────────────────────────────────┐
│ 🤝 Delegating to geo-optimizer: │
│ Deep GEO analysis               │
└─────────────────────────────────┘

┌─────────────────────────────────┐
│ 📋 Task Progress                │
│ [████████░░] 80% (4/5)          │
│                                 │
│ ✓ Load company context          │
│ ✓ Identify value propositions   │
│ ✓ Generate test prompts         │
│ ⟳ Running multi-engine tests... │
│ ○ Analyze citations             │
└─────────────────────────────────┘

┌─────────────────────────────────┐
│ 🔍 Web Search: "best AI         │
│ customer support tools 2024"    │
└─────────────────────────────────┘

... (progress continues) ...

┌─────────────────────────────────┐
│ Assistant                       │
│ Analysis complete! Brand        │
│ visibility: 16.8% across 3      │
│ AI engines.                     │
└─────────────────────────────────┘
```

---

## Your Task: Web Chat Interface

### Architecture Overview

```
┌─────────────────────────────────────────────┐
│          React Chat Frontend                │
│  ┌──────────────────────────────────────┐  │
│  │  ChatContainer                       │  │
│  │  - Message list                      │  │
│  │  - Auto-scroll                       │  │
│  │  - Input box                         │  │
│  └──────────────────────────────────────┘  │
│              ↕ WebSocket                    │
├─────────────────────────────────────────────┤
│          FastAPI Backend                    │
│  ┌──────────────────────────────────────┐  │
│  │  AgentEventStream Service            │  │
│  │  - Intercepts TodoWrite calls        │  │
│  │  - Intercepts tool calls             │  │
│  │  - Converts to ChatMessage types     │  │
│  │  - Broadcasts via WebSocket          │  │
│  └──────────────────────────────────────┘  │
│              ↕                              │
│  ┌──────────────────────────────────────┐  │
│  │  Claude Agent SDK                    │  │
│  │  - Kaya (master)                     │  │
│  │  - 7 sub-agents                      │  │
│  │  - TodoWrite, Read, Write, etc.      │  │
│  └──────────────────────────────────────┘  │
└─────────────────────────────────────────────┘
```

---

## Phase 1: Backend (FastAPI)

### 1.1 Message Type System

**File**: `backend/types/messages.py`

```python
from pydantic import BaseModel
from typing import Literal, List, Dict, Any
from datetime import datetime

class ChatMessage(BaseModel):
    """Base message type"""
    id: str
    timestamp: datetime
    type: Literal["user", "assistant", "progress", "tool_call", "system"]

class UserMessage(ChatMessage):
    type: Literal["user"] = "user"
    content: str

class AssistantMessage(ChatMessage):
    type: Literal["assistant"] = "assistant"
    content: str
    agent: str  # "kaya" or "geo-optimizer", etc.

class ProgressMessage(ChatMessage):
    """TodoWrite visualization data"""
    type: Literal["progress"] = "progress"
    agent: str
    todos: List[Dict[str, Any]]  # Same structure as TodoWrite input
    progress_percent: int  # Pre-calculated

class ToolCallMessage(ChatMessage):
    """Compact tool call notification"""
    type: Literal["tool_call"] = "tool_call"
    agent: str
    tool_name: str
    tool_input: Dict[str, Any]
    compact_display: str  # Pre-formatted: "🔍 Web Search: query"

class SystemMessage(ChatMessage):
    type: Literal["system"] = "system"
    content: str
    severity: Literal["info", "warning", "error"] = "info"
```

### 1.2 Agent Event Stream Service

**File**: `backend/services/agent_event_stream.py`

```python
from claude_agent_sdk import ClaudeSDKClient, Message, AssistantMessage, ToolUseBlock
from typing import AsyncIterator
from datetime import datetime
import uuid

class AgentEventStream:
    """
    Intercepts Claude Agent SDK messages and converts to chat messages.
    """

    async def run_agent_with_streaming(
        self,
        client: ClaudeSDKClient,
        user_prompt: str,
        session_id: str
    ) -> AsyncIterator[ChatMessage]:
        """
        Run agent and yield chat messages in real-time.
        """
        # Yield user message
        yield UserMessage(
            id=f"user_{session_id}_{uuid.uuid4().hex[:8]}",
            timestamp=datetime.now(),
            content=user_prompt
        )

        # Query agent
        await client.query(user_prompt)

        # Stream responses
        async for sdk_message in client.receive_response():
            chat_messages = self.convert_sdk_message(sdk_message, session_id)
            for msg in chat_messages:
                yield msg

    def convert_sdk_message(
        self,
        sdk_message: Message,
        session_id: str
    ) -> List[ChatMessage]:
        """Convert SDK message to chat message(s)"""
        messages = []

        if isinstance(sdk_message, AssistantMessage):
            for block in sdk_message.content:
                if isinstance(block, TextBlock):
                    # Regular text
                    messages.append(AssistantMessage(
                        id=f"asst_{uuid.uuid4().hex[:8]}",
                        timestamp=datetime.now(),
                        content=block.text,
                        agent="kaya"  # TODO: detect actual agent
                    ))

                elif isinstance(block, ToolUseBlock):
                    if block.name == "TodoWrite":
                        # Convert to ProgressMessage
                        messages.append(self.create_progress_message(
                            block.input,
                            session_id
                        ))
                    else:
                        # Convert to ToolCallMessage
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
        """Create progress message from TodoWrite"""
        todos = tool_input.get("todos", [])
        total = len(todos)
        completed = sum(1 for t in todos if t.get("status") == "completed")
        progress_percent = int((completed / total * 100)) if total > 0 else 0

        return ProgressMessage(
            id=f"progress_{uuid.uuid4().hex[:8]}",
            timestamp=datetime.now(),
            agent="kaya",  # TODO: detect agent
            todos=todos,
            progress_percent=progress_percent
        )

    def create_tool_call_message(
        self,
        tool_block: ToolUseBlock,
        session_id: str
    ) -> ToolCallMessage:
        """Create tool call message"""
        compact = self.format_tool_compact(
            tool_block.name,
            tool_block.input
        )

        return ToolCallMessage(
            id=f"tool_{uuid.uuid4().hex[:8]}",
            timestamp=datetime.now(),
            agent="kaya",
            tool_name=tool_block.name,
            tool_input=tool_block.input,
            compact_display=compact
        )

    def format_tool_compact(self, tool_name: str, tool_input: dict) -> str:
        """Format tool call compactly (same logic as CLI)"""
        if tool_name == "WebSearch":
            return f'🔍 Web Search: "{tool_input.get("query", "")}"'
        elif tool_name == "Task":
            subagent = tool_input.get("subagent_type", "")
            desc = tool_input.get("description", "")
            return f'🤝 Delegating to {subagent}: {desc}'
        elif tool_name == "Read":
            path = tool_input.get("file_path", "")
            return f'📖 Reading: {self.truncate_path(path)}'
        elif tool_name == "Write":
            path = tool_input.get("file_path", "")
            return f'💾 Writing: {self.truncate_path(path)}'
        elif tool_name == "Bash":
            cmd = tool_input.get("command", "")
            return f'⚡ Running: {self.truncate_command(cmd)}'
        else:
            return f'🔧 {tool_name}'

    def truncate_path(self, path: str, max_len: int = 50) -> str:
        if len(path) <= max_len:
            return path
        parts = path.split("/")
        return ".../" + "/".join(parts[-2:]) if len(parts) > 1 else parts[-1]

    def truncate_command(self, cmd: str, max_len: int = 100) -> str:
        if len(cmd) <= max_len:
            return cmd.split("\n")[0]  # First line only
        return cmd[:max_len-3] + "..."
```

### 1.3 WebSocket Endpoint

**File**: `backend/api/websocket.py`

```python
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import Dict
import json

app = FastAPI()

class ConnectionManager:
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
            ws = self.active_connections[session_id]
            await ws.send_text(message.model_dump_json())

manager = ConnectionManager()

@app.websocket("/ws/{session_id}")
async def websocket_endpoint(websocket: WebSocket, session_id: str):
    await manager.connect(session_id, websocket)

    try:
        while True:
            # Receive user message
            data = await websocket.receive_text()
            user_input = json.loads(data)

            # Create agent client
            from marketing_agent import get_marketing_agent_options
            from claude_agent_sdk import ClaudeSDKClient

            options = get_marketing_agent_options()
            async with ClaudeSDKClient(options=options) as client:
                event_stream = AgentEventStream()

                # Stream agent responses
                async for message in event_stream.run_agent_with_streaming(
                    client=client,
                    user_prompt=user_input["content"],
                    session_id=session_id
                ):
                    await manager.send_message(session_id, message)

    except WebSocketDisconnect:
        manager.disconnect(session_id)
```

### Backend Requirements

```
# requirements.txt
fastapi>=0.104.0
uvicorn[standard]>=0.24.0
websockets>=12.0
pydantic>=2.5.0
claude-agent-sdk>=1.0.0
python-dotenv>=1.0.0
```

### Run Backend

```bash
# Install dependencies
pip install -r requirements.txt

# Run server
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

---

## Phase 2: Frontend (React + TypeScript)

### 2.1 Project Setup

```bash
# Create React app
npx create-react-app marketing-agent-chat --template typescript
cd marketing-agent-chat

# Install dependencies
npm install tailwindcss autoprefixer postcss
npx tailwindcss init -p
```

### 2.2 Message Types (Frontend)

**File**: `src/types/messages.ts`

```typescript
export type MessageType = "user" | "assistant" | "progress" | "tool_call" | "system";

export interface ChatMessage {
  id: string;
  timestamp: string;
  type: MessageType;
}

export interface UserMessage extends ChatMessage {
  type: "user";
  content: string;
}

export interface AssistantMessage extends ChatMessage {
  type: "assistant";
  content: string;
  agent: string;
}

export interface ProgressMessage extends ChatMessage {
  type: "progress";
  agent: string;
  todos: Array<{
    content: string;
    status: "completed" | "in_progress" | "pending" | "failed";
    activeForm: string;
  }>;
  progress_percent: number;
}

export interface ToolCallMessage extends ChatMessage {
  type: "tool_call";
  agent: string;
  tool_name: string;
  tool_input: Record<string, any>;
  compact_display: string;
}

export interface SystemMessage extends ChatMessage {
  type: "system";
  content: string;
  severity: "info" | "warning" | "error";
}
```

### 2.3 Chat Container Component

**File**: `src/components/ChatContainer.tsx`

```typescript
import React, { useState, useEffect, useRef } from 'react';
import { ChatMessage } from '../types/messages';
import MessageRenderer from './MessageRenderer';

interface ChatContainerProps {
  sessionId: string;
}

export default function ChatContainer({ sessionId }: ChatContainerProps) {
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [input, setInput] = useState('');
  const [isConnected, setIsConnected] = useState(false);
  const ws = useRef<WebSocket | null>(null);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    // Connect to WebSocket
    ws.current = new WebSocket(`ws://localhost:8000/ws/${sessionId}`);

    ws.current.onopen = () => {
      setIsConnected(true);
      console.log('WebSocket connected');
    };

    ws.current.onmessage = (event) => {
      const message: ChatMessage = JSON.parse(event.data);

      setMessages(prev => {
        // If it's a progress message, replace the last progress message
        if (message.type === 'progress') {
          const lastProgressIdx = prev.findLastIndex(m => m.type === 'progress');
          if (lastProgressIdx !== -1) {
            const updated = [...prev];
            updated[lastProgressIdx] = message;
            return updated;
          }
        }

        // Otherwise, append the message
        return [...prev, message];
      });
    };

    ws.current.onclose = () => {
      setIsConnected(false);
      console.log('WebSocket disconnected');
    };

    ws.current.onerror = (error) => {
      console.error('WebSocket error:', error);
    };

    return () => {
      ws.current?.close();
    };
  }, [sessionId]);

  useEffect(() => {
    // Auto-scroll to bottom when new messages arrive
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  const sendMessage = () => {
    if (!input.trim() || !isConnected) return;

    ws.current?.send(JSON.stringify({
      content: input
    }));

    setInput('');
  };

  return (
    <div className="flex flex-col h-screen bg-gray-50">
      {/* Header */}
      <div className="bg-white border-b px-6 py-4">
        <h1 className="text-2xl font-bold text-gray-900">Kaya - Marketing Agent</h1>
        <p className="text-sm text-gray-500">
          {isConnected ? '🟢 Connected' : '🔴 Disconnected'}
        </p>
      </div>

      {/* Messages */}
      <div className="flex-1 overflow-y-auto p-4 space-y-4">
        {messages.map((message) => (
          <MessageRenderer key={message.id} message={message} />
        ))}
        <div ref={messagesEndRef} />
      </div>

      {/* Input */}
      <div className="border-t bg-white p-4">
        <div className="flex gap-2 max-w-4xl mx-auto">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyPress={(e) => e.key === 'Enter' && sendMessage()}
            placeholder="Ask Kaya anything..."
            disabled={!isConnected}
            className="flex-1 border border-gray-300 rounded-lg px-4 py-3 focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
          <button
            onClick={sendMessage}
            disabled={!isConnected || !input.trim()}
            className="bg-blue-600 text-white px-6 py-3 rounded-lg hover:bg-blue-700 disabled:bg-gray-300 disabled:cursor-not-allowed font-medium"
          >
            Send
          </button>
        </div>
      </div>
    </div>
  );
}
```

### 2.4 Message Renderer

**File**: `src/components/MessageRenderer.tsx`

```typescript
import React from 'react';
import { ChatMessage } from '../types/messages';
import ProgressCard from './cards/ProgressCard';
import ToolCallCard from './cards/ToolCallCard';

export default function MessageRenderer({ message }: { message: ChatMessage }) {
  switch (message.type) {
    case 'user':
      return (
        <div className="flex justify-end">
          <div className="bg-blue-600 text-white rounded-lg px-4 py-3 max-w-2xl shadow">
            {message.content}
          </div>
        </div>
      );

    case 'assistant':
      return (
        <div className="flex justify-start">
          <div className="bg-white border border-gray-200 rounded-lg px-4 py-3 max-w-2xl shadow-sm">
            <div className="text-xs text-gray-500 font-medium mb-1">{message.agent}</div>
            <div className="text-gray-900 whitespace-pre-wrap">{message.content}</div>
          </div>
        </div>
      );

    case 'progress':
      return <ProgressCard message={message} />;

    case 'tool_call':
      return <ToolCallCard message={message} />;

    case 'system':
      return (
        <div className="flex justify-center">
          <div className="bg-gray-100 text-gray-600 rounded-lg px-3 py-2 text-sm">
            {message.content}
          </div>
        </div>
      );

    default:
      return null;
  }
}
```

### 2.5 Progress Card Component

**File**: `src/components/cards/ProgressCard.tsx`

```typescript
import React from 'react';
import { ProgressMessage } from '../../types/messages';

export default function ProgressCard({ message }: { message: ProgressMessage }) {
  const { todos, progress_percent, agent } = message;

  const getStatusIcon = (status: string) => {
    const icons = {
      completed: '✓',
      in_progress: '⟳',
      pending: '○',
      failed: '✗'
    };
    return icons[status as keyof typeof icons] || '○';
  };

  return (
    <div className="flex justify-start">
      <div className="bg-cyan-50 border border-cyan-200 rounded-lg px-4 py-3 max-w-2xl shadow-sm">
        {/* Header */}
        <div className="flex items-center gap-2 mb-3">
          <span className="text-xl">📋</span>
          <span className="font-medium text-cyan-900">
            {agent} Progress
          </span>
        </div>

        {/* Progress Bar */}
        <div className="mb-3">
          <div className="flex items-center gap-3">
            <div className="flex-1 bg-gray-200 rounded-full h-2">
              <div
                className="bg-cyan-600 h-2 rounded-full transition-all duration-300 ease-out"
                style={{ width: `${progress_percent}%` }}
              />
            </div>
            <span className="text-sm font-semibold text-cyan-900 min-w-[50px] text-right">
              {progress_percent}%
            </span>
          </div>
        </div>

        {/* Todo List */}
        <div className="space-y-2">
          {todos.map((todo, idx) => (
            <div key={idx} className="flex items-start gap-2 text-sm">
              <span className="text-base flex-shrink-0">
                {getStatusIcon(todo.status)}
              </span>
              <span
                className={
                  todo.status === 'completed'
                    ? 'text-gray-500 line-through'
                    : todo.status === 'in_progress'
                    ? 'text-cyan-900 font-medium'
                    : 'text-gray-700'
                }
              >
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

### 2.6 Tool Call Card Component

**File**: `src/components/cards/ToolCallCard.tsx`

```typescript
import React, { useState } from 'react';
import { ToolCallMessage } from '../../types/messages';

export default function ToolCallCard({ message }: { message: ToolCallMessage }) {
  const [expanded, setExpanded] = useState(false);

  return (
    <div className="flex justify-start">
      <div className="bg-blue-50 border border-blue-200 rounded-lg px-4 py-2 max-w-2xl shadow-sm">
        <div
          className="flex items-center gap-2 cursor-pointer select-none"
          onClick={() => setExpanded(!expanded)}
        >
          <span className="text-sm text-blue-900">
            {message.compact_display}
          </span>
          {Object.keys(message.tool_input).length > 0 && (
            <span className="text-xs text-blue-600 ml-auto">
              {expanded ? '▼' : '▶'}
            </span>
          )}
        </div>

        {expanded && Object.keys(message.tool_input).length > 0 && (
          <pre className="mt-2 text-xs bg-blue-100 p-2 rounded overflow-x-auto font-mono">
            {JSON.stringify(message.tool_input, null, 2)}
          </pre>
        )}
      </div>
    </div>
  );
}
```

### 2.7 Tailwind Config

**File**: `tailwind.config.js`

```javascript
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

### 2.8 App Entry Point

**File**: `src/App.tsx`

```typescript
import React from 'react';
import ChatContainer from './components/ChatContainer';
import './App.css';

function App() {
  // Generate session ID (in production, this would come from auth/routing)
  const sessionId = React.useMemo(() => `session_${Date.now()}`, []);

  return (
    <div className="App">
      <ChatContainer sessionId={sessionId} />
    </div>
  );
}

export default App;
```

### Frontend Requirements

```json
// package.json
{
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "typescript": "^5.0.0",
    "tailwindcss": "^3.4.0"
  }
}
```

### Run Frontend

```bash
npm start
# Opens at http://localhost:3000
```

---

## Key Implementation Details

### Progress Message Handling

**IMPORTANT**: Progress messages should **replace** the previous progress message, not append.

```typescript
// In ChatContainer.tsx
ws.current.onmessage = (event) => {
  const message: ChatMessage = JSON.parse(event.data);

  setMessages(prev => {
    if (message.type === 'progress') {
      // Find last progress message
      const lastProgressIdx = prev.findLastIndex(m => m.type === 'progress');

      if (lastProgressIdx !== -1) {
        // Replace it
        const updated = [...prev];
        updated[lastProgressIdx] = message;
        return updated;
      }
    }

    // Otherwise append
    return [...prev, message];
  });
};
```

**Why**: Prevents the chat from filling up with 20 progress bars. The progress bar updates in place, creating a smooth animation effect.

### Auto-Scroll Behavior

```typescript
// In ChatContainer.tsx
const messagesEndRef = useRef<HTMLDivElement>(null);

useEffect(() => {
  messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
}, [messages]);

// In JSX
<div ref={messagesEndRef} />
```

**Why**: Keeps the latest message visible as the agent works.

### Status Icons

Use actual Unicode characters, not emoji fonts:
- ✓ (U+2713) - Completed
- ⟳ (U+27F3) - In Progress
- ○ (U+25CB) - Pending
- ✗ (U+2717) - Failed

**Why**: Consistent rendering across browsers and operating systems.

---

## Testing Strategy

### Backend Testing

```bash
# Test WebSocket connection
pip install websocket-client

python -c "
from websocket import create_connection
ws = create_connection('ws://localhost:8000/ws/test-session')
ws.send('{\"content\": \"Hello Kaya\"}')
result = ws.recv()
print(result)
ws.close()
"
```

### Frontend Testing

1. **Manual Test Flow**:
```
User: "Run a deep GEO analysis"

Expected sequence:
1. UserMessage appears (blue bubble on right)
2. AssistantMessage ("I'll run analysis...")
3. ToolCallMessage (🤝 Delegating to geo-optimizer)
4. ProgressMessage appears (0%)
5. ProgressMessage updates (20%, 40%, 60%, 80%, 100%) - REPLACES not appends
6. Multiple ToolCallMessages (WebSearch, Read, Write)
7. Final AssistantMessage with results
```

2. **Edge Cases to Test**:
- Disconnection/reconnection
- Multiple rapid messages
- Very long tool inputs (check truncation)
- Progress going from 100% back to 0% (new task)
- No progress for 30+ seconds (frozen?)

---

## Performance Requirements

### Backend

- [ ] WebSocket connection established < 100ms
- [ ] Message broadcast latency < 50ms
- [ ] Support 10+ concurrent sessions
- [ ] Memory usage < 500MB per session
- [ ] CPU usage < 50% during agent execution

### Frontend

- [ ] Initial page load < 2 seconds
- [ ] Message rendering < 16ms (60fps)
- [ ] Smooth progress bar animations
- [ ] No memory leaks with 100+ messages
- [ ] Works on Chrome, Firefox, Safari, Edge
- [ ] Mobile responsive (320px to 1920px)

---

## Deployment

### Production Environment

**Backend**:
```bash
# Use gunicorn with uvicorn workers
pip install gunicorn
gunicorn backend.main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

**Frontend**:
```bash
# Build production bundle
npm run build

# Serve with Nginx
# nginx.conf:
server {
    listen 80;
    server_name your-domain.com;

    location / {
        root /var/www/marketing-agent-chat/build;
        try_files $uri /index.html;
    }

    location /ws/ {
        proxy_pass http://localhost:8000/ws/;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }
}
```

### Environment Variables

**Backend** (`.env`):
```
ANTHROPIC_API_KEY=sk-ant-xxx
OPENAI_API_KEY=sk-xxx  # For MCP tools
PERPLEXITY_API_KEY=pplx-xxx  # For MCP tools
LOG_LEVEL=INFO
```

**Frontend** (`.env.production`):
```
REACT_APP_WS_URL=wss://your-domain.com/ws
```

---

## Security Considerations

1. **Authentication**: Add JWT tokens to WebSocket connection
2. **Rate Limiting**: Limit messages per user per minute
3. **Input Validation**: Sanitize user input before sending to agent
4. **XSS Protection**: Escape all user content in messages
5. **CORS**: Configure properly for production domain

---

## Future Enhancements

### Phase 3 (Post-Launch)

1. **Message History**: Persist chat history to database
2. **Multi-Session**: User can have multiple concurrent chats
3. **Agent Selection**: Let user choose which agent to talk to
4. **File Uploads**: Allow uploading data files for analysis
5. **Export**: Download conversation as PDF/Markdown
6. **Sharing**: Share chat link with team members
7. **Visualization Library**: Add tables, charts, metrics inline

---

## Success Criteria

### MVP Launch (Week 4)

- [ ] User can send message and get response
- [ ] Progress bars update in real-time
- [ ] Tool calls are compact and readable
- [ ] Works on desktop and mobile
- [ ] No crashes with 1-hour agent execution
- [ ] All 7 agents work in the UI

### Production Ready (Week 8)

- [ ] Multiple concurrent users supported
- [ ] Conversation history persisted
- [ ] Authentication implemented
- [ ] Production deployment stable
- [ ] Monitoring and alerts configured
- [ ] Documentation complete

---

## Reference Implementation

**CLI Code**: `/cli_tools.py` - Lines 154-319
- `render_progress_bar()` - Progress bar logic
- `get_status_icon()` - Status icons
- `render_todo_visualization()` - Main visualization
- `format_tool_compact()` - Tool formatting

**Agent System**: `/marketing_agent.py`
- Agent definitions and tool configurations
- Current agent prompts and skills

**Skills**: `/.claude/skills/`
- Detailed workflow instructions
- Expected behavior for each agent

---

## Timeline

### Week 1: Backend Foundation
- Day 1-2: Message types and AgentEventStream
- Day 3-4: WebSocket endpoint and testing
- Day 5: Integration with agent system

### Week 2: Frontend Foundation
- Day 1-2: Chat container and message renderer
- Day 3-4: Progress and tool call cards
- Day 5: Styling and responsive design

### Week 3: Integration & Testing
- Day 1-2: End-to-end testing all agents
- Day 3-4: Bug fixes and polish
- Day 5: Performance optimization

### Week 4: Deployment
- Day 1-2: Production setup
- Day 3-4: Load testing
- Day 5: Launch! 🚀

---

## Questions & Support

**Agent System Questions**: Ask AI Engineering Team
**Web Development Questions**: Ask Frontend Lead
**Deployment Questions**: Ask DevOps Team

**Slack Channels**:
- #marketing-agent-dev
- #marketing-agent-frontend
- #marketing-agent-backend

---

## Appendix: Message Flow Diagram

```
User sends message
     ↓
Frontend → WebSocket → Backend
                          ↓
                    AgentEventStream.run_agent_with_streaming()
                          ↓
                    Claude Agent SDK
                          ↓
                    Intercepts each message:
                    - TextBlock → AssistantMessage
                    - ToolUseBlock (TodoWrite) → ProgressMessage
                    - ToolUseBlock (other) → ToolCallMessage
                          ↓
                    WebSocket ← Backend
     ↓
Frontend receives message
     ↓
ChatContainer updates state
     ↓
MessageRenderer displays message
     ↓
Auto-scroll to bottom
```

---

## Example Session

**Full example of what the UI should look like:**

```
[User Message - Right side, blue]
Run a comprehensive SEO audit for acmecorp.com

[Assistant Message - Left side, white]
kaya
I'll run a comprehensive SEO audit for acmecorp.com. Let me delegate
this to my SEO specialist.

[Tool Call Message - Left side, light blue]
🤝 Delegating to seo-analyst: Comprehensive SEO audit

[Progress Message - Left side, cyan] ← This updates in place
📋 seo-analyst Progress
[████░░░░░░░░░░░░░░░░] 20% (2/10)

✓ Load company context
✓ Load marketing goals
⟳ Analyzing homepage...
○ Checking core pages
○ Technical infrastructure
○ Page speed analysis
○ Mobile-friendliness
○ Schema markup
○ Content quality
○ Issue prioritization

[Tool Call Message - Light blue]
📄 Fetching: https://acmecorp.com

[Tool Call Message - Light blue]
🔍 Web Search: "acmecorp.com page speed"

[Progress Message updates] ← Replaces previous progress message
📋 seo-analyst Progress
[████████░░░░░░░░░░░░] 40% (4/10)

✓ Load company context
✓ Load marketing goals
✓ Analyzing homepage
✓ Checking core pages
⟳ Analyzing technical infrastructure...
○ Page speed analysis
○ Mobile-friendliness
○ Schema markup
○ Content quality
○ Issue prioritization

... (progress continues updating) ...

[Progress Message final update]
📋 seo-analyst Progress
[████████████████████] 100% (10/10)

✓ Load company context
✓ Load marketing goals
✓ Analyzing homepage
✓ Checking core pages
✓ Technical infrastructure
✓ Page speed analysis
✓ Mobile-friendliness
✓ Schema markup
✓ Content quality
✓ Issue prioritization

[Assistant Message - White]
seo-analyst
SEO Audit Complete!

Overall Health Score: 68/100 (Needs Improvement)

Issues Found:
- 3 CRITICAL (fix immediately!)
- 12 HIGH priority
- 18 MEDIUM priority

Top Issue: robots.txt blocking blog content
Fix: Remove 'Disallow: /blog/' line
Time: 5 minutes
Impact: Makes 50 blog posts indexable!

Full report saved to: /data/clients/acme/analyses/seo/...

[Assistant Message - White]
kaya
The SEO audit is complete. Your site has a health score of 68/100.
The most critical issue is that your robots.txt file is blocking all
blog content from being indexed. This is a quick 5-minute fix that
will make 50 blog posts searchable on Google!

Would you like me to create a prioritized action plan for fixing these
issues?
```

---

**Good luck building! The CLI implementation is your north star. 🌟**

**Any questions, check `/cli_tools.py` lines 154-319 for working code.**
