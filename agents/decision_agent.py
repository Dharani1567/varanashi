def decision_agent(
    engagement,
    safety,
    context,
    timing,
    trending
):
    """
    Final decision-making agent.
    Applies strict, deterministic rules to decide:
    APPROVE / WARN / REFUSE
    """

    # 1️⃣ SAFETY VETO — ABSOLUTE RULE
    if safety.get("veto", False):
        return {
            "agent": "Decision Agent",
            "final_decision": "refuse",
            "explanation": "Refused due to safety or policy violation"
        }

    agents = [engagement, safety, context, timing, trending]
    votes = [a.get("vote", "warn") for a in agents]

    approve_count = votes.count("approve")
    refuse_count = votes.count("refuse")

    # 2️⃣ ANY REFUSE → REFUSE
    if refuse_count > 0:
        return {
            "agent": "Decision Agent",
            "final_decision": "refuse",
            "explanation": "At least one agent identified high risk or ambiguity"
        }

    # 3️⃣ AGREEMENT THRESHOLD
    agreement_ratio = approve_count / len(agents)
    if agreement_ratio < 0.6:
        return {
            "agent": "Decision Agent",
            "final_decision": "refuse",
            "explanation": "Insufficient agreement among agents"
        }

    # 4️⃣ ENGAGEMENT VS RISK
    engagement_score = engagement.get("engagement_score", 0)
    risk_score = safety.get("risk_score", 0)

    if engagement_score - risk_score < 20:
        return {
            "agent": "Decision Agent",
            "final_decision": "warn",
            "explanation": "Engagement does not sufficiently outweigh potential risk"
        }

    # 5️⃣ DEFAULT SAFE APPROVAL
    return {
        "agent": "Decision Agent",
        "final_decision": "approve",
        "explanation": "All checks passed with sufficient agreement"
    }
