# Classes
# Class Animals 4
# Hippo named LaShawnda

class Animal(object):
    """Makes cute animals."""
    is_alive = True
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # Add your method here!
    def description(self):
        print(self.name)
        print(self.age)

hippo = Animal("LaShawnda", 50)
hippo.description()
