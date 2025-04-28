# Finance AI Agent - Powered by Phidata Playground

This project is a fully agentic financial assistant that can:

- Fetch real-time stock prices
- Display stock fundamentals
- Summarize analyst recommendations
- Show the latest company news
- Plot real-time stock price charts

Built using:
- [Phidata](https://github.com/benjaminegger/phidata)
- [Groq API](https://groq.com/)
- [Plotly](https://plotly.com/)
- [Yahoo Finance API](https://finance.yahoo.com/)

## 🚀 Setup Instructions

1. Clone the repository:

```bash
git clone https://github.com/yourusername/AgentAI.git
cd AgentAI
```

2. Create and activate a virtual environment:

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

4. Create a .env file in the root folder:

```bash
OPENAI_API_KEY=your-openai-key
PHI_API_KEY=your-phidata-key
GROQ_API_KEY=your-groq-key
```

5. Run the app:

```bash
python playground.py
```

Visit the Playground URL shown in the console.
https://www.phidata.app/playground/chat


Sample Queries You Can Try
"Show me Tesla's stock chart over the past 6 months."

"Get Apple's latest news."

"Summarize analyst recommendations for NVIDIA."

"Compare Microsoft and Amazon fundamentals."

