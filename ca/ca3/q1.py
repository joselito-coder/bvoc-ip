# a program that mimics a working of a simple calculator.


# initial values
cont = 'y'
num_list = []


# Function to write output
def write_output(result):

    # Generate output string
    str_list = []
    for i in num_list:
        str_list.append(str(i))
    output_str = 'Answer is '
    op_pad = ' '+math_op+' '
    mult_str = op_pad.join(str_list)
    output_str += mult_str + ' = ' + str(result)

    # write the output to the file
    file = open('q1.txt','w')
    file.write(output_str)
    file.close()

    print("output is written to q1.txt")


# function to calculate the answer
def calc(num_list,operator):

    initial = 0
    initial_mult = 1

    if operator == '*':
        for number in num_list:
            initial_mult *= number
        
        return initial_mult

    elif operator == '+':
        for number in num_list:
            initial += number
        return initial


    elif operator == '-':
        for number in num_list:
            initial -= number
        return initial

    elif operator == '/':
        for number in num_list:
            initial -= number
        return initial

    

# Loop for taking input of  numbers 
while cont == 'y':
    number = int(input("Enter a number: "))
    num_list.append(number)

    cont = input("do you want to continue(y/n): ")


math_op = input("Enter math op: ")

# calculate result and write output
result = calc(num_list,math_op)
write_output(result)
