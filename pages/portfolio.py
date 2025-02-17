import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px

# Set up Portfolio Page
st.set_page_config(page_title="📈 Portfolio Overview", layout="wide")

# Initialize session state for portfolio & funds
if "funds" not in st.session_state:
    st.session_state.funds = 100000  # Default initial funds
if "portfolio" not in st.session_state:
    st.session_state.portfolio = {}  # Dictionary to track stocks

st.title("📊 Portfolio Overview")
st.markdown("A professional dashboard to track your investments in real-time, similar to Zerodha & Angel One.")

# If portfolio is empty, show message
if not st.session_state.portfolio:
    st.warning("Your portfolio is empty. Start investing to see details here!")
else:
    # Prepare Data for Portfolio Table
    portfolio_data = []
    total_invested = 0
    total_current_value = 0

    for ticker, data in st.session_state.portfolio.items():
        stock = yf.Ticker(ticker)
        stock_data = stock.history(period="1d")
        current_price = stock_data["Close"].iloc[-1] if not stock_data.empty else data["avg_price"]
        current_value = data["quantity"] * current_price
        profit_loss = current_value - data["total_spent"]
        growth = (profit_loss / data["total_spent"] * 100) if data["total_spent"] > 0 else 0

        portfolio_data.append({
            "Stock": ticker,
            "Quantity": data["quantity"],
            "Avg Price": f"₹{data['avg_price']:.2f}",
            "Total Spent": f"₹{data['total_spent']:.2f}",
            "Current Price": f"₹{current_price:.2f}",
            "Current Value": f"₹{current_value:.2f}",
            "P/L": f"₹{profit_loss:.2f}",
            "Growth %": f"{growth:.2f}%"
        })

        total_invested += data["total_spent"]
        total_current_value += current_value

    # Portfolio Table
    df_portfolio = pd.DataFrame(portfolio_data)
    st.dataframe(df_portfolio, height=400, use_container_width=True)
    
    # Display Portfolio Summary
    col1, col2, col3 = st.columns(3)
    col1.metric("💰 Total Invested", f"₹{total_invested:.2f}")
    col2.metric("📈 Current Value", f"₹{total_current_value:.2f}")
    col3.metric("📊 Net P/L", f"₹{(total_current_value - total_invested):.2f}", 
                delta=(total_current_value - total_invested), delta_color="normal")

    # Pie Chart: Portfolio Distribution
    fig_pie = px.pie(df_portfolio, names="Stock", values=[float(x[1:].replace(',', '')) for x in df_portfolio["Current Value"]], 
                      title="Portfolio Distribution", hole=0.3, color_discrete_sequence=px.colors.sequential.RdBu)
    st.plotly_chart(fig_pie, use_container_width=True)
    
    # Line Chart: Portfolio Performance Over Time
    st.subheader("📉 Stock Price Movement")
    stock_selected = st.selectbox("Select a stock to view price trends", [stock for stock in st.session_state.portfolio.keys()])
    if stock_selected:
        stock = yf.Ticker(stock_selected)
        stock_hist = stock.history(period="1mo")
        if not stock_hist.empty:
            fig_line = px.line(stock_hist, x=stock_hist.index, y="Close", title=f"{stock_selected} Price Movement")
            st.plotly_chart(fig_line, use_container_width=True)
        else:
            st.error("No price data available for this stock.")
