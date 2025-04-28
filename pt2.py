from phi.agent import Agent #type:ignore
from phi.tools.yfinance import YFinanceTools #type:ignore
from phi.tools.duckduckgo import DuckDuckGo #type:ignore
from phi.model.openai import OpenAIChat #type:ignore


from dotenv import load_dotenv
load_dotenv('/Users/rahulsharma/Desktop/Financial Agent wiht Phidata/.env')

# web search agent 
websearch_agent = Agent(
    name="web search agent",
    role="search the web for the information",
    model=OpenAIChat(id="gpt-3.5-turbo-0125"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True
)

# financial agent 
financial_agent = Agent(
    name="finance ai agent",
    model=OpenAIChat(id="gpt-3.5-turbo-0125"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True,company_news=True)],
    instructions=["Use tables to display the data"],
    show_tool_calls=True,
    markdown=True
)

# Multi-agent setup
multi_ai_agent = Agent(
    name="Multi AI Team",
    team=[websearch_agent, financial_agent],
    model=OpenAIChat(id="gpt-3.5-turbo-0125"),
    instructions=[
        "Always include sources and citations",
        "Use tables to display structured data",
        "Combine financial data with relevant market news",
        "Provide comprehensive analysis using both agents' capabilities",
    ],
    show_tool_calls=True,
    markdown=True,
    monitoring=True,
)

multi_ai_agent.print_response("Summarize analyst recommendations and share the latest news for AAPL", stream=True)