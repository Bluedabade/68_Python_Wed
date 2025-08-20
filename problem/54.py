def fahrenheit_to_celsius(fahrenheit: float) -> float:
    celsius = (fahrenheit - 32) * 5/9
    return(celsius)
def celsius_to_fahrenheit(celsius: float) -> float:
    fahrenheit = celsius * 9/5 +32
    return(fahrenheit)
cal = float(input("Enther tempurature in calcius: "))
far = float(input("Enther tempurature in fahrenheit: "))

result_far = fahrenheit_to_celsius(cal)
result_cal = fahrenheit_to_celsius(far)

print(result_cal,result_far)