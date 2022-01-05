# Program to print the below pattern
"""
4
    *
   **
  ***
 ****
"""

user_input = int(input("Enter Number : "))

spaces = user_input
for i in range(1,user_input+1):

    # print spaces
    for j in range(spaces):
        print(' ',end="")
    
    spaces -= 1

    # print star
    for k in range(i):
        print("*",end='')

    # new line
    print()
    