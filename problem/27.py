def build_set():
    int_set = set()
    while len(int_set) < 5 :
        number = int(input(f"Please Enter number {len(int_set)+1} :"))
        if(number) not in (int_set):
            int_set.add(number)
        else:
            print("Please try again")
    return(int_set)

print(build_set())
