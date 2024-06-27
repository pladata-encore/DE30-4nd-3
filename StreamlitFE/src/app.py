import streamlit as st
from main import main
from report import report
from pubgstats import PUBGStatsApp

st.sidebar.title("Menu")
page = st.sidebar.selectbox("Pages move on", ["Main", "Analysis Results","Search Match History"])

if page == "Main":
    main()
elif page == "Analysis Results":
    report()
elif page == "Search Match History":
    if __name__ == "__main__":
        app = PUBGStatsApp()
        app.run()
