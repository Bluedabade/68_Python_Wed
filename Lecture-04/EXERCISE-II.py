inventory =[
["Apple", 50, 0.75],
["Banana", 100, 0.50],
["Orange", 75, 0.80]
]
def update_inventory():
    item_name = input("Enter item name: ")
    quantity_sold = int(input("How much do you sold: "))
    for i in range (0, len(inventory)):
        for j in range(0, len(inventory[i])):
            # print(inventory[i][j])
            if(str(inventory[i][j]).upper() == item_name.upper()):
                inventory[i][1] -= quantity_sold
                print(f"{inventory[i][j]} is now: {inventory[i][1]}")
            if (j >= len(inventory[i])):
                j -= len(inventory[i])
        if (i >= len(inventory)):
            i -= len(inventory)

def calculate_total_value():
    for i in range (0, len(inventory)):
        print(f"{inventory[i][0]} is: {inventory[i][1] * inventory[i][2]}")
        if (i >= len(inventory)):
            i -= len(inventory)

def main():
    while True:
        print("1. update_inventory")
        func = int(input("Choose function:")) 
        if(func == 1):
            update_inventory()
        elif(func == 2):
            calculate_total_value()


main()



