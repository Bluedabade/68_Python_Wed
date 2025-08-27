with open('Lecture-08/employee.txt', 'r') as file:
    line = file.readline()
    feild = 0
    while(line):
        feild +=1
        if feild == 1 :
            print(f"Name: {line.strip()}")
        elif feild == 2 :
            print(f"ID: {line.strip()}")
        else:
            print(f"Dept: {line.strip()}")
        if feild == 3 :
            feild = 0
        line = file.readline()