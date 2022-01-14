# Q. Using a while loop print numbers from n to m ( where n and m are integers entered by the user )

# take m and n
n = int(input("Enter N: "))
m = int(input("Enter M: "))

if n  > m:
    while n >= m:
        print(n)
        n -= 1
else:
    while n <= m:
        print(n)
        n += 1

