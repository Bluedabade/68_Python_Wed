def calculate_parking_fee(hours: int, minutes: int) -> int:
    result = 0
    if hours < 2 and minutes < 1:
        return 0
    else:
        if hours == 1 and minutes >0:
            return hours *50
        else:
            result = (hours - 1) * 50
            if minutes > 0:
                result += 50

    return result            
hours = 3
minutes = 0
result = calculate_parking_fee(hours, minutes)
print(result)
