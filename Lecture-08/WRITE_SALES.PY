num_day = int(input("For how many day do you have sales?"))
with open('Lecture-08/sales.txt', 'w') as sales_file:
    for count in range(1,num_day+1):
        sales = float(input(f"Enter the sales for a day {count}: "))
        sales_file.write(str(sales)+ '\n')

print("Data Writing to sales.txt.")