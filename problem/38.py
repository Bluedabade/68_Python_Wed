def add(a: float, b: float) -> float:
    return(a+b)
def subtract(a: float, b: float) -> float:
    return(a-b)
def multiply(a: float, b: float) -> float:
    return(a*b)
def divide(a: float, b: float) -> float:
    if b == 0:
        return None
    else:
        return(a/b)

a = float(input("Enter your 1st number:"))
b = float(input("Enter your 2nd number:"))
result_add = add(a,b)
result_subtract = subtract(a,b)
result_multiply = multiply(a,b)
result_divide = divide(a,b)
print(f"{result_add}\t{result_subtract}\t{result_multiply}\t{result_divide}")