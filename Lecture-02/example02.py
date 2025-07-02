height = input("Enter your height in meter: ")
height = float(height)

weight = float(input("Please input your weight in kilogram: "))

bmi = weight / (height * height)
print("Your bmi: ", format(bmi, '.2f'))