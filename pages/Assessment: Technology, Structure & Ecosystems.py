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
dimension = "Technology, Structure & Ecosystems"
subdimensions = {
    "Technical Foundation": [
        "Our Use-Case has well-defined universal standards for sharing data and supporting interactions, resolving technical barriers.",
        "We have numerous sensors, smart terminals, and other IoT devices to provide support for data collection, processing and transmission within our IIP."
        "We want to integrate advances in computing technology, in particular graphical processing units, together with advanced display technologies embedded in current state-of-the-art head-mounted displays to our use-case. This allow us to experience photorealistic digital worlds at resolutions in which individual pixels are no longer distinguishable by human eyes.",
        "We have the resources and the knowhow to use modern technology to support the creation of a realistic IIP.",
        "Our use-case has a tangible number of clearly defined features.",
        "We know about upcoming dataprivacy and security challenges and will adress them accordingly.",
        "We don't face problems with cost and difficulty of technology development, content production cycles, social ethics, data privacy, or similar issues in our Use-Case."
    ],
    "Real-Time Processing": [
        "Our use-case would benefit of an remote manipulateable, real-time mapping within an IIP environment.",
        "Our use-case would benefit of real-time case sensitive data.",
        "We want to offer a wide range of applications that necessitate real time access to physical environment information.",
        "Our use-case would benefit from a simulation displayed virtually in real time.",
        "We believe that an IIP could support our value chain by building a real world simulation to predict and optimize the future and support the prescription on the real system running  parallel to the artificial ones.",
        "We have a multidisciplinary understanding that is facilitated at multiple levels to face the exploitation of the data and analytics."
    ],
    "Interoperability": [
        "We want our use-case to be more realistic, accessable, interoperable, and scalable.",
        "Increasing the interoperability across platforms and allowing users to develop and share content between virtual world, can be beneficial for our use-case.",
        "As the number of data and modernized devices increases, we recognize interoperability as a challenge of our use-case",
        "We have a group of multi-disciplinary experts that can aggregate their capabilities to work on an IIP.",
        "We want to enhance operational flexibility and gain a view to our performance and operating conditions based on real-time data that can be leveraged to enable better decision-making in operations such as condition monitoring, function simulation, evolution simulation, dynamic scheduling, predictive maintenance, and quality control."
    ],
    "Ecosystem": [
        "We want to achieve a truly immersive user experience with synchronized realities out of our use-case.",
        "Enabling immersive user engagement in a rich set of applications by all available human senses and personal metadata could benefit our use-case.",
        "Modelling our factories’ processes and connecting pieces of equipment across all production lines, could enable us to monitor high percentages of supply flows constantly, in a system and through this could benefit our use-case by using new data to refine redictive maintenance, reduce the downtime caused by stoppages and repairs, and drive greater precision in applications.",
        "We plan on operating on decentralized systems that use distributed ledger technology to record transactions and manage operations."
    ]
}
# Collect responses
st.title(f"Assessing the Dimension: {dimension}")
st.write("This dimension analyzes if there are underlying technology and structural aspects that support the virtual platform, including the system integration, scalability, and security measures that ensure a stable and reliable environment.")
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