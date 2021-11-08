"""
Author : Joselito
Date: 8-11-2021
Purpose: Validating username and password
"""

# take username and password as user input
username = input("Enter username: ")
password = input("Enter password: ")


# Check if username or password is empty if they are empty  then print the error message
if len(username) == 0 or len(password) == 0:
    print("Password or password cannot be empty")
else:
    # Check for other error cases
    if len(password) > 16:
        print("password cannot be more than 16 less")
    elif len(password) < 8:
        print("password cannot be less than 8 letters")
    else:
        print("username and password are correct")

