number1 = int(input("Enter number1 :"))
math_op1 = (input("Enter a math op1 :"))
user = input("Do you want to continue(y/n) ")

if user == "y":
    number2 = int(input("Enter number2 :"))
    math_op2 = (input("Enter a math op2 :"))
    user = input("Do you want to continue(y/n) ")

if user == "y":
    number3 = int(input("Enter number3 :"))
    math_op3 = (input("Enter a math op3 :"))
    user = input("Do you want to continue(y/n) ")

if user == "n":
    result = (number1 + number2 - number3)
    output = "result :" + math_op1 + \
        str(number1)+math_op2+str(number2) + \
        math_op3+str(number3)+" =" + str(result)

    file = open('q1.txt', 'w')
    file.write(output)
