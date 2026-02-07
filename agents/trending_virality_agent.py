import os
from utils.llm_client import call_llm


def trending_virality_agent(adapted_content, platform):
    """
    Estimates trend relevance and virality signals.
    Uses Grok for suggestion only, decision remains rule-based.
    """

    if not adapted_content or not adapted_content.strip():
        return {
            "agent": "Trending & Virality Agent",
            "trend_score": 0,
            "vote": "warn",
            "suggested_hooks": [],
            "explanation": "No content provided for trend analysis"
        }

    # ---------- FALLBACK (NO GROK KEY) ----------
    if not os.getenv("GROK_API_KEY"):
        return {
            "agent": "Trending & Virality Agent",
            "trend_score": 30,
            "vote": "warn",
            "suggested_hooks": [],
            "explanation": "Rule-based fallback used (no Grok API key)"
        }

    prompt = (
        f"You are analyzing social media trends for {platform}.\n"
        "Analyze the post below and respond with:\n"
        "- Trend Level: LOW / MEDIUM / HIGH\n"
        "- Suggested Hooks: up to 3 short phrases\n\n"
        "Rules:\n"
        "- Be conservative\n"
        "- Do NOT claim real-time data\n"
        "- Hooks must be generic phrases\n\n"
        f"Post:\n{adapted_content}"
    )

    try:
        response = call_llm(prompt).lower()

        # -------- SIMPLE PARSING --------
        if "high" in response:
            trend_level = "HIGH"
        elif "medium" in response:
            trend_level = "MEDIUM"
        else:
            trend_level = "LOW"

        # Extract hooks (very defensive)
        suggested_hooks = []
        lines = response.splitlines()
        for line in lines:
            if "-" in line and len(suggested_hooks) < 3:
                hook = line.replace("-", "").strip()
                if hook:
                    suggested_hooks.append(hook)

        # -------- MAP TO SCORE --------
        if trend_level == "HIGH":
            trend_score = 80
            vote = "approve"
            explanation = "Strong alignment with current trends"
        elif trend_level == "MEDIUM":
            trend_score = 55
            vote = "warn"
            explanation = "Moderate trend alignment"
        else:
            trend_score = 25
            vote = "warn"
            explanation = "Low trend relevance detected"

        return {
            "agent": "Trending & Virality Agent",
            "trend_score": trend_score,
            "vote": vote,
            "suggested_hooks": suggested_hooks,
            "explanation": explanation
        }

    except Exception:
        # ---------- SAFE FALLBACK ----------
        return {
            "agent": "Trending & Virality Agent",
            "trend_score": 30,
            "vote": "warn",
            "suggested_hooks": [],
            "explanation": "Fallback used after Grok failure"
        }
