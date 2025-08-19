def calculate_discounted_prices(prices, discount_percentage):
    result = []
    for i in range(len(prices)):
        discount = prices[i] * (1 - discount_percentage/ 100)
        result.append(discount)
    return(result)
        

prices = [100.0, 250.0, 75.0]
discount_percentage = 20.0

print(calculate_discounted_prices(prices, discount_percentage))