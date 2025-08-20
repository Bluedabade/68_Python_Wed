def separate_even_odd(arg):
    result = []
    odd = []
    even = []
    for num in (arg):
        if num % 2 == 0 :
            even.append(num)
        else:
            odd.append(num)
    result.append(sorted(even))
    result.append(sorted(odd))
    return(result)
arg = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(separate_even_odd(arg))