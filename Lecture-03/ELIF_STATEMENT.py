num_employees = int(input("Enter the number of employees: "))
if (num_employees < 50):
    print("this is small company")
elif(num_employees < 250):
    print("this is medium sized company")
elif(num_employees >= 250):
    print("this is large sized company")

