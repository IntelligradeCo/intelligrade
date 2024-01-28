import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils import *

# App title and layout
st.title("GPA Calculator")

# Sidebar navigation
st.sidebar.title("Navigation")
selected_feature = st.sidebar.selectbox("Select a Feature:", ["GPA Calculator", "Grade Tracker"])

# Main content area
if selected_feature == "GPA Calculator":
    # Calling make_table function
    courses_number = user_selections()
    make_table(courses_number)
elif selected_feature == "Grade Tracker":
    grade_tracker()

backup_consent = st.checkbox("Would you like to save your information for future use?")
if backup_consent == True:
    st.text_input("What's your name?: ")
    save_gpa()

