with open('Lecture-08/example.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())