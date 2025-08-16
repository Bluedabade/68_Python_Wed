def store_student_scores(student_data):
    result = {}
    for std_id , name , score in student_data:
        result[std_id] = {}
        result[std_id]["name"] = name
        result[std_id]["score"] = score 
    return(result)


student_data = [


    
("123456", "Alice", 85.5),
("654321", "Bob", 92.0),
("112233", "Charlie", 78.0)
]

print(store_student_scores(student_data))