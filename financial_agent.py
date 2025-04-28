from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
import openai
import os

# Load environment variables from .env
load_dotenv()

# Load API Keys
openai.api_key = os.getenv("OPENAI_API_KEY")
groq_api_key = os.getenv("GROQ_API_KEY")

# Debugging: print status
print("✅ GROQ API Key:", "Found" if groq_api_key else "Missing ❌")

# Define Groq model with correct model ID
groq_model = Groq(id="llama3-70b-8192", api_key=groq_api_key)

# Web Search Agent
web_search_agent = Agent(
    name="Web Search Agent",
    role="Search the web for recent information",
    model=groq_model,
    tools=[DuckDuckGo()],
    instructions=["Always include sources."],
    show_tool_calls=True,
    markdown=True,
)

# Finance Agent
finance_agent = Agent(
    name="Finance AI Agent",
    role="Provide financial analysis and news summaries.",
    model=groq_model,
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            stock_fundamentals=True,
            company_news=True
        )
    ],
    instructions=["Use tables for data. Always include sources."],
    show_tool_calls=True,
    markdown=True,
)

# Multi-agent combining both
multi_ai_agent = Agent(
    name="Multi AI Agent",
    team=[web_search_agent, finance_agent],
    instructions=[
        "Use financial tools and web search when needed.",
        "Combine insights. Use tables and cite sources."
    ],
    show_tool_calls=True,
    markdown=True,
)

# Run test query
multi_ai_agent.print_response(
    "Summarize analyst recommendation and share the latest news for NVDA",
    stream=True
)
