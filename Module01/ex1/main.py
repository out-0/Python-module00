
class Person:
    species = "human"

p1 = Person()
p2 = Person()

print("Before:")
print(f"p1.species: {p1.species}, id: {id(p1.species)}")
print(f"p2.species: {p2.species}, id: {id(p2.species)}")
print(f"Person.species: {Person.species}, id: {id(Person.species)}")

# Now let's "change" p1's species
p1.species = "alien"

print("\nAfter p1.species = 'alien':")
print(f"p1.species: {p1.species}, id: {id(p1.species)}")
print(f"p2.species: {p2.species}, id: {id(p2.species)}")
print(f"Person.species: {Person.species}, id: {id(Person.species)}")

print("\nLet's check what's inside each object:")
print(f"p1.__dict__: {p1.__dict__}")
print(f"p2.__dict__: {p2.__dict__}")
