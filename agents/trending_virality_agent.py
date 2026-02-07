from utils.tavily_client import search_tavily


def trending_virality_agent(adapted_content, platform):
    """
    Trend & Virality Agent using Tavily as a real-world data source.
    No LLM dependency. Fully deterministic scoring.
    """

    if not adapted_content or not adapted_content.strip():
        return {
            "agent": "Trending & Virality Agent",
            "trend_score": 0,
            "vote": "warn",
            "suggested_hooks": [],
            "explanation": "No content provided for trend analysis"
        }

    # 🔍 Query Tavily with topic + platform
    query = f"{platform} trends {adapted_content}"

    try:
        results = search_tavily(query)

    except Exception:
        return {
            "agent": "Trending & Virality Agent",
            "trend_score": 30,
            "vote": "warn",
            "suggested_hooks": [],
            "explanation": "Tavily unavailable; conservative fallback used"
        }

    if not results:
        return {
            "agent": "Trending & Virality Agent",
            "trend_score": 30,
            "vote": "warn",
            "suggested_hooks": [],
            "explanation": "No recent trend signals found"
        }

    # -------- SCORING LOGIC --------
    trend_score = min(80, 30 + len(results) * 10)

    vote = "approve" if trend_score >= 60 else "warn"

    # -------- SUGGESTED HOOKS (FROM TITLES) --------
    suggested_hooks = []
    for r in results[:3]:
        title = r.get("title", "")
        if title:
            suggested_hooks.append(title[:60])

    return {
        "agent": "Trending & Virality Agent",
        "trend_score": trend_score,
        "vote": vote,
        "suggested_hooks": suggested_hooks,
        "sources": [r.get("url") for r in results],
        "explanation": "Trend score derived from Tavily search signals"
    }
