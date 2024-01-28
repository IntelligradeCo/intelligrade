# Imports
import streamlit as st
import pandas as pd

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

# Grades for honor classes
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

# Grades for IB/AP classes
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

# Function to calculate average GPA
def calculate_avg_gpa(df):
    total_gpa = df['GPA'].sum()
    avg_gpa = total_gpa / len(df)
    return avg_gpa

# Function to get User's Name
def user():
    user_name = st.text_input("What's your name?: ")
    if user_name == '':
        print("Please enter your name to save data.")    
    return user_name

# Function to ask user inputs for number of courses
def user_selections():
    courses_number = st.number_input("How many courses would you like to calculate GPA for?", 1)
    return courses_number

# Convert dataframe to csv
def convert_df(df):
    return df.to_csv.encode('utf-8')

# Function to make and empty table using Pandas DataFrame
def make_table(num_rows):
    name = user()
    df = pd.DataFrame(columns=['Class Name', 'Letter Grade', 'Class Type', 'GPA'],
                      index=range(num_rows))
    
    # Display the table with input fields for each cell
    for i in range(num_rows):
        class_name = st.text_input(f"Class Name {i+1}", key=f"class_name_{i}")
        letter_grade = st.selectbox(f"Letter Grade {i+1}", ('A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'F'), key=f"letter_grade_{i}")
        class_type = st.selectbox(f"Class Type {i+1}", ('Normal', 'Honors', 'AP', 'IB'), key=f"class_type_{i}")
        
        if class_type == 'Normal':
            gpa = normal_classes_gpa[letter_grade]
        elif class_type == 'Honors':
            gpa = honors_classes_gpa[letter_grade]
        elif class_type == 'IB' or "AP":
            gpa = ib_ap_classes_gpa[letter_grade]

        df.loc[i] = [class_name, letter_grade, class_type, gpa]
        st.divider()

    
    st.text(f"Unofficial Transcript for {name}")
    # Displaying updated table
    st.table(df)
    # Calling Average GPA function
    avg_gpa = calculate_avg_gpa(df)
    st.write(f"Average GPA: {avg_gpa:.2f}")
    unofficial_transcript = convert_df(df)
    
    st.download_button(
    label="Download data as CSV",
    data=unofficial_transcript,
    file_name='large_df.csv',
    mime='text/csv',
)


    
    # Add save functionality
    if st.button("Save Data"):
        df["Name"] = name    
        df["Average GPA"] = avg_gpa # Add a 'avg_gpa' column
        df.to_csv("gpa_data.csv", index=False)
        st.success("Data saved successfully!")
        st.success("Data saved successfully!")
        # Printing Table for Demo
        st.download_button("Unofficial Transcript", "gpa_data.csv")
        st.table(df)
