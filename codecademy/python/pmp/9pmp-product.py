"""
Practice Makes Perfect!!!
"""

"""
Product!!!
Define a function called product that takes a list of integers as input
and returns the product of all of the elements in the list.

For example: product([4, 5, 5]) should return 100 (because 4 * 5 * 5 is 100).
"""
def product(integers):
    product = 1
    
    for i in integers:
        product *= i
    return product

integers = [4, 5, 5]
print(integers)
print(product(integers))
