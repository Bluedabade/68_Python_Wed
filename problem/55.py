def convert_thb_to_currency(amount: float, to_currency: str) -> float:
    if to_currency == 1 :
        result = amount * 0.030
        curen = "USD"
    elif to_currency == 2 :
        result = amount * 0.027
        curen = "EUR"
    elif to_currency == 2 :
        result = amount * 0.023
        curen = "GBP"
    elif to_currency == 2 :
        result = amount * 3.4
        curen = "JPY"
    else:
        result = amount * 0.045
        curen = "AUD"
    return result,curen
amount = float(input("Please enter amount bath: "))
print("Choose currency u want to convert to: ")
print("1 = USD")
print("2 = EUR")
print("3 = GBP")
print("4 = JPY")
print("5 = AUD")
to_currency = int(input("Enter number from above: "))
result ,curren = convert_thb_to_currency(amount,to_currency)
print(f"{amount} BTH Convert To {curren} = {result} {curren}")