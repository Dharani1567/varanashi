import os
from utils.grok_client import call_grok


def platform_adapter_agent(draft_content, platform):
    """
    Adapts content tone for a specific platform using Grok.
    Fully safe: no CrewAI, no Gemini, deterministic fallback.
    """

    if not draft_content or not draft_content.strip():
        return {
            "agent": "Platform Adapter Agent",
            "adapted_content": "",
            "explanation": "No draft content provided"
        }

    # ---------- FALLBACK (NO GROK KEY) ----------
    if not os.getenv("GROK_API_KEY"):
        if platform == "LinkedIn":
            adapted = draft_content
        elif platform == "Instagram":
            adapted = draft_content + " #insights"
        else:  # Twitter / X
            adapted = draft_content[:280]

        return {
            "agent": "Platform Adapter Agent",
            "adapted_content": adapted,
            "explanation": "Rule-based fallback used (no Grok API key)"
        }

    prompt = (
        f"Rewrite the following post for {platform}.\n"
        "Rules:\n"
        "- Preserve original meaning\n"
        "- Adjust tone for the platform\n"
        "- No hate, sarcasm, or exaggeration\n"
        "- No emojis unless platform is Instagram\n"
        "- Keep it concise\n\n"
        f"Post:\n{draft_content}"
    )

    try:
        adapted_content = call_grok(prompt)

        return {
            "agent": "Platform Adapter Agent",
            "adapted_content": adapted_content.strip(),
            "explanation": f"Content adapted for {platform} using Grok"
        }

    except Exception:
        # ---------- SAFE FALLBACK ----------
        return {
            "agent": "Platform Adapter Agent",
            "adapted_content": draft_content,
            "explanation": "Fallback used after Grok failure"
        }
