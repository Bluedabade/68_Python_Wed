def calculate_statistics(numbers):
    result = []
    for num in numbers:
        result.append(num*num)
    maximum = max(result)
    minimum = min(result)
    sum_value = sum(result)
    average = sum_value/len(result)
    return(result,maximum,minimum,sum_value,average)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(calculate_statistics(numbers))