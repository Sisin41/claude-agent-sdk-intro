#!/usr/bin/env bash
# Query Perplexity API with live web search (sonar-pro model)
# Usage: bash query-perplexity.sh "Your prompt here"
# Requires: PERPLEXITY_API_KEY environment variable
# Returns: JSON with {response, citations, web_results}

set -euo pipefail

PROMPT="${1:?Usage: query-perplexity.sh \"Your prompt here\"}"

if [ -z "${PERPLEXITY_API_KEY:-}" ]; then
  echo "Error: PERPLEXITY_API_KEY environment variable is not set" >&2
  exit 1
fi

RAW_RESPONSE=$(curl -s https://api.perplexity.ai/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ${PERPLEXITY_API_KEY}" \
  -d "$(jq -n \
    --arg prompt "$PROMPT" \
    '{
      model: "sonar-pro",
      messages: [
        {
          role: "system",
          content: "You are a helpful research assistant. Provide comprehensive answers with specific sources and citations."
        },
        {
          role: "user",
          content: $prompt
        }
      ],
      temperature: 0.7,
      max_tokens: 2000
    }')")

# Extract and restructure the response into our standard format
echo "$RAW_RESPONSE" | jq '{
  response: (.choices[0].message.content // "Error: No response received"),
  citations: (.citations // []),
  web_results: (.web_results // [])
}'
