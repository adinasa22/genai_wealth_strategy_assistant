import streamlit as st
from advisor import get_portfolio_advice

st.set_page_config(page_title="Wealth Strategy Assistant", layout="wide")

st.title("💰 GenAI Wealth Strategy Assistant")
st.markdown("A fully offline, open-source financial advisor powered by LLaMA3, LangChain, and ChromaDB.")

age = st.number_input("Investor Age", min_value=18, max_value=100, value=35)
goal = st.text_input("Financial Goal", value="Child’s education")
risk = st.selectbox("Risk Appetite", ["Low", "Moderate", "High"], index=1)
docs = st.file_uploader("Upload Financial Documents", accept_multiple_files=True)

if st.button("Get Portfolio Strategy"):
    with st.spinner("Processing..."):
        response = get_portfolio_advice(age, goal, risk, docs)
        st.markdown("### 📊 Portfolio Recommendation")
        st.write(response)