#  Program to print below pattern
"""
4

   *
  ***
 *****
*******
"""

user_input = int(input("Enter Number: "))
spaces = user_input-1
stars = 1

for i in range(1,user_input +1):

    # print spaces
    for space in range(spaces):
        print(' ',end='')
    
    spaces -= 1

    for star in range(stars):
        print('*',end="")
    stars += 2
    
    print()