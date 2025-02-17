import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
import json
import os

# Mock user authentication (replace with real user identification)
def get_user_id():
    return st.text_input("Enter User ID (e.g., user1, user2)").strip()

# File to store session data
DATA_DIR = "user_data"
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

def get_data_file(user_id):
    return os.path.join(DATA_DIR, f"{user_id}_trading_data.json")

def save_data(user_id):
    """Save session data to a JSON file."""
    data = {
        "funds": st.session_state.funds,
        "portfolio": st.session_state.portfolio,
        "transactions": st.session_state.transactions
    }
    with open(get_data_file(user_id), "w") as f:
        json.dump(data, f)

def load_data(user_id):
    """Load session data from a JSON file if it exists."""
    data_file = get_data_file(user_id)
    if os.path.exists(data_file):
        with open(data_file, "r") as f:
            data = json.load(f)
            st.session_state.funds = data.get("funds", 100000)
            st.session_state.portfolio = data.get("portfolio", {})
            st.session_state.transactions = data.get("transactions", [])
    else:
        st.session_state.funds = 100000
        st.session_state.portfolio = {}
        st.session_state.transactions = []

# Get user ID
user_id = get_user_id()
if user_id:
    # Initialize session state
    if "funds" not in st.session_state:
        load_data(user_id)

    st.set_page_config(page_title="Virtual Trading Platform", layout="wide")

    # Sidebar: Display funds
    st.sidebar.markdown(
        f"""
        <div style="border-radius: 10px; padding: 20px; background: #2c3e50; color: white; text-align: center; font-size: 18px; font-weight: bold;">
            💰 Your Funds: ₹{st.session_state.funds:,.2f}
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Tabs for Trading and Portfolio
    tab1, tab2, tab3 = st.tabs(["Trading", "Portfolio", "Transaction History"])

    with tab1:
        st.markdown(
            """
            <div style="border-radius: 15px; padding: 15px; background: linear-gradient(to right, #8e44ad, #e67e22); text-align: center; color: white; font-size: 24px; font-weight: bold;">
                Virtual Trading Platform
            </div>
            """,
            unsafe_allow_html=True,
        )

        ticker = st.text_input("Enter Stock Symbol (e.g., AAPL, TSLA, RELIANCE.NS)").upper()

        if ticker:
            try:
                stock = yf.Ticker(ticker)
                stock_data = stock.history(period="1mo")

                if not stock_data.empty:
                    stock_price = stock_data["Close"].iloc[-1]
                    st.metric(label=f"📉 {ticker} Current Price", value=f"₹{stock_price:.2f}")

                    # Stock Price Graph
                    fig = go.Figure()
                    fig.add_trace(go.Scatter(x=stock_data.index, y=stock_data['Close'], mode='lines', name='Close Price'))
                    fig.update_layout(title=f"{ticker} Price Trend", xaxis_title="Date", yaxis_title="Price", template="plotly_dark")
                    st.plotly_chart(fig)

                    # Buy & Sell section
                    col1, col2 = st.columns(2)

                    with col1:
                        quantity_buy = st.number_input(f"Buy {ticker} Quantity", min_value=1, value=1, step=1)
                        if st.button("🔵 Buy Stock", use_container_width=True):
                            total_cost = stock_price * quantity_buy
                            if st.session_state.funds >= total_cost:
                                st.session_state.funds -= total_cost
                                st.session_state.portfolio[ticker] = {
                                    "quantity": st.session_state.portfolio.get(ticker, {}).get("quantity", 0) + quantity_buy,
                                    "avg_price": stock_price,
                                    "total_spent": total_cost
                                }
                                st.session_state.transactions.append({"Stock": ticker, "Type": "Buy", "Quantity": quantity_buy, "Price": stock_price, "Total": total_cost})
                                save_data(user_id)
                                st.success(f"✅ Bought {quantity_buy} shares of {ticker} at ₹{stock_price:.2f}")
                            else:
                                st.error("❌ Insufficient funds!")

                    with col2:
                        quantity_sell = st.number_input(f"Sell {ticker} Quantity", min_value=1, value=1, step=1)
                        if st.button("🔴 Sell Stock", use_container_width=True):
                            if ticker in st.session_state.portfolio and st.session_state.portfolio[ticker]["quantity"] >= quantity_sell:
                                total_sell_value = stock_price * quantity_sell
                                st.session_state.funds += total_sell_value
                                st.session_state.portfolio[ticker]["quantity"] -= quantity_sell
                                if st.session_state.portfolio[ticker]["quantity"] == 0:
                                    del st.session_state.portfolio[ticker]
                                st.session_state.transactions.append({"Stock": ticker, "Type": "Sell", "Quantity": quantity_sell, "Price": stock_price, "Total": total_sell_value})
                                save_data(user_id)
                                st.success(f"✅ Sold {quantity_sell} shares of {ticker} at ₹{stock_price:.2f}")
                            else:
                                st.error("❌ Not enough shares to sell!")

            except Exception:
                st.warning("⚠️ Unable to fetch stock data. Please check the symbol and try again.")

    with tab2:
        st.subheader("📊 Portfolio Overview")
        if st.session_state.portfolio:
            df_portfolio = pd.DataFrame([{"Stock": stock, "Quantity": data["quantity"], "Avg Price": f"₹{data['avg_price']:.2f}"} for stock, data in st.session_state.portfolio.items()])
            st.table(df_portfolio)
        else:
            st.info("Your portfolio is empty. Start trading!")

    with tab3:
        st.subheader("📜 Transaction History")
        if st.session_state.transactions:
            df_transactions = pd.DataFrame(st.session_state.transactions)
            st.table(df_transactions)
        else:
            st.info("No transactions recorded yet.")
