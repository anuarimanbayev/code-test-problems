"""
Practice Makes Perfect!!!
"""

"""
String Reversal!!!
"""

text = "Python!"

def reverse(text):
    # Use the length command to find out the index of the last character, 1-n
    index = len(text)
    print(index)
    # Create an emptry string to store the new reversed result of the string text
    result = ""
    while index > 0:
        # Append the last character, 1-n, of the n on the 0-n scale
        result = result + text[index - 1]
        # Decrease the index pointer that looks into the string text
        index = index - 1
    return result

print(reverse(text))
