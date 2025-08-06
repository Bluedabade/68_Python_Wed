student = {"name" : "Alice", "age" : "25","grade" : "A"}

student["age"] = 26
student["Major"] = "Computer Science"
print(student)

del student["grade"]
print(student)

removed_major = student.pop("Major")
print(removed_major)
print(student)