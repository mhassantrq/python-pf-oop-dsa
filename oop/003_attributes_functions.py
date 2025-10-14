"""
Class member functions and attributes
"""

class Student():
    def __init__(self, name, id, subject):      #   parameters with values
        #   name, id and subject variables of class Student represented with 'self.'
        self.name = name
        self.id = id
        self.subject = subject

    def std_info(self):     #   class member function
        print(f'Student Name: {self.name}, id: {self.id}, subject: {self.subject}')

std = Student('Jon', 123, 'Chemistry')

std.std_info()  #   calling class member function

std.id = 456        #   changing value of member attributes of class with object std

std.std_info()