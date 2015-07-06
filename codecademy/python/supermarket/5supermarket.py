prices = {
    "banana" : 4,
    "apple"  : 2,
    "orange" : 1.5,
    "pear"   : 3,
}
stock = {
    "banana" : 6,
    "apple"  : 0,
    "orange" : 32,
    "pear"   : 15,
}

# Displaying the content of the keys in two dictionaries
# Displaying the item and its associated price and stock
for key in prices:
    print(key)
    print("price: %s" % prices[key])
    print("stock: %s" % stock[key])

# Total value of inventory    
total = 0
for key in prices:
    number = prices[key] * stock[key]
    print(number)
    total = total + number

print(total)
