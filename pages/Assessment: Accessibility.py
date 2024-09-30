import streamlit as st
import numpy as np

# Define the current dimension
dimension = "Accessibility"

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

# Example questions for this dimension
subdimensions = {
    "Remote Access": [
        "Remote Control: Our use-case benefits from enabling remote access and control of machines, physical objects, and environments through digital twins or other IIP technologies.",
        "Breaking Geographical and Time Constraints: Our use-case would benefit from eliminating geographical and time constraints, allowing users to interact and collaborate remotely across regions.",
        "Human-Human and Human-Machine Interactions: Our use-case benefits from enabling human-human and human-machine interactions regardless of geographical location, enhancing collaboration and communication.",
        "Remote Monitoring and Automation: Our use-case benefits from the integration of remote monitoring, real-time data access, and automated task management.",
        "Safety and Sustainability: Remote work and access ensure user safety, sustainability, and the ability to adapt to unpredictable crises and challenges."
    ],
    "Repeatability": [
        "Safe and Cost-efficient Simulations: Our use-case benefits from the ability to simulate real-world actions repeatedly in a safe environment, reducing costs, risks, and resource usage.",
        "Flexible and Repeatable Operations: Our use-case benefits from being flexible in terms of space, time, and repetition of actions, which increases productivity and efficiency.",
        "Virtual Recreational Goods: The ability to create endless copies of virtual goods and recreational content within a repeatable environment benefits our use-case."
        ],
    "Public Access": [
        "Inclusivity: Our use-case benefits from providing equal access to knowledge, digital goods, and services regardless of users' geographical location, economic status, or knowledge level.",
        "Global Participation: Enabling a global audience to participate and collaborate in real-time through our IIP increases diversity, access, and involvement.",
        "Broader Access: Our use-case benefits from giving users access to exclusive or otherwise restricted experiences, operations, or events through our IIP.",
        "Information Sharing: The transfer of real-world information to a digital platform enables faster dissemination of knowledge and collaborative manufacturing."
        ]
}

# Collect responses
st.title(f"Assessing the Dimension: {dimension}")
st.write("Figures out how important it is to make the use-case accessible to a wide range of people, including those with different abilities, and provides a user-friendly experience that can be easily adapted to different technological environments.")
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
progress = 1 / 8  # First dimension of eight
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
