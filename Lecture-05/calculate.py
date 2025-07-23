def calculate_states(numbers):
    total_sum = sum(numbers)
    average = total_sum / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    return(total_sum,average,maximum,minimum)

numbers = (5, 10 , 15 , 20 ,25)
total, avg, maxnum, minnum = calculate_states(numbers)

print(f"Total sum is: {total}")
print(f"Average is: {avg}")
print(f"Maximum is: {maxnum}")
print(f"minumum is: {minnum}")
