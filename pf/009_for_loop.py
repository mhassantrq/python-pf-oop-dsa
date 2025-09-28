"""
Loop is an iterative structure which repeats the same operations for some or many iterations.

The for loop is a kind of loop which python provides for handling multiple iterations.
"""



"""
For loop uses the range function to run for a specified number of iteration
range function can have multiple values.

if range has 2 values,
the loop below with range(0, 6) will run from initial value of 0 to final value of 6 - 1 = 5.
"""
for i in range(0, 6):
    #   print i, and see that iterations start from 0 and end at 5. last value of range is not included
    print(i)



"""
if range has 1 value

For loop woth only one value in range function

this means that initial value will be assumped 0 and will run until 5-1 = 4.
"""
for i in range(5):
    print(i)


"""
if range has 3 values,

For loop with three values in range function

range(5, 100, 3)

this means that initial value if 5, final value is 100-1 and each iteration will jump 3 numbers
so 5, then 8, then 11 and so on.
"""
for i in range(5, 100, 3):
    print(i)



"""
for loop can alse be run on a list or a string.

if youre not familiar with list or arrays, visit ds directory of this repo.
"""

for w in "hello python":
    print(w)
#   this will iterate over every character in the string provided


for d in [55, 68, 2, 61, 73]:
    print(d)
#   this will iterate over every element in the list provided