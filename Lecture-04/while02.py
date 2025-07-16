keep_going = 'y'
while keep_going.lower() == 'y':

    sales = float(input("Pleas input your amount of sales:"))
    comm_rate = float(input("Pleas input your amount of comm_rate:"))

    commission = sales * comm_rate

    print(f'The commission rate is ${commission:.2f}')

    keep_going = input("Do you want to keep calculate another? (y/n)")