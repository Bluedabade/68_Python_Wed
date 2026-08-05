from abc import ABC, abstractmethod

class employee(ABC):
    def emp_id(self, id, name, age,salary):
        pass

class childemployee(employee):
    def emp_id(self,id):
        print("Employee id is:",id)

emp1 = childemployee()
emp1.emp_id(id)
