def print_number_pattern(rows: int) -> None:
    for i in range(1,rows+1):
        for j in range(0,rows-i):
            print("-",end="")
        for j in range(rows-i,rows):
            print(rows-j,end="")
        print("")

rows = int(input("How many rows?: "))
print_number_pattern(rows)

# def print_full_number_pyramid(rows: int) -> None:
#     for i in range(1, rows+1):
#         print(" " * (rows - i), end="")

#         for j in range(1, i+1):
#             print(j, end="")

#         for j in range(i-1, 0, -1):
#             print(j, end="")

#         print("")

# rows = int(input("How many rows?: "))
# print_full_number_pyramid(rows)
