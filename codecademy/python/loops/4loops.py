"""
LOOPS!!!
"""

"""
FOR in strings
"""

thing = "spam!"

for c in thing:
    print(c)

word = "eggs!"

# Your code here!
for c in word:
    print(c)

"""
Replacing A/a
"""
phrase = "A bird in the hand..."

# Add your for loop
for char in phrase:
    if char == "A" or char == "a":
        print("X",)
    else:
        print(char,)

#Don't delete this print statement!
print

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
