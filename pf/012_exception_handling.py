"""
Exception handling is used to manage situations where an error may occur causing system to crash or worsen.

To perform this, try and exception is used.

lets see below
"""

try:    #   this block contains piece of code which may cause an exception
    num=5
    num /= 0    #   since division by 0 causes an error.
except:     #   due to error, this block will be executed
    print('An error')

"""
in the above example number 5 is to be divided by zero. since division by zero can cause error, we'll put this code in the try block
every try block will either have an except block as given above or a finally block.

except will contain code to be run incase of an error. moreover, except block can catch specific exceptions as well.
lets see an example of this below.
"""

try:
    num=5
    num /= 0
except ZeroDivisionError:
    print('division by zero')

"""
It can be seen that except block can be used to catch specific type of error. like zero division error and more.

try block can also have finally block. finally block is run regardless of an exception or not.
"""

try:
    num=5
    num /= 0
except:
    print('This will run as there will be error in this case')
finally:
    print('finally block with error raised')


try:
    num=5
    num /= 2
except:
    print('This will not run as there will be no error in this case')
finally:
    print('finally block without error raised')
