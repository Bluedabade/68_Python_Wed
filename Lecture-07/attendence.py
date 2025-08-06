attendence_week = [
    ["Alice","Bob","Charlie","David"],
    ["Alice","Charlie","David"],
    ["Alice","Bob","David"],
    ["Alice","David","Eve"],
    ["Bob","Charlie","David"]

]

attendence_sets = [set(day) for day in attendence_week]
print(attendence_sets)

present_every_day = set.intersection(*attendence_sets)
print(f"Present every day: {present_every_day}")

all_students = set.union(*attendence_sets)
absen_at_least_one_day = all_students - present_every_day
print("Absent at least one day", absen_at_least_one_day)

first_day_present = attendence_sets[0]
last_day_present = attendence_sets[-1]
first_day_but_not_last = list(first_day_present - last_day_present)
print("Present on first day but absent on last day:", first_day_but_not_last)

unique_student_count = len(all_students)
print("Total unique student:", unique_student_count)