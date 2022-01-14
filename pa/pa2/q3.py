# Q3. Take input for phone number, full name and age. ( phone number has to be 10chars, name cannot be empty, age has to be greater than 15 )

def validate_number(PhNumStr):
    if PhNumStr.isnumeric() and len(PhNumStr) == 10:
        return True
    return False
    

def validate_name(name):
    if len(name) == 0:
        return False
    return True
    

def validate_age(age):
    if age > 15:
        return True
    return False

phone_number = input("enter Phone number: ")
full_name = input("Enter full name: ")
age = int(input("Enter age: "))

if not validate_number(phone_number):
    print("Phone Number invalid")
elif not validate_name(full_name):
    print("Name should not be blank")
elif not validate_age(age):
    print("Age should be greater than 15")
else:
    print("Everything is valid, You can now proceed")





