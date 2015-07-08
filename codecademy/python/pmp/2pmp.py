"""
Practice Makes Perfect!!!
"""

"""
factorial
"""
def factorial(x):
    result = 1
    while x > 0:
        result = result * x
        x -= 1
    return result

print(factorial(4))
print(factorial(1))
print(factorial(3))

"""
is_prime
"""
def is_prime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    else:
        for i in range(2, x-1):
            if x%i == 0:
                return False
        return True

print(is_prime(9))
print(is_prime(11))
print(is_prime(21))
