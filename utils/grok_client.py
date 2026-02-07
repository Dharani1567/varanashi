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
        # ✅ SAFEST MODEL
        "model": "grok-2-latest",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.2
    }

    response = requests.post(
        GROK_API_URL,
        headers=headers,
        json=payload,
        timeout=20
    )

    # 🔍 SHOW REAL ERROR IF ANY
    if response.status_code != 200:
        raise RuntimeError(
            f"Grok API error {response.status_code}: {response.text}"
        )

    data = response.json()

    # 🔒 Defensive parsing
    if "choices" not in data or not data["choices"]:
        raise RuntimeError(f"Invalid Grok response: {data}")

    return data["choices"][0]["message"]["content"]
