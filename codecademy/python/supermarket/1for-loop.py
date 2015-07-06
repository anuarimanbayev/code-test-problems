# FOR loop in LISTS & DICTIONARIES
# Remember to use Python3 syntax for print statement with parentheses!


# FOR loop in LISTS
names = ["Adam","Alex","Mariah","Martine","Columbus"]
for x in names:
    print(x)

# FOR loop in DICTIONARIES
webster = {
	"Aardvark" : "A star of a popular children's cartoon show.",
    "Baa" : "The sound a goat makes.",
    "Carpet": "Goes on the floor.",
    "Dab": "A small amount."
}

# Add your code below!
for key in webster:
    print(webster[key]) # prints the content of keys, in this case definitions of words
