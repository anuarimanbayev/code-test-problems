# REVIEW
# Advanced Topics in Python
# Iterators for Dictionaries REVIEW
movies = {
    "Monty Python and the Holy Grail": "Great",
    "Monty Python's Life of Brian": "Good",
    "Monty Python's Meaning of Life": "Okay"
}

"""
Call the appropriate method on movies such that it will print out all the items
in the dictionary - that is each key and each value
"""
print(movies.items())
"""
You'll just want to print the result of calling the .items() method
on your movies.
No loops necessary!
"""

for key in movies:
    print(key, movies[key])
