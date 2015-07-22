# REVIEW
# Advanced Topics in Python
# List Comprehensions REVIEW
movies = {
    "Monty Python and the Holy Grail": "Great",
    "Monty Python's Life of Brian": "Good",
    "Monty Python's Meaning of Life": "Okay"
}

"""
List that consists of only the numbers between 1 and 15(inclusive)
that are evenly divisible by 3 or 5
Hidden FizzBuzz problem
"""
threes_and_fives = [x for x in range(1, 16) if x%3==0 or x%5==0]
print(threes_and_fives)

# List Slicing
"""
1) Message 'garbled' is backwards
2) The letter we want is every other letter

Use list slicing to extract the message and save it to a variable called message
"""

garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"

message = garbled[::-1][::2]

print(message)

# Lambda Expressions REVIEW
garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"

message = filter(lambda x: x != "X", garbled)

print(message)
