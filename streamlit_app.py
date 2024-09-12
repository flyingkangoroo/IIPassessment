import streamlit as st

#initialize page
st.set_page_config(page_title="Business Use-Case IIP-Assessment",
                   layout="centered")

# Initialize default responses with neutral value (3) if not already done
if 'responses' not in st.session_state:
    st.session_state.responses = {dimension: 3 for dimension in [
        "Identity & Reputation", "Presence", "Social Interactions", 
        "Collaboration", "Accessibility", "Economy & Transactions", 
        "Technology, Structure & Ecosystems", "Simulation & Modelling"
    ]}

st.title("Prototype: IIP-Assessment")
st.markdown("""
### Welcome to the Business Use-Case Viability Assessment Tool

This tool is designed to help you evaluate the viability of a business use-case that may be transformed into an industrial immersive platform (IIP). 

The assessment will guide you through the following eight empirical arised and validated dimensions:
- **Identity & Reputation**
- **Presence**
- **Social Interactions**
- **Collaboration**
- **Accessibility**
- **Economy & Transactions**
- **Technology, Structure & Ecosystems**
- **Simulation & Modelling**


Each of these dimensions has been carefully chosen to reflect key aspects of a business use-case and its potential as an IIP. You will answer a series of questions related to each dimension, and the results will be visualized in real time. The survey will save your answers unless you don't refresh your browser. This survey takes about 20minutes.

---  
            
### About This Tool

Please note that this is only a **prototype**, developed as part of a **Master’s Thesis**. The creation of this assessment tool follows a **Design Science Research (DSR) approach**, which emphasizes building and evaluating artifacts to address real-world problems. 

This tool is intended for **demonstration purposes** only and should not be used as a final, comprehensive assessment solution.

---

### How It Works

1. You will assess each of the 8 core dimensions using a Likert scale, where you rate various statements from *Strongly Disagree* to *Strongly Agree*.
2. The tool will dynamically calculate the average score for each dimension and present your results in a **spider chart** (also known as a radar chart) at the end of the assessment.
3. You can revisit any dimension at any time during the assessment to review or update your responses.

---

### Acknowledgment

This prototype was created in the context of a **Master's Thesis** as part of research conducted in the field of business use-case viability for industrial immersive platforms. The tool aims to contribute to the academic and practical understanding of how businesses can evaluate the feasibility of implementing immersive technologies within their operations.

---

### Get Started

To begin the assessment, navigate to the first dimension from the sidebar or click the button below.
""")

# Start assessment button
if st.button("Start Assessment"):
    st.write("Navigate to the first assessment page from the sidebar.")

st.sidebar.write("IIP Assessment Model")
