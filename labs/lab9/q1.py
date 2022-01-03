# Program which prints names of the students whose marks are above 60

user_num = int(input("Enter A number: "))

elig_names = []

# take names and marks
for i in range(user_num):
    user_name = input("Enter name: ")
    user_marks = int(input("Enter marks: "))

    if user_marks > 60:
        elig_names.append(user_name)


# print all the names
for name in elig_names:
    print(name)


