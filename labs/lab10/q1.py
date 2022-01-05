# python program to print pattern according to the user input
# Eg:
# Enter Number: 3
# +
# ++
# +++


user_input = int(input("Enter number: "))

# print pattern
for i in range(1,user_input + 1):
    print(i * '+')