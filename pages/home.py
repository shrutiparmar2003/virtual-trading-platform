import streamlit as st

# Set page config
st.set_page_config(page_title="Virtual Trading", page_icon="📈", layout="wide")

# Custom Styling
page_bg = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@500;600&family=Lora:wght@400;500&display=swap');

    body {
        background-color: #0d0d0d;
        font-family: 'Lora', serif;
    }

    /* Navbar - Lowered and Right-Aligned */
    .navbar {
        position: fixed;
        top: 60px;  /* Lowered the navbar */
        right: 20px; /* Moved it to the right */
        background: rgba(20, 20, 20, 0.9);
        padding: 10px 20px;
        text-align: right; /* Align links to the right */
        z-index: 1000;
        box-shadow: 0px 2px 10px rgba(255, 255, 255, 0.2);
        border-radius: 10px;
    }

    .navbar a {
        color: white;
        text-decoration: none;
        font-size: 16px;
        margin: 0 20px;
        font-family: 'Montserrat', sans-serif;
    }

    .navbar a:hover {
        text-shadow: 0px 0px 10px #ff8c00;
    }

    /* Glowing Title Box with Purple-Orange Edge */
    .title-container {
        display: flex;
        justify-content: center;
        margin-top: 60px;
    }

    .title-box {
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 15px 35px;
    border-radius: 25px; /* Rounded corners */
    font-size: 40px;
    font-weight: 600;
    color: white;
    text-shadow: 0px 0px 30px #8a2be2, 0px 0px 50px #ff8c00;
    font-family: 'Montserrat', sans-serif;
    text-align: center;
    position: relative;
    background: rgba(20, 20, 20, 0.9);
    z-index: 1; /* Keep content above border */
}

.title-box::before {
    content: "";
    position: absolute;
    top: -6px;
    left: -6px;
    right: -6px;
    bottom: -6px;
    background: linear-gradient(45deg, #8a2be2, #ff8c00);
    border-radius: 30px; /* Ensure the border is rounded */
    z-index: -1; /* Place behind the box */
}


    @keyframes borderGlow {
        0% { border-image-source: linear-gradient(45deg, #8a2be2, #ff8c00); }
        50% { border-image-source: linear-gradient(45deg, #ff8c00, #8a2be2); }
        100% { border-image-source: linear-gradient(45deg, #8a2be2, #ff8c00); }
    }

    /* Description Box */
    .description-box {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 50px;
    }

    .description-content {
        max-width: 700px;
        padding: 20px 30px;
        border-radius: 15px;
        text-align: center;
        background: rgba(255, 255, 255, 0.1);
        border: 2px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0px 0px 20px rgba(255, 255, 255, 0.4);
        font-size: 18px;
        color: #e0e0e0;
        font-family: 'Lora', serif;
        line-height: 1.6;
    }

    /* Steps Heading */
    .steps-heading {
        text-align: center;
        font-size: 32px;
        color: white;
        text-shadow: 0px 0px 15px #00bfff;
        margin-top: 80px;
        font-family: 'Montserrat', sans-serif;
    }

    /* Steps Cards */
    .steps-container {
        display: flex;
        justify-content: center;
        gap: 30px;
        margin-top: 30px;
    }

    .step-card {
        width: 300px;
        background: rgba(20, 20, 20, 0.9);
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0px 4px 10px rgba(255, 255, 255, 0.2);
        border: 2px solid rgba(255, 255, 255, 0.2);
        position: relative;
        font-family: 'Lora', serif;
        color: white;
        text-align: center;
    }

    /* Sleek Spiral Binding */
    .step-card::before {
        content: "";
        position: absolute;
        left: -15px;
        top: 10px;
        width: 10px;
        height: 100%;
        background: linear-gradient(to bottom, white 10%, transparent 20%, white 30%, transparent 40%);
        border-radius: 50%;
        box-shadow: 0px 0px 10px rgba(255, 255, 255, 0.4);
    }

</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

# Navbar - Now positioned on the right side
st.markdown(
    """
    <div class="navbar">
        <a href="#">Home</a>
        <a href="#">Markets</a>
        <a href="#">Trade</a>
        <a href="#">Portfolio</a>
        <a href="#">Help</a>
    </div>
    """,
    unsafe_allow_html=True,
)

# Centered Title with Glowing Box (Purple-Orange Edge)
st.markdown("<div class='title-container'><div class='title-box'>PAPER TRADING</div></div>", unsafe_allow_html=True)

# Centered Description Box
st.markdown(
    """
    <div class="description-box">
        <div class='description-content'>
            Master the art of trading without the risk. <br> 
            Experience real-time market simulations, test strategies, and build confidence before investing real money. <br> 
            The perfect playground for aspiring traders and seasoned investors alike.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Steps Heading
st.markdown("<div class='steps-heading'>How to Start Paper Trading</div>", unsafe_allow_html=True)

# Steps Cards
st.markdown(
    """
    <div class="steps-container">
        <div class="step-card">
            <h3>Step 1</h3>
            <p> Set Up Portfolio – Start with a virtual balance and track real-time stocks.</p>
        </div>
        <div class="step-card">
            <h3>Step 2</h3>
            <p>Place Trades – Buy/sell stocks with live market data and manage holdings.</p>
        </div>
        <div class="step-card">
            <h3>Step 3</h3>
            <p>Analyze & Improve – Monitor performance, get AI insights, and refine strategies.</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)
