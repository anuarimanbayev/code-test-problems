# Classes
# REVIEW
# Modifying Member Variables

# Car the parent class
class Car(object):
    # Member Variable 1 of class Car
    condition = "new"

    # Initialization Function
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg = mpg

    # Display Function
    def display_car(self):
        print("This is a " + self.color + " " + self.model + " with " + str(self.mpg) + " MPG.")

    # Member Variable 1 Modification Function
    def drive_car(self):
        self.condition = "used"
        
# Electric Car child class of parent class, Car
class ElectricCar(Car):
    def __init__(self, model, color, mpg, battery_type):
        self.model = model
        self.color = color
        self.mpg = mpg
        self.battery_type = battery_type
        
# Instancing a variable my_car with class Car and attributes
my_car = Car("DeLorean", "silver", 88)

# Display Output statements
print(my_car.display_car())
