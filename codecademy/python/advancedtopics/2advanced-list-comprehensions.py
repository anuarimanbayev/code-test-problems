# REVIEW
# Advanced Topics in Python
# List Comprehension

doubles_by_3 = [x*2 for x in range(1,6) if (x*2) % 3 == 0]

# Even Squares
even_squares = [x**2 for x in range(1,11) if x % 2 == 0]

print(even_squares)

# Cubes of the numbers 1 through 10 only if the Cube is evenly divisible by four
cubes_by_four = [x**3 for x in range(1,11) if (x**3) % 4 == 0]

print(cubes_by_four)

# Slicing
# Python 3 needs List function to turn Range function output into a list!
my_list = list(range(1, 11)) # List of numbers 1 - 10

# Add your code below!
# Print out every odd element of my_list from start to finish
print(my_list[::2])

# Add your code below!
# Reverse of my_list
backwards = my_list[::-1]
print(backwards)

# Go backwards through a list of 100 to 0 by tens
to_one_hundred = list(range(101))

backwards_by_tens = to_one_hundred[::-10]

print(backwards_by_tens)

# Practice Makes Perfect!!!
# 1 to 21
to_21 = list(range(1,22))

# 1, 3, 5, odds until 21
odds = to_21[::2]

# 8 to 14
middle_third = to_21[7:14]

print(to_21)
print(odds)
print(middle_third)

# Lambda is a small, anonymous function
# Python is a functional language, able to pass functions as variables or lists
languages = ["HTML", "JavaScript", "Python", "Ruby"]
print(filter(lambda x: x == "Python", languages))

# Lambda and Filter
squares = [x**2 for x in range(1, 11)]
print(filter(lambda x: x >= 30 and x <= 70, squares))
