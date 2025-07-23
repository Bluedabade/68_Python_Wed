def is_armstroung(num):
    digit_lenght = len(str(num))
    total = 0
    is_arms = False
    for i in num:
        total += int(i)**digit_lenght
    if(total == int(num)):
        is_arms = True
    return is_arms,total

value = input("Please enter number: ")
result, total_sum = is_armstroung(value)
print(f"{result} {value} = {total_sum}")



