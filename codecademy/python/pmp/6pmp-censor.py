"""
Practice Makes Perfect!!!
"""

"""
Censor!!!
Write a function called censor that takes two strings, text and word, as input.
It should return the text with the word you chose replaced with asterisks.

censor("this hack is wack hack", "hack")
should return:
"this **** is wack ****"

Assume your input strings won't contain punctuation or upper case letters.
The number of asterisks you put should correspond to the number of letters in the censored word.
"""

text = "Hey hey hey, it's fat Albert!"
word = "hey"

def censor(text,word):
    text_split = text.split()
    new_text = []

    for x in text_split:
        if x == word:
            starsies = "*" * len(word)
            new_text.append(starsies)
        else:
            new_text.append(x)
    fin_text = " ".join(new_text)
    return fin_text
    
print(text)
print(word)
print(censor(text, word))
