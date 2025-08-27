with open('Lecture-08/sales.txt', 'r') as sales_file:
    for line in sales_file:
        amount = float(line.strip())
        print(f"Sales amount: {amount:.2f}")