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
        "Realism: Our use-case benefits from integrating realistic human factors, such as postures, gestures, and facial expressions, to create a highly immersive experience.",
        "Multisensory: Our use-case can enhance immersion through multisensory experiences and haptic feedback to create a more realistic interaction.",
        "Realistic Simulation: Our IIP aims to represent our use-case in a realistic or pseudo-natural manner, closely mirroring real-world scenarios.",
        "Platform Usability: We want our IIP to offer easy navigation and a seamless user experience that enhances user engagement and motivation.",
        "Immersive Scenarios: Our use-case benefits from providing immersive and interactive environments that simulate real-world experiences and enable users to behave as they would in physical scenarios."
        ],
    "Sensors": [
        "Multisensory: Our use-case benefits from integrating multiple senses through sensors to provide precise and immersive feedback, including sight, sound, and touch.",
        "Real-Time Interaction: Our IIP enables users to interact with real-time, accurate representations of the use-case, simulating movements, gestures, and spatial information effectively.",
        "Haptic Feedback: We aim to simulate tactile sensations and force feedback to create a realistic experience for users engaging with the IIP.",
        "Visual and Audio Fidelity: Our use-case benefits from high-quality visual and auditory stimuli, providing photorealistic environments and accurate soundscapes.",
        "Sensor Integration: Our IIP incorporates sensors to facilitate natural interactions such as eye contact, gestures, and facial expressions, creating an authentic experience for users."
        ],
    "Simulation": [
        "Real-World Movements: Our IIP enables realistic simulation of real-world movements, providing a natural and immersive experience for users.",
        "User Engagement: The integration of digital and physical simulations in our IIP adds value to our use-case by enhancing user engagement and creating more dynamic, immersive experiences."
        ],
    "Interactive Environment": [
        "User Control: Our IIP allows users to have significant control over their interactions with both virtual environments and other users, enhancing engagement.",
        "Social and Collaborative Interaction: Our use-case benefits from integrating social interactions and collaboration, where users can interact in real-time with others and contribute to a shared virtual space.",
        "Immersive Feedback: Our use-case benefits from providing real-time feedback to users, enabling immersive interactions and immediate responses in a virtual environment.",
        "User Experience and Usability: A strong focus on user experience and usability within our IIP is critical for enhancing emotional involvement and user satisfaction.",
        "Real-World Interaction: Our use-case benefits from replicating real-world interactions within the IIP, where users’ actions in the virtual world have meaningful effects on both virtual and real environments."
        ]
}

# Collect responses
st.title(f"Assessing the Dimension: {dimension}")
st.write("Asses how important it is, that a user feels 'present' in the virtual environment, achieved through realism, immersion, interaction, and emotional engagement. Presence is critical to ensuring that the virtual experience effectively and accurately simulates real-world scenarios or provides immersive, meaningful interactions.")
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
