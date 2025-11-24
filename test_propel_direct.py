#!/usr/bin/env python3
"""
Direct SDK test for propel.io analysis (non-interactive).
This bypasses the Rich interactive CLI and calls the SDK directly.
"""

import asyncio
import sys
from pathlib import Path

# Add project to path
sys.path.insert(0, str(Path(__file__).parent))

from marketing_agent import get_marketing_agent_options
from claude_agent_sdk import ClaudeSDKClient
from cli_tools import parse_and_print_message
from rich.console import Console

async def test_propel_analysis():
    """Run propel.io analysis directly via SDK."""
    console = Console()

    console.print("\n" + "="*70, style="bold cyan")
    console.print("🧪 Testing Agent with propel.io Analysis", style="bold cyan")
    console.print("="*70 + "\n", style="bold cyan")

    # Get agent options
    console.print("📝 Loading agent configuration...", style="yellow")
    options = get_marketing_agent_options(model="sonnet")

    # Verify MCP servers
    if hasattr(options, 'mcp_servers') and options.mcp_servers:
        console.print("✓ MCP servers configured", style="green")

    console.print("✓ Agent initialized\n", style="green")

    # Test prompt
    prompt = """Please analyze propel.io:

1. Run a LIGHT GEO analysis with only 10 test prompts for propel.io
2. Also perform a preliminary SEO analysis of their website

Keep both analyses brief since this is a test run to verify the system works."""

    console.print("📤 Sending prompt:", style="bold yellow")
    console.print(f"   \"{prompt[:100]}...\"\n", style="yellow")

    try:
        # Create SDK client
        async with ClaudeSDKClient(options=options) as client:
            # Send query
            await client.query(prompt)

            console.print("⏳ Processing (this may take several minutes)...\n", style="yellow")

            # Receive and display response
            message_count = 0
            async for message in client.receive_response():
                message_count += 1

                # Print raw message for debugging
                if message_count == 1:
                    console.print(f"[dim]Received first message (type: {message.get('type', 'unknown')})[/dim]\n")

                # Parse and print using our CLI visualization
                parse_and_print_message(message, console)

            console.print(f"\n✅ Completed! Processed {message_count} messages\n", style="bold green")

    except Exception as e:
        console.print(f"\n❌ Error: {e}\n", style="bold red")
        import traceback
        traceback.print_exc()
        return False

    return True

async def main():
    """Run the test."""
    console = Console()

    success = await test_propel_analysis()

    console.print("\n" + "="*70, style="bold")
    if success:
        console.print("✅ TEST COMPLETED SUCCESSFULLY", style="bold green")
    else:
        console.print("❌ TEST FAILED", style="bold red")
    console.print("="*70 + "\n", style="bold")

    return 0 if success else 1

if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)
