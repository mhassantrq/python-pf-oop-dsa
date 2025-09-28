"""
lists are data structures used in python to store values.

elements in list are easily changeable.
duplicates are allowed in a list.


"""

#   list is defined using sqaure brackets, with elements separated by comma
varlist = [5, 8, 1, 6, 8, 9]
print(varlist)



"""
an important and flexible thing about list is that it allows elements of different data types
"""

#   initialize list with multiple data types, below list has all four different data types
varlist = [55, True, 'hello', 2.5]
print(varlist)


#   find the length of list
length_of_list = len(varlist)
print(f'Length of list: {length_of_list}')


#   access an element of list with index number 
print(varlist[2])   #   access index 2 which means 3rd element as indexing starts from 0


"""
new elements can be added in the list

to add an element at the end of the list, use the 'append' function
to add an element at the specified index of the list, use the 'insert' function

lets see below
"""

varlist.append('last element')
print(varlist)
#   in above code, the string 'last element' is appended at the the end of varlist. printing varlist can confirm this.


varlist.insert(2, 'the index 2 element')
print(varlist)
#   in the above code element is added at index 2. and the rest of list elements are moved to their index + 1 position


"""
to remove an element.

use remove function and give the element as its parameter.
use remove pop and give the index as its parameter.
"""

varlist.remove('hello')
print(varlist)

varlist.pop(2)
print(varlist)
