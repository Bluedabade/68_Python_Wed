def highest_sales_country(sales_data):
    result = []
    max_amount = 0
    for country , amount in sales_data.items():
        if amount > max_amount:
            result = []
            result.append(country)
            result.append(amount)
            max_amount = amount
        if amount  == max_amount and country not in (result):
            result.append(country)
            result.append(amount)
    return(tuple(result))
sales_data = {
"Thailand": 1500,
"Laos": 1200,
"Vietnam": 1800,
"Japan": 1700,
"China": 2000,
"asd": 2000,
"h": 2000
}

print(highest_sales_country(sales_data))