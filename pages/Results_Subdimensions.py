import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Function to plot radar chart for each dimension
def plot_radar(categories, values, title="Radar Chart"):
    N = len(categories)
    angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
    values += values[:1]  # Ensure the plot closes at the last point
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)

    ax.fill(angles, values, color='blue', alpha=0.25)
    ax.plot(angles, values, color='blue', linewidth=2)

    ax.set_yticks([1, 2, 3, 4, 5])
    ax.set_yticklabels(['1', '2', '3', '4', '5'])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=10)
    ax.set_title(title)

    return fig

# Function to fetch the values for subdimensions, default to 3 if not filled
def get_subdimension_values(dimension, subdimensions):
    # Ensure that the dimension is correctly structured in session state
    if dimension not in st.session_state.responses or isinstance(st.session_state.responses[dimension], int):
        # If the dimension is missing or is an integer, initialize it as a dictionary
        st.session_state.responses[dimension] = {
            "questions": {},  # For storing individual question responses
            "overall": 3  # Default overall score
        }
    
    # Fetch the values for each subdimension
    values = []
    for subdimension in subdimensions:
        subdimension_key = f"{dimension}-{subdimension}"
        # Default to 3 if no response is found for the subdimension
        values.append(st.session_state.responses[dimension]["questions"].get(subdimension_key, 3))
    
    return values

# Dictionary with dimensions and their respective subdimensions
dimensions = {
    "Identity & Reputation": ["Personalization", "Sociability", "Users"],
    "Presence": ["Immersion", "Sensors", "Interactive Environment"],
    "Social Interactions": ["Collaboration", "Interactive Environment", "Communication", "Interaction"],
    "Collaboration": ["Collaboration", "Co-Creation"],
    "Accessibility": ["Remote Access", "Repeatability", "Public Access"],
    "Economy & Transactions": ["Business Expansion", "Customer Satisfaction", "Operations"],
    "Technology, Structure & Ecosystems": ["Technical Foundation", "Real-Time Processing", "Interoperability", "Ecosystem"],
    "Simulation & Modelling": ["Case Simulation", "Risk-Free Environment", "Smart Factory", "Human-Machine Collaboration"]
}

# Initialize session state responses if not available
if 'responses' not in st.session_state:
    st.session_state.responses = {
        dimension: {"questions": {}, "overall": 3} for dimension in dimensions
    }

# Detailed results page: Spider chart for each dimension
st.title("Detailed Results: Spider Charts for Each Dimension")

# Loop through each dimension and generate the spider chart
for dimension, subdimensions in dimensions.items():
    st.subheader(f"{dimension}")

    # Get the values for subdimensions (default to 3 if not filled)
    values = get_subdimension_values(dimension, subdimensions)

    # Plot the radar chart for this dimension
    fig = plot_radar(subdimensions, values, title=f"{dimension} - Subdimension Scores")
    st.pyplot(fig)
