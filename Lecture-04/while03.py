keep_going = 'y'
while keep_going.lower() == 'y':

    sales = float(input("Enter the item's wholesale cost:"))

    retail_price = sales * 2.5

    print(f'The retail_price rate is ${retail_price:.2f}')

    keep_going = input("Do you want to keep calculate another? (y/n)")