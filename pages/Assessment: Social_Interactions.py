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
dimension = "Social Interaction"
if dimension not in st.session_state.responses:
    st.session_state.responses[dimension] = {}
subdimensions = {
    "Collaboration": [
        "Our IIP shall enable remote collaboration.",
        "Our IIP could function as a virtual workspace with natural interaction, prompt communication and a high immersion.",
        "The creation of communities and the active participation within them could be benefitial for our use-case.",
        "Enabling stakeholders to collaborate in several ways such as engaging in discussions or analyzing cases from different perspectives is beneficial for our use-case.",
        "Enabling collaborative interactions between users is a goal."
    ],
    "Interactive Environment": [
        "A seamless connectivity between users and users, between users and platforms, between platforms and platforms, and between operating systems and operating systems is beneficial for our use-case.",
        "We want to integrate social elements through interactivity, new interaction modalities with plenty of opportunities for novel social networking and community development in our use-case.",
        "Enabling proactive interactions across the real and virtual world could be beneficial for our use-case.",
        ],
    "Communication": [
        "We want our users to share experiences, give advice, and support others within the IIP.",
        "If our users could remotely check on tasks, and communicate to update each other on task status, it would help our workflow.",
        "We aim to build designated virutal work spaces (such as Meeting Rooms, Collaboration Rooms, Training Rooms, Simulation Rooms, Interview Rooms) for our workers.",
        "We want to enable our users to have the opportunity to observe and actively participate in interactions with other users.",
        "We wish for an additional channel of communication with existing Users, Customers."
    ],
    "Interaction": [
        "we want our users to experience sensory feedback from the stakeholders within the new IIP, such as body language, facial expressions, and eye contact.",
        "We believe that successful interactions and creating an immersive environment can be beneficial for our use-case.",
        "We want to simulating face-to-face interactions within our IIP to enhance our day-to-day interactions.",
        "We want to foster user-user interaction in our use-case."
    ]
}
# Collect responses
st.title(f"Assessing the Dimension: {dimension}")
st.write("This dimension assesses the the importance of various ways in which users interact within the virtual environment, focusing on the quality of communication, the ability to collaborate, and the overall sense of community. Effective social interactions can be critical to creating a vibrant and engaging virtual ecosystem.")
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