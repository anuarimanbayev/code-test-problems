# Advanced Topics in Python
# BITS

# Counting in base 2
one = 0b1
two = 0b10
three = 0b11
four = 0b100
five = 0b101
six = 0b110
seven = 0b111
eight = 0b1000
nine = 0b1001
ten = 0b1010
eleven = 0b1011
twelve = 0b1100

print(0b1)
print(0b10)
print(0b11)
print(0b100)
print(0b101)
print(0b110)
print(0b111)
print(0b1000)
print(0b1001)
print(0b1010)
print(0b1011)
print(0b1100)

"""
bin() takes an integer as input and returns the binary representation
of that integer in a string
"""
print(bin(1))
print(bin(2))
print(bin(3))
print(bin(4))
print(bin(5))

"""
int() function that can turn non-intger input into integer has also a second
parameter. When given a string containing a number and the base that number is in,
the function will return the valueof that number converted to base ten.
"""
print(int("1",2))
print(int("10",2))
print(int("111",2))
print(int("0b100",2))
print(int(bin(5),2))
# Print out the decimal equivalent of the binary 11001001.
print(int("11001001", 2))

"""
Left and Right Shift Bitwise operators shift the bits of a number over
by a designated number of slots. Shifting all the 1s and 0s left or right by
the specified number of slots.
"""
shift_right = 0b1100
shift_left = 0b1

# Your code here!
shift_right = shift_right >> 2
shift_left = shift_left << 2

print(bin(shift_right))
print(bin(shift_left))

"""
Bitwise AND (&) operator compares two numbers on a bit a level and
returns a number where the bits of that number are turned on,
if the corresponding bits of both numbers are
"""
print(bin(0b110 & 0b101))

"""
itwise OR (|) operator compares two numbers on a bit level and
returns a number where the bits of that number are turned on
if either of the corresponding bits of either number are 1
"""
print(bin(0b1110 | 0b101))

"""
OR (^) or exclusive or operator compares two numbers on a bit level and
returns a number where the bits of that number are turned on
if either of the corresponding bits of the two numbers are 1, but not both.
"""
print(bin(0b1110 ^ 0b101))

"""
bitwise NOT operator (~) just flips all of the bits in a single number,
effectively adding one to the number and then making it negative.
"""
print(~1)
print(~2)
print(~3)
print(~42)
print(~123)

"""
bit mask is just a variable that aids you with bitwise operations.
A bit mask can help you turn specific bits on, turn others off,
or just collect data from an integer about which bits are on or off.
"""
def check_bit4(input):    
    mask = 0b1000
    desired = input & mask

    if desired > 0:
        return "on"
    else:
        return "off"

"""
You can also use masks to turn a bit in a number on using |.
Using the bitwise | operator will turn a corresponding bit on if it is off
and leave it on if it is already on.
"""
a = 0b10111011
mask = 0b100
desired = a | mask
print(bin(desired))

"""
Using the XOR (^) operator is very useful for flipping bits. Using
^ on a bit with the number one will return a result where that bit is flipped.

You'll need a mask the same length as a in which all of the bits are turned
on (all set to 1).
"""
a = 0b11101110
mask = 0b11111111
desired = a ^ mask
print(bin(desired))

# Slip and Slide
"""
Use the left shift (<<) and right shift (>>) operators to slide masks into place.

Use the << operator to move your mask into place and the ^ operator to flip your desired bit.
"""
def flip_bit(number, n):
    mask = (0b1 << n-1)
    result = number ^ mask  
    return bin(result)
