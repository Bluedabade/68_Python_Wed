def print_diamond_pattern(n: int) -> None:
    median = n / 2
    for i in range(1,int(median)):
        # print(int(median)-i)
        for k in range(1,int(median)-i+1):
            print("*",end="")
        for k in range(int(median)-i,int(median)+i):
            print("-",end="")
        for k in range(int(median) +i, n):
            print("*",end="")
        print("")
    for i in range(int(median)-1,0,-1):
        # print(int(median)-i)
        for k in range(1,int(median)-i+1):
            print("*",end="")
        for k in range(int(median)-i,int(median)+i):
            print("-",end="")
        for k in range(int(median) +i, n):
            print("*",end="")
        print("")

n = int(input("How many rows?: "))
print_diamond_pattern(n)