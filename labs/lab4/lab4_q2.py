# q2. write a python program to replace user input 1 with user input 2 from the above string.
words = 'How to enable virtualisation, run Manjaro on Windows 10 systems, and more!'

# Take user input 1
user_input_1 = input("Enter Word to search: \n>> ")

# Take user input 2
user_input_2 = input("Enter The word to replace with "+ user_input_1+":\n>> ")
 
# check if the user_input_1 is the words string, if it is found, replace it with the user_input_2 else do nothing
if words.find(user_input_1) != -1:
    replaced_word = words.replace(user_input_1, user_input_2)

    print("Original String:",words)
    print("Replaced String:",replaced_word)
