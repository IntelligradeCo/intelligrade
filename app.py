import streamlit as st
import pandas as pd

# Function to calculate GPA
def calculate_gpa(grades):
    # Your GPA calculation logic goes here
    # This is a simple example, you should customize it based on your school's grading scale
    gpa = sum(grades) / len(grades)
    return round(gpa, 2)

# Function to save data to CSV
def save_to_csv(data, filename='gpa_data.csv'):
    df = pd.DataFrame(data, columns=['Student Name', 'Grades', 'GPA'])
    df.to_csv(filename, index=False)

# Function to load data from CSV
def load_from_csv(filename='gpa_data.csv'):
    try:
        df = pd.read_csv(filename)
        return df.to_dict(orient='records')
    except FileNotFoundError:
        return []

# Main Streamlit app
def main():
    st.title('GPA Calculator')

    # Load existing data or initialize an empty list
    data = load_from_csv()

    # User input section
    student_name = st.text_input('Enter Student Name:')
    grades_str = st.text_input('Enter Grades (comma-separated):')

    if st.button('Calculate GPA'):
        try:
            grades = [float(grade.strip()) for grade in grades_str.split(',')]
            gpa = calculate_gpa(grades)
            st.success(f'{student_name}\'s GPA: {gpa}')

            # Save data to list
            data.append({'Student Name': student_name, 'Grades': grades, 'GPA': gpa})

            # Save data to CSV
            save_to_csv(data)

        except ValueError:
            st.error('Invalid input. Please enter grades as numbers separated by commas.')

    # Display existing data
    st.subheader('Existing Data:')
    df = pd.DataFrame(data)
    st.dataframe(df)

main()
