"""
Arithemtic operators in Python
"""


num1, num2 = 74, 60

#   addition operator
res = num1 + num2
print(f'Addition Operator: {res}')


#   subtraction operator
res = num1 - num2
print(f'Subtraction Operator: {res}')


#   multiplication operator
res = num1 * num2
print(f'Multiplication Operator: {res}')


#   division operator
res = num1 / num2
print(f'Division Operator: {res}')


#   exponentiation operator
"""
this operator is represented by two asteriks

num1 ** num2
this means that num1 raised to power num2.
"""
res = num1 ** num2
print(f'Exponentiation Operator: {res}')


#   floor division operator
"""
this operator is represented by two slashes //

num1 // num2
this means that num1 divided by num2 and taking floor of the answer

example:  10 // 3 results in 10/3 == 3.33 and its floor is 3.
"""
res = num1 // num2
print(f'Floor Division Operator: {res}')


#   modulus operator
"""
this operator is represented by percentage symbol %

num1 % num2
this means that num1 divided by num2 and answer is the remainder after division

example:  10 % 3 results in remainder 1.
"""
res = num1 % num2
print(f'Modulus Operator: {res}')
