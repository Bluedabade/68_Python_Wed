def group_by_unit_digit(numbers):
    result = []
    for i in range(0,10):
        result.append([])

    for num in numbers:
        unit = num % 10 
        result[unit].append(num)
    return(result)


numbers = [21, 34, 51, 23, 37, 44, 60, 11, 91, 99]

print(group_by_unit_digit(numbers))