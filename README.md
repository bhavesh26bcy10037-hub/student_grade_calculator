# Student Grade Calculator

A simple, command-line Python application developed for a first-year **Python Essentials** course. This program calculates total marks, percentage, grade, pass/fail status, and academic standing for students based on their performance across five core subjects.

---

## 1. Project Description

The **Student Grade Calculator** is a menu-driven terminal tool designed to automate student grade evaluation. It takes student details (Name and Roll Number) along with marks scored in 5 fixed subjects (out of 100). The program computes the overall total, percentage score, assigns a letter grade, checks whether the student passed all individual subjects, and displays an academic result card in the terminal.

The project is structured across modular Python files to demonstrate object-oriented programming, data structures, and operators covered in a foundational Python curriculum.

---

## 2. Objective

The primary objectives of this project are:
* To practice core Python fundamentals in a realistic, beginner-friendly application.
* To demonstrate the use of standard Python data structures (`tuple`, `list`, `dict`, `set`, `frozenset`, and `array`).
* To apply arithmetic, relational, logical, membership, identity, and bitwise operators.
* To structure code cleanly into separate modules and classes without relying on third-party frameworks.
* To validate user input gracefully without complex libraries or unlearned constructs.

---

## 3. Features

* **Terminal-Based Interface**: Runs completely from standard command-line environments.
* **Input Validation**: Ensures marks are valid numbers between 0 and 100 without using advanced exception handling.
* **Array-Based Processing**: Utilizes Python's built-in `array` module for numeric calculation.
* **Comprehensive Evaluation**:
  * Total score calculation out of 500.
  * Exact percentage calculation.
  * Standard letter grading (`A+` to `F`).
  * Pass/Fail determination (must score at least 40 in every subject to pass).
  * Academic standing flags (Pass with Distinction for scores 75% and above).
* **Multi-Student Support**: Process results for multiple students consecutively in a single session.
* **Clean Result Card**: Displays a formatted ASCII report card in the console.

---

## 4. Python Concepts Used

This project strictly adheres to the first-year Python syllabus topics:

| Topic | Implementation in Project |
| :--- | :--- |
| **Python Fundamentals & I/O** | `print()` statements for report cards and banners, `input()` for reading user values. |
| **Membership Operators (`in`, `not in`)** | Checking if a grade exists in `VALID_GRADES` and `PASSING_GRADES`. |
| **Assignment Operators (`=`, `+=`)** | Variable assignments and accumulator sum in the `calculate_total` loop. |
| **Bitwise Operators (`\|`, `&`)** | Encoding and decoding academic standing flags (`FLAG_PASS = 1`, `FLAG_DISTINCTION = 2`). |
| **`type()` Function** | Inspecting array element data types in `calculate_total`. |
| **Identity Operators (`is`, `is not`)** | Checking if `student.total is None` before printing reports, and type comparisons. |
| **Arithmetic Operators (`+`, `/`, `*`)** | Summation, division, and percentage calculations. |
| **Division with Mixed Data Types** | Float-by-int division: `(total / max_marks) * 100.0`. |
| **Operator Precedence** | Natural use of parentheses in mathematical calculations. |
| **Type Conversion** | Converting string inputs to floats using `float()` and formatting with `str()`. |
| **Relational Operators** | `<`, `>`, `<=`, `>=`, `==`, `!=` for boundary conditions and grade thresholds. |
| **Logical Operators (`and`, `or`, `not`)** | Compound conditional logic in grade assignment and subject pass verification. |
| **Control Flow (`if`, `elif`, `else`, `for`, `while`)** | Multi-branch grade assignment, subject iteration, and validation loops. |
| **Functions** | Dedicated, single-purpose functions in `grade_calculator.py` and `main.py`. |
| **Modules & Packages** | Separation of concerns across `student.py`, `grade_calculator.py`, and `main.py`. |
| **Array Data Structure** | `array('f', marks_list)` for numerical storage and computation. |
| **Core Data Structures** | |
| • `tuple` | Fixed subjects tuple: `SUBJECTS = ("Python", "Mathematics", ...)` |
| • `list` | Collecting user inputs prior to array conversion. |
| • `dict` | Mapping subject names to their respective marks (`{"Python": 85.0, ...}`). |
| • `set` | Collection of unique allowable grades `VALID_GRADES`. |
| • `frozenset` | Immutable set of passing grades `PASSING_GRADES`. |
| **Object-Oriented Programming** | Simple `Student` class with attributes and methods. |

---

## 5. Project Structure

```text
student-grade-calculator/
│
├── main.py                 # Main entry point and user interaction loop
├── student.py              # Beginner-friendly Student class definition
├── grade_calculator.py     # Core calculations, data structures, and bitwise logic
├── README.md               # Documentation and execution guide
└── tests/
    └── test_project.py     # Standalone assertions test script
```

---

## 6. Requirements

* **Python Version**: Python 3.6 or higher.
* **External Dependencies**: None. Uses only standard Python library modules (`array`, `sys`, `os`).

---

## 7. How to Install Python

If Python is not already installed on your system:

### On Windows
1. Visit the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Download the latest Python 3 installer.
3. Run the installer and ensure you check the box: **"Add Python to PATH"**.
4. Complete the installation wizard.

### On macOS / Linux
* **macOS**: Install via Homebrew: `brew install python3` or download the installer from python.org.
* **Linux (Ubuntu/Debian)**: Run `sudo apt update && sudo apt install python3` in the terminal.

Verify installation by running:
```bash
python --version
# or
python3 --version
```

---

## 8. How to Download the Project

1. Download or extract the project folder `student-grade-calculator` to your local computer.
2. Open your terminal (Command Prompt, PowerShell, or Terminal).
3. Navigate into the project directory:
   ```bash
   cd student-grade-calculator
   ```

---

## 9. How to Run the Project from Terminal

### Running the Application
From inside the project directory, run:
```bash
python main.py
```
*(On macOS/Linux systems where `python` points to Python 2, use `python3 main.py`)*

### Running the Automated Tests
The project includes self-contained test cases using plain Python assertions:
```bash
python tests/test_project.py
```
*(Or `python3 tests/test_project.py`)*

---

## 10. Example Execution

```text
==============================================
        STUDENT GRADE CALCULATOR
==============================================
Welcome! This system calculates totals, percentages,
grades, and academic standing for 5 subjects.

Enter student name   : Rahul Sharma
Enter roll number    : CS-2026-101

Enter marks for each subject:
Enter marks for Python (0 - 100): 88.5
Enter marks for Mathematics (0 - 100): 92.0
Enter marks for Computer Fundamentals (0 - 100): 79.0
Enter marks for English (0 - 100): 84.0
Enter marks for Communication Skills (0 - 100): 76.5

==============================================
                STUDENT RESULT
==============================================
Name       : Rahul Sharma
Roll No    : CS-2026-101
----------------------------------------------
Subject-wise Marks:
  Python                    : 88.5 / 100
  Mathematics               : 92.0 / 100
  Computer Fundamentals     : 79.0 / 100
  English                   : 84.0 / 100
  Communication Skills      : 76.5 / 100
----------------------------------------------
Total Marks: 420.0 / 500.0
Percentage : 84.0%
Grade      : A
Result     : PASS
Standing   : Passed with Distinction
==============================================

Would you like to calculate another student? (yes/no): no

Exiting Student Grade Calculator. Have a great day!
```

---

## 11. Grade Calculation Logic

Marks are assigned based on the overall percentage score:

| Percentage Range | Grade | Description |
| :--- | :--- | :--- |
| **90% – 100%** | **A+** | Outstanding |
| **80% – 89.99%** | **A** | Excellent |
| **70% – 79.99%** | **B** | Very Good |
| **60% – 69.99%** | **C** | Good |
| **50% – 59.99%** | **D** | Satisfactory |
| **40% – 49.99%** | **E** | Pass |
| **Below 40%** | **F** | Fail |

### Pass/Fail Rules
1. A student must achieve at least **40.0 marks in each individual subject**. Scoring below 40 in even one subject results in a **FAIL** regardless of the overall percentage.
2. The overall grade must be in the passing set (`A+`, `A`, `B`, `C`, `D`, or `E`).

### Standing Criteria (Bitwise Evaluation)
* **Passed with Distinction**: Student passed all subjects AND achieved an overall percentage of 75.0% or higher.
* **Passed**: Student passed all subjects with a percentage between 40.0% and 74.99%.
* **Failed / Needs Improvement**: Student failed one or more subjects or achieved less than 40.0% overall.

---

## 12. Limitations

* **Session Memory Only**: Records exist only during runtime and are not saved to a database or file.
* **Terminal Interface**: Designed strictly for standard text consoles without a graphical interface.
* **Fixed Subjects**: Configured for 5 standard first-year computer science subjects.

---

## 13. Author

* **Course**: Python Essentials (First-Year Coursework)
* **Project**: Student Grade Calculator
