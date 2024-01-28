import streamlit as st
from utils import *

# App title and layout
st.title("GPA Calculator")

# Calling functions from utils to create and run calculator
courses_number = user_selections()
make_table(courses_number)




