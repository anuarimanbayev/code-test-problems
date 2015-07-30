# Classes
# File I/O: File Input/Output
# Read Line from File #4

"""
You can open files in write-only mode ("w"), read-only mode ("r"),
read and write mode ("r+"), and append mode ("a",
which adds any new data you write to the file to the end of the file).
"""
my_file = open("text.txt","r")

for i in range(3):
    print(my_file.readline())
    
my_file.close()
