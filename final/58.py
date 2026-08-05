def find_divisors(num: int) -> list:
    divisors = []
    for i in range(1 ,num +1):
        if num % i == 0:
            divisors.append(i)
    return divisors
num = int(input("Input Number: "))

result = find_divisors(num)
print(result)