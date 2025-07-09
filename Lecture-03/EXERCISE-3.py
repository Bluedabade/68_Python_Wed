work_hours = int(input("Enter the number of hours worked:"))
hourly_pay = float(input("Enter the hourlypay rate:"))
gross = 0
if work_hours <= 40:
    gross = work_hours * hourly_pay
else:
    gross = (hourly_pay * 40) + ((work_hours - 40) * (hourly_pay * 1.5))
print(f'The gross pay is ${gross}')