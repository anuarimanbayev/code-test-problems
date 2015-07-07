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
Hide the ship...
"""
def random_row(board):
    row = random.randint(0,len(board)-1)
    return row
    
def random_col(board):
    col = random.randint(0,len(board)-1)
    return col


"""
Debugging Code
To be removed later
"""
ship_row = random_row(board)
ship_col = random_col(board)
print(ship_row)
print(ship_col)


"""
Allowing only 4 guesses
"""
for turn in range(4):
    # ... and seek the ship! Guessing prompt!
    # raw_input of Python 2 (Codecademy lesson) was renamed to just input of Python 3
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))

    """
    Victory and Loss Conditions
    """
    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sank my battleship!")
        # To end the board game after victory condition is met
        break
    else:
        # Handling incorrect user input
        if guess_row not in range(5) or guess_col not in range(5):
            print("Oops, that's not even in the ocean.")
        elif board[guess_row][guess_col] == "X":
            print("You guessed that one already.")
        else:
            print("You missed my battleship!")
            board[guess_row][guess_col] = "X"
            print_board(board)
        if turn == 3:
            print("Game Over")
    print(turn + 1)

"""

Extra Credit!!!

You can also add on to your Battleship! program to make it more complex and fun to play. Here are some ideas for enhancements—maybe you can think of some more!

    Make multiple battleships: you'll need to be careful because you need to make sure that you don’t place battleships on top of each other on the game board. You'll also want to make sure that you balance the size of the board with the number of ships so the game is still challenging and fun to play.

    Make battleships of different sizes: this is trickier than it sounds. All the parts of the battleship need to be vertically or horizontally touching and you’ll need to make sure you don’t accidentally place part of a ship off the side of the board.

    Make your game a two-player game.

    Use functions to allow your game to have more features like rematches, statistics and more!

Some of these options will be easier after we cover loops in the next lesson. Think about coming back to Battleship! after a few more lessons and see what other changes you can make!
"""
