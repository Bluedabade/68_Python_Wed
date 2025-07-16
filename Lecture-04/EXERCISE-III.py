max = 100
rows = int(input("How many rows do you want to display number:"))
count = max // rows
num = 0;
for i in range(int((max / count))):
    for j in range(0, int(count)):
        num+=1
        if num > max: 
            continue
        print(num,",", end="")
    if max % rows != 0 and i == int((max / count)-1):
        for k in range(num,(max)):
            num+=1
            print(num,",", end="")
    print("\n")
        


#int((max / count))