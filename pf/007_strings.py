"""
strings have been discussed to some extent in the previous files.

lets explore some functions that can be performed on or with strings.
"""

str_var = "hello, this is strings in python"

#   upper case all string
str_var = str_var.upper()
print(str_var)


#   lower case all string
str_var = str_var.lower()
print(str_var)


#   capital the first alphabet of string
str_var = str_var.capitalize()
print(str_var)


#   capital the first alphabet of every word in string
str_var = str_var.title()
print(str_var)


#   print only some portion of a string, via slicing
str_var = str_var[5:15]     # str only from 5th element to 14 element
print(str_var)