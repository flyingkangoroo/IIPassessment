import streamlit as st
import numpy as np

# Define the current dimension
dimension = "Technology, Structure & Ecosystems"

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
    "Technical Foundation": [
        "Resources, Infrastructure, and Realism: Our use-case benefits from having the necessary resources, infrastructure, and modern technology to create a realistic, interoperable, and scalable IIP.",
        "Data Standards and Privacy: Our use-case has well-defined data standards, governance, and privacy protections to ensure smooth data sharing and technical security.",
        "Integration of Advanced Devices: Our use-case benefits from integrating IoT devices, sensors, and advanced processing technologies that enhance data collection, visualization, and interaction within the IIP.",
        "Scalability and User Access: We have access the necessary technology, equipment, and technical infrastructure to ensure that all users can fully engage with an IIP, supported by the appropriate tools, output devices, and operators for seamless interaction with real-world environments.",
        "Technology Acceptance: Our use case is defined by clear features, fosters user adoption through understanding key influencing factors, and leverages well-structured data with ongoing efforts to reduce latency and enhance IIP quality"
    ],
    "Real-Time Processing": [
        "Real-Time Mapping: Our use-case benefits from real-time mapping and data handling with standardized data formats, protocols, and interfaces, which enhance operations, decision-making, and system optimization within the IIP.",
        "Predictive Systems: Our use-case would benefit from real-time simulations and predictive systems that improve quality, efficiency, and cost-effectiveness in operations.",
        "Real-Time Interaction: Real-time user interactions with objects and avatars in the IIP enhance our use-case by improving engagement and collaboration."  
    ],
    "Interoperability": [
        "Cross-Platform Access: Ensuring interoperability across platforms, devices, and departments improves our use-case by enabling seamless data exchange and collaboration",
        "Operational Flexibility: Increasing interoperability within our use-case allows us to improve operational flexibility and real-time performance monitoring.",
        "Interdisciplinary Collaboration: Our use-case benefits from interdisciplinary collaboration and systematic methodologies that support high-level automation and decision-making."
    ],
    "Ecosystem": [
        "Immersive User Engagement	Our use-case benefits from creating a truly immersive experience where users engage with applications using a wide range of sensory inputs.",
        "Decentralized Systems	Our use-case benefits from operating on decentralized systems and involving stakeholders effectively within the IIP."
    ]
}
# Collect responses
st.title(f"Assessing the Dimension: {dimension}")
st.write("Analyzes if there are underlying technology and structural aspects that support the virtual platform, including the system integration, scalability, and security measures that ensure a stable and reliable environment.")
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
progress = 8 / 8  # Eighth dimension of eight
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
