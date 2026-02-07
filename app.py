import streamlit as st

from agents.content_creator import content_creator_agent
from agents.platform_adapter import platform_adapter_agent
from agents.context_sarcasm_agent import context_sarcasm_agent
from agents.trending_virality_agent import trending_virality_agent
from agents.engagement_agent import engagement_agent
from agents.safety_policy_agent import safety_policy_agent
from agents.timing_intelligence_agent import timing_intelligence_agent
from agents.decision_agent import decision_agent


st.set_page_config(page_title="Multi-Agent Social Media Manager", layout="centered")

st.title("🤖 Multi-Agent AI Social Media Manager")
st.write("Responsible, explainable, refusal-first automation")

# ---------------- USER INPUT ----------------
topic = st.text_input("Enter a post topic")
platform = st.selectbox("Select Platform", ["LinkedIn", "Instagram", "Twitter"])

if st.button("Run Agents") and topic:

    # ---------------- AGENT FLOW ----------------
    content = content_creator_agent(topic)
    adapted = platform_adapter_agent(content["draft"], platform)

    context = context_sarcasm_agent(adapted["adapted_content"])
    trending = trending_virality_agent(adapted["adapted_content"], platform)
    engagement = engagement_agent(adapted["adapted_content"])
    safety = safety_policy_agent(adapted["adapted_content"])
    timing = timing_intelligence_agent(platform)

    decision = decision_agent(
        adapted["adapted_content"],
        engagement,
        safety,
        context,
        trending,
        timing
    )

    # ---------------- DISPLAY ----------------
    st.subheader("🧠 Agent Outputs")

    st.write("### Content Creator Agent")
    st.write(content)

    st.write("### Platform Adapter Agent")
    st.write(adapted)

    st.write("### Context & Sarcasm Agent")
    st.write(context)

    st.write("### Trending & Virality Agent")
    st.write(trending)

    st.write("### Engagement Agent")
    st.write(engagement)

    st.write("### Safety & Policy Agent")
    st.write(safety)

    st.write("### Timing Intelligence Agent")
    st.write(timing)

    st.subheader("🚦 Final Decision")
    st.success(decision["final_decision"].upper())
    st.write(decision["explanation"])

else:
    st.info("Enter a topic and click 'Run Agents'")
