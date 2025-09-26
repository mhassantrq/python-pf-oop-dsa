"""
to store different data and values in python, variables are used.

there are different types of variables, with different datatypes.


variables have data types. These indicate the type of data that is stored in the variable.
Most common data types include:
    int:        for integer values such as 1, 55, 34 etc.
    float:      for float values, values that have decimal point or fractional values such as 1.5, 55.69 etc.
    bool:       for boolean values which include only one to two values, either True or False.
    string:     for string values, values that are enclosed in quotes such as 'hello' or "hello" etc.

    
unlike some other languages such as c++, c, java etc. python does not need to specifically declare variables with data types.
its created the very time once you assign a value to a variable, a its data type is automatically assign based on the value given to it.
to check the data type of a variable, use the type() function and pass the name of variable as parameter to it. 


variable names should begin with either underscore or alphabets, small or upper case such as name, NAME, _name
name can include numbers after the first character such as var1, var2
longer name or multiple names can be joined using underscore such as student_name


lets explore this further:
"""

#   to use a variable, assign a value to it

#   int variable
var = 5
print(f'int variable: {type(var)}')    # this will output int class as the var we initialized above int float value

#   float variable
var = 5.69
print(f'float variable: {type(var)}')    # this will output float class as the var we initialized above has float value

#   bool variable
var = True
print(f'bool variable: {type(var)}')    # this will output bool class as the var we initialized above has bool value

#   string variable
var = 'hello'
print(f'string variable: {type(var)}')    # this will output string class as the var we initialized above has string value



#   a variable value can be changed afterwards in the code as well
#   for example:

var = 5     #   int value given

#   later on this variable can be re used with changed value and data type

var = 'hello'   #   now the same variable is re used with changed value and data type


#   assigning multiple variables multiple values
var1, var2 = 55, 69

"""
this way multiple values are assigned to multiple variables in a single line,
variable names separated by commas, and on right side of assignment operator, multiple values separated by commas.

the first value in sequence will be assigned to first variable in sequence, and so on and so forth.
"""


"""
variables can be deleted as well once they are no longer needed,

using del 
example:
"""

var = 4

del var

#   now var named variable cannot be used unless its initialized again with a value.


