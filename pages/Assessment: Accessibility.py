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
dimension = "Accessibility"
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
st.write("in this section you should assess your usecase DESCRIBE!!!")
subdimension_scores = []
for subdimension, questions in subdimensions.items():
    st.subheader(subdimension)
    scores = []
    for question in questions:
        score = st.radio(question, ('Strongly Disagree', 'Somewhat Disagree', 'Neutral', 'Somewhat Agree', 'Strongly Agree'), 
                         index=2, key=f"{dimension}-{subdimension}-{question}")
        score_value = {'Strongly Disagree': 1, 'Somewhat Disagree': 2, 'Neutral': 3, 'Somewhat Agree': 4, 'Strongly Agree': 5}
        scores.append(score_value[score])
    
    # Calculate the average score for the subdimension and store in session state
    subdimension_average = np.mean(scores)
    subdimension_scores.append(subdimension_average)

# Calculate the overall score for the dimension by averaging subdimension scores
overall_dimension_score = np.mean(subdimension_scores)
st.session_state.responses[dimension] = overall_dimension_score

# Progress bar calculation (1/8 for the first page)
progress = 1 / 8  # Adjust this number based on the current dimension page
st.progress(progress)

# Navigation
col1, col2 = st.columns([1, 1])

if col1.button("Previous"):
    st.write("Navigate to the previous page in the sidebar.")

if col2.button("Next"):
    st.write("Navigate to the next page in the sidebar.")