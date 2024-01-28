import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils import *

# App title and layout
st.title("GPA Calculator")


# Main content area
if selected_feature == "GPA Calculator":
    # Calling make_table function
    courses_number = user_selections()
    make_table(courses_number)




