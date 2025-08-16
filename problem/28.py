def check_membership(s: set, input_value: str) -> bool:
    input_string = input_value
    if input_value.isdigit():
        input_string = int(input_value)
    if input in s:
        return (True)
    else:
        return(False)

s = {1, 2, 3, 'a', 'e', 'i', 'o', 'u', "red", "green", "blue"}

input_value = input("Please input something: ")
print(check_membership(s, input_value))