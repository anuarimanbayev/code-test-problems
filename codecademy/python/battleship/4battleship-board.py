"""
BATTLESHIP PROJECT
In this project you will build a simplified, one-player version of the classic board game Battleship! In this version of the game, there will be a single ship hidden in a random location on a 5x5 grid. The player will have 10 guesses to try to sink the ship.

To build this game we will use our knowledge of lists, conditionals and functions in Python.

The first thing we need to do is to set up the game board.
"""

# Python 3 needs to import the "random" library in order to use randit function
import random

# Setting up the empty board
board = []


"""
Create a 5 x 5 grid initialized to all 'O's and store it in board.
"""
for i in range(0, 5):
    i = ["O"] * 5
    board.append(i)

print(board)


"""
Custom Print on each separate line or row
"""
def print_board(board):
    for row in board:
        # Printing pretty, using the join command
        print(" ".join(row))
        
print_board(board)


"""
Adding 2-dimensional 'hidden' battleship!
"""
def random_row(board):
    row = random.randint(0,len(board)-1)
    return row
    
def random_col(board):
    col = random.randint(0,len(board)-1)
    return col

random_row(board)
random_col(board)
