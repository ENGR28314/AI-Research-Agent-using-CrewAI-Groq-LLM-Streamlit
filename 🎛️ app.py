import streamlit as st
from agent import research_agent
from utils.search import web_search

st.title("AI Research Agent 🧠")

topic = st.text_input("Enter your research topic:")

if st.button("Generate Report"):
    if topic:
        st.write("🔍 Searching DuckDuckGo...")
        search_results = web_search(topic)

        st.write("📄 Generating Report...")
        # Combine search results into context
        context = "\n".join(search_results)

        # Ask the agent to write a report
        report = research_agent.llm.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a helpful research assistant."},
                {"role": "user", "content": f"Write a detailed research report on: {topic}\n\nUse this context:\n{context}"}
            ]
        )

        st.markdown(report.choices[0].message["content"])
    else:
        st.warning("Please enter a topic first.")
