# Answer to q1
# Take user input
value = int(input("Enter value: "))
# Initialize a
a = 0
# code if the value is greater than 0
if value > 0:
    a += 1
# code if the value is greater than 5
if value > 5:
    a += 2
# code if the value is greater than 10
if value > 10:
    a += 3
# code if the value is greater than 0 , 5 , 10
if value > 0 and value >5 and value >10:
    a += 4

# Print the result
print('result',a)

# Question two

ph  = input("Enter ph: ")
name = input('enter name: ')

if name == '':
    print("name cannot be empty")

if ph == '':
    print("Ph cannot be empty")

if len(ph) != 10:
    print('ph has to be 10 chrs')

if not ph.isdigit():
    print("ph cannot have alphabets")
