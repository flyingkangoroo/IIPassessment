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
dimension = "Simulation & Modelling"
subdimensions = {
    "Case Simulation": [
        "Our use-case provides sufficient sensor data to simulate a realistig and real-time 3D environment. We aim to use the resulting virtual replication can be used for simulation, visualization, and collaboration, using a set of interlinked, real-time layers of information.",
        "Our use-case is convertable to an equivalent virtual form.",
        "Our use case contains tasks/events that can have serious consequences if performed incorrectly and therefore require a lot of experience/practice. A simulation of such events could help to avoid serious consequences due to incorrect execution.",
        "Through the intelligently capturing of real-time data in our use-case and the simulation of all the gathered data, we hope to replay certain situations so that evident decisions can be made on abnormalities.",
        "Our use case includes tasks/events that are very resource intensive. In order to be able to practice these tasks without wasting resources, a simulation for practicing purposes could be advantageous.",
        "We think that a mirrored counter part of the real-world to allow apparently genuine visual experiences in a virtual space contributes to our current use-case.",
        "By transforming our use-case, we hope to create generally accessible knowledge for all stakeholders (regardless of their current level of knowledge, economic circumstances or social status).",
        "Our use-case could benefit from new production capabilities, including manipulating the virtual environment and combining digital visual production with our real-world production.",
        "We want our use-case to be datadriven, and precicely meet our consumers needs in an interactive, immersive, and recreational way.",
        "In order to understand our use case, special knowledge is required, which could be conveyed through high immersion and additional overlays and thus be accessible to a broader mass.",
        "We want to overlay digital visual stiumuli into physical surroundings as an intensification of our real-world use-case."
    ],
    "Risk-Free Environment": [
        "Our use case involves high operational risks, which could be reduced to an absolute minimum through remote control, simulation or better training.",
        "Our use-case requires the use of practical activities that could be risky or difficult to replicate in a real-world environment, so implementing an IIP could be worthwhile.",
        "Our use-case contains facets that could be dangerous for users under certain circumstances - however, these risks could be reduced by using an IIP.",
        "Through the seamless connection and interaction between the real-world and our virtual IIP we could reduce risks of human operators in our current use-case by using remote controlled tools/ machines instead.",
        "Our use-case is strongly affected by external environmental risk conditions that could be reduced by a virtual environment that can truly reflect the current state of the use-case.",
        "Our use-case has currently no guaranteed safe operation of machines/ tools/ vehicles. We imagine to improve this through real-time dynamic remote control and can be seamlessly interfaced with an IIP."
    ],
    "Smart Factory": [
        "We've got the potential of developing a smart factory by mapping links and scenes of the physical world (R&D design, manufacturing, logistics, marketing, product service, etc.) in the virtual space.",
        "Our use-case could benefit from a digital informational construct of a physical system (a digital twin).",
        "Through the implementation of a smart factory like IIP we hope to reduce downtime and increase the productivity of our use-case.",
        "Our use-case could benefit from an up-to-date and accurate digital representation of the physical object's data values, states, and properties since this could allow users to access data and control parameters intuitively using their prior spatial knowledge of the physical site.",
        "We aim to make full use of models, data, and intelligence, to improve our use-cases whole life cycle management, and provide real-time, efficient and intelligent services featuring flexibility, reliability, transparency and risk & error pre-warning.",
        "We want to benefit from the ability to collect and analyze real-time data from our use-case and optimize production chain by saving costs, increasing efficiencies, and breaking information silos.",
        "Our use-case could benefit from a virtual system based on the description of the real world that is made to predict and optimize the future, or support the prescription on real system running  parallel to the artificial ones.",
        "The synchronization of the information flow between the physical system and its digital counterpart, allowing for real-time observation, evaluation, and decision-making could be beneficial for our use-case."
    ],
    "Human-Machine Collaboration": [
        "Having a strong control over an interaction with a robot/ machine/ tool enhances the presence and situational awareness and therefore the success of a remotework application.",
        "In our use-case the integration of human–machine collaboration via IIP could be established.",
        "We believe that human–machine interactions may have a distinctive contribution to fostering a users active engagement in our use-case scenario.",
        "To allow individuals and machines to connect and interact in real time in the virtual world, regardless of their geographical location could be a beneficial extension to our use-case"
        "We could imagine an IIP integration into our current manufacturing systems to decrease scrap and rework, reduce unscheduled downtime, reduce compliance costs, increase throughput and improve our training."
    ]
}
# Collect responses
st.title(f"Assessing the Dimension: {dimension}")
st.write("This dimension analyzes how important simulation and modeling tools are to create accurate, real-world representations within the virtual environment, allowing users to experiment, predict outcomes, and interact with digital twins of physical systems.")
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
progress = 6 / 8  # Adjust this number based on the current dimension page
st.progress(progress)

# Navigation
col1, col2 = st.columns([1, 1])

if col1.button("Previous"):
    st.write("Navigate to the previous page in the sidebar.")

if col2.button("Next"):
    st.write("Navigate to the next page in the sidebar.")