import streamlit as st
from main import main
from report import report
from data import data


st.sidebar.title("Menu")
page = st.sidebar.selectbox("Pages move on", ["Main", "Analysis Results", "Data"])

if page == "Main":
    main()
elif page == "Analysis Results":
    report()
elif page == "Data":
    data()
