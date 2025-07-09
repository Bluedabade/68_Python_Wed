#program to compare the string "Mare" and "Mark"

#Define the string
string1 = "Mary"
string2 = "Mark"

#Compare the string for equlity
if string1 == string2:
    print(f'"{string1}" and "{string2}" are equal.')
else:
    print(f'"{string1}" and "{string2}" are not equal.')

#lexicographical comparision
if string1 < string2:
    print(f'"{string1}" come before "{string2}" in lexicographical order.')
elif string1 > string2:
    print(f'"{string1}" come after "{string2}" in lexicographical order.')

#Case-insesitive comparision
if string1.lower() == string2.lower():
    print(f'"{string1}" and "{string2}" are equal when case is ignore.')
else:
    print(f'"{string1}" and "{string2}" are not equal when case is ignore.')


