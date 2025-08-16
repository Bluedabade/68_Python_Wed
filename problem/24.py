def store_student_info(student_data):
    result = {}
    for student_id, name in student_data:
        result[student_id] = name
    return result



student_data = [("123456", "Alice" ), ("654321", "Bob"), ("112233", "Charlie")]
print(store_student_info(student_data))