"""
LOOPS!!!
"""

"""
Something completely different about Python is the while/else construction. while/else is similar to if/else, but there is a difference: the else block will execute anytime the loop condition is evaluated to False. This means that it will execute if the loop is never entered or if the loop exits normally. If the loop exits as the result of a break, the else will not be executed.

In this example, the loop will break if a 5 is generated, and the else will not execute. Otherwise, after 3 numbers are generated, the loop condition will become false and the else will execute.
"""
import random

print("Lucky Numbers! 3 numbers will be generated.")
print("If one of them is a '5', you lose!")

count = 0
while count < 3:
    num = random.randint(1, 6)
    print(num)
    if num == 5:
        print("Sorry, you lose!")
        break
    count += 1
else:
    print("You win!")

"""
Guessing Game 2.0
"""
from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)
print("A random number between 1 and 10 is generated")
print(random_number)

guesses_left = 3
# Start your game!
while guesses_left > 0:
    guess = int(input("Your guess: "))
    if guess == random_number:
        print("You win!")
        break
    guesses_left -= 1
else:
    print("You lose.")

"""
FOR your hobbies
"""
hobbies = []

# Add your code below!
for i in range(3):
    hobby = input("Enter a hobby: ")
    hobbies.append(hobby)
    i += 1

print(hobbies)
