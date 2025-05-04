import streamlit as st
import yfinance as yf
import json
import os
import pandas as pd

# File for storing watchlists persistently
WATCHLIST_FILE = "watchlists.json"

# Load existing watchlists or create a new one
if os.path.exists(WATCHLIST_FILE):
    with open(WATCHLIST_FILE, "r") as f:
        watchlists = json.load(f)
else:
    watchlists = {}

# Streamlit Page Configuration
st.set_page_config(page_title="📃 Watchlist Manager", layout="wide")

# Google-Themed Watchlist Manager Box
st.markdown(
    """
    <style>
        .google-box {
            background: linear-gradient(135deg, #4285F4, #34A853, #FBBC05, #EA4335);
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.2);
            color: white;
            text-align: center;
        }
    </style>
    <div class="google-box">
        <h1>📃 Watchlist Manager</h1>
        <p>Easily track your favorite stocks in real-time! 🚀</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Select or Create Watchlist
watchlist_names = list(watchlists.keys())
selected_watchlist = st.selectbox("📂 Choose a Watchlist:", ["Create New"] + watchlist_names)

if selected_watchlist == "Create New":
    new_watchlist_name = st.text_input("Enter Watchlist Name:")
    if st.button("➕ Create Watchlist"):
        if new_watchlist_name and new_watchlist_name not in watchlists:
            watchlists[new_watchlist_name] = []
            with open(WATCHLIST_FILE, "w") as f:
                json.dump(watchlists, f)
            st.success(f"✅ Created Watchlist: **{new_watchlist_name}**")
            st.rerun()
        else:
            st.warning("⚠️ Watchlist name is empty or already exists!")

elif selected_watchlist:
    st.subheader(f"📜 Watchlist: {selected_watchlist}")

    # Add Stock Section
    stock_symbol = st.text_input("Enter Stock Symbol (e.g., TSLA, AAPL, INFY):")
    if st.button("📥 Add Stock"):
        if stock_symbol and stock_symbol.upper() not in watchlists[selected_watchlist]:
            watchlists[selected_watchlist].append(stock_symbol.upper())
            with open(WATCHLIST_FILE, "w") as f:
                json.dump(watchlists, f)
            st.success(f"✅ {stock_symbol.upper()} added!")
            st.rerun()
        else:
            st.warning("⚠️ Stock already in watchlist or input is empty!")

    # Display Stocks in Watchlist
    if watchlists[selected_watchlist]:
        for stock in watchlists[selected_watchlist]:
            try:
                # Import the Alpha Vantage module
                import sys
                import os
                sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
                import alpha_vantage_api as av
                
                # First try with Alpha Vantage as primary source
                history = av.get_stock_data(stock, period="1d")
                
                if history.empty:
                    # Try with a different time period in Alpha Vantage
                    history = av.get_stock_data(stock, period="5d")
                    
                    # If still empty, fall back to Yahoo Finance
                    if history.empty:
                        stock_data = yf.Ticker(stock)
                        history = stock_data.history(period="1d")
                        if history.empty:
                            history = stock_data.history(period="5d")
                            if not history.empty:
                                stock_price = f"₹{history['Close'].iloc[-1]:.2f}"
                            else:
                                stock_price = "N/A"
                        else:
                            stock_price = f"₹{history['Close'].iloc[-1]:.2f}"
                    else:
                        stock_price = f"₹{history['Close'].iloc[-1]:.2f}"
                else:
                    stock_price = f"₹{history['Close'].iloc[-1]:.2f}"

                col1, col2, col3, col4 = st.columns([2, 1, 1, 1])

                with col1:
                    st.write(f"**{stock}**")

                with col2:
                    st.write(stock_price)

                with col3:
                    if st.button(f"❌ Remove {stock}", key=f"remove_{stock}"):
                        watchlists[selected_watchlist].remove(stock)
                        with open(WATCHLIST_FILE, "w") as f:
                            json.dump(watchlists, f)
                        st.rerun()

                with col4:
                    if st.button(f"📈 View {stock}", key=f"view_{stock}"):
                        st.session_state["selected_stock"] = stock
                        st.rerun()

            except Exception as e:
                st.error(f"Error fetching {stock}: {e}")

    else:
        st.info("📌 No stocks added yet. Start adding!")

    st.markdown("---")

    # 📊 Price Alerts
    st.subheader("📊 Price Alerts")
    alert_stock = st.selectbox("Select Stock for Alert", watchlists[selected_watchlist], key="alert_stock")
    alert_price = st.number_input("Set Price Alert (₹)", min_value=0.0, format="%.2f", key="alert_price")
    if st.button("🔔 Set Alert"):
        st.success(f"✅ Alert set for **{alert_stock}** at ₹{alert_price:.2f}")

    st.markdown("---")

    # 📈 Stock Performance Charts
    st.subheader("📈 Stock Performance Charts")
    chart_stock = st.selectbox("Select Stock to View Chart", watchlists[selected_watchlist], key="chart_stock")
    if st.button("📉 Show Chart"):
        # Import the Alpha Vantage module
        import sys
        import os
        sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        import alpha_vantage_api as av
        
        # First try with Alpha Vantage as primary source
        chart_history = av.get_stock_data(chart_stock, period="6mo")
        
        if chart_history.empty:
            # Try with a different time period in Alpha Vantage
            chart_history = av.get_stock_data(chart_stock, period="1y")
            
            # If still empty, fall back to Yahoo Finance
            if chart_history.empty:
                st.info(f"Trying alternative data source for {chart_stock}...")
                chart_stock_data = yf.Ticker(chart_stock)
                chart_history = chart_stock_data.history(period="6mo")
                
                if chart_history.empty:
                    chart_history = chart_stock_data.history(period="1y")
                    if chart_history.empty:
                        st.error(f"❌ Unable to fetch chart data for {chart_stock}. Please verify the stock symbol.")
                        st.stop()
                    else:
                        st.success(f"✅ Successfully retrieved {chart_stock} chart data from Yahoo Finance!")
                else:
                    st.success(f"✅ Successfully retrieved {chart_stock} chart data from Yahoo Finance!")
        
        chart_data = chart_history["Close"]
        st.line_chart(chart_data)

    st.markdown("---")

    
