def engagement_agent(adapted_content):
    """
    Estimates engagement potential of a post.
    Rule-based and deterministic.
    """

    if not adapted_content or not adapted_content.strip():
        return {
            "agent": "Engagement Agent",
            "engagement_score": 0,
            "vote": "warn",
            "explanation": "No content provided to evaluate engagement"
        }

    score = 40  # base score
    text = adapted_content.lower()

    # Engagement boosters
    if "?" in text:
        score += 15

    if len(text.split()) < 30:
        score += 10

    if any(word in text for word in ["how", "why", "what", "thoughts"]):
        score += 10

    if any(word in text for word in ["tips", "guide", "thread", "lesson"]):
        score += 10

    if "\n" in adapted_content:
        score += 5

    # Cap the score
    score = min(score, 100)

    # Decision logic
    if score >= 70:
        vote = "approve"
        explanation = "High engagement potential detected"
    else:
        vote = "warn"
        explanation = "Moderate engagement; could be improved"

    return {
        "agent": "Engagement Agent",
        "engagement_score": score,
        "vote": vote,
        "explanation": explanation
    }
