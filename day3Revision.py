i1 = 5
i2 = -5
f = 5.5
s1 = 'hello' #str sequence
s2 = " hello " #str sequence
b1 = True
b2 = False

# We can use * operator on string to perform string repetition
print(s1 * 69)

#to get type of any variable we can use the type() function
result = type(i1+i2)
print(result)

# We can take user input using input() function
name = input("Enter your name: ")
print(name,type(name))
# We can typecast string to int, float using respective function
num = input("Enter a number")

num_converted = int(num)
print(num_converted,type(num_converted),type(name))

