"""
LOOPS!!!
"""

"""
For your lists
"""
numbers  = [7, 9, 12, 54, 99]

print("This list contains: ")

for num in numbers:
    print(num)

# Add your loop below!
for num in numbers:
    print(num ** 2)

"""
For your dictionaries
"""
d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}

for key in d:
    # Your code here!
    print(key, d[key])
    
"""
Counting as you go -enumerate function
"""
choices = ['pizza', 'pasta', 'salad', 'nachos']

print('Your choices are:')
for index, item in enumerate(choices):
    print(index+1, item)

"""
Multiple Lists
"""
list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
    # Add your code here!
    if a > b:
        print(a)
    elif b > a:
        print(b)
    else:
        print("Both equal!")

"""
For / Else Statement
"""
fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print('You have...')
for f in fruits:
    if f == 'tomato':
        print('A tomato is a fruit!') # (It actually is.)
    print('A', f)
else:
    print('A fine selection of fruits!')
