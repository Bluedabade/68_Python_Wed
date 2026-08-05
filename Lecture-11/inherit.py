class Dog:
    species = "Canis familiaris"

    def calAge(self, age):
        print('Dog age is {} years'.format(age * 7))
    
class SomeBread(Dog):
    pass

class SomeOtherBread(Dog):
    species = 'reptille'

    def calAge(self, age):
        print('SomeBread age is {} years'.format(age * 5))

frank = SomeBread()
print(frank.species)
frank.calAge(2)

beans = SomeOtherBread()
print(beans.species)
beans.calAge(2)