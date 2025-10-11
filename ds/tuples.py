"""
tuple is built in data structure in python.

tuples are immutable, this means that any value in the tuple once created or assigned cannot be changed later on.

tuples can have values of different data types.
tuples are ordered.
"""

#   define a tuple with values
var_tuple = (5, 6.3, 'hi')

#   check tuple type
print(type(var_tuple))

print(var_tuple)


#   tuples can be defined without parenthesis as well
var_tuple = 5, 3.5, 'hello'

#   lets see if this is still a tuple without parenthesis
print(type(var_tuple))

#   tuples are immutable, their values cannot changed once created. lets examine below
var_tuple = (5, 3.8, 'python', 7, 'tuple')

print(f'1st Element: {var_tuple[0]}')

#   lets try to change the value of index 0
var_tuple[0] = 6

#   as you can see from output, the above line of reassigning the index 0 raises a type error
