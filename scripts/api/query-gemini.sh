#!/usr/bin/env bash
# Query Google Gemini with optional search grounding
# Usage: ./query-gemini.sh "your prompt here" [model]
#
# Requires: GEMINI_API_KEY environment variable
# Returns: JSON response from Gemini API
#
# Models:
#   gemini-2.0-flash   - Fast, good for batch testing
#   gemini-2.0-pro     - More capable, slower

set -euo pipefail

PROMPT="${1:?Usage: query-gemini.sh \"prompt\" [model]}"
MODEL="${2:-gemini-2.0-flash}"

if [ -z "${GEMINI_API_KEY:-}" ]; then
  echo '{"error": "GEMINI_API_KEY not set"}' >&2
  exit 1
fi

ESCAPED_PROMPT=$(printf '%s' "$PROMPT" | python3 -c 'import sys,json; print(json.dumps(sys.stdin.read()))')

curl -s "https://generativelanguage.googleapis.com/v1beta/models/${MODEL}:generateContent?key=${GEMINI_API_KEY}" \
  -H "Content-Type: application/json" \
  --max-time 30 \
  --retry 3 \
  --retry-delay 2 \
  -d "{
    \"contents\": [{
      \"parts\": [{\"text\": $ESCAPED_PROMPT}]
    }],
    \"tools\": [{
      \"google_search\": {}
    }]
  }"
