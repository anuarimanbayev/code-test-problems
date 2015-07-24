# Classes
# REVIEW
# Class Basics

"""
We also use the word object in parentheses because we want our classes to
inherit the object class. This means that our class has all the properties
of an object, which is the simplest, most basic class
"""
class Car(object):
    """
    Classes can have member variables that store information about each class object.
    We call them member variables since they are information that belongs to the class object.
    """
    condition = "new"

    """
    There is a special function named __init__() that gets called whenever we create a new
    instance of a class. It exists by default, even though we don't see it. However, we can
    define our own __init__() function inside the class, overwriting the default version. 
    """
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg = mpg

"""
We can use classes to create new objects,
which we say are instances of those classes.
"""
my_car = Car("DeLorean", "silver", 88)
"""
Since the attribute condition belongs to the object my_car,
you'll need to use dot notation to access the object's member variable: my_car.condition.
"""
print(my_car.condition)
print(my_car.model)
print(my_car.color)
print(my_car.mpg)
