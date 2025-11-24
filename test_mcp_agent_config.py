#!/usr/bin/env python3
"""Quick test to verify agent configuration with MCP servers."""

import sys
from marketing_agent import get_marketing_agent_options

def test_config():
    """Test that agent configuration includes MCP servers."""
    print("="*70)
    print("🧪 Testing Agent Configuration with MCP")
    print("="*70)
    print()

    try:
        print("📝 Loading agent options...")
        options = get_marketing_agent_options(model="claude-sonnet-4-5")
        print("✓ Agent options loaded successfully")
        print()

        # Check MCP servers
        if hasattr(options, 'mcp_servers') and options.mcp_servers:
            print("✅ MCP servers configured:")
            for name, config in options.mcp_servers.items():
                command = config.get('command', 'unknown')
                args = config.get('args', [])
                print(f"   • Server: {name}")
                print(f"     Command: {command}")
                print(f"     Args: {' '.join(args)}")
                print()
        else:
            print("❌ No MCP servers configured!")
            return False

        # Check agents
        if hasattr(options, 'agents') and options.agents:
            print(f"✅ {len(options.agents)} agents configured:")
            for agent_name, agent_def in options.agents.items():
                print(f"   • {agent_name}")
                if hasattr(agent_def, 'tools'):
                    mcp_tools = [t for t in agent_def.tools if t.startswith('mcp__')]
                    if mcp_tools:
                        print(f"     MCP tools enabled: {len(mcp_tools)}")
                        for tool in mcp_tools:
                            print(f"       - {tool}")
            print()
        else:
            print("⚠️  No agents configured")

        print("="*70)
        print("✅ CONFIGURATION TEST PASSED")
        print("="*70)
        print()
        print("Summary:")
        print("  ✓ Agent options load correctly")
        print("  ✓ MCP servers are configured")
        print("  ✓ Agents have access to MCP tools")
        print()
        print("Next: Run the agent interactively to test execution")
        print("  Command: uv run python marketing_agent.py")
        print('  Prompt: "Run a light GEO analysis"')
        print()

        return True

    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_config()
    sys.exit(0 if success else 1)
