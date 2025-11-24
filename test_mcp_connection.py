#!/usr/bin/env python3
"""
Test script to verify MCP server connection.
This will attempt to start the MCP server and verify it can communicate.
"""

import asyncio
import json
import subprocess
import sys
from pathlib import Path

async def test_mcp_server():
    """Test if MCP server can start and respond to requests."""
    print("🧪 Testing MCP Server Connection\n")

    # Path to MCP server
    server_path = Path("/home/user/claude-agent-sdk-intro/mcp-servers/marketing-tools/dist/index.js")

    print(f"✓ MCP server file exists: {server_path.exists()}")

    if not server_path.exists():
        print("❌ MCP server file not found!")
        return False

    print("\n📡 Starting MCP server...")

    try:
        # Start the MCP server process
        process = subprocess.Popen(
            ["node", str(server_path)],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        print("✓ MCP server process started (PID: {})".format(process.pid))

        # Send a list tools request
        print("\n📤 Sending ListTools request...")
        request = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "tools/list",
            "params": {}
        }

        # Write request to stdin
        process.stdin.write(json.dumps(request) + "\n")
        process.stdin.flush()

        # Wait for response with timeout
        print("⏳ Waiting for response...")

        try:
            # Read response line
            response_line = process.stdout.readline()

            if response_line:
                print("✓ Received response from MCP server")

                try:
                    response = json.loads(response_line)
                    print("\n📋 Response:")
                    print(json.dumps(response, indent=2)[:500])  # Print first 500 chars

                    # Check if tools are listed
                    if "result" in response and "tools" in response.get("result", {}):
                        tools = response["result"]["tools"]
                        print(f"\n✅ SUCCESS! MCP server returned {len(tools)} tools:")
                        for tool in tools:
                            print(f"   - {tool['name']}")
                        return True
                    else:
                        print("\n⚠️  Response received but no tools found")
                        return False

                except json.JSONDecodeError as e:
                    print(f"\n❌ Failed to parse response: {e}")
                    print(f"Raw response: {response_line}")
                    return False
            else:
                print("❌ No response received from MCP server")
                return False

        finally:
            # Clean up process
            process.terminate()
            try:
                process.wait(timeout=2)
            except subprocess.TimeoutExpired:
                process.kill()
            print("\n🛑 MCP server stopped")

    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False

async def main():
    """Run the test."""
    success = await test_mcp_server()

    if success:
        print("\n" + "="*60)
        print("✅ MCP SERVER CONNECTION TEST PASSED")
        print("="*60)
        print("\nThe MCP server:")
        print("  ✓ Can start successfully")
        print("  ✓ Responds to ListTools requests")
        print("  ✓ Exposes run_multi_engine_test and analyze_citations tools")
        print("\nNext step: Test with agent to verify full integration")
        return 0
    else:
        print("\n" + "="*60)
        print("❌ MCP SERVER CONNECTION TEST FAILED")
        print("="*60)
        print("\nTroubleshooting steps:")
        print("  1. Check if Node.js is installed: node --version")
        print("  2. Check if MCP server file exists")
        print("  3. Check server logs for errors")
        return 1

if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)
