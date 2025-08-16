def prime_numbers_in_range(start, end):
    result = []
    
    if start < 1 or start > 1000 or end < 1 or end > 1000:
        print("out of range")
        return None
    

    for i in range (start, end+1):
        is_Prime = True
        for j in range(1, i+1):
            if j > 1 and j < i and i % j == 0 :
                is_Prime = False
        if is_Prime == True and j != 1 :
            result.append(j)    
        
    return(result,sum(result))

start = int(input("Please enter starting number: "))
end = int(input("Please enter ending number: "))
print(prime_numbers_in_range(start, end))