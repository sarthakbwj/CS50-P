#### Project Name: Student Stream Classification Project
##### Student Name: Sarthak Bhardwaj
#### Place and Country: Pune, India

Video Demo Link:

# Overview

This project processes student data from a CSV file, categorizing students by their academic streams based on the subject they study, and calculating their academic year based on their birth year. The project reads input from a CSV file, processes the data, and writes the results into an output CSV file with three columns: student name, academic stream, and year in school.

# Key Features
Stream Classification: Subjects are classified into three streams: Science, Commerce, and Arts, based on predefined criteria.
Academic Year Calculation: The academic year is calculated based on the student's birth year, assuming that students enter university at 18 years old.
Error Handling: The program handles various command-line argument errors and missing files gracefully, notifying the user when issues occur.

Files
1. new_student.csv
This is the input CSV file containing details of students, including their names, subjects, and birth years.

# Sample content: #

name,subject,birthyear
Rahul,History,2005
Ayush,Finance,2002
Abhay,Chemistry,2004
Jessica,Earth Sciences,2005
Vedanshi,Accountant,2003
Param,Mathematics,2003
Gunjan,Insurance,2002
Sarthak,Philosophy,2005
Karan,Physics,2004
Tejas,Computer Science,2004

2. project.py
This Python script is the core of the project. It processes the input CSV file, classifies each student's subject into a stream, calculates their academic year, and writes the processed data into a new CSV file.

Key Functions:

check_correct_args(): Verifies that the correct number of command-line arguments are provided and that they point to CSV files.
select_stream(sub): Classifies the given subject into one of three streams: Science, Commerce, or Arts.
select_birthyear(year): Calculates the student’s academic year based on their birth year, assuming they start university at age 18.

3. after.csv
This is the output CSV file generated after running project.py. It contains the following headers: name, stream, and year.

# Sample output: #

name,stream,year
Rahul,Arts,Year 1
Ayush,Commerce,Year 4
Abhay,Science,Year 2
Jessica,Science,Year 1
Vedanshi,Commerce,Year 3
Param,Science,Year 3
Gunjan,Commerce,Year 4
Sarthak,Arts,Year 1
Karan,Science,Year 2
Tejas,Science,Year 2


4. test_project.py
This file contains unit tests written using the pytest framework. It tests various components of the project.py script, ensuring that the stream classification and year calculations are correct, and that the program handles command-line arguments properly.

# Tests Included: #

test_check_correct_args(): Ensures correct handling of command-line arguments.
test_select_stream(): Verifies that subjects are correctly classified into their respective streams.
test_select_birthyear(): Confirms that birth years are properly converted into academic years.

# How to Run #

1. Clone the repository:

git clone (https://github.com/sarthakbwj/CS50-P.git)
cd final_project

2. Install the required dependencies (optional):
This project uses only Python's built-in libraries (csv, sys, pytest), so no external dependencies are needed. However, make sure you have Python installed on your system.

3. Run the script:
To execute the script, use the following command:

python project.py new_student.csv after.csv
Here, new_student.csv is the input file, and after.csv is the output file that will be created after processing.

4. Run the tests:
To run the tests using pytest, use this command:

pytest test_project.py
This will execute the tests and verify that the code behaves as expected.

# Error Handling #

The script includes several built-in checks to ensure it runs smoothly:

Command-line Argument Errors: The script will raise an error if too many or too few arguments are provided, or if the input/output files are not in CSV format.
File Not Found: If the input CSV file is missing, the script will exit with a "File not found" message.
Stream Classification: If a subject does not match any predefined categories, it is classified as "No Stream".


# Conclusion #

This project serves as a practical example of working with CSV files in Python, as well as error handling, stream classification, and simple calculations. The addition of unit tests ensures that the program functions as expected, and the streamlined command-line interface makes it easy to run and use.

