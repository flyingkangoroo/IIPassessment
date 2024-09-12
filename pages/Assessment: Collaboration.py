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
dimension = "Collaboration"

subdimensions = {
    "Collaboration": [
        "Our Use-Case would benefit of an immersive virtual environment capable of imitating a corporate setting with various scenarios for collaborative use.",
        "Our Use-Case would benefit by an IIP-enabled multi-party collaborative manufacturing.",
        "We think that a a virtual workspace with natural interaction, prompt communication and a high immersion could benefit our use-case.",
        "In our use-case the creation, copy, maintenance, selling or exchanging of contents is important to the users.",
        "We want to enable collaboration when traditional real-world interactions are not feasible.",
        "We want to enable stakeholders to collaborate in several ways such as engaging in discussions or analyzing cases from different perspectives."
    ],
    "Co-Creation": [
        "We want our users to participate in specific activities and events together and simultaneously with other participants."
        "It would be beneficial for our use-case if stakeholders were interested in cocreating the offering.",
        "We want to benefit from a re-ignited power of user-generated content by previous consumers, and ultimately, optimize the value co-creation process both before, during, and after consumers’ experiences."
        "Our Users can self-construct their knowledge and values based on their original knoledge structures."
    ]
}
# Collect responses
st.title(f"Assessing the Dimension: {dimension}")
st.write("This dimension analyzes the relevance of mechanisms that allow users to collaborate on common goals in real time, emphasizing the importance of tools and features that support effective teamwork and task coordination within a virtual space.")
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