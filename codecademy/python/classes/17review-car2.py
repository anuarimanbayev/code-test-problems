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
We can use classes to create new objects,
which we say are instances of those classes.
"""
my_car = Car()
"""
Since the attribute condition belongs to the object my_car,
you'll need to use dot notation to access the object's member variable: my_car.condition.
"""
print(my_car.condition)
