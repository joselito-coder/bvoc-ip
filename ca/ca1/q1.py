"""
Author : Joselito
Date: 8-11-2021
Purpose: Printing grade of a student based on their marks
"""

# take the user input about their grade
student_grade = int(input("Enter grade: "))

# Check for each condition and output the grade
if student_grade >=51 and student_grade <= 60:
    print("A")
elif student_grade >= 41 and student_grade <= 50:
    print("B")
elif student_grade >= 31 and student_grade <= 40:
    print("C")
elif student_grade >= 21 and student_grade <= 30:
    print("D")
elif student_grade >= 11 and student_grade <= 20:
    print("E")
elif student_grade >= 0 and student_grade <= 10:
    print("F")
else:
    print("Invalid grade")

