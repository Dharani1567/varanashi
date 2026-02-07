from datetime import datetime

def timing_intelligence_agent(platform):
    """
    Evaluates whether the current time is optimal for posting.
    Rule-based and deterministic.
    """

    hour = datetime.now().hour

    if platform == "LinkedIn":
        best_hours = range(9, 17)
    elif platform == "Instagram":
        best_hours = range(18, 22)
    elif platform == "Twitter":
        best_hours = range(12, 15)
    else:
        best_hours = []

    if hour in best_hours:
        return {
            "agent": "Timing & Engagement Intelligence Agent",
            "timing_score": 80,
            "vote": "approve",
            "explanation": "Current time aligns with peak engagement hours"
        }

    return {
        "agent": "Timing & Engagement Intelligence Agent",
        "timing_score": 40,
        "vote": "warn",
        "explanation": "Posting outside peak engagement hours"
    }

