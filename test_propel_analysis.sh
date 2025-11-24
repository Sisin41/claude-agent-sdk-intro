#!/bin/bash
# Test script for propel.io analysis

echo "🚀 Starting agent test for propel.io..."
echo ""

# Create input file with prompts
cat > /tmp/agent_input.txt << 'EOF'
Please analyze propel.io:

1. Run a GEO analysis with only 10 test prompts (light mode) for propel.io
2. Also perform a preliminary SEO analysis of their website

Keep both analyses brief since this is a test run.
exit
EOF

echo "📤 Sending prompt to agent..."
echo ""

# Run agent with input
cd /home/user/claude-agent-sdk-intro
uv run python marketing_agent.py < /tmp/agent_input.txt

echo ""
echo "✅ Test completed!"
