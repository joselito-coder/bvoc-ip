# if else conditions

# Program 1
# num = int(input("Enter a number: "))
# Possible comparision operators that can be used with if 
# < (less than)
# <= (less than or equal to)
# > (greater than)
# >= (greater than or equal to)
# == (equal to)
# != (not equal to)
# if num > 5:
#     print("The number is > 5")
# else:
#     print("The number is not > 5")

# Program 2
# TODO



# Else if
# a = 1

# if a == 0 :
#     print('a is zero')
# elif a == 1:
#     print('a is one')
# elif a == 2:
#     print('a is two')
# else:
#     print("a is not zero , one or two")

a = 1

if a > 10 :
    print('a  a > 10')
elif a > 20:
    print(' a > 20')
elif a > 30:
    print(' a > 30')
else:
    print("a is not Greater than 20")



# last program
day = input("Enter day")

if day == 'mon':
    print("Buy 1kg Apples")
elif day == 'tue':
    print('Buy 2kg Onions')
    print('Buy 1kg Rice')
elif day == 'wed':
    print('Buy 2kg banana')
elif day == 'thu':
    print('Buy 2kg mango')
elif day == 'fri':
    print("Buy Ice cream")
else:
    print('Zomato or Swiggy')


per = int(input("Enter percentage(%): "))

if per < 0:
    print("Invalid")
elif per < 40 : 
    print('Fail')
elif per > 100:
    print('Invalid')
else :
    print("Pass")
