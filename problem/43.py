def calculate_coins(amount):
    coin_10 = amount // 10
    remain = amount%10
    coin_5 = remain // 5
    remain = remain % 5
    coin_2 = remain // 2
    remain = remain % 2
    coin_1 = remain // 1

    return(coin_10,coin_5,coin_2,coin_1)

amount = 50
print(calculate_coins(amount))