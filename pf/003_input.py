"""
for taking input in python, an input() funciton is used.

the very moment an input is taken, it has to be assigned to a variable to be used later on.

you can pass a string message in the input function for the user to know what to input

lets see an example below:
"""

name = input('enter your name: ')   #   input function has a message, and its value will be assigned to name variable


#   print the name variable to see what the user has input
print(f'entered name is: {name}')


"""
it is important to note that whatever the user inputs, by default the input returns a string value.
every single input taken, no matter the value, by default is a string.
"""

#   take a number input
num = input('enter a number: ')


#   check the data type of input
print(type(num))

"""
as you can see that the type of num is string, and not an int.
this is because by default, the input function return the input value as a string.

for you to be able to use this input and treat it as a number. the first thing to be is to convert it
to an int or float.

to convert it. Just pass the input value a parameter to int() or float()

for example:    int(num)    or      float(num)

lets see an example below:
"""


new_num = input('enter a number: ')

print(f'input by default: {type(new_num)}')

new_num = int(new_num)

print(f'input after conversion to int: {type(new_num)}')


#   the same way as above, the number can be converted to float.

new_num = input('enter a number: ')

print(f'input by default: {type(new_num)}')

new_num = float(new_num)

print(f'input after conversion to float: {type(new_num)}')

