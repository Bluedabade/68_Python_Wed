from abc import ABC, abstractmethod
class Absclass(ABC):
    def print(self,x):
        print("Passed value is:",x)
    
    @abstractmethod
    def task(self):
        print("we are in abstract method")

class test_class(Absclass):
    def task(self):
        print("we are in implemented abstract method")

class example_class(Absclass):
    def task(self):
        print("we are in implemented abstract method of example class")

test_obj = test_class()
test_obj.task()
test_obj.print(100)

example_obj = example_class()
example_obj.task()
example_obj.print(200)

print("test_obj is instance of test_class:",isinstance(test_obj,Absclass))
print("example_obj is instance of example_class:",isinstance(example_obj,Absclass))
