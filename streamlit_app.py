import streamlit as st

st.title("Welcome to the Business Use-Case Viability Assessment")
st.write("This app allows you to assess various dimensions of a business use-case and see your results visualized in real time.")

st.sidebar("Menu")
if st.button("Start Assessment"):
    st.write("initializing")
    st.page_link("assessment.py")