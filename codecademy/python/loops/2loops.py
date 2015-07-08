"""
LOOPS!!!
"""

"""
While Loop vs. If statement
"""

count = 0

if count < 5:
    print("Hello, I am an if statement and count is", count)
    
while count < 10:
    print("Hello, I am a while and count is", count)
    count += 1

loop_condition = True

while loop_condition:
    print("I am a loop")
    loop_condition = False

num = 1

while num < 11:  # Fill in the condition
    # Print num squared
    print(num ** 2)
    # Increment num (make sure to do this!)
    num += 1

"""
Catching simple errors
"""
choice = input('Enjoying the course? (y/n)')

while choice != "y" and choice != "n":  # Fill in the condition (before the colon)
    choice = input("Sorry, I didn't catch that. Enter again: ")

"""
Catching an Infinite Loop error
"""
count = 0

while count < 10: # Add a colon. Synatx Error.
    print(count)
    # Increment count. Logical Error.
    count += 1

"""
Alternative way to stop an Infinite Loop error
Use the break command
"""
count = 0

while True:
    print(count)
    count += 1
    if count >= 10:
        break
