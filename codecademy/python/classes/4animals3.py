# Classes
# Class Animals 3
# Class Scope demonstration with is_alive variable set to True for the entire class

class Animal(object):
    """Makes cute animals."""
    is_alive = True
    def __init__(self, name, age):
        self.name = name
        self.age = age

zebra = Animal("M'bile", 2)
giraffe = Animal("T'allone", 1)
panda = Animal("Po", 7)

print(zebra.name, zebra.age, zebra.is_alive)
print(giraffe.name, giraffe.age, giraffe.is_alive)
print(panda.name, panda.age, panda.is_alive)
