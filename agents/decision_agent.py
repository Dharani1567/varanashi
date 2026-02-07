def decision_agent(
    engagement,
    safety,
    context,
    trending,
    timing
):
    """
    Final decision-making agent.
    Applies strict, deterministic rules to decide:
    APPROVE / WARN / REFUSE
    """

    explanations = []

    # 1️⃣ SAFETY VETO — ABSOLUTE RULE
    if safety.get("veto", False):
        return {
            "agent": "Decision Agent",
            "final_decision": "refuse",
            "explanation": "Refused due to safety or policy violation"
        }

    # 2️⃣ COLLECT VOTES & CONFIDENCE
    agents = [engagement, safety, context, trending, timing]

    votes = [a.get("vote", "warn") for a in agents]

    approve_count = votes.count("approve")
    warn_count = votes.count("warn")
    refuse_count = votes.count("refuse")

    # 3️⃣ ANY REFUSE VOTE → REFUSE
    if refuse_count > 0:
        return {
            "agent": "Decision Agent",
            "final_decision": "refuse",
            "explanation": "At least one agent identified high risk or ambiguity"
        }

    # 4️⃣ LOW CONFIDENCE CHECK
    for a in agents:
        confidence = a.get("confidence")
        if confidence is not None and confidence < 40:
            return {
                "agent": "Decision Agent",
                "final_decision": "refuse",
                "explanation": "Refused due to low confidence from one or more agents"
            }

    # 5️⃣ AGREEMENT THRESHOLD
    agreement_ratio = approve_count / len(agents)

    if agreement_ratio < 0.6:
        return {
            "agent": "Decision Agent",
            "final_decision": "refuse",
            "explanation": "Insufficient agreement among agents"
        }

    # 6️⃣ ENGAGEMENT VS RISK CHECK
    engagement_score = engagement.get("engagement_score", 0)
    risk_score = safety.get("risk_score", 0)

    if engagement_score - risk_score < 20:
        return {
            "agent": "Decision Agent",
            "final_decision": "warn",
            "explanation": "Engagement does not sufficiently outweigh potential risk"
        }

    # 7️⃣ DEFAULT SAFE APPROVAL
    return {
        "agent": "Decision Agent",
        "final_decision": "approve",
        "explanation": "All checks passed with sufficient agreement and confidence"
    }
