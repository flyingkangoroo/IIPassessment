import streamlit as st
import numpy as np

# Initialize session state for responses if it doesn't exist
if 'responses' not in st.session_state:
    st.session_state.responses = {}

# Survey questions for the assessment
dimensions = {
    "Identity & Reputation": {
        "Personalization": [
            "A Configuration of our use-case would benefit our customer/ user.",
            "The Identity of our Customer/ User is relevant for our Product/ Service."
            # Additional questions here
        ],
        # Other subdimensions
    },
    # Other dimensions
}

# Collect responses
for dimension, subdimensions in dimensions.items():
    st.subheader(dimension)
    for subdimension, questions in subdimensions.items():
        st.write(f"**{subdimension}**")
        scores = []
        for question in questions:
            score = st.radio(question, ('Strongly Disagree', 'Somewhat Disagree', 'Neutral', 'Somewhat Agree', 'Strongly Agree'), index=2, key=f"{dimension}-{subdimension}-{question}")
            score_value = {'Strongly Disagree': 1, 'Somewhat Disagree': 2, 'Neutral': 3, 'Somewhat Agree': 4, 'Strongly Agree': 5}
            scores.append(score_value[score])
        
        # Store the average score for each subdimension in session_state
        st.session_state.responses[f"{dimension}-{subdimension}"] = np.mean(scores)

st.write("Once you complete the assessment, navigate to the 'Results' page to see your results.")
