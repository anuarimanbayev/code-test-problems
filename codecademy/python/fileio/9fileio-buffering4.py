# Classes
# File I/O: File Input/Output
# PSA: Buffering Data #4
"""
Note that we don't explicitly close() our file,
and remember that if we don't close a file, our data
will get stuck in the buffer.
"""

with open("text.txt", "w") as my_file:
    my_file.write("Cowabunga!")
