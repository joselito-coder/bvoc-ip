n = 1
if n > 5:
    print("a")
if n > 3:
    print("b")
if n > 2:
    print("")


# Scond program
d = input("Enter direction ")
pos = 0

# if d == 'l':
#     print("move left")
#     pos = pos - 1
# elif d == 'r':
#     print('move right')
#     pos = pos +1

# else:
#     print('invalid')

print(pos)

# third program

num1 = int(input('Enter num 1 : '))
num2 = int(input("Enter num2 : "))
op = input("enter math op: ")

# if op == "+":
#     print(num1 + num2)
# elif op == "-":
#     print(num1 - num2)
# elif op == "*":
#     print(num1 * num2)
# elif op == "/":
#     print(num1 / num2)
# else:
#     print("invalid")
if op == "add":
    print(num1 + num2)
elif op == "sub":
    print(num1 - num2)
elif op == "mul":
    print(num1 * num2)
elif op == "div":
    print(num1 / num2)
else:
    print("invalid")