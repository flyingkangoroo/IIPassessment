import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Function to plot radar chart
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

# Retrieve responses from session_state
if 'responses' in st.session_state:
    responses = st.session_state.responses
    # Always get all the dimension names
    categories = list(responses.keys())
    
    # Get the actual values (or defaults) for each dimension
    values = [responses[dimension] if dimension in responses else 3 for dimension in categories]

    # Radar chart for the results
    st.subheader("Results - Spider Web Chart for Overall Dimensions")
    fig = plot_radar(categories, values, title="Dimension Averages")
    st.pyplot(fig)

else:
    st.write("No responses found. Please complete the assessment first.")