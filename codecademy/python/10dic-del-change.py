# key - animal_name : value - location 
zoo_animals = { 'Unicorn' : 'Cotton Candy House',
'Sloth' : 'Rainforest Exhibit',
'Bengal Tiger' : 'Jungle House',
'Atlantic Puffin' : 'Arctic Exhibit',
'Rockhopper Penguin' : 'Arctic Exhibit'}
# A dictionary (or list) declaration may break across multiple lines
print(zoo_animals)

# Removing the 'Unicorn' entry. (Unicorns are incredibly expensive.)
del zoo_animals['Unicorn']
# Removing the ferocious Sloth and its prey the Bengal Tiger
del zoo_animals['Sloth']
del zoo_animals['Bengal Tiger']
print(zoo_animals)

# Your code here!
zoo_animals['Rockhopper Penguin'] = 'Antarctic Exhibit'
# Rockhopper Penguins belong to Antarctica in the Southern Hemisphere around Chile and New Zealand
# Atlantic Puffin belongs in Arctica in the Northern Hemisphere, near Canada and Russian Federation

print(zoo_animals)
