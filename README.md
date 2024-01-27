# IntelliGrade GPA Calculator

IntelliGrade GPA Calculator is a web application that allows users to calculate their GPA for different courses based on their letter grades and class types. It supports normal, honors, AP, and IB classes, and follows the standard 4.0 scale. It can be used by students, teachers, parents, or anyone who wants to know their GPA.

## Installation

To install IntelliGrade GPA Calculator, you need to clone the GitHub repository and install the dependencies.

```bash
git clone https://github.com/IntelligradeCo/intelligrade.git
cd intelligrade
pip install -r requirements.txt
```

## Usage

To run IntelliGrade GPA Calculator, you need to launch the Streamlit app.

```bash
streamlit run app.py
```

Then, you can access the web interface at http://localhost:8501 and enter the number of courses you want to calculate GPA for. You will see a table with input fields for each course, where you can enter the class name, letter grade, and class type. The app will automatically calculate the GPA for each course and the average GPA for all courses. You can also see a pie chart that shows the distribution of your grades.

## Features

IntelliGrade GPA Calculator has the following features:

- A user-friendly web interface that allows users to enter and edit their courses and grades
- A dynamic table that displays the courses and grades and updates the GPA in real time
- A validation system that checks the input values and shows error messages if they are invalid

## Technologies

IntelliGrade GPA Calculator is built with the following technologies:

- Python 3.9
- Streamlit 1.2.0
- Pandas 1.3.4
- Matplotlib 3.5.0

## Contributing

IntelliGrade GPA Calculator is an open-source project and welcomes contributions from anyone who is interested. If you want to contribute, please follow these steps:

- Fork the repository and create a new branch
- Make your changes and commit them with a clear message
- Push your branch and create a pull request
- Wait for the review and feedback

## License

IntelliGrade GPA Calculator is licensed under the MIT License. See the LICENSE file for more details.
