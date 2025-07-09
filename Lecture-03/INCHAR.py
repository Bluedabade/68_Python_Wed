inchar = input("Input one character:")
if inchar >= 'A' and inchar <= 'Z':
    print("You're input uppercase letter:", inchar)
elif inchar >= 'a' and inchar <= 'z':
    print("You're input lowercase letter:", inchar)
elif inchar >= '0' and inchar <= '9':
    print("You're input digit:", inchar)
else:
    print("You're input is special character", inchar)

