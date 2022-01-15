# Print A pattern

user_number = input("Enter Number: ")

# count of trailing zeroes
pad_zero = len(user_number) -1
# count for leading spaces
spaces = 0

# print pattern
for number in user_number:
    print(' '*spaces,end='')
    print(number,end='')
    print(pad_zero * '0')

    pad_zero-=1
    spaces += 1
