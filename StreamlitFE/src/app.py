import streamlit as st
from main import main
from report import report

st.sidebar.title("Menu")
page = st.sidebar.selectbox("Pages move on", ["Main", "Analysis Results"])

if page == "Main":
    main()
elif page == "Analysis Results":
    report()
