"""
Student Grade Calculator
tests/test_project.py - Unit verification using plain Python assert statements.
"""

import sys
import os

# Add the parent project directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from student import Student
from grade_calculator import (
    SUBJECTS,
    FLAG_PASS,
    FLAG_DISTINCTION,
    calculate_total,
    calculate_percentage,
    calculate_grade,
    determine_result,
    calculate_performance_flag,
    get_standing_description
)


def test_calculate_total():
    """Verify total calculation using array summation."""
    marks = [85.0, 90.0, 78.0, 82.0, 75.0]
    total = calculate_total(marks)
    assert round(total, 1) == 410.0, "Total calculation failed!"
    print("[OK] test_calculate_total passed")


def test_calculate_percentage():
    """Verify percentage calculation and operator precedence."""
    total = 410.0
    max_marks = 500.0
    percentage = calculate_percentage(total, max_marks)
    assert round(percentage, 2) == 82.0, "Percentage calculation failed!"
    print("[OK] test_calculate_percentage passed")


def test_calculate_grade():
    """Verify grade boundary logic."""
    assert calculate_grade(95.0) == "A+", "Grade A+ check failed!"
    assert calculate_grade(90.0) == "A+", "Grade A+ boundary failed!"
    assert calculate_grade(85.0) == "A", "Grade A check failed!"
    assert calculate_grade(80.0) == "A", "Grade A boundary failed!"
    assert calculate_grade(75.0) == "B", "Grade B check failed!"
    assert calculate_grade(65.0) == "C", "Grade C check failed!"
    assert calculate_grade(55.0) == "D", "Grade D check failed!"
    assert calculate_grade(45.0) == "E", "Grade E check failed!"
    assert calculate_grade(35.0) == "F", "Grade F check failed!"
    print("[OK] test_calculate_grade passed")


def test_determine_result():
    """Verify pass/fail logic with individual subject thresholds."""
    # Case 1: Student passed all subjects
    passing_marks = {
        "Python": 80.0,
        "Mathematics": 75.0,
        "Computer Fundamentals": 85.0,
        "English": 70.0,
        "Communication Skills": 65.0
    }
    assert determine_result(passing_marks, "B") == "PASS", "Pass result check failed!"

    # Case 2: Student failed one subject even if overall marks are high
    failing_marks = {
        "Python": 95.0,
        "Mathematics": 90.0,
        "Computer Fundamentals": 35.0,  # Below 40
        "English": 88.0,
        "Communication Skills": 80.0
    }
    assert determine_result(failing_marks, "B") == "FAIL", "Fail subject check failed!"
    print("[OK] test_determine_result passed")


def test_bitwise_performance_flags():
    """Verify bitwise flags encoding and decoding."""
    # Pass with Distinction (>= 75.0%)
    status_distinction = calculate_performance_flag("PASS", 82.0)
    assert status_distinction == (FLAG_PASS | FLAG_DISTINCTION), "Bitwise distinction encoding failed!"
    assert (status_distinction & FLAG_PASS) != 0, "Bitwise pass check failed!"
    assert (status_distinction & FLAG_DISTINCTION) != 0, "Bitwise distinction check failed!"
    assert get_standing_description(status_distinction) == "Passed with Distinction"

    # Pass without Distinction (< 75.0%)
    status_regular_pass = calculate_performance_flag("PASS", 68.0)
    assert status_regular_pass == FLAG_PASS, "Bitwise regular pass failed!"
    assert (status_regular_pass & FLAG_DISTINCTION) == 0, "Bitwise non-distinction check failed!"
    assert get_standing_description(status_regular_pass) == "Passed"

    # Fail
    status_fail = calculate_performance_flag("FAIL", 45.0)
    assert status_fail == 0, "Bitwise fail flag check failed!"
    assert get_standing_description(status_fail) == "Failed / Needs Improvement"
    print("[OK] test_bitwise_performance_flags passed")


def test_student_class():
    """Verify Student class attributes, methods, and identity operator."""
    marks = {"Python": 90.0, "Mathematics": 85.0}
    student = Student("John Doe", "CS101", marks)

    # Check identity before calculation
    assert student.total is None, "Student total should initially be None!"

    # Set results and verify identity check
    student.set_results(175.0, 87.5, "A", "PASS", 3)
    assert student.total is not None, "Student total should not be None after assignment!"
    assert student.name == "John Doe"
    assert student.roll_no == "CS101"
    assert student.grade == "A"
    assert student.result == "PASS"
    print("[OK] test_student_class passed")


def run_all_tests():
    """Run all verification tests."""
    print("=" * 46)
    print("RUNNING STUDENT GRADE CALCULATOR TESTS")
    print("=" * 46)
    test_calculate_total()
    test_calculate_percentage()
    test_calculate_grade()
    test_determine_result()
    test_bitwise_performance_flags()
    test_student_class()
    print("=" * 46)
    print("ALL TESTS PASSED SUCCESSFULLY! (6/6)")
    print("=" * 46)


if __name__ == "__main__":
    run_all_tests()
