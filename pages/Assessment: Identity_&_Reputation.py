import streamlit as st
import numpy as np

# Initialize session state for storing responses if not already done
if 'responses' not in st.session_state:
    # Prefill all dimensions with a neutral value of 3
    st.session_state.responses = {
        "Identity & Reputation": 3,
        "Presence": 3,
        "Social Interactions": 3,
        "Collaboration": 3,
        "Accessibility": 3,
        "Economy & Transactions": 3,
        "Technology, Structure & Ecosystems": 3,
        "Simulation & Modelling": 3
    }

# Survey questions for "Identity & Reputation"
dimension = "Identity & Reputation"
subdimensions = {
    "Personalization": [
        "A Configuration of our use-case would benefit our customer/ user.",
        "The Identity of our Customer/ User is relevant for our Product/ Service.",
        "The customization of our use-case environment benefits the Customer/ User.",
        "We prefer individual instead of ‘one-size-fits-all’ solutions.",
        "We recognize hyper-personalization as an opportunity for development."
    ],
    "Sociability": [
        "We want Customers/ Users to get engaged at different levels by expressing brand desire.",
        "We want customers with similar interests/ problems to interact with each other.",
        "We think that avatar-mediated communication is more diversified than text-based communication.",
        "We could imagine our customer journey in a gameificated way to enhance user motivation."
    ],
    "Users": [
        "We are considering user diversity when designing the platform.",
        "Personalization of our product could better fulfill customer needs.",
        "We plan on adding a social interaction space for the stakeholder of our use-case"
    ]
}

# Collect responses
st.title(f"Assessing the Dimension: {dimension}")
st.write("This dimension focuses on how important the support of creation, management, and evolution of user identities, and the creation and maintenance of the users virtual reputation within the virtaul environment is. This includes degrees of immersion, personalization, and multiple forms of interaction and collaboration.")
subdimension_scores = []
all_answered = True  # A flag to track if all questions are answered

# Loop through subdimensions and questions
for subdimension, questions in subdimensions.items():
    st.subheader(subdimension)
    scores = []
    for question in questions:
        # Generate a unique key for each question
        question_key = f"{dimension}-{subdimension}-{question}"
        
        # Check if this question already has a saved answer in st.session_state.responses
        if question_key in st.session_state.responses[dimension]:
            saved_answer = st.session_state.responses[dimension][question_key]
            initial_index = saved_answer - 1  # Convert saved score back to index (1-5 to 0-4)
        else:
            initial_index = 2  # Default to 'Neutral'

        # Display the radio button with the previously selected value (if available)
        score = st.radio(
            question,
            ('Strongly Disagree', 'Somewhat Disagree', 'Neutral', 'Somewhat Agree', 'Strongly Agree'),
            index=initial_index, key=question_key
        )

        score_value = {'Strongly Disagree': 1, 'Somewhat Disagree': 2, 'Neutral': 3, 'Somewhat Agree': 4, 'Strongly Agree': 5}
        scores.append(score_value[score])

        # Store the selected answer in session_state
        st.session_state.responses[dimension][question_key] = score_value[score]
    
    # Calculate the average score for the subdimension
    subdimension_average = np.mean(scores)
    subdimension_scores.append(subdimension_average)

# Calculate the overall score for the dimension by averaging subdimension scores
overall_dimension_score = np.mean(subdimension_scores)
st.session_state.responses[dimension]['overall'] = overall_dimension_score

# Alert if not all questions are answered (optional)
if not all_answered:
    st.warning("Some questions are not answered. You can continue, but it is recommended to answer all questions.")

# Navigation buttons
col1, col2 = st.columns([1, 1])

if col1.button("Previous"):
    st.write("Navigate to the previous page.")

if col2.button("Next"):
    st.write("Navigate to the next page.")