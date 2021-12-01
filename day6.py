"""
string methods taught : 
    <string>.split([seperator])==> splits the string into the list based on the [seperator]
    <string>.lower()==> Converts the <string> to lowercase

    <string>.upper() ==> Converts the <string> to uppercase

    <string>.isalpha() ==> Return True if all characters in the string are alphabetic and there is at least one character

    <string>.find(sub[, start[, end]]) ==> Return the lowest index in the string where substring sub is found within the slice s[start:end]. Optional arguments start and end are interpreted as in slice notation. Return -1 if sub is not found.
    <string>.isalpha() ==> 

    <string>.isnumeric() ==> Return True if all characters in the string are numeric characters, and there is at least one character, False otherwise.

    <string>.isdigit() ==> Return True if all characters in the string are digits and there is at least one character, False otherwise.

    not operateor  ==> not is a Boolean operatior, The operator 'not' yields True if its argument is false, False otherwise

    in operator ==> ~in~ operator is a Membership test operator, The operators in and not in test for membership. x in s evaluates to True if x is a member of s, and False otherwise.

"""


# program 1
# s = "Returns true if all characters"
# s = "1 2 3 4 5 6"
# s = "1,2,3,4,5,6"
# s = "1-2-3-4-5-6"
# l = s.split()
# l = s.split(',')
# l = s.split('-')
# print(l)
# print(int(l[0] )+ int(l[1]))

# program 2
# name = 'john doe'
# uname = name.upper()
# lname = name.lower()
# # print(uname)
# print(lname)

# program 3
# name = 'Retusn True if the string'
# # index = name.find('if')
# # print(index)
# if 'the' in name:
#     print("yes")
# else:
#     print('no')

# program 4
s = 'TrueiftheString'
s_n ='1234242'
# if s.isalpha():
#     print("Yes")
# else:
#     print("no")

print(s_n.isdigit())
print(s_n.isnumeric())
