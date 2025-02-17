import streamlit as st
import numpy as np
import math

# Set page config
st.set_page_config(page_title="Financial Calculator India", layout="wide")

# Custom CSS for Stylish Fonts and Pastel Theme
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

        html, body, [class*="st-"] {
            font-family: 'Poppins', sans-serif;
        }

        .select-box {
            background: #F7E6AD;
            color: #4A4A4A;
            border-radius: 12px;
            padding: 15px;
            font-size: 22px;
            text-align: center;
            font-weight: 600;
            box-shadow: 0px 0px 8px rgba(0, 0, 0, 0.1);
        }

        .calculator-box {
            padding: 20px;
            border-radius: 12px;
            color: #4A4A4A;
            font-weight: 500;
            box-shadow: 0px 0px 8px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }

        .emi-box {background: #FADADD;}
        .fd-box {background: #C3E2DD;}
        .sip-box {background: #FCE1A9;}
        .tax-box {background: #D6C3E2;}

        .result {
            font-size: 20px;
            font-weight: 600;
            color: #4A4A4A;
            background: rgba(255,255,255,0.8);
            padding: 10px;
            border-radius: 8px;
            text-align: center;
            margin-top: 15px;
            box-shadow: 0px 0px 6px rgba(0, 0, 0, 0.1);
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown(
    """
    <style>
        .title-box {
            text-align: center;
            background-color: #b4ea7e;
            padding: 15px;
            border-radius: 12px;
            font-family: 'Poppins', sans-serif;
            font-size: 32px;
            font-weight: bold;
            color: #5E4B56;
            margin-bottom: 20px;
        }
    </style>
    <div class="title-box">
        💰 FinEase: Your Smart Financial Companion 
    </div>
    """,
    unsafe_allow_html=True
)

# Two-Column Layout (Left: Calculator, Right: Image)
col1, col2 = st.columns([1.2, 1])  

with col1:
    st.markdown('<div class="select-box">Choose a Calculator</div>', unsafe_allow_html=True)
    calc_choice = st.selectbox("", ["EMI Calculator", "Fixed Deposit Calculator", "SIP Investment Calculator", "Income Tax Calculator"])

with col2:
    st.image("https://cdn.dribbble.com/userupload/23923455/file/original-b972c33d76e61f5a32412d44227cfab9.gif", use_container_width=True)



# EMI Calculator
if calc_choice == "EMI Calculator":
    st.markdown('<div class="calculator-box emi-box">📌 EMI Calculator</div>', unsafe_allow_html=True)
    principal = st.number_input("Loan Amount (₹)", min_value=0, value=500000, step=10000)
    rate = st.number_input("Interest Rate (Annual %)", min_value=0.0, value=7.5, step=0.1)
    tenure = st.number_input("Loan Tenure (Years)", min_value=1, value=10, step=1)
    
    if st.button("Calculate EMI"):
        monthly_rate = rate / (12 * 100)
        months = tenure * 12
        emi = (principal * monthly_rate * (math.pow(1 + monthly_rate, months))) / (math.pow(1 + monthly_rate, months) - 1)
        st.markdown(f'<div class="result">Your Monthly EMI: ₹{emi:.2f}</div>', unsafe_allow_html=True)

# FD Calculator
elif calc_choice == "Fixed Deposit Calculator":
    st.markdown('<div class="calculator-box fd-box">📌 Fixed Deposit Calculator</div>', unsafe_allow_html=True)
    deposit = st.number_input("Initial Deposit (₹)", min_value=0, value=50000, step=1000)
    fd_rate = st.number_input("Annual Interest Rate (%)", min_value=0.0, value=6.5, step=0.1)
    years = st.number_input("Duration (Years)", min_value=1, value=5, step=1)
    
    if st.button("Calculate FD Maturity"):
        maturity = deposit * math.pow((1 + (fd_rate / 100)), years)
        st.markdown(f'<div class="result">Maturity Amount: ₹{maturity:.2f}</div>', unsafe_allow_html=True)

# SIP Calculator
elif calc_choice == "SIP Investment Calculator":
    st.markdown('<div class="calculator-box sip-box">📌 SIP Investment Calculator</div>', unsafe_allow_html=True)
    sip_amount = st.number_input("Monthly Investment (₹)", min_value=0, value=5000, step=500)
    sip_rate = st.number_input("Expected Annual Return (%)", min_value=0.0, value=12.0, step=0.1)
    sip_years = st.number_input("Investment Duration (Years)", min_value=1, value=10, step=1)
    
    if st.button("Calculate SIP Returns"):
        months = sip_years * 12
        monthly_rate = (sip_rate / 12) / 100
        future_value = sip_amount * (((math.pow(1 + monthly_rate, months)) - 1) / monthly_rate) * (1 + monthly_rate)
        st.markdown(f'<div class="result">Estimated Future Value: ₹{future_value:.2f}</div>', unsafe_allow_html=True)

# Tax Calculator
elif calc_choice == "Income Tax Calculator":
    st.markdown('<div class="calculator-box tax-box">📌 Income Tax Calculator</div>', unsafe_allow_html=True)
    income = st.number_input("Enter Your Annual Income (₹)", min_value=0, value=500000, step=10000)
    
    if st.button("Calculate Tax"):
        tax = 0
        if income <= 250000:
            tax = 0
        elif income <= 500000:
            tax = (income - 250000) * 0.05
        elif income <= 1000000:
            tax = (250000 * 0.05) + (income - 500000) * 0.2
        else:
            tax = (250000 * 0.05) + (500000 * 0.2) + (income - 1000000) * 0.3
        st.markdown(f'<div class="result">Your Estimated Tax: ₹{tax:.2f}</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; font-weight: bold;'>© 2025 Financial Calculator India | Built with ❤️ </p>", unsafe_allow_html=True)
