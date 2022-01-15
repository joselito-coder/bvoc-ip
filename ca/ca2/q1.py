# q1.Find the percentage and total marks of a student.

user_marks = input("Enter Marks: ")

marks_list = user_marks.split()

total = 0

for marks in marks_list:
    total += int(marks)

print("Total:",total)

percentage = total/ len(marks_list)

print("Percentage: " +str(round(percentage)) + "%")



