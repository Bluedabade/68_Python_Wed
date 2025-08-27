def example_a_plus_mode():
    with open('example_a+.txt', 'a+') as file:
        file.seek(0)

        content = file.read()
        print("Current content of the file: ")
        print(content)

        file.write("Appending a new line at the end. \n")

        file.seek(0)

        update_content = file.read()
        print("\nUpdated content of the file: ")
        print(update_content)

example_a_plus_mode()