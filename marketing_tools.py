"""
Marketing Tools - Programmatic Tool Calling Support

Custom tools designed for programmatic calling via code execution.
These tools enable token-efficient batch processing of large-scale
marketing analysis workflows.
"""

import os
from typing import Any, Dict, List

# ============================================================================
# PROGRAMMATIC TOOLS DEFINITIONS
# ============================================================================

PROGRAMMATIC_TOOLS = [
    # ========================================================================
    # GEO: Multi-Engine Query Tools
    # ========================================================================
    {
        "name": "query_chatgpt",
        "description": """Query ChatGPT (GPT-4) with a prompt and return the response text.

        Designed for programmatic calling from code execution to enable:
        - Batch querying of multiple prompts
        - In-code processing of responses
        - Token-efficient aggregation of results

        Returns: String response from ChatGPT

        Note: Requires OPENAI_API_KEY environment variable.""",
        "input_schema": {
            "type": "object",
            "properties": {
                "prompt": {
                    "type": "string",
                    "description": "The prompt to send to ChatGPT"
                },
                "model": {
                    "type": "string",
                    "description": "Model to use (default: gpt-4o)",
                    "default": "gpt-4o"
                },
                "max_tokens": {
                    "type": "number",
                    "description": "Maximum tokens in response (default: 1000)",
                    "default": 1000
                }
            },
            "required": ["prompt"]
        },
        "allowed_callers": ["code_execution_20250825"]
    },

    {
        "name": "query_perplexity",
        "description": """Query Perplexity AI with a prompt and return the response with citations.

        Designed for programmatic calling from code execution to enable:
        - Batch querying across multiple prompts
        - Citation extraction in code
        - Token-efficient aggregation

        Returns: JSON string with response and citations

        Note: Requires PERPLEXITY_API_KEY environment variable.""",
        "input_schema": {
            "type": "object",
            "properties": {
                "prompt": {
                    "type": "string",
                    "description": "The prompt to send to Perplexity"
                },
                "model": {
                    "type": "string",
                    "description": "Model to use (default: llama-3.1-sonar-large-128k-online)",
                    "default": "llama-3.1-sonar-large-128k-online"
                }
            },
            "required": ["prompt"]
        },
        "allowed_callers": ["code_execution_20250825"]
    },

    {
        "name": "query_gemini",
        "description": """Query Google Gemini with a prompt and return the response text.

        Designed for programmatic calling from code execution to enable:
        - Batch querying of multiple prompts
        - In-code processing of responses
        - Token-efficient aggregation of results

        Returns: String response from Gemini

        Note: Requires GOOGLE_API_KEY environment variable.""",
        "input_schema": {
            "type": "object",
            "properties": {
                "prompt": {
                    "type": "string",
                    "description": "The prompt to send to Gemini"
                },
                "model": {
                    "type": "string",
                    "description": "Model to use (default: gemini-2.0-flash-exp)",
                    "default": "gemini-2.0-flash-exp"
                }
            },
            "required": ["prompt"]
        },
        "allowed_callers": ["code_execution_20250825"]
    },

    # ========================================================================
    # SEO: Backlink Analysis Tools
    # ========================================================================
    {
        "name": "fetch_backlink_data",
        "description": """Fetch backlink data for a domain from SEO APIs.

        Returns CSV-formatted string with backlink records. Can return very large
        datasets (1M+ tokens) for processing programmatically.

        DO NOT load full results into context - designed for programmatic processing
        where code execution filters and aggregates data before returning insights.

        Returns: CSV string with columns: source_domain, target_url, anchor_text,
                 domain_authority, spam_score, first_seen, last_seen

        Note: Requires SEO_API_KEY environment variable (Ahrefs, Moz, or similar).""",
        "input_schema": {
            "type": "object",
            "properties": {
                "domain": {
                    "type": "string",
                    "description": "Domain to fetch backlinks for (e.g., 'example.com')"
                },
                "limit": {
                    "type": "number",
                    "description": "Maximum number of backlinks to fetch (default: 10000)",
                    "default": 10000
                }
            },
            "required": ["domain"]
        },
        "allowed_callers": ["code_execution_20250825"]
    },

    # ========================================================================
    # Analytics: Data Aggregation Tools
    # ========================================================================
    {
        "name": "read_analytics_file",
        "description": """Read analytics data file and return JSON string.

        Designed for programmatic aggregation across multiple time periods.
        Code execution can load multiple months/years of data, aggregate in Python,
        and return only summary statistics.

        Returns: JSON string with analytics data

        Example usage in code:
        ```python
        jan = await read_analytics_file("/data/analytics-jan.json")
        feb = await read_analytics_file("/data/analytics-feb.json")
        mar = await read_analytics_file("/data/analytics-mar.json")

        # Aggregate in code
        quarterly_data = aggregate_months([jan, feb, mar])
        return quarterly_data  # Only summary to context
        ```""",
        "input_schema": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to analytics JSON file"
                }
            },
            "required": ["file_path"]
        },
        "allowed_callers": ["code_execution_20250825"]
    },
]


# ============================================================================
# TOOL IMPLEMENTATIONS
# ============================================================================
# These would be implemented server-side to handle tool calls from code execution

async def handle_query_chatgpt(prompt: str, model: str = "gpt-4o", max_tokens: int = 1000) -> str:
    """
    Implementation for query_chatgpt tool.
    Called when code execution invokes this tool.
    """
    import openai

    client = openai.AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    response = await client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=max_tokens
    )

    return response.choices[0].message.content


async def handle_query_perplexity(prompt: str, model: str = "llama-3.1-sonar-large-128k-online") -> str:
    """
    Implementation for query_perplexity tool.
    Called when code execution invokes this tool.
    """
    import httpx
    import json

    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://api.perplexity.ai/chat/completions",
            headers={
                "Authorization": f"Bearer {os.getenv('PERPLEXITY_API_KEY')}",
                "Content-Type": "application/json"
            },
            json={
                "model": model,
                "messages": [{"role": "user", "content": prompt}]
            },
            timeout=30.0
        )

        result = response.json()

        # Return JSON string with response and citations
        return json.dumps({
            "response": result["choices"][0]["message"]["content"],
            "citations": result.get("citations", [])
        })


async def handle_query_gemini(prompt: str, model: str = "gemini-2.0-flash-exp") -> str:
    """
    Implementation for query_gemini tool.
    Called when code execution invokes this tool.
    """
    import google.generativeai as genai

    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    model_instance = genai.GenerativeModel(model)

    response = await model_instance.generate_content_async(prompt)

    return response.text


async def handle_fetch_backlink_data(domain: str, limit: int = 10000) -> str:
    """
    Implementation for fetch_backlink_data tool.
    Called when code execution invokes this tool.

    Note: This is a placeholder. In production, integrate with Ahrefs, Moz, or SEMrush API.
    """
    # Placeholder implementation - would integrate with actual SEO API
    import csv
    from io import StringIO

    output = StringIO()
    writer = csv.writer(output)

    # Write header
    writer.writerow([
        'source_domain', 'target_url', 'anchor_text',
        'domain_authority', 'spam_score', 'first_seen', 'last_seen'
    ])

    # In production: Fetch from SEO API
    # For now, return placeholder data
    for i in range(min(limit, 100)):  # Limit to 100 for demo
        writer.writerow([
            f'referring-site-{i}.com',
            f'https://{domain}/page-{i}',
            f'anchor text {i}',
            60 + (i % 40),  # DA 60-100
            i % 10,  # Spam score 0-9
            '2024-01-01',
            '2024-12-01'
        ])

    return output.getvalue()


async def handle_read_analytics_file(file_path: str) -> str:
    """
    Implementation for read_analytics_file tool.
    Called when code execution invokes this tool.
    """
    import json

    with open(file_path, 'r') as f:
        data = json.load(f)

    return json.dumps(data)


# ============================================================================
# TOOL HANDLER REGISTRY
# ============================================================================

TOOL_HANDLERS = {
    "query_chatgpt": handle_query_chatgpt,
    "query_perplexity": handle_query_perplexity,
    "query_gemini": handle_query_gemini,
    "fetch_backlink_data": handle_fetch_backlink_data,
    "read_analytics_file": handle_read_analytics_file,
}
