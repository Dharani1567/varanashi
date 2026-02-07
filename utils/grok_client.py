import os
import requests

GROK_API_URL = "https://api.x.ai/v1/chat/completions"


def call_grok(prompt):
    api_key = os.getenv("GROK_API_KEY")

    if not api_key:
        raise RuntimeError("GROK_API_KEY not set")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "grok-2",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.2
    }

    response = requests.post(GROK_API_URL, headers=headers, json=payload)
    response.raise_for_status()

    return response.json()["choices"][0]["message"]["content"]
