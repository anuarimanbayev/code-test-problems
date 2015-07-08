"""
Practice Makes Perfect!!!
"""

"""
Count!!!
Return the number of times the item occurs in the list.
For example: count([1,2,1,1], 1) should return 3
(because 1 appears 3 times in the list).
"""
def count(sequence, item):
    found = 0
    
    for i in sequence:
        if i == item:
            found += 1
    return found

sequence = [1, 2, 1, 1]
item = 1

print(sequence)
print(item)
print(count(sequence, item))
