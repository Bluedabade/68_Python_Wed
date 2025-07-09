#Example of the identity operater

#two variables pointing to same list opject
a = [1,2,3]
b = a
#Two variables pointing to deffernt list opjects with the same content

c= [1,2,3]
d= [1,2,3]

print("a is b") # true, since a and b refer to the same objects
print("a is c") #False, since a and b refer to different objects
print("c is d") #False, since a and b refer to different objects

# Using he ifenity operator
print("a == c")
print("c == d")
