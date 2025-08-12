performance_data = {
    "Sales":{
        "Alice" : [80,85,88,90],
        "Bob" : [70,75,78,80],
        "Charlie" : [60,65,70,72]
    },
    "Engineering":{
        "Eve" : [85,88,87,90],
        "David" : [90,92,94,95],
        "Frank" : [88,87,86,85]
    },
    "HR":{
        "Grace" : [70,72,74,76],
        "Heidi" : [65,68,70,73],
        "Ivan" : [60,62,64,66]
    }
}
def average_employee_score():
    average_performance_score = {}
    for depart , employees in performance_data.items():
        average_performance_score[depart] ={}
        for employee, score  in employees.items():
           average = sum(score)/len(score)
           average_performance_score[depart][employee] = average
    return(average_performance_score)

def top_performer():
    top_performer_score = {}
    average_performance_score = average_employee_score()
    for depart, employees in average_performance_score.items():
        top_score = 0
        for employee , score in employees.items():
            if score > top_score:
                top_score = score
                top_employee = employee
        top_performer_score[depart] = {top_employee:top_score}
    return(top_performer_score)

def best_department():
    average_performance_score = average_employee_score()
    # print(average_performance_score)
    best_depart_result = {}
    best_score = 0
    for depart ,employees in average_performance_score.items():
        sum_score = 0
        for employee , score in employees.items():
            sum_score += score
        average = sum_score / len(employees)
        if average > best_score:
            best_score = average
            best_depart = depart
    best_depart_result = {best_depart: best_score}
    # print(best_depart_result)
    return(best_depart_result)

def continuous_improvers():
    continue_improver_result = {}
    for depart , employess in performance_data.items():
        continue_list = []
        for employee , scores in employess.items():
            continue_improve = True
            previous_score = 0
            for score in scores:
                if score < previous_score:
                    continue_improve = False
                previous_score = score
            if continue_improve == True :
                continue_list.append(employee)
    
        continue_improver_result[depart] = continue_list.copy()
        # print(f"{depart}: {continue_list}")

    return(continue_improver_result)

                        
def main():
    average_performance_score = average_employee_score()
    top_perform = top_performer()
    best_depart = best_department()
    continue_improve = continuous_improvers()
    print(f"Average Performance Score: {average_performance_score}")
    print(f"Top Performers: {top_perform}")
    print(f"Best Department: {best_depart}")
    print(f"Continuous Improvers: {continue_improve}")

    print("Summary Report:")
    for depart , employees in average_performance_score.items():
        print(f"Department: {depart}")
        for employee , score in employees.items():
            print(f"|---{employee}: Average Score = {score}")
        best_perform , best_perform_score = next(iter(top_perform[depart].items()))
        print(f"Top Performer: {best_perform} with Average Score = {best_perform_score}")
        print("_________________________________________________")
    best_depart_result , best_depart_score = next(iter(best_depart.items()))
    print(f"Best Department: {best_depart_result} with Average Score = {best_depart_score:.2f}")
        
    
main()