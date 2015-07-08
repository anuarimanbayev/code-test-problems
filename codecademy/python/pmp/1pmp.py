"""
Practice Makes Perfect!!!
"""

"""
is_even function
"""
def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

"""
is_int function
"""
# x = 2.1
# int(x) = 2
# 2.1 - 2 = 0.1! This means it's a float, not an integer
def is_int(x):
    if x - int(x) == 0:
        return True
    else:
        return False
"""
digit_sum function
"""
def digit_sum(n):
    result = []
    digits = str(n)
    for digit in digits:
       digit = int(digit)
       result.append(abs(digit))
    return sum(result)

"""
Challenge
If you're looking for a challenge, try this:
To get the rightmost digit of a number, you can modulo (%) the number by 10.
To remove the rightmost digit you can floor divide (//) the number by 10.
Don't worry if you're not familiar with floor division—you can look up the documentation here.
Remember, this is a challenge!
Try working this into a pattern to isolate all of the digits and add them to a total.
"""
def digit_sum2(n):
    total = 0
    while n > 0:
        total = total + n%10
        n = n // 10
    return total
print(digit_sum2(1234))
