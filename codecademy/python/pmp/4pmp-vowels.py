"""
Practice Makes Perfect!!!
"""

"""
Vowels!!!
Anti-Vowel Jihad!
Remove all vowels
"""
text = 'Hey You! Look Words!'
print(text)

def anti_vowel(text):
    result = ""
    for c in text:
        if c in "aeiouAEIOU":
            c = text.replace(c, "")
        else:
            result = result + c
    return result

print(anti_vowel(text))
