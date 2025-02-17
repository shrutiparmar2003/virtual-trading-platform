import streamlit as st

# Set page config
st.set_page_config(page_title="Investment Dashboard", layout="wide")

# Sidebar navigation
st.sidebar.title("📍 Navigation")
st.sidebar.page_link("pages\home.py", label="🏠 Home")
st.sidebar.page_link("pages\portfolio.py", label="📈 Portfolio Overview")
st.sidebar.page_link("pages\history_transactions.py", label="💵 Transaction History")
st.sidebar.page_link("pages\watchlists.py", label="👀 Add Favourite stocks to watchlist")
st.sidebar.page_link("pages\calculator_finance.py", label="🧮 Want to calculate?")
st.sidebar.page_link("pages\live_finance_news.py", label="📰Keep yourself updated with latest news?")



# Welcome Section
st.title("📊 Investment Dashboard")
st.markdown("Track your investments in real-time with a professional dashboard, similar to Zerodha & Angel One.")

st.image("https://cdn.dribbble.com/users/2287419/screenshots/15413328/media/a9669a616e20bb52a58aab3bb534d2c3.gif" , width=300)

st.info("Use the sidebar to navigate through different sections of the app.")
