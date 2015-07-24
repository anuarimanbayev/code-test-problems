# Classes
# Class Animals 6
# Sloth and Ocelot showing off Member Variable attribute

class Animal(object):
    """Makes cute animals."""
    is_alive = True
    health = "good"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # Add your method here!
    def description(self):
        print(self.name)
        print(self.age)

hippo = Animal("LaShawnda", 50)
hippo.description()

sloth = Animal("Dima", 47)
ocelot = Animal("Quetzcoatl", 12)

print(hippo.health)
print(sloth.health)
print(ocelot.health)
