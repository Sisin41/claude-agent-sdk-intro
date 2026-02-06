#!/usr/bin/env bash
# Query Gemini API with Google Search grounding (gemini-2.0-flash-exp model)
# Usage: bash query-gemini.sh "Your prompt here"
# Requires: GOOGLE_API_KEY environment variable
# Returns: JSON with {response, grounding_metadata, citations}

set -euo pipefail

PROMPT="${1:?Usage: query-gemini.sh \"Your prompt here\"}"

if [ -z "${GOOGLE_API_KEY:-}" ]; then
  echo "Error: GOOGLE_API_KEY environment variable is not set" >&2
  exit 1
fi

RAW_RESPONSE=$(curl -s "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash-exp:generateContent?key=${GOOGLE_API_KEY}" \
  -H "Content-Type: application/json" \
  -d "$(jq -n \
    --arg prompt "$PROMPT" \
    '{
      contents: [
        {
          parts: [
            {
              text: $prompt
            }
          ]
        }
      ],
      tools: [
        {
          google_search_retrieval: {
            dynamic_retrieval_config: {
              mode: "MODE_DYNAMIC",
              dynamic_threshold: 0.3
            }
          }
        }
      ],
      generationConfig: {
        temperature: 0.7,
        maxOutputTokens: 2000
      }
    }')")

# Extract and restructure the response into our standard format
RESPONSE_TEXT=$(echo "$RAW_RESPONSE" | jq -r '.candidates[0].content.parts[0].text // "Error: No response received"')
GROUNDING=$(echo "$RAW_RESPONSE" | jq '.candidates[0].groundingMetadata // {}')
CITATIONS=$(echo "$RAW_RESPONSE" | jq '[.candidates[0].groundingMetadata.groundingChunks[]? | {url: .web.uri, title: .web.title}] // []')

jq -n \
  --arg response "$RESPONSE_TEXT" \
  --argjson grounding_metadata "$GROUNDING" \
  --argjson citations "$CITATIONS" \
  '{
    response: $response,
    grounding_metadata: $grounding_metadata,
    citations: $citations
  }'
