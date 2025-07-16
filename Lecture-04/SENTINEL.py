rows = int(input("How many rows?"))
columns = int(input("How many columns?"))
for i in range(0,rows):
    line = ''
    for j in range(0,columns):
        line = line +'*'
    print(line)