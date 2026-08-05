def compare_string_lengths(str1: str, str2: str) -> str:
    longer = ""
    str1_len = len(str1)
    str2_len = len(str2)

    if str1_len > str2_len:
        length = str1_len - str2_len
        longer = "first"
    elif str2_len > str1_len:
        length =  str2_len - str1_len
        longer = "seccond"
    else:
        return None, 0
    return longer,length


str1 = input("Input String 1: ")
str2 = input("Input String 2: ")

longer_one, lenght = compare_string_lengths(str1, str2)

if not longer_one and not lenght:
    print("Is equire")
else:
    print(f"The {longer_one} string is longer by {lenght} character(s).")