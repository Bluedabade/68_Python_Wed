def calculate_median(numbers):
    numbers.sort()
    if(len(numbers) % 2 == 0):
        result = (numbers[len(numbers)//2] + numbers[(len(numbers)//2) -1]) / 2
    else:
        result = numbers[len(numbers)//2]
    print(numbers)
    return result


numbers = [8, 4, 7, 4, 6, 2, 10, 9, 3, 7, 1,10]
print(calculate_median(numbers))