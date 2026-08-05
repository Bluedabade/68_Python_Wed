from datetime import datetime

def days_between_dates(date1: str, date2: str) -> int:
    d1 = datetime.strptime(date1, "%Y-%m-%d")
    d2 = datetime.strptime(date2, "%Y-%m-%d")
    
    delta = abs((d2 - d1).days)   
    return delta


date1 = "2024-08-01"
date2 = "2024-08-10"

result = days_between_dates(date1, date2)
print(f"Number of days between {date1} and {date2}: {result}")
