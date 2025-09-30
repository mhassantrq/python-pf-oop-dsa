"""
Functions are pieces of code or blocks of code that are made to reuse the specific piece of code or to structure the code

in python the functions are defined using the 'def' keyword followed by the name of the function.

like other programming languages, functions need to be called to be able to execute.

lets see below how this works.
"""

def test_function():    #   function header with def name of function and parenthesis ending with colon
    print('test function')  #   lines in side the function
    print('second line')

test_function()     #   calling the above function by writing its name and parenthesis


"""
you can also make functions with passing variables to it.
these variables are passed as parameters within the parenthesis after the funciton name

lets see below
"""

def sum_of_digits(num1, num2):  #   two parameters num1 and num2
    num3 = num1 + num2          
    print(f'Sum of {num1} and {num2} is {num3}')

sum_of_digits(5, 6)             #   call function with function name and passing two values for parameters



"""
functions can also return a value.
lets convert above sum function to return the sum instead of printing it
"""

def sum_of_digits(num1, num2):  #   two parameters num1 and num2
    num3 = num1 + num2
    return num3

sum = sum_of_digits(5, 6)   #   since the function will return the value of sum, assign it to a variable get the returned value

print(f'sum: {sum}')