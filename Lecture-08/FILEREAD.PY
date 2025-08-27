def main():
    infile = open('Lecture-08/philosophers.txt', 'r')

    file_contents = infile.read()

    infile.close()

    print(file_contents)

main()