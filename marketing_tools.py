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
        "description": """Query ChatGPT (GPT-4o) with a prompt and return the response text.

        **IMPORTANT FOR GEO TESTING**: This simulates what users with ChatGPT Plus (web search enabled) see.
        While the API doesn't have direct web search, we instruct the model to provide current information
        as if browsing were enabled, which reflects the user experience we're testing for GEO.

        Designed for programmatic calling from code execution to enable:
        - Batch querying of multiple prompts
        - In-code processing of responses
        - Token-efficient aggregation of results
        - Testing brand visibility in AI search results

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
                    "description": "Model to use (default: gpt-4o - latest as of Jan 2025)",
                    "default": "gpt-4o"
                },
                "max_tokens": {
                    "type": "number",
                    "description": "Maximum tokens in response (default: 1500)",
                    "default": 1500
                }
            },
            "required": ["prompt"]
        },
        "allowed_callers": ["code_execution_20250825"]
    },

    {
        "name": "query_perplexity",
        "description": """Query Perplexity AI with web search enabled and return response with citations.

        **IMPORTANT FOR GEO TESTING**: Uses Perplexity's online search models which actively
        search the web to answer queries. This is CRITICAL for GEO testing as we're checking
        if companies appear in real-time web search results.

        Designed for programmatic calling from code execution to enable:
        - Batch querying across multiple prompts with live web search
        - Citation extraction in code (URLs where brand is mentioned)
        - Token-efficient aggregation
        - Testing brand visibility in AI search results

        Returns: JSON string with response and citations array

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
                    "description": "Model to use (default: sonar-pro - latest online model with web search)",
                    "default": "sonar-pro"
                }
            },
            "required": ["prompt"]
        },
        "allowed_callers": ["code_execution_20250825"]
    },

    {
        "name": "query_gemini",
        "description": """Query Google Gemini with Google Search grounding enabled.

        **IMPORTANT FOR GEO TESTING**: Uses Gemini with Google Search grounding which allows
        the model to search the web in real-time. This is CRITICAL for GEO testing as we're
        checking if companies appear when Gemini searches Google.

        Designed for programmatic calling from code execution to enable:
        - Batch querying of multiple prompts with live web search via Google
        - In-code processing of responses
        - Token-efficient aggregation of results
        - Testing brand visibility in Gemini's search-grounded responses

        Returns: JSON string with response and grounding metadata (sources, URLs)

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
                    "description": "Model to use (default: gemini-2.0-flash-exp - latest with grounding support)",
                    "default": "gemini-2.0-flash-exp"
                },
                "enable_search_grounding": {
                    "type": "boolean",
                    "description": "Enable Google Search grounding (default: true)",
                    "default": true
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

async def handle_query_chatgpt(prompt: str, model: str = "gpt-4o", max_tokens: int = 1500) -> str:
    """
    Implementation for query_chatgpt tool.
    Called when code execution invokes this tool.

    Note: For GEO testing, we simulate ChatGPT Plus with web search enabled by
    instructing the model to provide current information as users would see.
    """
    import openai

    client = openai.AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    # System message to simulate web search behavior for GEO testing
    system_message = {
        "role": "system",
        "content": (
            "You are ChatGPT with web search enabled. Provide current, accurate information "
            "as if you have access to recent web content. When answering questions about "
            "products, services, or companies, cite specific sources and URLs when relevant. "
            "Respond as users with ChatGPT Plus (search enabled) would see."
        )
    }

    response = await client.chat.completions.create(
        model=model,
        messages=[system_message, {"role": "user", "content": prompt}],
        max_tokens=max_tokens,
        temperature=0.7
    )

    return response.choices[0].message.content


async def handle_query_perplexity(prompt: str, model: str = "sonar-pro") -> str:
    """
    Implementation for query_perplexity tool.
    Called when code execution invokes this tool.

    Uses Perplexity's latest online search models which actively search the web.
    Critical for GEO testing as it shows real-time brand visibility in search results.
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
                "messages": [{"role": "user", "content": prompt}],
                # Ensure we get citations for GEO testing
                "return_citations": True,
                "return_images": False,
                "temperature": 0.2  # Lower temp for more consistent results
            },
            timeout=45.0  # Longer timeout for web search
        )

        result = response.json()

        # Return JSON string with response and citations
        return json.dumps({
            "response": result["choices"][0]["message"]["content"],
            "citations": result.get("citations", []),
            "web_results": result.get("web_results", [])  # Additional search metadata
        })


async def handle_query_gemini(prompt: str, model: str = "gemini-2.0-flash-exp", enable_search_grounding: bool = True) -> str:
    """
    Implementation for query_gemini tool.
    Called when code execution invokes this tool.

    Enables Google Search grounding for real-time web search capabilities.
    Critical for GEO testing as it shows brand visibility when Gemini searches Google.
    """
    import google.generativeai as genai
    import json

    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

    # Configure tools for search grounding if enabled
    tools = None
    if enable_search_grounding:
        tools = [genai.Tool(google_search=genai.GoogleSearch())]

    model_instance = genai.GenerativeModel(
        model,
        tools=tools if enable_search_grounding else None
    )

    response = await model_instance.generate_content_async(
        prompt,
        generation_config=genai.GenerationConfig(
            temperature=0.7,
            max_output_tokens=1500
        )
    )

    # Extract grounding metadata (sources) if available
    grounding_metadata = {}
    if hasattr(response, 'grounding_metadata') and response.grounding_metadata:
        grounding_metadata = {
            "search_queries": getattr(response.grounding_metadata, 'search_queries', []),
            "grounding_chunks": [
                {
                    "web": {
                        "uri": chunk.web.uri if hasattr(chunk, 'web') else None,
                        "title": chunk.web.title if hasattr(chunk, 'web') else None
                    }
                }
                for chunk in getattr(response.grounding_metadata, 'grounding_chunks', [])
            ]
        }

    # Return JSON with response and grounding metadata
    return json.dumps({
        "response": response.text,
        "grounding_metadata": grounding_metadata,
        "citations": [
            chunk.get("web", {}).get("uri")
            for chunk in grounding_metadata.get("grounding_chunks", [])
            if chunk.get("web", {}).get("uri")
        ] if grounding_metadata else []
    })


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
