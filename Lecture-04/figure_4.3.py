char_input = input("Please enter word:")
vowels = "aeiouAEIOU"
result_char = ""
for char in char_input:
    if char in vowels:
        result_char = result_char + "*"
    else:
        result_char = result_char + char

print(result_char)
