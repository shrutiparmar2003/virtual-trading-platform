import streamlit as st
import pandas as pd

st.title("📜 Transaction History")

if "transactions" in st.session_state and st.session_state.transactions:
    df = pd.DataFrame(st.session_state.transactions)
    st.table(df)
else:
    st.info("No transactions recorded yet.")
