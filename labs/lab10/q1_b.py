# Program to print pattern of Numbers
# Eg:
# 1
# 2 2
# 3 3 3

user_input = int(input("Enter number: "))

# print pattern
for i in range(1,user_input+1):
    for j in range(i):
        print(i,end=" ")
    print()


