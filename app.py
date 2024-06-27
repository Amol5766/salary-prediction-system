import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from explore_page import show_explore_page
from predict_page import show_predict_page

# Function definitions remain the same...

# Set page title and favicon
def main():
    st.set_page_config(
        page_title="",
        page_icon="😶‍🌫️",
        layout="wide",
        initial_sidebar_state="auto",
    )

# Add a stylish header with a 3D effect and light red title
st.markdown(
    """
    <style>
    .st-title {
        color: rgb(255, 75, 75); /* Light red color */
    }

    .stFrame {
        background-color: #00BFFF; /* Neon blue background */
        box-shadow: 0 0 20px rgba(255, 7, 58, 1.00);
        border-radius: 20px;
        padding: 40px;
    }
    </style>
    """
    , unsafe_allow_html=True
)

st.markdown("<h1 class='st-title'>Welcome to AI Insight 🚀</h1>", unsafe_allow_html=True)



# Sidebar navigation
page = st.sidebar.selectbox("Choose an Option", ("Predict", "Explore"))

# Create a CSS class for the content frame with 3D styling and neon blue background
st.markdown(
    """
    <style>
    .stTitle {
        color: rgb(255 75 75 / 88%); /* Change color to red with alpha transparency */
    }

    .stFrame {
        background-color: #00BFFF; /* Neon blue background */
        box-shadow: 0 0 20px rgba(255, 7, 58, 1.00);
        border-radius: 20px;
        padding: 40px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Show the selected page with the 3D frame
if page == "Predict":
    show_predict_page()
else:
    show_explore_page()

# Add a footer with modern styling
st.sidebar.markdown("About >>>")
st.sidebar.info("Made by SHAMBHAVI")

# Optional: Add a 3D floating button for feedback or contact
st.markdown(
    """
    <style>
    .feedback-button {
        position: fixed;
        bottom: 20px;
        right: 20px;
        background-color: #00BFFF;
        color: black;
        border: none;
        border-radius: 50%;
        width: 60px;
        height: 60px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        font-size: 34px;
        cursor: pointer;
    }
    </style>
    <a href="gmailto:shambhaviyalagach@gmail.com" class="feedback-button" target="_blank">💟</a>
    """,
    unsafe_allow_html=True,
)