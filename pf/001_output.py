"""
In python the function used to output on console is the print() function.
"""

#   simple print usage
print('Hello')

"""
You can use both single or double quotes around a string within print function.

print('Hello') and print("Hello")   are both used and both are correct.
"""

print("using double quotes")
print('using single quotes')


#   You can concatenate multiple strings in print
#   Using concatenation in print function

var1 = 'hello'
var2 = 'python'

print(var1 + ' ' + var2)    # concatenate multiple strings in print

#   theres an other way to include variables within print function. using the format string

print(f'hello {var2}')  #   using f with quotes. In quotes, to include a variable, enclose its name within curly brackets