# q3. write a python program that prints a sub string 'systems' from the above string.
words = 'How to enable virtualisation, run Manjaro on Windows 10 systems, and more!'

# calculate the start index
systems_index = words.find('systems')
# end_index = (index of word) + (length of word)
systems_length = len('systems')

# calculate the end index
systems_end_index = systems_index + systems_length

# calculate the substring
substring = words[systems_index:systems_end_index]

print("The substring is:",substring)
 