import streamlit as st
from PIL import Image

# Page config
st.set_page_config(
    page_title="Stock Prediction Portal",
    page_icon="📈",
    layout="wide",
)

# Custom CSS for styling
st.markdown("""
    <style>
    .title {
        font-size: 48px;
        font-weight: 700;
        color: #1f77b4;
        text-align: center;
    }
    .subtitle {
        font-size: 24px;
        color: #4c4c4c;
        text-align: center;
        margin-bottom: 40px;
    }
    .center {
        display: flex;
        justify-content: center;
        margin-top: 30px;
    }
    .btn {
        background-color: #87CEFA;  /* Light sky blue */
        color: black;
        padding: 0.8em 2em;
        border-radius: 10px;
        text-decoration: none;
        font-size: 20px;
        transition: background-color 0.3s ease;
        font-weight: 600;
    }
    .btn:hover {
        background-color: #63bde4;  /* Darker sky blue on hover */
    }
    .card-container {
        display: flex;
        flex-wrap: wrap;
        justify-content: space-around;
        margin-top: 10px;
    }
    .card {
        background-color: #f9f6ff;
        border-left: 6px solid #a78bfa;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
        padding: 20px;
        margin: 10px;
        width: 230px;
        text-align: center;
        transition: transform 0.3s ease;
    }
    .card:nth-child(2) {
        background-color: #fff8f0;
        border-left-color: #fbbf24;
    }
    .card:nth-child(3) {
        background-color: #f0fdf4;
        border-left-color: #34d399;
    }
    .card:nth-child(4) {
        background-color: #f0f9ff;
        border-left-color: #38bdf8;
    }
    .card:hover {
        transform: scale(1.05);
    }
    .card h4 {
        color: #333;
        margin-bottom: 10px;
    }
    .card p {
        color: #555;
        font-size: 16px;
    }
    </style>
""", unsafe_allow_html=True)

# Title and subtitle
st.markdown('<div class="title">📊 Welcome to the Stock Prediction Portal</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Get future insights on stock prices powered by machine learning</div>', unsafe_allow_html=True)

# Image and features
col1, col2 = st.columns(2)

with col1:
    st.image("https://cdn-icons-png.flaticon.com/512/2620/2620854.png", width=300)

with col2:
    st.markdown("""
        <div class="card-container">
            <div class="card">
                <h4>📈 Real-time Prediction</h4>
                <p>Access up-to-date forecasts for popular stocks.</p>
            </div>
            <div class="card">
                <h4>📊 Visual Trends</h4>
                <p>View trends and patterns with interactive plots.</p>
            </div>
            <div class="card">
                <h4>🧠 ML Powered</h4>
                <p>Leverages trained models for price forecasting.</p>
            </div>
            <div class="card">
                <h4>🎯 Easy Interface</h4>
                <p>User-friendly design for smooth experience.</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="center"><a class="btn" href="https://stock-prediction-9wmqgypekyxqpjnfhhsa2j.streamlit.app/" target="_blank">Launch Prediction App 🚀</a></div>', unsafe_allow_html=True)

# Footer
st.markdown("---")

