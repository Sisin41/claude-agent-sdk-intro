#!/usr/bin/env bash
# Query Perplexity AI with web search enabled
# Usage: ./query-perplexity.sh "your prompt here" [model]
#
# Requires: PERPLEXITY_API_KEY environment variable
# Returns: JSON response with citations array
#
# Models:
#   sonar-pro      - Best for GEO testing (web search, citations)
#   sonar          - Lighter, faster

set -euo pipefail

PROMPT="${1:?Usage: query-perplexity.sh \"prompt\" [model]}"
MODEL="${2:-sonar-pro}"

if [ -z "${PERPLEXITY_API_KEY:-}" ]; then
  echo '{"error": "PERPLEXITY_API_KEY not set"}' >&2
  exit 1
fi

ESCAPED_PROMPT=$(printf '%s' "$PROMPT" | python3 -c 'import sys,json; print(json.dumps(sys.stdin.read()))')

curl -s https://api.perplexity.ai/chat/completions \
  -H "Authorization: Bearer $PERPLEXITY_API_KEY" \
  -H "Content-Type: application/json" \
  --max-time 30 \
  --retry 3 \
  --retry-delay 2 \
  -d "{
    \"model\": \"$MODEL\",
    \"messages\": [
      {\"role\": \"user\", \"content\": $ESCAPED_PROMPT}
    ]
  }"
