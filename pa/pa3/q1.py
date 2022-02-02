
cont = 'y'

def calc_result(op,fNum,sNum):
    if op == '+':
        return fNum + sNum
    elif op == '-':
        return fNum - sNum
    elif op == '/':
        return fNum / sNum
    elif op == '*':
        return fNum * sNum

def gen_output(numlist,oplist):
    steps = 1
    initialNumber = 0

    output = ''

    for i in range(len(numlist)):

        result = initialNumber + numlist[i]
        result = calc_result(oplist[i],initialNumber,numlist[i])
        output += 'Step ' + str(i+1)+ " : " + str(initialNumber) +' '+ oplist[i] + ' ' + str(numlist[i]) + ' = ' + str(result) + '\n' 

        initialNumber = result

    return output



def inp_num():
    num = int(input("Enter a number: "))
    num_list.append(num)


def inp_op():
    isValid = False
    op = input("Enter a math op: ")
    if op in ['+','-','*','/']:
        isValid = True

    if isValid:
        op_list.append(op)
    else:
        print("Please enter valid op")
        exit()
    

num_list = []
op_list = []


while cont =='y':
    # print("hello")
    inp_num()
    inp_op()
    cont = input("Do you want to continue(y/n): ")
    print()

output = gen_output(num_list,op_list)

file = open('q1.txt','w')
file.write(output)
file.close()

