import streamlit as st

# Initialize default responses with neutral value (3) if not already done
if 'responses' not in st.session_state:
    st.session_state.responses = {dimension: 3 for dimension in [
        "Identity & Reputation", "Presence", "Social Interactions", 
        "Collaboration", "Accessibility", "Economy & Transactions", 
        "Technology, Structure & Ecosystems", "Simulation & Modelling"
    ]}

st.title("Welcome to the Business Use-Case Viability Assessment")
st.write("This app allows you to assess various dimensions of a business use-case and see your results visualized in real time.")

st.sidebar.write("IIP Assessment Model")
