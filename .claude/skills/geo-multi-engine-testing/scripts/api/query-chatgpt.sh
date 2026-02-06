#!/usr/bin/env bash
# Query ChatGPT API with search enabled (gpt-4o model)
# Usage: bash query-chatgpt.sh "Your prompt here"
# Requires: OPENAI_API_KEY environment variable
# Returns: Plain text response from ChatGPT

set -euo pipefail

PROMPT="${1:?Usage: query-chatgpt.sh \"Your prompt here\"}"

if [ -z "${OPENAI_API_KEY:-}" ]; then
  echo "Error: OPENAI_API_KEY environment variable is not set" >&2
  exit 1
fi

curl -s https://api.openai.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ${OPENAI_API_KEY}" \
  -d "$(jq -n \
    --arg prompt "$PROMPT" \
    '{
      model: "gpt-4o",
      messages: [
        {
          role: "system",
          content: "You are a helpful assistant. Provide comprehensive, well-sourced answers. When possible, cite specific sources and URLs."
        },
        {
          role: "user",
          content: $prompt
        }
      ],
      temperature: 0.7,
      max_tokens: 2000
    }')" | jq -r '.choices[0].message.content // "Error: No response received"'
