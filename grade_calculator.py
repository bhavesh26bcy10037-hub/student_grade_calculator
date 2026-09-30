"""
Student Grade Calculator
grade_calculator.py - Calculation logic, data structures, and evaluation metrics.
"""

from array import array

# Tuple: A fixed, immutable collection of subject names
SUBJECTS = (
    "Python",
    "Mathematics",
    "Computer Fundamentals",
    "English",
    "Communication Skills"
)

# Set: Unique collection of valid grade designations
VALID_GRADES = {"A+", "A", "B", "C", "D", "E", "F"}

# Frozenset: Immutable set of passing grades
PASSING_GRADES = frozenset({"A+", "A", "B", "C", "D", "E"})

# Bitwise flags for student performance status
FLAG_PASS = 1         # Bit 0 (0b0001): Passed all subjects
FLAG_DISTINCTION = 2  # Bit 1 (0b0010): Scored 75% or above


def calculate_total(marks_list):
    """
    Calculate the total marks using Python's standard array data structure.
    Demonstrates: array module, type() function, and arithmetic assignment (+=).
    """
    # Create an array of single-precision floating-point numbers ('f')
    marks_array = array('f', marks_list)

    # Simple type demonstration on array elements
    if len(marks_array) > 0:
        first_element_type = type(marks_array[0])
        # Verifying type naturally without unnecessary complexity
        if first_element_type is not float:
            pass

    total = 0.0
    for mark in marks_array:
        total += mark

    return total


def calculate_percentage(total, max_marks):
    """
    Calculate the percentage score.
    Demonstrates: operator precedence with parentheses, arithmetic division
    with mixed numeric types (float and int).
    """
    percentage = (total / max_marks) * 100.0
    return percentage


def calculate_grade(percentage):
    """
    Determine the letter grade based on the percentage.
    Demonstrates: if/elif/else ladder, relational operators (>=, <),
    and logical AND operator.
    """
    if percentage >= 90.0:
        grade = "A+"
    elif percentage >= 80.0 and percentage < 90.0:
        grade = "A"
    elif percentage >= 70.0 and percentage < 80.0:
        grade = "B"
    elif percentage >= 60.0 and percentage < 70.0:
        grade = "C"
    elif percentage >= 50.0 and percentage < 60.0:
        grade = "D"
    elif percentage >= 40.0 and percentage < 50.0:
        grade = "E"
    else:
        grade = "F"

    # Membership operator check against set of valid grades
    if grade in VALID_GRADES:
        return grade
    return "F"


def determine_result(marks_dict, grade, passing_mark=40.0):
    """
    Determine whether the student passed or failed.
    A student passes only if they score >= passing_mark in EVERY subject
    AND their overall grade is in PASSING_GRADES.
    Demonstrates: for loop, relational operators, membership operator with frozenset,
    and logical AND, NOT, OR operators.
    """
    has_failed_subject = False

    for subject in marks_dict:
        mark = marks_dict[subject]
        if mark < passing_mark:
            has_failed_subject = True
            break

    # frozenset membership check
    has_passing_grade = grade in PASSING_GRADES

    # Condition using logical NOT, AND, and OR
    if (not has_failed_subject) and has_passing_grade:
        return "PASS"
    else:
        return "FAIL"


def calculate_performance_flag(result, percentage):
    """
    Encode student standing using bitwise OR (|) operator.
    - Bit 0 (1): Academic Pass
    - Bit 1 (2): Distinction (>= 75.0%)
    """
    status = 0

    if result == "PASS":
        status = status | FLAG_PASS
        if percentage >= 75.0:
            status = status | FLAG_DISTINCTION

    return status


def get_standing_description(status):
    """
    Decode student standing using bitwise AND (&) operator.
    """
    is_passed = (status & FLAG_PASS) != 0
    is_distinction = (status & FLAG_DISTINCTION) != 0

    if is_passed and is_distinction:
        return "Passed with Distinction"
    elif is_passed and not is_distinction:
        return "Passed"
    else:
        return "Failed / Needs Improvement"
