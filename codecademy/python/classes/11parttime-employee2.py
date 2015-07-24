# Classes
# Class Inheritance
# PartTimeEmployee class supercalls its parent class, Employee Class method

class Employee(object):
    """Models real-life employees!"""
    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00

# Add your code below!
class PartTimeEmployee(Employee):
    """Models part-time employees!"""
    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 12.00
        
    def full_time_wage(self, hours):
        return super(PartTimeEmployee, self).calculate_wage(hours)

milton = PartTimeEmployee("Milton")
print(milton.full_time_wage(10))
