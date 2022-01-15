# q3.Count the number of 0,1,2,3,4,5,6,7,8,9 from a given string


user_input = input("Enter string: ")

if user_input.isnumeric():

    # list to store the number
    list_ttd = []
    # list to store the occurance of that number
    list_babu = []

    list_charcount = list(range(10))


    # counting the characters
    for number in user_input:
        if int(number) in list_charcount:
            if number not in list_ttd:
                list_ttd.append(number)
                list_babu.append(user_input.count(number))


    # loop to print the count of the numbers
    for i in range(len(list_ttd)):
        print(list_ttd[i],':',list_babu[i])
