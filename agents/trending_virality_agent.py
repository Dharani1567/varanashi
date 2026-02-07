from crewai import Agent, Task, Crew
from langchain_google_genai import ChatGoogleGenerativeAI
from datetime import datetime, timedelta


def trending_virality_agent(adapted_content, platform):
    """
    Uses an LLM to estimate trend relevance and virality signals.
    Decisions remain rule-based; this agent provides a signal only.
    """

    if not adapted_content:
        return {
            "agent": "Trending & Virality Agent",
            "trend_score": 0,
            "vote": "warn",
            "suggested_hooks": [],
            "explanation": "No content provided for trend analysis"
        }

    llm = ChatGoogleGenerativeAI(
        model="gemini-pro",
        temperature=0.3
    )

    agent = Agent(
        role="Trend & Virality Analyst",
        goal="Estimate how aligned the content is with current platform trends",
        backstory=(
            "You analyze internet-wide patterns to estimate what is trending "
            "on different social platforms without claiming real-time accuracy."
        ),
        llm=llm,
        verbose=False
    )

    task = Task(
        description=(
            f"Analyze the following post for trend relevance on {platform}:\n\n"
            f"'{adapted_content}'\n\n"
            "Return ONLY a JSON object with:\n"
            "{\n"
            '  "trend_level": "LOW | MEDIUM | HIGH",\n'
            '  "suggested_hooks": ["hook1", "hook2"]\n'
            "}\n"
            "Rules:\n"
            "- Hooks must be short phrases\n"
            "- Do not invent real-time claims\n"
            "- Be conservative\n"
        ),
        expected_output='JSON with trend_level and suggested_hooks.'
    )

    crew = Crew(
        agents=[agent],
        tasks=[task]
    )

    raw = crew.kickoff().strip()

    # --- Safe parsing (simple & defensive) ---
    trend_level = "LOW"
    suggested_hooks = []

    if "HIGH" in raw:
        trend_level = "HIGH"
    elif "MEDIUM" in raw:
        trend_level = "MEDIUM"

    if "[" in raw and "]" in raw:
        try:
            hooks_part = raw.split("[", 1)[1].split("]", 1)[0]
            suggested_hooks = [
                h.strip().strip('"').strip("'")
                for h in hooks_part.split(",")
                if h.strip()
            ]
        except Exception:
            suggested_hooks = []

    # --- Convert signal → deterministic score & vote ---
    if trend_level == "HIGH":
        trend_score = 80
        vote = "approve"
        explanation = "Strong alignment with current trends"
    elif trend_level == "MEDIUM":
        trend_score = 55
        vote = "warn"
        explanation = "Moderate trend alignment; relevance may be limited"
    else:
        trend_score = 25
        vote = "warn"
        explanation = "Low trend relevance detected"

    return {
        "agent": "Trending & Virality Agent",
        "trend_score": trend_score,
        "vote": vote,
        "suggested_hooks": suggested_hooks[:3],
        "explanation": explanation
    }
