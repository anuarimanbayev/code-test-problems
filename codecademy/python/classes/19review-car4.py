# Classes
# REVIEW
# Class Basics

class Car(object):
    # Member Variable of class Car
    condition = "new"

    # Initialization Function
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg = mpg

    # Display Function
    def display_car(self):
        print("This is a " + self.color + " " + self.model + " with " + str(self.mpg) + " MPG.")

# Instancing a variable my_car with class Car and attributes
my_car = Car("DeLorean", "silver", 88)

# Single Print statement
print(my_car.display_car())
