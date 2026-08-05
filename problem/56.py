def convert_currency(amount: float, from_currency: str, to_currency: str) -> float:
    cur_eur = 0.85
    cur_bgp = 0.75
    cur_jpy = 110
    cur_thb = 32
    cur_usd = 1
    
    if from_currency == 5:
        cur_in_usd = amount / cur_thb
    elif from_currency == 4:
        cur_in_usd = amount / cur_jpy
    elif from_currency == 3:
        cur_in_usd = amount / cur_bgp
    elif from_currency == 2:
        cur_in_usd = amount / cur_eur
    else:
        cur_in_usd = amount

    if to_currency == 5:
        result = cur_in_usd * cur_thb
    elif to_currency == 4:
        result = cur_in_usd * cur_jpy
    elif to_currency == 3:
        result = cur_in_usd * cur_bgp
    elif to_currency == 2:
        result = cur_in_usd * cur_eur
    else:
        result = amount
    return result


amount = float(input("Amout: "))
print("USD = 1")
print("EUR = 2")
print("GBP = 3")
print("JPY = 4")
print("THB = 5")

from_currency = int(input("From Currency: "))

print("USD = 1")
print("EUR = 2")
print("JPY = 4")
print("THB = 5")
to_currency = int(input("To Currency: "))

result = convert_currency(amount,from_currency,to_currency)

print(f"{result:.2f}")