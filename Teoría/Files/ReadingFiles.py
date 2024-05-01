# Open the file in read ('r') mode
file = open('file.txt', 'r')

# Open the file using 'with' in read ('r') mode
with open('file.txt', 'r') as file:
    # further code
  
# Reading and Storing the Entire Content of a File
# Using the read method, you can retrieve the complete content of a file
# and store it as a string in a variable for further processing or display.
# Step 1: Open the file you want to read
with open('file.txt', 'r') as file:
    # Step 2: Use the read method to read the entire content of the file
    file_stuff = file.read()
    # Step 3: Now that the file content is stored in the variable 'file_stuff',
    # you can manipulate or display it as needed.
    # For example, let's print the content to the console:
    print(file_stuff)
# Step 4: The 'with' statement automatically closes the file when it's done,
# ensuring proper resource management and preventing resource leaks.

#Reading a file line by line
file = open('file.txt', 'r')
line1 = file.readline()  # Reads the first line
line2 = file.readline()  # Reads the second line
print(line1)  # Print the first line
if 'important' in line2:
    print('This line is important!')
while True:
    line = file.readline()
    if not line:
        break  # Stop when there are no more lines to read
    print(line)
  file.close()

#Reading specific characters
file = open('file.txt', 'r')
file.seek(10)  # Move to the 11th byte (0-based index)
characters = file.read(5)  # Read the next 5 characters
print(characters)
file.close()

#Example: Importing libraries to open a file
from pyodide.http import pyfetch

import pandas as pd

filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt"

async def download(url, filename):

    response = await pyfetch(url)

    if response.status == 200:

        with open(filename, "wb") as f:

            f.write(await response.bytes())

await download(filename, "example1.txt")

print("done")

# Read the Example1.txt
example1 = "example1.txt"
file1 = open(example1, "r")

# Print the path of file
file1.name

# Print the mode of file, either 'r' or 'w'
file1.mode

# Read the file
FileContent = file1.read()
FileContent

# Print the file with '\n' as a new line
print(FileContent)

# Type of file content
type(FileContent)

# Close file after finish
file1.close()

# Open file using with
with open(example1, "r") as file1:
    FileContent = file1.read()
    print(FileContent)

# Read first four characters
with open(example1, "r") as file1:
    print(file1.read(4))

# Read certain amount of characters

with open(example1, "r") as file1:
    print(file1.read(4))
    print(file1.read(4))
    print(file1.read(7))
    print(file1.read(15))

# Read one line

with open(example1, "r") as file1:
    print("first line: " + file1.readline())

#We can also pass an argument to  readline()  to specify the number of charecters we want to read. However, unlike  read(),  readline() can only read one line at most.
with open(example1, "r") as file1:

  # Iterate through the lines

with open(example1,"r") as file1:
        i = 0;
        for line in file1:
            print("Iteration", str(i), ": ", line)
            i = i + 1
    print(file1.readline(20)) # does not read past the end of line
    print(file1.read(20)) # Returns the next 20 chars


# Read all lines and save as a list

with open(example1, "r") as file1:
    FileasList = file1.readlines()
