def print_diamond_pattern(n: int) -> None:
    for i in range(1,n+1):
        for j in range(i):
            print("*", end="")
        print("\t")
    for i in range(n-1,0,-1):
        for j in range(i):
            print("*", end="")
        print("\t")
n = int(input("How many rows?: "))
print(print_diamond_pattern(n))