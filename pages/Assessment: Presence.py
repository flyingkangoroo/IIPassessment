import streamlit as st
import numpy as np

# Define the current dimension
dimension = "Presence"

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
    "Immersion": [
        """We are planning on integrating the "human factor" in your IIP through accurate posutres, gestures and other human factors.""",
        "We want the stakeholders of our use-case to experience sensory feedback from the partners in our IIP, such as body language, facial expressions, and eye contact.",
        "We want to integrate the features ‘immediacy’ and ‘low latency’, ‘virtuality’ and ‘virtual identity’ to enhance the immersiveness.",
        "Creating a high-quality consumer experience through the creation of realistic environmental simulations could enhance our use-case.",
        "Generating a sense of presence in a virtual environment such that the user can act and behave as if the IIP environment is real, thereby enabling scenarios or experiments otherwise difficult to reproduce in the real world. immersion in IIPs can help our users to focus on actually experiencing the provided content rather than grasping just the interface would benefit our use-case.",
        "We want to strengthen our use-case awareness, positioning, branding and/ or management through integrating an IIP."
        ],
    "Sensors": [
        "Our IIP should enables users to mobilize their eyes, ears, mouth, nose and other body senses through precreated simulations and interactive devices such as head-mounted displays, earphones, handles and data gloves, and achieve their goals through different ways such as voice, movement, eye movements and gestures, thus achieving a nearly natural and “personal experience” interaction.",
        "We want to allow users to engage in an authentic and immersive way by integrating the sensors for precise visualization of gestures, postures, facial expressions and movements.",
        "We recreate physical real-world experiences through the integration of haptic feedback technologies.",
        "We plan on overlaying digital visual stimuli onto the real world to vitalize real-world experiences and create a more engaging experience.",
        "We make sure to integrate the necessary sensors to minimize the chance of misunderstandings and erroneous judgements through non-verbal communicationcues"
        ],
    "Interactive Environment": [
        "It benefits our case if the user has as much control about their interactions with other humans or machines as possible.",
        "Considering the diversity of interactions between different interfaces and contents is beneficial for our use-case.",
        "It is important that we enable immediate feedback for our use-case."
        ]
}

# Collect responses
st.title(f"Assessing the Dimension: {dimension}")
st.write("This dimension identifies the needs for economic aspects of the virtual environment, including the creation, exchange, and management of virtual goods, services, and currencies.")
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
progress = 5 / 8  # fifth dimension of eight
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
