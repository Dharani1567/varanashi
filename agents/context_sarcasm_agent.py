import os
from utils.llm_client import call_llm


def context_sarcasm_agent(adapted_content):
    if not adapted_content:
        return {
            "agent": "Context & Sarcasm Agent",
            "ambiguity_score": 0,
            "vote": "approve",
            "explanation": "No content to analyze"
        }

    # ---------- FALLBACK ----------
    if not os.getenv("GROK_API_KEY"):
        return {
            "agent": "Context & Sarcasm Agent",
            "ambiguity_score": 20,
            "vote": "approve",
            "explanation": "Fallback used (no Grok API key)"
        }

    prompt = (
        "Classify the following text as either 'ambiguous' or 'clear'.\n\n"
        f"{adapted_content}"
    )

    try:
        response = call_llm(prompt)
        ambiguity_score = 70 if "ambiguous" in response else 30
        vote = "warn" if ambiguity_score >= 60 else "approve"

        return {
            "agent": "Context & Sarcasm Agent",
            "ambiguity_score": ambiguity_score,
            "vote": vote,
            "explanation": "Grok-based ambiguity analysis"
        }

    except Exception:
        return {
            "agent": "Context & Sarcasm Agent",
            "ambiguity_score": 30,
            "vote": "approve",
            "explanation": "Fallback after Grok failure"
        }
