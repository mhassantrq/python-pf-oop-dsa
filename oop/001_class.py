"""
Class in python

classes are used to represent entites in python.
these are blueprint containing attributes of class, variables and functions.

class is defined as follows:
"""

#   class keyword accompanied by the name of class. Student in this case.
class Student:
    def name(self):     #   a member function of the class
        print('this is student class')

"""
creating object of a class

state the object name, assignment operator and class name ending with parenthesis 
"""
std = Student()

std.name()
