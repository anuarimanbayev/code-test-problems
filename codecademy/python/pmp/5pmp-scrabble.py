"""
Practice Makes Perfect!!!
"""

"""
Scrabble!!!
"""
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}

# Assume input is only one word containing no spaces or punctuation
# No score multipliers
# Handle for uppercase, lowercase, or a mix of characters
def scrabble_score(word):
    total = 0
    word = word.lower()
    for c in word:       
        total = total + score[c]
    return total

word = "Scrabble"
print(word)
print(scrabble_score(word))
