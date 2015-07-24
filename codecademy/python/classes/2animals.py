# Classes
# Class Animals

"""class that does nothing! Just passes by!"""
class Animal(object):
    pass

"""Initialization Step 1"""
class Animal(object):
    def __init__(self):
        pass

"""Setting Name Parameter"""
class Animal(object):
    def __init__(self, name):
        self.name = name

"""Zebra named M'bile"""
class Animal(object):
    def __init__(self, name):
        self.name = name
        
zebra = Animal("M'bile")
print(zebra.name)
