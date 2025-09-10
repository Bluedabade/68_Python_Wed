try:
    value = int(input("Enter a number: "))
    result = 10 / value
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Cannot divide by zere")
else:
    print(f"The result is {result}")
    
print("End of program")