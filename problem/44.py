def calculate_investment_growth(principal,annual_rate, years):
    result = []
    for year in range(1,years+1):
        sum = principal * (1+annual_rate/100)**year
        result.append(f"{sum:.2f}")
    return(result)


principal = 1000
annual_rate = 5
years = 5

print(f"{calculate_investment_growth(principal,annual_rate, years)}",)