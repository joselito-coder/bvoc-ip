# variable names cannot have 3 in the starting, and they are alphanumeric 
# For example
# 342var = 69 # this is not a valid variable
# Variables can't also have special symbols like + - < > 
# Variables can either start with _ or any letter but not numbers
hello_world = "Kono world da" # This is a valid variable

# to take user input we use the input() function
# first_name = input("Enter your name : ")

# print("hello,",first_name)

# type casting
# We can type cast an string returned from input() function into an integer using the int() function
# n1 = input("Enter number : ")
# n2 = input("Enter number : ")

# type casting to int
# n1 = int(n1)
# n2 = int(n2)

#type casting to float
# n1 = float(n1)
# n2 = float(n2)

# calculating result
# result = n1 + n2
# print(result)

# percentage calculating program
name = input("Enter your name: ")

# Taking the input
phy = input("Enter marks in phy: ")
chem = input("Enter marks in chem: ")
bio = input("Enter marks in bio: ")
eng = input("Enter marks in eng: ")
hin = input("Enter marks in hin: ")

# typecast to float
phy = float(phy)
chem = float(phy)
bio = float(phy)
eng = float(phy)
hin = float(phy)

#  add the marks and calculate the percentage
marks = phy + chem + bio + eng + hin
percentage = (marks / 500) * 100

#rounding the percentage
# round() function rounds a number
percentage = round(percentage)

print('percentage of',name,'is',percentage,"%")
