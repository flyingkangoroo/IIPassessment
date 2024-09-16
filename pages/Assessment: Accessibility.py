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
        "For our Use-Case it is beneficial if one could control machines or similar remote entities remotely by leveraging a digital twin of the machine in its environment.",
        "It could be beneficial for our use-case if users could access data and control parameters through a digital representation of the physical object.",
        "We want to break space, time or ressource constraints by enabling remote access in our use-case.",
        "We need to enable human-human interactions, where they are not feasible in the real-world.",
        "We want to bridge geographical disparities by enabling users in underserved regions to collaborate seamlessly with distant counterparts, thereby expanding opportunities for support and collaboration.",
        "Enabling human-human and human-machine interactions regardless of their geographical location could be beneficial for our use-case.",
        "We think that accessibility without the constraints of the real world and therefore also ensuring sustainability in the face of unpredictable crises and challenges would secure a bright future for our use-case."
    ],
    "Repeatability": [
        "Enabling unlimited repetitions of tasks that usually cost large amounts of ressources, are dangerous, or have similar restrictions could be beneficial for our use-case.",
        "Enabling users to experience educational consequences of their actions, without hurting themselfs could be beneficial for our use-case.",
        "We think it could be beneficial to afford the user the ability to experience hazardous situations while never compromising his/her safety and health in our use-case.",
        "We think that endless copies of virtual goods within a remotely accessable environment could be beneficial for our use-case.",
        "The unlimited poissibility of repeating actions in a safe environment could be beneficial for our use-case."
        ],
        "Public Access": [
        "We want to provide equal opportunities for every user regardless of their current knowledge level, economic circumstances, or social status by creating an IIP.",
        "It could be beneficial for our use-case if operations where operateable for everyone, regardless of the users geographical location.",
        "we want to design a shared digital ecosystem where ressources are shared and available on a global scale to a bigger population.",
        "We want to eliminate geographical barriers, which allows a global audience to participate in real time without physically traveling. This fact increases the attendance and the diversity of the inputs and perspectives to our use-case",
        "we want to give access to information, be more inclusive and making it universally available, fostering connections among individuals from diverse geographic backgrounds."
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
