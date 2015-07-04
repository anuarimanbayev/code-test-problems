start_list = [5, 3, 1, 2, 4]
square_list = []

print(start_list)

# Your code here!
for number in start_list:
    number = number ** 2
    square_list.append(number)

print(square_list)
square_list.sort()
print(square_list)
