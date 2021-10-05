# Program to classify percentage according to category

# Take percentage as input from the user
percentage = int(input("Enter your percentage: "))

if percentage < 0:
    print("Invalid")
# Condition for failing
elif percentage < 40:
    print("Fail")
# Condition for pass class
elif percentage < 50:
    print("Pass class")
# Condition for second class
elif percentage < 60:
    print("Second class")
# Condition for First class
elif percentage < 75:
    print("First class")
# Condition for Distinction class
elif percentage <= 100:
    print("Distinction")
# Validating other corner cases (Invalid percentages)

elif percentage > 100:
    print("Invalid")
else:
    print("Invalid")
