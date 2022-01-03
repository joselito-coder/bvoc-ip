# Program that prints the odd and even numbers that the user inputeed

# function to print a list
def print_list(list,prompt):
    print(prompt)
    for element in list:
        print(element)

# function to check if a number is even 
def isEven(number):
    return number % 2 == 0


user_num = int(input("Enter your number: "))

# init list
even_numbers_list = []
odd_numbers_list = []

# Take user numbers
for i in range(user_num):
    num = int(input("number: "))
    if isEven(num):
        even_numbers_list.append(num)
    else:
        odd_numbers_list.append(num)

# print odd and even numbers
print_list(even_numbers_list,"Even: ")
print_list(odd_numbers_list,"Odd: ")