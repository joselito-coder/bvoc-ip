# data types 
# 'shankar doe'
# 1
# 1.1
# False or True

# If else conditions
# age = int(input("Enter your age "))
# # weight = int(input('Enter your weight '))

# # if age > 20 and weight > 70:
# # if age > 20 :
# #     print("you are allowed to enter")
# # else:
# #     print("not allowed")

username = input('Enter username: ')
password = input('Enter password: ')

isPasswordValid = True
isUsernameValid = True

if len(username) == 0:
    print("username cannot be empty")
    isUsernameValid = False

if len(password) < 6:
    print("Please enter a password > 6 characters")
    isPasswordValid = False

if isPasswordValid and isUsernameValid:
    print("Valid details")
else:
    print("Invalid details")