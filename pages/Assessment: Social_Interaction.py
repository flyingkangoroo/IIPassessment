import streamlit as st
import numpy as np

# Define the current dimension
dimension = "Social Interaction"

# Initialize session state for storing responses if not already done
if 'responses' not in st.session_state:
    st.session_state.responses = {}

# Ensure the current dimension is initialized in the session state correctly
if dimension not in st.session_state.responses or isinstance(st.session_state.responses[dimension], int):
    # If dimension is missing or stored incorrectly as an int, initialize it properly
    st.session_state.responses[dimension] = {
        "questions": {},  # For storing individual question responses
        "overall": 3  # Default overall score (can be updated later)
    }

subdimensions = {
    "Collaboration": [
        "Remote & Virtual Collaboration: Our use-case would benefit from immersive virtual environments that simulate corporate settings and include collaborative spaces like meeting rooms, training rooms, and workspaces.",
        "Community Participation: Our use-case would benefit from enabling multi-party collaboration and remote collaboration when traditional real-world interactions are not feasible."
    ],
    "Interactive Environment": [
        "Social Interaction Spaces: Our use-case would benefit from the creation of social interaction spaces where users can seamlessly interact with each other and with the system.",
        " Social Networking	Seamless connectivity between users, platforms, and operating systems enhances our use-case by fostering smoother interactions."
    ],
    "Communication": [
       "Avatar-Mediated Communication: Avatar-mediated communication, including non-verbal cues like gestures and facial expressions, improves user experience and fosters better interactions in our use-case.",
        "Experience Sharing: Our use-case benefits from enabling users to share experiences, provide advice, and support others through virtual interactions.",
        "Collaboration Tools: The use-case can be improved by enabling remote task management, collaboration rooms, and communication updates between users."
    ],
    "Interaction": [
        "Simulated Interactions	Simulating face-to-face interactions and providing sensory feedback, such as body language and eye contact, enhances user engagement in our use-case.",
        "Enhanced User Interaction	Our use-case benefits from enabling users to interact with digital objects in real-time through various sensory and interactive modalities."
    ]
}
# Collect responses
st.title(f"Assessing the Dimension: {dimension}")
st.write("Assesses the importance of various ways in which users interact within the virtual environment, focusing on the quality of communication, the ability to collaborate, and the overall sense of community. Effective social interactions can be critical to creating a vibrant and engaging virtual ecosystem.")
subdimension_scores = []
all_answered = True  # A flag to track if all questions are answered

for subdimension, questions in subdimensions.items():
    st.subheader(subdimension)
    scores = []
    for question in questions:
        # Generate a unique key for each question
        question_key = f"{dimension}-{subdimension}-{question}"

        # Check if this question already has a saved answer in st.session_state.responses[dimension]['questions']
        if question_key in st.session_state.responses[dimension]["questions"]:
            saved_answer = st.session_state.responses[dimension]["questions"][question_key]
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

        # Store the selected answer in session_state under 'questions'
        st.session_state.responses[dimension]["questions"][question_key] = score_value[score]

    # Calculate the average score for the subdimension
    subdimension_average = np.mean(scores)
    subdimension_scores.append(subdimension_average)

# Calculate the overall score for the dimension by averaging subdimension scores
overall_dimension_score = np.mean(subdimension_scores)
st.session_state.responses[dimension]['overall'] = overall_dimension_score

# Display progress
progress = 7 / 8  # Seventh dimension of eight
st.progress(progress)

# Alert if not all questions are answered (optional)
if not all_answered:
    st.warning("Some questions are not answered. You can continue, but it is recommended to answer all questions.")

# Navigation buttons
col1, col2 = st.columns([1, 1])

if col1.button("Previous"):
    st.write("Navigate to the previous page.")

if col2.button("Next"):
    st.write("Navigate to the next page.")
