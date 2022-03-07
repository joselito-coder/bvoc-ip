A = [ [4,5,6],
      [6,9,2],
      [4,5,6]
]

A = [ [2,3],
      [4,5],
]

# for row in A:
#     print('|',end=' ')
#     for element in row:
#         print(element  ,end=' ')

#     print('|',end='')
#     print()

num_rows = int(input("Enter rows: "))

num_cols = int(input('Enter number of columns'))

matrix = []

for i in range(num_rows):
    row =[]
    print(f" \nEnter The values for Row:{i+1}")
    for j in range(num_cols):
        number = int(input("Enter Number: "))
        row.append(number)
    
    matrix.append(row)

print(matrix)
