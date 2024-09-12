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
dimension = "Economy & Transaction"
subdimensions = {
    "Business Expansion": [
        "We wish for a new space for brand exposure to new customers and an additional channel of communication with existing consumers.",
        "We want to create several opportunities for new consumer products",
        "We want to create new Business Model opportunities, such as the virtual promotion of real-world products through the sale of a virtual model corresponding to a real and unique object, and the offering of virtual goods, contents, and services existing only in the virtual realm and unrepeatable in the real world due to physical constraints.",
        "We want to improve our production processes by integrating more data, better visualization, or similar advantages.",
        "We want to solve problems and perform tasks that are difficult or impossible to solve and conduct in real life, such as dangerous chemical experiments, lack of space for organizing events, and exploring outer space or ancient history."
    ],
    "Customer Satisfaction": [
        "We want to enhance consumer/ user engagement.",
        "We want to better satisfy the needs of our Users/ Consumers than our current solution and think the development of an IIP could help."
        "We want to include decentralized financial transactions through blockchain systems and hyper-personalization opportunities."
        """We need to satisfy "experience-oriented" customers/ users."""
    ],
        "Operations": [
        "Our IIP plays an important role in our next generation of manufacturing systems because it allows simulation results to be shown in a realistic, intuitive, economic and safe way.",
        "Enabling an exact production of our users needs, that are better monitored through our platform could be beneficial for our use-case.",
        "We believe that enhancing operational flexibility and giving a view to the performance and operating conditions based on real-time data, can be leveraged to enable better decision-making in operations such as condition monitoring, function simulation, evolution simulation, dynamic scheduling, predictive maintenance, and quality control.",
        "We want to enable training with rare/ expensive/ unique materials thanks to according simulation.",
        "We believe that implementing an IIP in existing manufacturing systems adds value through decreasing scrap and rework, reducing unscheduled downtime, reducing compliance costs, increasing throughput and improving training."
    ]
}
# Collect responses
st.title(f"Assessing the Dimension: {dimension}")
st.write("This dimension identifies the needs for economic aspects of the virtual environment, including the creation, exchange, and management of virtual goods, services, and currencies.")
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
progress = 3 / 8  # Adjust this number based on the current dimension page
st.progress(progress)

# Navigation
col1, col2 = st.columns([1, 1])

if col1.button("Previous"):
    st.write("Navigate to the previous page in the sidebar.")

if col2.button("Next"):
    st.write("Navigate to the next page in the sidebar.")