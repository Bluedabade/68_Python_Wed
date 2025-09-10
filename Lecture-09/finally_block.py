try:
    numerator = float(input("Enter the numerator: "))
    donuminator = float(input("Enter the donuminator: "))

    result = numerator / donuminator
    print(f"The result is: {result}")

except ZeroDivisionError:
    print("Error: You cannot divide by zero")

except ValueError:
    print("Error: Invalid input. Please enter numeric values.")

finally:
    print("Excution completed, whether an exception occurred or not.")

print("End of program")