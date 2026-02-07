def safety_policy_agent(adapted_content):
    """
    Rule-based safety and policy checker with veto power.
    This agent can STOP the system from posting.
    """

    if not adapted_content:
        return {
            "agent": "Safety & Policy Agent",
            "risk_score": 0,
            "vote": "warn",
            "veto": False,
            "explanation": "No content provided for safety evaluation"
        }

    text = adapted_content.lower()
    risk_score = 10
    veto = False

    # High-risk keywords → immediate veto
    high_risk_keywords = [
        "hate", "kill", "violence", "terrorist",
        "racist", "sexist", "abuse", "harassment"
    ]

    # Medium-risk keywords → warning
    medium_risk_keywords = [
        "stupid", "idiot", "lazy", "dumb"
    ]

    for word in high_risk_keywords:
        if word in text:
            return {
                "agent": "Safety & Policy Agent",
                "risk_score": 90,
                "vote": "refuse",
                "veto": True,
                "explanation": f"High-risk policy violation detected: '{word}'"
            }

    for word in medium_risk_keywords:
        if word in text:
            return {
                "agent": "Safety & Policy Agent",
                "risk_score": 60,
                "vote": "warn",
                "veto": False,
                "explanation": f"Potentially offensive language detected: '{word}'"
            }

    return {
        "agent": "Safety & Policy Agent",
        "risk_score": risk_score,
        "vote": "approve",
        "veto": False,
        "explanation": "No safety or policy violations detected"
    }
