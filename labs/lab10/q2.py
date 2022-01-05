# program to add and print the total of the digits in a numbers


user_input = input("enter your number : ")

if user_input.isnumeric():
    sum = 0

    for number in user_input:
        sum += int(number)
    
    print(sum)

else:
    print("Please enter a valid number")