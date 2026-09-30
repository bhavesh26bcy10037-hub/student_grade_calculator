"""
Student Grade Calculator
student.py - Contains the Student class representing a student's academic record.
"""

from grade_calculator import get_standing_description


class Student:
    """
    A simple class to represent a student and their academic results.
    """

    def __init__(self, name, roll_no, marks):
        """
        Initialize the Student instance with basic details.
        """
        self.name = name
        self.roll_no = roll_no
        self.marks = marks  # Dictionary of subject-wise marks
        self.total = None
        self.percentage = None
        self.grade = None
        self.result = None
        self.performance_flag = 0

    def set_results(self, total, percentage, grade, result, performance_flag):
        """
        Store the calculated academic metrics for the student.
        """
        self.total = total
        self.percentage = percentage
        self.grade = grade
        self.result = result
        self.performance_flag = performance_flag

    def display_report(self):
        """
        Print the student result card in a clean, readable text format.
        """
        # Identity operator check to ensure calculations were performed
        if self.total is None:
            print("Error: Results have not been calculated yet.")
            return

        standing = get_standing_description(self.performance_flag)
        max_possible_marks = float(len(self.marks) * 100)

        print("\n" + "=" * 46)
        print("                STUDENT RESULT")
        print("=" * 46)
        print("Name       : " + self.name)
        print("Roll No    : " + self.roll_no)
        print("-" * 46)
        print("Subject-wise Marks:")
        for subject in self.marks:
            mark = self.marks[subject]
            # Simple formatted output using basic string alignment
            print("  " + subject + " " * (26 - len(subject)) + ": " + str(mark) + " / 100")
        print("-" * 46)
        print("Total Marks: " + str(self.total) + " / " + str(max_possible_marks))
        print("Percentage : " + str(round(self.percentage, 2)) + "%")
        print("Grade      : " + self.grade)
        print("Result     : " + self.result)
        print("Standing   : " + standing)
        print("=" * 46)
