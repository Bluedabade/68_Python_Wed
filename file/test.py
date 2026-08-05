with open("file/test.txt", 'a+') as file:
    file.write("This is mother fucker!.\n")

    file.seek(0)

    lines = file.readlines()

    print(lines)