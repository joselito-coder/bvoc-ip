# Question --> take input for a string and an integer, print the character at that given index. ( an error message should print the integer entered is greater than the Len of the string )

# Solution
# Take string as an input from the user
user_string = input("Enter any string: ")

# take an index integer from the user 
user_index = int(input("Enter any number which is less than the length of string: "))

# check if the integer entered by the user is greater than the user string
# len(user_string) -1 because the index of a string starts from zero so we would have to deduct 1 from the original string
if user_index > len(user_string) - 1 :
    print("Invalid")
else:
    print(user_string[user_index])
