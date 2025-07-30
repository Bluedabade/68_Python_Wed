heroes = ['Ironman','Thor','Hulk','Spiderman']

def Display_Heroes():
    return(heroes)

def Add_Heroes():
    print(f"Data in list heroes: {heroes} ")
    input_heroes = input("Enter the heroes you want to add: ")
    heroes.append(input_heroes)
    return(heroes)

def Insert_Heroes():
    enum_hero = list(enumerate(heroes))
    print(f"Data in list heroes: {enum_hero} ")
    position = int(input("Enter position you want to insert heroes: "))
    input_heroes = input("Enter the heroes you want to insert:")
    heroes.insert(position,input_heroes)
    return(heroes)

def Remove_Heroes():
    input_heroes = input("Enter the heroes you want to remove: ")
    heroes.remove(input_heroes)

def Sorted_Heroes():
    sort_input = input("Ascending/Decending (A/D): ")
    if (sort_input.upper() == "A"):
        heroes.sort()
    elif(sort_input.upper() == "D"):
        heroes.sort()
        heroes.reverse();
    return(heroes)

def main():
    while(True):
        print("1.Display_Heroes")
        print("2.Add_Heroes")
        print("3.Insert_Heroes")
        print("4.Remove_Heroes")
        print("5.Sorted_Heroes")
        choose = input("Choose fucntion: ")
        if(choose == '1'):
            Display_Heroes()
        elif(choose == '2'):
            Add_Heroes()
        elif(choose == '3'):
            Insert_Heroes()
        elif(choose == '4'):
            Remove_Heroes()
        elif(choose == '5'):
            Sorted_Heroes()
        else:
            continue
        print(f"Output: {heroes} ")

main()
