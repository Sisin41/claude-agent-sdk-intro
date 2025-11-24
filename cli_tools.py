"""
CLI tools and convenience functions for working with the Claude Agent SDK in the terminal.
"""

from claude_agent_sdk import (
    AssistantMessage, 
    TextBlock, 
    ResultMessage, 
    ToolUseBlock, 
    ToolResultBlock, 
    ThinkingBlock, 
    UserMessage, 
    Message, 
    SystemMessage
)
from rich import print
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.console import Console
from rich.prompt import Prompt
from rich.syntax import Syntax
from dotenv import load_dotenv
from typing import Literal
import argparse
import json
load_dotenv()


# --------------------------------
# Parse runtime args from CLI
# --------------------------------

parser = argparse.ArgumentParser()
parser.add_argument("--stats", "-s", default="False", help="Print session stats")
parser.add_argument("--model", "-m", default="sonnet", help="Model to use")
parser.add_argument("--output-style", "-os", default="Personal Assistant", help="Output style to use")
parser.add_argument("--print-raw", "-pr", default="False", help="Print raw messages")


# --------------------------------
# Convenience functions for printing messages
# --------------------------------

def print_rich_message(
        type: Literal["user", "assistant", "tool_use", "tool_result", "system"],
        message: str,
        console: Console
        ):
    """
    Prints a message in a panel with a title and border color based on the message type.
    """
    styles = {
        "user": {
            "message_style": "bold yellow",
            "panel_title": "User Prompt",
            "border_style": "yellow"
            },
        "assistant": {
            "message_style": "bold green",
            "panel_title": "Assistant",
            "border_style": "green"
            },
        "tool_use": {
            "message_style": "bold blue",
            "panel_title": "Tool Use",
            "border_style": "blue"
            },
        "tool_result": {
            "message_style": "bold magenta",
            "panel_title": "Tool Result",
            "border_style": "magenta"
            },
        "system": {
            "message_style": "bold cyan",
            "panel_title": "System Message",
            "border_style": "cyan"}
    }

    # For tool results, try to apply JSON syntax highlighting
    if type == "tool_result" and is_json_string(message):
        panel_content = Syntax(message, "json", theme="monokai", line_numbers=False)
    else:
        panel_content = Text(message, style=styles[type]["message_style"])

    if type == "system":
        panel=Panel.fit(
            panel_content,
            title=styles[type]["panel_title"],
            border_style=styles[type]["border_style"]
            )
    else:
        panel=Panel(
            panel_content,
            title=styles[type]["panel_title"],
            border_style=styles[type]["border_style"]
            )
    console.print(panel, end="\n\n")


def is_json_string(text: str) -> bool:
    """Check if a string is valid JSON"""
    try:
        json.loads(text)
        return True
    except json.JSONDecodeError:
        return False


def format_tool_result(content) -> str:
    """
    Format tool result content nicely, handling nested JSON strings.
    """
    if isinstance(content, str):
        # Try to parse as JSON and format it
        try:
            parsed = json.loads(content)
            return json.dumps(parsed, indent=2)
        except json.JSONDecodeError:
            return content
    elif isinstance(content, list):
        # Handle list of content blocks (common format)
        formatted_parts = []
        for item in content:
            if isinstance(item, dict) and "text" in item:
                # Try to parse the text field as JSON
                text_content = item["text"]
                try:
                    parsed_json = json.loads(text_content)
                    formatted_json = json.dumps(parsed_json, indent=2)
                    formatted_parts.append(formatted_json)
                except json.JSONDecodeError:
                    # If not JSON, just use the text as-is
                    formatted_parts.append(text_content)
            else:
                # For other dict structures, format as JSON
                formatted_parts.append(json.dumps(item, indent=2))
        return "\n\n".join(formatted_parts)
    else:
        # For other types, convert to JSON
        return json.dumps(content, indent=2)


def get_user_input(console: Console) -> str:
    """
    Get user input and display it in a rich panel in one step.
    Returns the user input string.
    """
    user_input = Prompt.ask("\n[bold yellow]You[/bold yellow]", console=console)
    print()
    return user_input


def render_progress_bar(current: int, total: int, width: int = 20) -> str:
    """Render ASCII progress bar"""
    if total == 0:
        return "[" + "░" * width + "] 0% (0/0)"

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


def render_todo_visualization(tool_input: dict, console: Console):
    """Render TodoWrite visualization from tool input"""
    todos = tool_input.get("todos", [])

    if not todos:
        return

    # Calculate progress
    total = len(todos)
    completed = sum(1 for t in todos if t.get("status") == "completed")

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


def format_tool_compact(tool_name: str, tool_input: dict) -> str:
    """Format tool call compactly for display"""
    if tool_name == "WebSearch":
        query = tool_input.get("query", "")
        return f'🔍 Web Search: "{query}"'

    elif tool_name == "WebFetch":
        url = tool_input.get("url", "")
        # Truncate long URLs
        display_url = url if len(url) < 60 else url[:57] + "..."
        return f'📄 Fetching: {display_url}'

    elif tool_name == "Read":
        file_path = tool_input.get("file_path", "")
        # Show just filename if path is long
        if len(file_path) > 50:
            parts = file_path.split("/")
            file_path = ".../" + "/".join(parts[-2:]) if len(parts) > 1 else parts[-1]
        return f'📖 Reading: {file_path}'

    elif tool_name == "Write":
        file_path = tool_input.get("file_path", "")
        if len(file_path) > 50:
            parts = file_path.split("/")
            file_path = ".../" + "/".join(parts[-2:]) if len(parts) > 1 else parts[-1]
        return f'💾 Writing: {file_path}'

    elif tool_name == "Bash":
        command = tool_input.get("command", "")
        # Truncate long commands
        if len(command) > 100:
            command = command[:97] + "..."
        # Show just first line if multiline
        first_line = command.split("\n")[0]
        if len(command.split("\n")) > 1:
            first_line += "..."
        return f'⚡ Running: {first_line}'

    elif tool_name == "Task":
        subagent = tool_input.get("subagent_type", "unknown")
        description = tool_input.get("description", "")
        return f'🤝 Delegating to {subagent}: {description}'

    elif tool_name == "Grep":
        pattern = tool_input.get("pattern", "")
        path = tool_input.get("path", "current directory")
        return f'🔎 Searching for "{pattern}" in {path}'

    elif tool_name == "Glob":
        pattern = tool_input.get("pattern", "")
        return f'📁 Finding files: {pattern}'

    elif tool_name == "Edit":
        file_path = tool_input.get("file_path", "")
        if len(file_path) > 50:
            parts = file_path.split("/")
            file_path = ".../" + "/".join(parts[-2:]) if len(parts) > 1 else parts[-1]
        return f'✏️  Editing: {file_path}'

    else:
        # Default format for unknown tools
        return f'🔧 {tool_name}'


def parse_and_print_message(
        message: Message,
        console: Console,
        print_stats: bool = False
        ):
    """
    Parse and print a message based on its type and content.
    """
    # Assistant messages include TextBlock, ToolUseBlock, ThinkingBlock, and ToolResultBlock
    # https://docs.claude.com/en/api/agent-sdk/python#content-block-types
    if isinstance(message, SystemMessage):
        if message.subtype == "compact_boundary":
            print_rich_message(
                "system",
                f"Compaction completed \nPre-compaction tokens: {message.data["compact_metadata"]["pre_tokens"]} \nTrigger: {message.data["compact_metadata"]["trigger"]}",
                console
                )
        else:
            print_rich_message("system", json.dumps(message.data, indent=2), console)
    elif isinstance(message, AssistantMessage):
        for block in message.content:
            if isinstance(block, TextBlock):
                print_rich_message("assistant", block.text, console)
            elif isinstance(block, ToolUseBlock):
                # Check if this is TodoWrite - render visualization
                if block.name == "TodoWrite":
                    render_todo_visualization(block.input, console)
                else:
                    # Use compact formatting for other tools
                    compact_display = format_tool_compact(block.name, block.input)

                    # Create compact panel
                    panel = Panel(
                        compact_display,
                        border_style="blue",
                        padding=(0, 1)
                    )
                    console.print(panel, end="\n\n")
            elif isinstance(block, ThinkingBlock):
                print_rich_message("assistant", "Thinking...", console)
    elif isinstance(message, UserMessage):
        for block in message.content:
            if isinstance(block, ToolResultBlock):
                formatted_content = format_tool_result(block.content)
                print_rich_message("tool_result", formatted_content, console)
    elif isinstance(message, ResultMessage):
        
        if print_stats:
            result = message.subtype
            session_id = message.session_id
            duration_s = message.duration_ms/1000
            cost_usd = message.total_cost_usd
            input_tokens = message.usage["input_tokens"]
            output_tokens = message.usage["output_tokens"]

            session_stats = {
                "Session ID": session_id,
                "Result": result,
                "Duration (s)": f"{duration_s:.2f}",
                "Cost (USD)": f"${cost_usd:.2f}" if cost_usd else "N/A",
                "Input Tokens": input_tokens,
                "Output Tokens": output_tokens
            }

            if session_stats:
                stats_table = Table(
                    title="Session Stats",
                    show_header=False,
                    title_style="bold blue"
                )
                stats_table.add_column(style="cyan", no_wrap=True)
                stats_table.add_column(style="yellow")

                for stat_name, stat_value in session_stats.items():
                    stats_table.add_row(stat_name, str(stat_value))

                console.print(stats_table, end="\n")
