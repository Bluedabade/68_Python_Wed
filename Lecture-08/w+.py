def example_w_plus_mode():
    with open('example_w+.txt', 'w+') as file:
        file.write("THis is the first line in the file.\n")
        file.write("THis is the second line in the file.\n")

        file.seek(0)

        content = file.read()
        print("Content of the file: ")
        print(content)

example_w_plus_mode()