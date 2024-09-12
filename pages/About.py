import streamlit as st

# Set page title and layout
st.set_page_config(page_title="About the Business Use-Case Viability Model", layout="centered")

# Page title
st.title("About the Business Use-Case Viability Assessment Model")

# Introduction section
st.markdown("""
### Overview

The **Business Use-Case Viability Assessment Tool** is part of a prototype developed during a **Master's Thesis**. This model evaluates the feasibility of business use-cases that may benefit from **Industrial Immersive Platforms (IIPs)**, like those found in the **Industrial Metaverse**.

This tool was constructed as part of a research project aimed at exploring how businesses can leverage immersive platforms to optimize their operations. It combines several research approaches, including literature reviews and qualitative interviews, to create a practical and academically informed framework.

---

### Methodology

The construction of this model follows a **Design Science Research (DSR)** methodology. This approach is commonly used to create and evaluate artifacts (such as models and tools) that solve real-world problems. The DSR methodology used here involved the following key stages:

1. **Problem Identification**: 
   The lack of structured approaches for evaluating the viability of immersive platforms in industrial settings was identified as a gap in current research and practice.

2. **Literature Review**: 
   A **Systematic Literature Review (SLR)** was conducted to gather data on existing use-cases of the industrial metaverse, identifying over 262 unique characteristics that affect the viability of different use-cases.

3. **Qualitative Interviews**: 
   Following the SLR, **20 semi-structured interviews** were conducted with industry experts. These interviews helped refine the dimensions identified in the literature review and ensured that the model was aligned with real-world industrial needs.

4. **Model Construction**: 
   The data collected through the literature review and interviews were analyzed using **Grounded Theory** and the **Gioia Methodology**. This process allowed the development of a set of dimensions that guide the assessment of the viability of different industrial immersive platform use-cases.

---

### Research Context

This project is grounded in **Design Science Research (DSR)**, which emphasizes the creation of solutions that are both academically rigorous and practically applicable. The model provides valuable insights for businesses looking to expand into the industrial metaverse, helping decision-makers evaluate which use-cases offer the highest potential for success.

The tool is a **prototype** and was developed specifically as part of a **Master’s Thesis** in **Business Innovation**. The research draws from recent advances in **Industry 4.0** technologies, such as **Virtual Reality (VR)**, **Augmented Reality (AR)**, and **Mixed Reality (MR)**, and applies them to industrial use-cases.

---

### Prototype Disclaimer

Please note that this is a **prototype**. While it has been designed with rigorous academic backing, further validation and testing are required before it can be fully implemented in an industrial setting.

---
""")

# Add a "continue" button to return to the main page or assessment
if st.button("continue with Assessment"):
    st.write("You can navigate using the sidebar.")
