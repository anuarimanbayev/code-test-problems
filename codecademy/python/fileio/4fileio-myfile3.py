# Classes
# File I/O: File Input/Output
# Read from File only #3

"""
You can open files in write-only mode ("w"), read-only mode ("r"),
read and write mode ("r+"), and append mode ("a",
which adds any new data you write to the file to the end of the file).
"""
my_file = open("output.txt", "r")

print my_file.read()

my_file.close()
