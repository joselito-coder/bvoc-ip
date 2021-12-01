"""
Author: Joselito
Date: 12-11-2021
Purpose: Calculate from user given expression 
"""
# Take user input
user_expression = input("enter statement: ")

# split the expression so that the numbers and operators are extractable
expression_eval = user_expression.split(" ")

# Extract the first number, last number and the operator from the string
first_number = expression_eval[0]
last_number = expression_eval[-1]
operator = expression_eval[1]

# Check if the user has provided valid argument
if first_number.isnumeric() and last_number.isnumeric():
    # typecast values
    first_number = int(first_number)
    last_number = int(last_number)

    #  If the user has provided a valid operator then print the result else print error message
    if operator == "+":
        print( "The answer is",first_number + last_number)
    elif operator == "-":
        print( "The answer is",first_number - last_number)
    elif operator == "/":
        print( "The answer is",first_number / last_number)
    elif operator == "*":
        print( "The answer is",first_number * last_number)
    elif operator == "%":
        print( "The answer is",first_number % last_number)
    else:
        print("Malformed Expression")
# Print error message if not
else:
    print("Malformed Expression")