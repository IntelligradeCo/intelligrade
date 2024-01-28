import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils import *

# App title and layout
st.title("GPA Calculator")


courses_number = user_selections()
make_table(courses_number)




