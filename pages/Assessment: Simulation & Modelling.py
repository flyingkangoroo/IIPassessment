import streamlit as st
import numpy as np

# Define the current dimension
dimension = "Simulation & Modelling"

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
    "Case Simulation": [
        "Simulation for Practice, Training, and Risk Mitigation: Our use-case involves resource-intensive, high-risk, or physically challenging tasks/events that would benefit from simulation for practice, training, and risk mitigation—overcoming time, space, and geographical constraints, and fostering real-world application understanding.",
        "Transforming Real-World Use-Cases: We aim to transform our real-world use-case into an equivalent virtual or immersive experience to enhance accessibility, knowledge sharing, and collaboration among users.",
        "Collaboration and Consumer Engagement: Our use-case would benefit from enabling users to collaborate and interact with others and three-dimensional objects in a simulated environment, using data-driven simulations to meet consumer needs and develop new production capabilities.",
        "Precise Simulations: We want to create precise and detailed simulations of complex or intangible real-world objects, integrating various simulation tools and models to ensure quality and enabling the real-time transfer of simulated actions to the real world."
    ],
    "Risk-Free Environment": [
        "Reducing Operational Risks: Our use-case benefits from reducing operational risks through remote control, simulation, or better training provided by an IIP.",
        "Minimizing Dangerous Consequences: Our use-case contains dangerous activities that could be safely simulated and practiced in a risk-free virtual environment.",
        "Remote Risk Management: Our use-case benefits from using virtual environments to reduce the risks associated with real-world external conditions."
    ],
    "Smart Factory": [
        "Smart Factory Integration: Our use-case benefits from integrating a digital twin or smart factory model to monitor production flows, optimize maintenance, and improve production efficiency.",
        "Data Synchronization: Our use-case would benefit from real-time monitoring of physical systems and synchronized updates between the physical and digital environments.",
        "Optimizing Production: Our use-case benefits from optimizing production processes through digital models that reduce downtime, scrap, and resource waste."    
    ],
    "Human-Machine Collaboration": [
        "Enhancing Human-Machine Interaction: Our use-case benefits from human-machine collaboration within the IIP, enhancing user engagement, remote control, and immersive experiences.",
        "Optimizing Manufacturing: Our use-case benefits from integrating human-machine collaboration to optimize manufacturing processes, reduce errors, and increase throughput."
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
progress = 6 / 8  # sixth dimension of eight
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
