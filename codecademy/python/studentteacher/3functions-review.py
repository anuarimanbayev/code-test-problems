# FUNCTIONS REVIEW


# Changing function from + to *
number = 5

def my_function(x):
    return x * 3

print(my_function(number))

m = 5
n = 13
# Add add_function here!
def add_function(x, y):
    return x + y

print(add_function(m, n))


# String Concatenation in Functions
n = "Hello"

def string_function(s):
    return s + "world"

print(string_function(n))


# Using an Element from a List in a Function
def list_function(x):
    return x[1]

n = [3, 5, 7]
print(list_function(n))


# Modifying an Element within a Function
def list_function(x):
    x[1] = x[1] + 3
    return x

n = [3, 5, 7]
print(list_function(n))


# List Manipulation in Functions
n = [3, 5, 7]
# Append the number 9 to lst
def list_extender(lst):
    lst.append(9)
    return lst

print(list_extender(n))


# Printing out a list item by item in a function
n = [3, 5, 7]

def print_list(x):
    for i in range(0, len(x)):
        print(x[i])

print_list(n)


# Modifying each element in a list in a function
n = [3, 5, 7]

def double_list(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x

print(double_list(n))


# Passing a range into a function
def my_function(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x

print(my_function([0, 1, 2])) # Add your range between the parentheses!


# Iterating over a list in a function
n = [3, 5, 7]

def total(numbers):
    result = 0
    for number in numbers:
        result = result + number
    return result


# Using strings in lists in functions
n = ["Michael", "Lieberman"]
# Add your function here
def join_strings(words):
    result = ""
    for i in range(len(words)):
        result = result + words[i]
    return result

print(join_strings(n))


# Using two lists as two arguments in a function
m = [1, 2, 3]
n = [4, 5, 6]

def join_lists(x, y):
    return x + y

print(join_lists(m, n))
# You want this to print [1, 2, 3, 4, 5, 6]


# Flatten Lists
n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]

def flatten(lists):    
    results = []
    for i in lists:
        results = results + i       
    return results

print(flatten(n))
