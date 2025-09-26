"""
Logical Operators

    and:    it needs all operands to be true in order for final result to be true
    or:     it needs atleast one operand to be true in order for final result to be true
    not:    it changes the true value to false, and false to true
    

"""

var1, var2 = True, False

#   and operator
res = var1 and var2
print(f'And Operator: {res}')

#   or operator
res = var1 or var2
print(f'Or Operator: {res}')

#   not operator
res = not var1
print(f'Not Operator: {res}')