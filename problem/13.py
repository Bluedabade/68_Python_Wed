def reverse_string(string):
    reverse_string = "".join(reversed(string))
    # reverse_string = string[::-1]
    return(reverse_string)

string = input("Enter a word: ")
print(reverse_string(string))
