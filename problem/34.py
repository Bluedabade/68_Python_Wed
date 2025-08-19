def print_rectangle_pattern(rows, columns):
    for i in range(rows):
        for j in range(columns):
            print("*", end="")
        print("\t")


rows = int(input("How many rows?: "))
columns = int(input("How many colums?: "))
print(print_rectangle_pattern(rows, columns))