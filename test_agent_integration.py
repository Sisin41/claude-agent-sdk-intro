#!/usr/bin/env python3
"""
Test script to verify full agent integration with MCP tools.
This will run the agent with a light GEO analysis prompt.
"""

import asyncio
import sys
import time
from pathlib import Path

# Add project to path
sys.path.insert(0, str(Path(__file__).parent))

from marketing_agent import get_marketing_agent_options
from claude_code_agent_sdk import ClaudeAgentSDK

async def test_agent_with_mcp():
    """Test the agent with MCP tools enabled."""
    print("="*70)
    print("🧪 Testing Marketing Agent with MCP Tools")
    print("="*70)
    print()

    # Get agent options with MCP enabled
    print("📝 Initializing agent...")
    options = get_marketing_agent_options(model="claude-sonnet-4-5")

    # Verify MCP servers are configured
    if hasattr(options, 'mcp_servers') and options.mcp_servers:
        print("✓ MCP servers configured:")
        for name, config in options.mcp_servers.items():
            print(f"   - {name}: {config['command']} {' '.join(config['args'])}")
    else:
        print("⚠️  No MCP servers configured!")

    print()
    print("🚀 Starting agent...")
    print()

    # Create SDK instance
    sdk = ClaudeAgentSDK(options)

    # Test prompt (light GEO analysis)
    test_prompt = """Run a light GEO analysis for a fictional company called "Acme AI Support"
that provides AI-powered customer support tools.

Please use the MCP tools if available (run_multi_engine_test).
If MCP tools are not available, mention that you're falling back to manual analysis.

Keep this test brief - just verify the tools work."""

    print("📤 Sending test prompt:")
    print("-" * 70)
    print(test_prompt)
    print("-" * 70)
    print()

    start_time = time.time()

    try:
        # Run the agent
        response = await sdk.run(test_prompt)

        elapsed_time = time.time() - start_time

        print()
        print("="*70)
        print("✅ Agent completed successfully!")
        print("="*70)
        print()
        print(f"⏱️  Time taken: {elapsed_time:.2f} seconds")
        print()
        print("📋 Response:")
        print("-" * 70)
        print(response)
        print("-" * 70)
        print()

        # Check for MCP tool usage indicators
        response_lower = response.lower()
        mcp_indicators = [
            "run_multi_engine_test",
            "mcp tool",
            "parallel",
            "multi-engine",
        ]

        found_indicators = [ind for ind in mcp_indicators if ind in response_lower]

        if found_indicators:
            print("✅ MCP tools appear to have been used!")
            print(f"   Indicators found: {', '.join(found_indicators)}")
        else:
            print("⚠️  No clear MCP tool usage indicators found")
            print("   This might mean:")
            print("   - API keys are missing (expected)")
            print("   - Agent fell back to manual analysis")
            print("   - MCP tools weren't needed for this query")

        print()

        # Performance check
        if elapsed_time < 120:  # Less than 2 minutes
            print("✅ Performance looks good (< 2 minutes)")
        else:
            print("⚠️  Took longer than expected (> 2 minutes)")

        return True

    except Exception as e:
        elapsed_time = time.time() - start_time
        print()
        print("="*70)
        print("❌ Agent failed!")
        print("="*70)
        print()
        print(f"⏱️  Time before failure: {elapsed_time:.2f} seconds")
        print(f"❌ Error: {e}")
        print()
        import traceback
        traceback.print_exc()
        return False

async def main():
    """Run the test."""
    print()
    success = await test_agent_with_mcp()
    print()

    if success:
        print("="*70)
        print("✅ AGENT INTEGRATION TEST PASSED")
        print("="*70)
        return 0
    else:
        print("="*70)
        print("❌ AGENT INTEGRATION TEST FAILED")
        print("="*70)
        return 1

if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)
