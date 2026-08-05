def calculate_total_payment(num_bills, bills):
    result = 0
    result = sum(bills)
    if result >= 10000:
        result = result - (0.2 * result)
    elif result >= 5000:
        result = result - (0.1 * result)
    elif result >= 100:
        result = result - (0.05 * result)
    return result



num_bills = 3
bills = [3000, 4000, 3500]
result = calculate_total_payment(num_bills, bills)
print(result)