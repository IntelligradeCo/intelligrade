import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Function to find out type of class
def class_type():
    class_types = ['Honors', 'AP', 'IB', 'Normal']
    selected_class = st.selectbox('Select Class Type:', class_types)
    return selected_class

class_type()