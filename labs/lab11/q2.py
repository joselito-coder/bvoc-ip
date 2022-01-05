# Print pattern like the below
"""
4
****
***
**
*
"""
user_input = int(input("Enter Number: "))

for i in range(user_input,0,-1):
    print(i * '*')