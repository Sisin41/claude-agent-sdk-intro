#!/usr/bin/env python3
"""
Batch query multiple AI engines in parallel.

Usage:
    python3 batch-query.py --prompts prompts.json --engines chatgpt,perplexity,gemini --output results.json

Input (prompts.json):
    [
        {"id": "p1", "text": "What are the best project management tools?"},
        {"id": "p2", "text": "Compare Asana vs Monday.com"}
    ]

Output (results.json):
    [
        {"prompt_id": "p1", "engine": "chatgpt", "response": "...", "citations": []},
        {"prompt_id": "p1", "engine": "perplexity", "response": "...", "citations": ["url1", "url2"]},
        ...
    ]

Requires: OPENAI_API_KEY, PERPLEXITY_API_KEY, GEMINI_API_KEY as needed.
"""

import argparse
import asyncio
import json
import os
import sys
import time
from pathlib import Path

try:
    import httpx
    HAS_HTTPX = True
except ImportError:
    HAS_HTTPX = False

# Fallback to subprocess curl if httpx not available
import subprocess


def query_chatgpt_sync(prompt: str, model: str = "gpt-4o", max_tokens: int = 1500) -> dict:
    """Query ChatGPT via curl subprocess."""
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        return {"error": "OPENAI_API_KEY not set"}

    payload = json.dumps({
        "model": model,
        "max_tokens": max_tokens,
        "messages": [{"role": "user", "content": prompt}]
    })

    result = subprocess.run(
        ["curl", "-s", "https://api.openai.com/v1/chat/completions",
         "-H", f"Authorization: Bearer {api_key}",
         "-H", "Content-Type: application/json",
         "--max-time", "30",
         "-d", payload],
        capture_output=True, text=True
    )

    try:
        data = json.loads(result.stdout)
        content = data.get("choices", [{}])[0].get("message", {}).get("content", "")
        return {"response": content, "citations": [], "raw": data}
    except (json.JSONDecodeError, IndexError):
        return {"error": result.stdout or result.stderr}


def query_perplexity_sync(prompt: str, model: str = "sonar-pro") -> dict:
    """Query Perplexity via curl subprocess."""
    api_key = os.environ.get("PERPLEXITY_API_KEY")
    if not api_key:
        return {"error": "PERPLEXITY_API_KEY not set"}

    payload = json.dumps({
        "model": model,
        "messages": [{"role": "user", "content": prompt}]
    })

    result = subprocess.run(
        ["curl", "-s", "https://api.perplexity.ai/chat/completions",
         "-H", f"Authorization: Bearer {api_key}",
         "-H", "Content-Type: application/json",
         "--max-time", "30",
         "-d", payload],
        capture_output=True, text=True
    )

    try:
        data = json.loads(result.stdout)
        content = data.get("choices", [{}])[0].get("message", {}).get("content", "")
        citations = data.get("citations", [])
        return {"response": content, "citations": citations, "raw": data}
    except (json.JSONDecodeError, IndexError):
        return {"error": result.stdout or result.stderr}


def query_gemini_sync(prompt: str, model: str = "gemini-2.0-flash") -> dict:
    """Query Gemini via curl subprocess."""
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        return {"error": "GEMINI_API_KEY not set"}

    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
    payload = json.dumps({
        "contents": [{"parts": [{"text": prompt}]}],
        "tools": [{"google_search": {}}]
    })

    result = subprocess.run(
        ["curl", "-s", url,
         "-H", "Content-Type: application/json",
         "--max-time", "30",
         "-d", payload],
        capture_output=True, text=True
    )

    try:
        data = json.loads(result.stdout)
        parts = data.get("candidates", [{}])[0].get("content", {}).get("parts", [])
        content = " ".join(p.get("text", "") for p in parts if "text" in p)
        # Extract grounding citations if present
        grounding = data.get("candidates", [{}])[0].get("groundingMetadata", {})
        citations = [c.get("uri", "") for c in grounding.get("groundingChunks", []) if "uri" in c]
        return {"response": content, "citations": citations, "raw": data}
    except (json.JSONDecodeError, IndexError, KeyError):
        return {"error": result.stdout or result.stderr}


ENGINE_MAP = {
    "chatgpt": query_chatgpt_sync,
    "perplexity": query_perplexity_sync,
    "gemini": query_gemini_sync,
}


def run_batch(prompts: list, engines: list, max_concurrent: int = 10) -> list:
    """Run all prompt x engine combinations with concurrency limiting."""
    results = []
    tasks = [(p, e) for p in prompts for e in engines]
    total = len(tasks)

    for i, (prompt, engine) in enumerate(tasks):
        query_fn = ENGINE_MAP.get(engine)
        if not query_fn:
            results.append({
                "prompt_id": prompt["id"],
                "engine": engine,
                "error": f"Unknown engine: {engine}"
            })
            continue

        print(f"  [{i+1}/{total}] {engine}: {prompt['id']}", file=sys.stderr)

        try:
            response = query_fn(prompt["text"])
            results.append({
                "prompt_id": prompt["id"],
                "prompt_text": prompt["text"],
                "engine": engine,
                "response": response.get("response", ""),
                "citations": response.get("citations", []),
                "error": response.get("error"),
                "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
            })
        except Exception as e:
            results.append({
                "prompt_id": prompt["id"],
                "engine": engine,
                "error": str(e)
            })

    return results


def main():
    parser = argparse.ArgumentParser(description="Batch query AI engines")
    parser.add_argument("--prompts", required=True, help="Path to prompts JSON file")
    parser.add_argument("--engines", default="chatgpt,perplexity,gemini",
                        help="Comma-separated engines (chatgpt,perplexity,gemini)")
    parser.add_argument("--output", required=True, help="Path to write results JSON")
    parser.add_argument("--max-concurrent", type=int, default=10,
                        help="Max concurrent requests")
    args = parser.parse_args()

    with open(args.prompts) as f:
        prompts = json.load(f)

    engines = [e.strip() for e in args.engines.split(",")]

    print(f"Running {len(prompts)} prompts x {len(engines)} engines = {len(prompts)*len(engines)} queries", file=sys.stderr)

    results = run_batch(prompts, engines, args.max_concurrent)

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(results, f, indent=2)

    print(f"Results written to {args.output}", file=sys.stderr)

    # Summary
    success = sum(1 for r in results if not r.get("error"))
    failed = sum(1 for r in results if r.get("error"))
    citations = sum(len(r.get("citations", [])) for r in results)
    print(f"Summary: {success} success, {failed} failed, {citations} total citations", file=sys.stderr)


if __name__ == "__main__":
    main()
