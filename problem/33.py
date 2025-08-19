def calculate_median(provinces):
    values = sorted(provinces.values())
    n = len(values)
#   sorted_provinces = list(sorted(provinces.items(), key=lambda x : x[1]))
    if n % 2 == 1:  
        median = values[n // 2]
    else:           
        median = (values[n // 2 - 1] + values[n // 2]) / 2 
    result = [(country, count) for country, count in provinces.items() if count == median]
    return result        
provinces = {'Thailand':76, 'Laos':17, 'Vietnam':58, 'Japan':47,'Hang':46, 'China':23}

print(calculate_median(provinces))