# Take name and phone number as input from user
name = input("Enter name: ")
phone_number = input("Enter PhoneNumber: ")

# validate phone number
if len(phone_number) == 10 and phone_number.isdigit():
    print("Nice phone number")
else:
    print("Invalid Phone number")

# validate name
if len(name) < 1:
    print("Invalid name")
else:
    print("Nice name",name,":)")