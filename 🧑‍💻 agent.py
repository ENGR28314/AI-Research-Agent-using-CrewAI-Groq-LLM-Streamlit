from crewai import Agent
from groq import Groq

# Initialize Groq LLM
llm = Groq(model="openai/gpt-oss-120b")

# Define the research agent
research_agent = Agent(
    role="AI Research Agent",
    goal="Write detailed research reports on given topics",
    backstory="An AI assistant that searches the web and synthesizes information into clear reports.",
    llm=llm
)
