with open("file/file.txt",'r') as file:
    rec = 1
    content = file.readlines()
    for line in content:
        if rec == 1:
            print(f"Name: {line.strip()}")
        if rec == 2 :
            print(f"ID: {line.strip()}")
        if rec == 3 :
            print(f"Dept: {line.strip()}")
        if rec == 3 :
            rec = 1
        else:
            rec += 1

        
