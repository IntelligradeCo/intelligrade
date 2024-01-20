import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

data = []

# Class Types to GPA
normal_classes_gpa = {
    "A+": 4.0,
    "A": 4.0,
    "A-": 3.7,
    "B+": 3.3,
    "B": 3.0,
    "B-": 2.7,
    "C+": 2.3,
    "C": 2.0,
    "C-": 1.7,
    "D+": 1.3,
    "D": 1.0,
    "F": 0.0
}

honors_classes_gpa = {
    "A+": 4.5,
    "A": 4.5,
    "A-": 4.2,
    "B+": 3.8,
    "B": 3.5,
    "B-": 3.2,
    "C+": 2.8,
    "C": 2.5,
    "C-": 2.2,
    "D+": 1.8,
    "D": 1.5,
    "F": 0.0
}


ib_ap_classes_gpa = {
    "A+": 5.0,
    "A": 5.0,
    "A-": 4.7,
    "B+": 4.3,
    "B": 4.0,
    "B-": 3.7,
    "C+": 3.3,
    "C": 3.0,
    "C-": 2.7,
    "D+": 2.3,
    "D": 2.0,
    "F": 0.0
}

# Function to find out type of class
def class_type():
    class_types = ['Honors', 'AP', 'IB', 'Normal']
    selected_class = st.selectbox('Select Class Type:', class_types)
    return selected_class

def user_selections():
    courses_number = st.number_input("How many courses would you like to calculate GPA for?", 1)
    return courses_number

def make_table(courses_number):
    for i in range(courses_number):
        class_name = st.text_input(f"Class Name {i+1}")
        letter_grade = st.selectbox(f"Letter Grade {i+1}", ('A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'F'))
        class_type = st.selectbox(f"Class Type {i+1}", ('Normal', 'Honors', 'AP', 'IB'))
        data.append([class_name, letter_grade, class_type])
    
        df = pd.DataFrame(data, columns=['Class Name', 'Letter Grade', 'Class Type'])
    st.table(df)

courses_number = user_selections()
make_table(courses_number)

def convert_gpa(selected_class):
    if selected_class == 0:
        print("HI")

user_selections()
make_table()

