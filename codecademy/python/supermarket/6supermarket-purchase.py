shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
    
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Supermarket Purchase
def compute_bill(food):
    total = 0
    for item in food:
        # To check whether there is enough stock in inventory to sell this item
        if stock[item] > 0:
            total = total + prices[item]
            # to decrease the inventory stock count
            stock[item] = stock[item] - 1
    return(total)

purchase = compute_bill(shopping_list)
print(purchase)
print(stock["banana"])
print(stock["orange"])
