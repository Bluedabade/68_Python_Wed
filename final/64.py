def calculate_required_grades(current_gpa, target_gpa ,credits):
    i = 0.0
    while i < 4.0:
        grade_target = []
        target_credits = []
        for j in range(len(credits)):
            target_credits.append(i * credits[j])
            grade_target.append(i)
            # print(grade_target)
            print(sum(target_credits) / sum(credits))
            if sum(target_credits) / sum(credits) > target_gpa:
                break
        i+= 0.5
    target_gpa_list = []
    for grade in grade_target:
        if grade == 4 :
            target_gpa_list.append("A")
        elif grade == 3.5 :
            target_gpa_list.append("B+")
        elif grade == 3:
            target_gpa_list.append("B")
        elif grade == 2.5 :
            target_gpa_list.append("C+")
        elif grade == 2 :
            target_gpa_list.append("C")
        elif grade == 1.5 :
            target_gpa_list.append("D+")
        elif grade == 1 :
            target_gpa_list.append("D")
    return target_gpa_list
            



current_gpa = 2.8
target_gpa = 1
credits = [3, 4, 3, 2, 3]
print(calculate_required_grades(current_gpa, target_gpa ,credits))