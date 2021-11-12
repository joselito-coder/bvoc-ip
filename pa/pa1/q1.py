"""
Author: Joselito
Date: 12-11-2021
Purpose: Basic calculator using python
"""

# Take user input
first_number = int(input("enter num1 : "))
second_number = int(input("enter num2 : "))
operator = input("enter math operator : ")

#  If the user has provided a valid operator then print the result else print error message
if operator == "+":
    print( "The answer is",first_number + second_number)
elif operator == "-":
    print( "The answer is",first_number - second_number)
elif operator == "/":
    print( "The answer is",first_number / second_number)
elif operator == "*":
    print( "The answer is",first_number * second_number)
elif operator == "%":
    print( "The answer is",first_number % second_number)
else:
    print("Invalid operator")
