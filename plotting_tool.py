from phi.tools import tool
import plotly.graph_objs as go
import yfinance as yf
import base64
from io import BytesIO

@tool
def plot_stock_chart(symbol: str, period: str = "6mo") -> str:
    """
    Plot the stock price chart for a given company symbol over the specified period.
    
    Args:
        symbol (str): Stock ticker symbol (e.g., 'AAPL', 'TSLA')
        period (str): Historical period (e.g., '1mo', '3mo', '6mo', '1y', '2y', '5y')
    
    Returns:
        str: A markdown image link that displays the stock chart.
    """
    # Fetch historical stock data
    ticker = yf.Ticker(symbol)
    hist = ticker.history(period=period)

    if hist.empty:
        return f"❌ Could not fetch historical stock data for `{symbol}`."

    # Create a line chart
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=hist.index,
        y=hist['Close'],
        mode='lines',
        name='Close Price'
    ))
    fig.update_layout(
        title=f"{symbol} Stock Price over {period}",
        xaxis_title='Date',
        yaxis_title='Stock Price (USD)',
        template="plotly_white"
    )

    # Save plot to a buffer in PNG format
    buffer = BytesIO()
    fig.write_image(buffer, format="png")
    buffer.seek(0)

    # Encode image to base64
    img_base64 = base64.b64encode(buffer.read()).decode('utf-8')

    # Return as markdown image that Playground can render
    return f"![{symbol} Stock Chart](data:image/png;base64,{img_base64})"
