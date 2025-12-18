class Person:
    pass

p1 = Person()
p2 = Person()

print(id(p1))
print(id(p2))
print(id(Person))

print(type(Person))
print(type(p1))
print(type(p2))

print(dir(Person))
print(dir(p1))
print(dir(p2))
