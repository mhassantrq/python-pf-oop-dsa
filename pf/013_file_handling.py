"""
File handling refers to handle file operations in python such as open, close, read, write or delete files.

modes for file handling
a:  append
r:  read
w:  write
x:  create
t:  text
b:  binary
"""


#   to open a file with mode read
#   the first parameter is the file path and the second parameter is the mode, such as r for read
f = open('data.txt', 'r')


#   to print file, store it in a variable
var = f.read()
print(var)

"""
read():         reads the complete file, stores as a single string
readline():     reads a single line
readlines():    reads complete file, but stores as a list of lines
"""
f.close()


#   to write to a file
f = open('data.txt', 'w')
f.write('hello')
f.close()

#   to append to a file
f = open('data.txt', 'a')
f.write(' python')
f.close()


"""
the difference between write and append mode:
write mode clears all the file and then writes lines on blank file
append does not clear all data, but just adds new lines with the existing data
"""

"""
when you open a file, you must close it after you're done with your task.

to not worry about closing file every time you open it.
using the 'with' command
this will take care of closing the file itself.
"""

with open('data.txt', 'r') as f:
    var = f.read()
    print(var)