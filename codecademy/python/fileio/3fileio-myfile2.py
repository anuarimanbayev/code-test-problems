# Classes
# File I/O: File Input/Output
# MyFile Write

"""
You can open files in write-only mode ("w"), read-only mode ("r"),
read and write mode ("r+"), and append mode ("a",
which adds any new data you write to the file to the end of the file).
"""
my_list = [i**2 for i in range(1,11)]

my_file = open("output.txt", "r+")

# Add your code below!
for item in my_list:
    my_file.write(str(item) + "\n")

my_file.close()
