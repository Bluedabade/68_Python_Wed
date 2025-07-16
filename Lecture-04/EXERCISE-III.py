max = 100
rows = int(input("How many rows do you want to display number:"))
count = max / rows
num = 0;
for i in range(int((max / count))):
    for j in range(0, int(count)+1):
        num+=1
        if num > max: 
            continue
        print(num,",", end="")
    print("\n",i+1)

#int((max / count))