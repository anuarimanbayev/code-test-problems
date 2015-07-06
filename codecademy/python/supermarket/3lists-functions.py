# Lists + Functions

def fizz_count(x):
    count = 0
    for item in x:
        if item == "fizz":
            count = count + 1
    return count
    
# Test Case
fizzcatfizz = ("fizz", "cat", "fizz")
fizzycat = fizz_count(fizzcatfizz)

print(fizzycat)
