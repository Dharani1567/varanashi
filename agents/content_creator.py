import os
from utils.grok_client import call_grok


def content_creator_agent(topic):
    """
    Content Creator Agent using Grok with safe fallback.
    No CrewAI. No Gemini.
    """

    if not topic or not topic.strip():
        return {
            "agent": "Content Creator Agent",
            "draft": "",
            "explanation": "No topic provided"
        }

    # ---------- FALLBACK (NO API KEY) ----------
    if not os.getenv("GROK_API_KEY"):
        return {
            "agent": "Content Creator Agent",
            "draft": f"Here’s a thought on {topic}. Curious to hear perspectives.",
            "explanation": "Rule-based fallback used (no Grok API key)"
        }

    prompt = (
        "Write a neutral, professional social media post about the topic below.\n"
        "Do NOT use emojis. Keep it short and thoughtful.\n\n"
        f"Topic: {topic}"
    )

    try:
        draft = call_grok(prompt)

        return {
            "agent": "Content Creator Agent",
            "draft": draft.strip(),
            "explanation": "Draft generated using Grok"
        }

    except Exception:
        return {
            "agent": "Content Creator Agent",
            "draft": f"Here’s a thought on {topic}. Curious to hear perspectives.",
            "explanation": "Fallback used after Grok failure"
        }
