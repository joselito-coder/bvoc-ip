# string = 'shankar_doe'

# for characters in string:
#     print(characters)


# for i in range(1,11,2):
#     print(i,'X 2 =',i * 2)

# for i in range(2,10,2):
#     print(i)

# count = int(input("Enter loo count: "))

# for i in range(count):
#     print(i)


subject_count = int(input('how many subjects per year? '))

# for n in range(subject_count):
#     print(n)

subjects = []

for n in range(subject_count):
    sub = int(input("Enter subject marks: "))
    subjects.append(sub)
    print(subjects)