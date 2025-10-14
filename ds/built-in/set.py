"""
Sets are built in data structures in python

they are unordered
their values are easily changeable

sets strictly does not allow duplicate values
"""

var_set = {5, 1, 3, 5, 8}

print(var_set)

#   sets can be used to find unique elements from a list as well. lets explore below:

var_list = [5, 6, 8, 1, 2, 5, 'hi', 'hello', 5, 1, 2, 'hi']

var_set = set(var_list)     #   make a set from list, this way all unique values will be picked up

print(var_set)

#   add element in set
var_set.add(7)
print(f'After add 7: {var_set}')


#   remove an element
var_set.remove(2)
print(f'After remove 2: {var_set}')


#   add elements, more than one
var_set.update([10, 15, 20, 25])
print(f'After add 10, 15, 20, 25: {var_set}')


#   remove an element
var_set.discard(5)
print(f'After discard 5: {var_set}')


#   the difference between remove() and discard()
#   remove(): using this can cause an error if the element to be removed does not exist
#   discard(): using this does not cause an error if the element to be removed does not exist
