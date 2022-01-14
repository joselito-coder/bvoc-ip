# REading from a file

# f = open('test.txt','r')

# file_data = f.read()

# print(file_data)
# print(type(file_data))

# f.close()

f = open('test.txt','a')

f.write('\n\nBABU OP!\n\n')
f.write('babu is awesome!\n')
f.write('Babu is op!\n')
f.close()

