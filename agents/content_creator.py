from crewai import Agent, Task, Crew
from langchain_google_genai import ChatGoogleGenerativeAI
from utils.api_guard import safe_llm_call


def content_creator_agent(topic):
    """
    LLM-based content creator with safe fallback.
    """

    def llm_logic():
        llm = ChatGoogleGenerativeAI(
            model="gemini-pro",
            temperature=0.6
        )

        agent = Agent(
            role="Content Creator Agent",
            goal="Generate neutral social media drafts",
            llm=llm
        )

        task = Task(
            description=f"Write a neutral social media post about {topic}.",
            expected_output="Short post draft."
        )

        crew = Crew(
            agents=[agent],
            tasks=[task]
        )

        return crew.kickoff().strip()

    def fallback(reason):
        return f"Here’s a thought on {topic}. Curious to hear perspectives."

    draft = safe_llm_call(llm_logic, fallback)

    return {
        "agent": "Content Creator Agent",
        "draft": draft,
        "explanation": "Draft generated using LLM with safe fallback"
    }
