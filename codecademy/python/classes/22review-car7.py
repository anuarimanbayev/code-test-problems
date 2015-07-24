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
        return "This is a %s %s with %s MPG" % (self.color, self.model, str(self.mpg))
    
    # Member Variable 1 Modification Function
    def drive_car(self):
        self.condition = "used"

# Instancing a variable my_car with class Car and attributes
my_car = Car("DeLorean", "silver", 88)

# Display Output statements for Car class instance of my_car variable
print(my_car.condition)
my_car.drive_car()
print(my_car.condition)
print(my_car.display_car())

# Electric Car child class of parent class, Car
class ElectricCar(Car):
    def __init__(self, model, color, mpg, battery_type):
        self.model = model
        self.color = color
        self.mpg = mpg
        self.battery_type = battery_type

    def drive_car(self):
        self.condition = "like new"

    def display_car(self):
        return "This is a %s %s with %s MPG on %s battery in %s condition." % (self.color, self.model, str(self.mpg), self.battery_type, self.condition)
        
# Instancing a variable my_car with class Car and attributes
my_car = ElectricCar("JaguarXJ2020", "turquoise", 150, "molten salt")

# Display Output statements for Car class instance of my_car variable
print(my_car.condition)
my_car.drive_car()
print(my_car.condition)
print(my_car.display_car())
