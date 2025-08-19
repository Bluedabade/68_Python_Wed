def calculate_profit(sales, costs):
    list_sale = list(sales)
    result = []
    for i in range(len(sales)):
        profit = sales[i] - costs[i]
        result.append(profit)
    sum_profit = sum(result)
    return(tuple(result),sum_profit)
    

sales = (10000.0, 15000.0, 20000.0, 25000.0, 30000.0)
costs = (7000.0, 8000.0,9000.0, 11000.0, 12000.0)
print(calculate_profit(sales, costs))