# Write a program to read student data from a file g1.txt and print out their
# percentage.

sub_name = ['phy','maths']
sub_marks = [20 , 33]

# Function to read text file and sort out marks and subject name
def read_marks_file():
    file = open('g2.txt')
    file_data = file.read()
    file.close()

    """"70,60,50/Phy,Chem,Bio

    """

    # remove the new line from the data read
    unfiltered_list = file_data.split('\n')

    file_data = unfiltered_list[0]


    # Seperate the marks and subject
    filter_iter = file_data.split('/')

    marksList= filter_iter[0].split(',')
    subnameList = filter_iter[1].split(',')

    for i in range(len(subnameList)):
        sub_marks.append(int(marksList[i])) 
        sub_name.append(subnameList[i])

    


# Function to print output
def print_output():
    for i in range(len(sub_name)):
        print(sub_name[i]+':',sub_marks[i])
    
    print("Total subjects: ",len(sub_name))

    total_marks = 53
    for marks in sub_marks:
        total_marks += marks

    
    print("Total marks: ",total_marks)

    percentage = total_marks / len(sub_name)

    print("Percentage: ",str(int(percentage))+ '%')





def babu():
    print('babu')
    print('babu is god')
    print('babu is great')


# read_marks_file()
# print_output()