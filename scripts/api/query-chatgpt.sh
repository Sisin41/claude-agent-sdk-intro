#!/usr/bin/env bash
# Query ChatGPT (GPT-4o) via OpenAI API
# Usage: ./query-chatgpt.sh "your prompt here" [model] [max_tokens]
#
# Requires: OPENAI_API_KEY environment variable
# Returns: JSON response from OpenAI API

set -euo pipefail

PROMPT="${1:?Usage: query-chatgpt.sh \"prompt\" [model] [max_tokens]}"
MODEL="${2:-gpt-4o}"
MAX_TOKENS="${3:-1500}"

if [ -z "${OPENAI_API_KEY:-}" ]; then
  echo '{"error": "OPENAI_API_KEY not set"}' >&2
  exit 1
fi

# Escape prompt for JSON (handle newlines, quotes, backslashes)
ESCAPED_PROMPT=$(printf '%s' "$PROMPT" | python3 -c 'import sys,json; print(json.dumps(sys.stdin.read()))')

curl -s https://api.openai.com/v1/chat/completions \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  --max-time 30 \
  --retry 3 \
  --retry-delay 2 \
  -d "{
    \"model\": \"$MODEL\",
    \"max_tokens\": $MAX_TOKENS,
    \"messages\": [
      {\"role\": \"user\", \"content\": $ESCAPED_PROMPT}
    ]
  }"
