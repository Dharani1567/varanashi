from crewai import Agent, Task, Crew
from langchain_google_genai import ChatGoogleGenerativeAI


def context_sarcasm_agent(adapted_content):
    """
    Uses an LLM to detect ambiguity or sarcasm.
    This agent provides a signal only — no veto power.
    """

    if not adapted_content:
        return {
            "agent": "Context & Sarcasm Agent",
            "ambiguity_score": 0,
            "vote": "warn",
            "explanation": "No content provided for context analysis"
        }

    llm = ChatGoogleGenerativeAI(
        model="gemini-pro",
        temperature=0.2
    )

    agent = Agent(
        role="Context & Sarcasm Analyst",
        goal="Identify ambiguity, sarcasm, or unclear intent in content",
        backstory=(
            "You analyze text to detect sarcasm, irony, or ambiguous intent "
            "that could lead to misinterpretation."
        ),
        llm=llm,
        verbose=False
    )

    task = Task(
        description=(
            f"Analyze the following post for ambiguity or sarcasm:\n\n"
            f"'{adapted_content}'\n\n"
            "Respond with one of the following labels only:\n"
            "- CLEAR\n"
            "- SOMEWHAT_AMBIGUOUS\n"
            "- HIGHLY_AMBIGUOUS"
        ),
        expected_output="One label indicating clarity level."
    )

    crew = Crew(
        agents=[agent],
        tasks=[task]
    )

    result = crew.kickoff().strip()

    # Translate LLM signal → score + vote
    if result == "HIGHLY_AMBIGUOUS":
        return {
            "agent": "Context & Sarcasm Agent",
            "ambiguity_score": 80,
            "vote": "refuse",
            "explanation": "High ambiguity or sarcasm detected; intent may be misinterpreted"
        }

    elif result == "SOMEWHAT_AMBIGUOUS":
        return {
            "agent": "Context & Sarcasm Agent",
            "ambiguity_score": 50,
            "vote": "warn",
            "explanation": "Moderate ambiguity detected; clarification may be needed"
        }

    else:
        return {
            "agent": "Context & Sarcasm Agent",
            "ambiguity_score": 10,
            "vote": "approve",
            "explanation": "Content intent appears clear"
        }
