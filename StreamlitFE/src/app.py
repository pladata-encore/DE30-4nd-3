import streamlit as st
from main import main
from report import report
from data import data


st.sidebar.title("이동하기")
page = st.sidebar.selectbox("페이지 이동하기", ["메인", "분석 결과", "데이터"])

if page == "메인":
    main()
elif page == "분석 결과":
    report()
elif page == "데이터":
    data()
