import os
from dotenv import load_dotenv
import phi
import openai

from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from phi.playground import Playground, serve_playground_app
from fastapi.middleware.cors import CORSMiddleware

# 📈 Import the custom stock chart tool
from plotting_tool import plot_stock_chart

# 🔐 Load environment variables
load_dotenv()

# Set API keys
phi.api.api_key = os.getenv("PHI_API_KEY")
openai.api_key = os.getenv("OPENAI_API_KEY")
groq_api_key = os.getenv("GROQ_API_KEY")

print("✅ PHI API Key:", "Found" if phi.api.api_key else "❌ Missing")
print("✅ GROQ API Key:", "Found" if groq_api_key else "❌ Missing")

# 🧠 Define Groq model
groq_model = Groq(id="llama3-70b-8192", api_key=groq_api_key, max_tokens=2000)

# 🌐 Web Search Agent
web_search_agent = Agent(
    name="Web Search Agent",
    role="Search the web for relevant information",
    model=groq_model,
    tools=[DuckDuckGo()],
    instructions=[
        "Always include sources in your response.",
        "Do not use financial tools.",
    ],
    show_tool_calls=True,
    markdown=True,
    memory_messages_limit=5,
)

# 💼 Financial Agent
finance_agent = Agent(
    name="Finance AI Agent",
    role="Provides financial insights, analyst recommendations, and stock charting.",
    model=groq_model,
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            stock_fundamentals=True,
            company_news=True
        ),
        plot_stock_chart
    ],
    instructions=[
        "Use financial tools only when a valid stock symbol is provided.",
        "Space out tool calls; avoid calling multiple tools at once.",
        "Use tables for presenting data. Include charts when asked.",
        "Cite your sources properly."
    ],
    show_tool_calls=True,
    markdown=True,
    memory_messages_limit=5,
)

# 🤖 Multi AI Agent
multi_ai_agent = Agent(
    name="Multi AI Agent",
    team=[web_search_agent, finance_agent],
    instructions=[
        "Use finance tools carefully based on the question.",
        "Space out tool calls sequentially.",
        "Prefer clean tables, sources, and charts when relevant.",
        "Handle missing symbols gracefully."
    ],
    show_tool_calls=True,
    markdown=True,
    memory_messages_limit=5,
)

# 🚀 Playground App (✅ added memory_messages_limit=5)
app = Playground(
    agents=[finance_agent, web_search_agent, multi_ai_agent],
).get_app()

# 🌍 CORS Middleware for browser compatibility
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🧩 Launch server
if __name__ == "__main__":
    serve_playground_app("playground:app", port=1114, reload=True)
