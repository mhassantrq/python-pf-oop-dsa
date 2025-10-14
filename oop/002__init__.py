"""
__init___ member function in python class is a constructor which is called automatically once an object of the class is created
"""

class Student():
    def __init__(self):
        print('Constructor called automatically')


#   after creating object, constructor is called automatically
std = Student()


"""
you can also pass parameters via object creation to the init constructor
"""

class Student():
    def __init__(self, name, id):
        print(f'Constructor called automatically with name: {name} and id: {id}')


#   after creating object, constructor is called automatically
std = Student('Jon', '123')
