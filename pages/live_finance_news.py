import streamlit as st
import feedparser

# Function to fetch financial news
def get_finance_news():
    url = "https://news.google.com/rss/search?q=finance+OR+stock+market+OR+cryptocurrency&hl=en-IN&gl=IN&ceid=IN:en"
    feed = feedparser.parse(url)
    return feed.entries[:10]  # Get top 10 news articles

# Page Configuration
st.set_page_config(page_title="Live Finance News Hub", layout="wide")

# Custom CSS for Styling
st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

        * {
            font-family: 'Poppins', sans-serif;
        }

        .title-container {
            text-align: center;
            font-size: 36px;
            font-weight: 700;
            color: #ffffff;
            text-shadow: 0px 0px 8px #ff8c00, 0px 0px 12px #ff8c00;
            margin-bottom: 25px;
        }

        .news-card {
            background: linear-gradient(135deg, #7b2cbf 0%, #c77dff 100%);
            padding: 20px;
            border-radius: 12px;
            margin-bottom: 15px;
            box-shadow: 4px 4px 12px rgba(0, 0, 0, 0.15);
        }

        .news-title {
            font-size: 20px;
            font-weight: 600;
            color: #ffffff;
        }

        .news-link {
            display: inline-block;
            background: #ffffff;
            padding: 6px 12px;
            border-radius: 8px;
            font-size: 14px;
            font-weight: 500;
            color: #7b2cbf;
            text-decoration: none;
            transition: all 0.3s ease-in-out;
            box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.2);
        }

        .news-link:hover {
            background: #7b2cbf;
            color: #ffffff;
        }

        .news-published {
            font-size: 14px;
            color: #f8f9fa;
            margin-bottom: 8px;
        }

        .refresh-btn {
            display: flex;
            justify-content: center;
            margin-top: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title with Glowing Orange Effect
st.markdown("<div class='title-container'>📈 Live Finance News Hub</div>", unsafe_allow_html=True)

# Fetch and Display News
news_list = get_finance_news()
for news in news_list:
    with st.container():
        st.markdown(f"""
        <div class='news-card'>
            <div class='news-title'>{news.title}</div>
            <div class='news-published'>🗓 Published: {news.published}</div>
            <a class='news-link' href='{news.link}' target='_blank'>🔗 Read More</a>
        </div>
        """, unsafe_allow_html=True)

# Add a refresh button
st.markdown("<div class='refresh-btn'>", unsafe_allow_html=True)
if st.button("🔄 Refresh News"):
    st.rerun()
st.markdown("</div>", unsafe_allow_html=True)
