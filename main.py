"""
Student Grade Calculator
main.py - Entry point and user interface for the terminal application.
"""

from student import Student
from grade_calculator import (
    SUBJECTS,
    calculate_total,
    calculate_percentage,
    calculate_grade,
    determine_result,
    calculate_performance_flag
)


def is_valid_number(text):
    """
    Check if a string represents a valid non-negative number (integer or decimal).
    Uses basic string methods without try/except.
    """
    cleaned = text.strip()
    if len(cleaned) == 0:
        return False

    parts = cleaned.split(".")
    if len(parts) == 1:
        # Integer: must contain only digits
        return parts[0].isdigit()
    elif len(parts) == 2:
        # Decimal: both sides must be digits (e.g. 75.5 or 0.5)
        return parts[0].isdigit() and parts[1].isdigit()
    else:
        return False


def get_valid_mark(subject):
    """
    Prompt the user for a subject mark and validate that it is between 0 and 100.
    Uses while loop and comparison operators.
    """
    while True:
        prompt = "Enter marks for " + subject + " (0 - 100): "
        user_input = input(prompt)

        if is_valid_number(user_input):
            mark = float(user_input)
            if mark >= 0.0 and mark <= 100.0:
                return mark
            else:
                print("Invalid range! Marks must be between 0 and 100.")
        else:
            print("Invalid input! Please enter a valid numerical value.")


def input_student_details():
    """
    Prompt for basic student identification details.
    """
    while True:
        name = input("\nEnter student name   : ").strip()
        if len(name) > 0:
            break
        print("Name cannot be empty. Please enter the student's name.")

    while True:
        roll_no = input("Enter roll number    : ").strip()
        if len(roll_no) > 0:
            break
        print("Roll number cannot be empty. Please enter a valid roll number.")

    return name, roll_no


def input_all_marks(subjects_tuple):
    """
    Collect marks for all subjects defined in the tuple.
    Returns a dictionary mapping subject names to float marks.
    """
    print("\nEnter marks for each subject:")
    marks_dict = {}

    for subject in subjects_tuple:
        mark = get_valid_mark(subject)
        marks_dict[subject] = mark

    return marks_dict


def process_student():
    """
    Handle one complete student evaluation cycle.
    """
    name, roll_no = input_student_details()
    marks_dict = input_all_marks(SUBJECTS)

    # Instantiate the Student object
    student = Student(name, roll_no, marks_dict)

    # Prepare list of numeric marks for calculation
    marks_list = []
    for subject in SUBJECTS:
        marks_list.append(marks_dict[subject])

    # Perform calculations using modular functions
    total = calculate_total(marks_list)
    max_marks = float(len(SUBJECTS) * 100)
    percentage = calculate_percentage(total, max_marks)
    grade = calculate_grade(percentage)
    result = determine_result(marks_dict, grade)
    performance_flag = calculate_performance_flag(result, percentage)

    # Assign calculated results to student object and display report
    student.set_results(total, percentage, grade, result, performance_flag)
    student.display_report()


def main():
    """
    Main application loop.
    Allows calculating multiple student results in a single session.
    """
    print("=" * 46)
    print("        STUDENT GRADE CALCULATOR")
    print("=" * 46)
    print("Welcome! This system calculates totals, percentages,")
    print("grades, and academic standing for 5 subjects.")

    while True:
        process_student()

        # Prompt for next student or exit
        choice = input("\nWould you like to calculate another student? (yes/no): ").strip().lower()
        if choice != "yes" and choice != "y":
            print("\nExiting Student Grade Calculator. Have a great day!")
            break


if __name__ == "__main__":
    main()
