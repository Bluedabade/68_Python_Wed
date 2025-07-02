start = int(input("Enter your start number"))
end =  int(input("Enter your start number"))
while(start <= end):
    if(start % 3 > 0 and start % 4 > 0 and start % 5 > 0):
        print(start)
    start+=1