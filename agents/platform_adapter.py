from crewai import Agent, Task, Crew
from langchain_google_genai import ChatGoogleGenerativeAI
from utils.api_guard import safe_llm_call


def platform_adapter_agent(draft_content, platform):
    """
    Uses LLM via CrewAI to adapt content tone for a specific platform.
    Includes safe fallback if API fails.
    """

    if not draft_content:
        return {
            "agent": "Platform Adapter Agent",
            "adapted_content": "",
            "explanation": "No draft content provided"
        }

    def llm_logic():
        llm = ChatGoogleGenerativeAI(
            model="gemini-pro",
            temperature=0.4
        )

        agent = Agent(
            role="Platform Adapter Agent",
            goal="Adapt content tone while preserving original meaning",
            backstory=(
                "You specialize in rewriting content to match platform norms "
                "without changing intent, facts, or sentiment."
            ),
            llm=llm,
            verbose=False
        )

        task = Task(
            description=(
                f"Rewrite the following post for {platform}:\n\n"
                f"'{draft_content}'\n\n"
                "Rules:\n"
                "- Preserve original meaning\n"
                "- Adjust tone for the platform\n"
                "- No hate, sarcasm, or exaggeration\n"
                "- No emojis unless platform is Instagram\n"
                "- Keep it concise"
            ),
            expected_output="Platform-appropriate rewritten post."
        )

        crew = Crew(
            agents=[agent],
            tasks=[task]
        )

        return crew.kickoff().strip()

    def fallback(reason):
        # safest fallback: return original content unchanged
        return draft_content

    adapted_content = safe_llm_call(llm_logic, fallback)

    return {
        "agent": "Platform Adapter Agent",
        "adapted_content": adapted_content,
        "explanation": f"Content adapted for {platform} using LLM with safe fallback"
    }
