#!/usr/bin/env python3
import json
import os
import sys
import textwrap

def main():
    # ---- Validate token ----
    token = os.environ.get("GH_MODELS_TOKEN", "").strip()
    if not token:
        print("ERROR: GH_MODELS_TOKEN missing", file=sys.stderr)
        sys.exit(1)

    # ---- Read system prompt ----
    try:
        with open("orchestration/master-prompt.md", "r", encoding="utf-8") as f:
            system_prompt = f.read()
    except FileNotFoundError:
        print("ERROR: orchestration/master-prompt.md not readable", file=sys.stderr)
        sys.exit(1)

    # ---- Gather inputs ----
    page_type = os.environ.get("PAGE_TYPE", "").strip()
    assigned_pillar = os.environ.get("ASSIGNED_PILLAR", "").strip()
    entity_concept = os.environ.get("ENTITY_CONCEPT", "").strip()
    url_slug = os.environ.get("URL_SLUG", "").strip()

    missing = [k for k, v in [("page_type", page_type), ("assigned_pillar", assigned_pillar),
                               ("entity_concept", entity_concept), ("url_slug", url_slug)] if not v]
    if missing:
        print(f"ERROR: Missing inputs: {', '.join(missing)}", file=sys.stderr)
        sys.exit(1)

    user_message = textwrap.dedent(f"""\
        Page Type: {page_type}
        Assigned Pillar: {assigned_pillar}
        Primary Topic / Entity Concept: {entity_concept}
        Target URL Slug: {url_slug}

        Generate all 14 required deliverables per your system instructions.
    """)

    # ---- Prepare API request ----
    payload = {
        "model": "gpt-4o",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user",   "content": user_message}
        ],
        "max_tokens": 4000,
        "temperature": 0.3
    }

    api_url = "https://models.inference.ai.azure.com/chat/completions?api-version=2024-04-01-preview"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    # ---- Call API ----
    try:
        import requests
        resp = requests.post(api_url, headers=headers, json=payload, timeout=120)
        if resp.status_code != 200:
            print(f"HTTP {resp.status_code}: {resp.text}", file=sys.stderr)
            sys.exit(1)
        data = resp.json()
    except ImportError:
        import urllib.request
        import urllib.error
        req = urllib.request.Request(api_url, data=json.dumps(payload).encode("utf-8"),
                                     headers=headers, method="POST")
        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                data = json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            error_body = e.read().decode("utf-8", errors="replace")
            print(f"HTTP ERROR {e.code}: {error_body}", file=sys.stderr)
            sys.exit(1)

    if "choices" not in data or not data["choices"]:
        print(f"UNEXPECTED API RESPONSE: {json.dumps(data, indent=2)}", file=sys.stderr)
        sys.exit(1)

    content = data["choices"][0]["message"]["content"]

    # ---- Write output ----
    run_number = os.environ.get("GITHUB_RUN_NUMBER", "unknown")
    actor = os.environ.get("GITHUB_ACTOR", "unknown")

    header = f"""---
# Outline Agent Output
**Run:** {run_number}
**Branch:** outline
**Triggered by:** {actor}
**Page Type:** {page_type}
**Assigned Pillar:** {assigned_pillar}
**Entity Concept:** {entity_concept}
**URL Slug:** {url_slug}
---

"""
    with open("outline-output.md", "w", encoding="utf-8") as f:
        f.write(header + content)

    print(f"Success: output written to outline-output.md")
    sys.exit(0)

if __name__ == "__main__":
    main()
