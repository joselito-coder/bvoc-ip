# Write a program to print the n times table till m.


# take m and n
n = int(input("Enter N: "))
m = int(input("Enter M: "))

while m >= 1:
    print(n,"X",m,"=",n*m) 
    m -= 1