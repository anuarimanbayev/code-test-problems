# Classes
# File I/O: File Input/Output
# PSA: Buffering Data #5
"""
Note that we don't explicitly close() our file, and
remember that if we don't close a file, our data
will get stuck in the buffer.
"""

with open("text.txt", "w") as my_file:
    my_file.write("Cowabunga!")
    if my_file.closed == False:
        my_file.close()
    print(my_file.closed)
