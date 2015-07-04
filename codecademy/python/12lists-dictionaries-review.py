# Lists and Dictionaries
# REVIEW PROGRAM

inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']    
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 

# Your code here
# Adding a key 'pocket' and assining a list to it
inventory['pocket'] = ['seashell', 'strange berry', 'lint']

#Sorting the list found under the key 'backpack'
inventory['backpack'].sort()

# Removing the item 'dagger' from the 'backpack' key
inventory['backpack'].remove('dagger')
# del inventory['backpack'] would remove the entire backpack key

# Adding 50 to the number stored under the 'gold' key
inventory['gold'] = 550
print(inventory)
