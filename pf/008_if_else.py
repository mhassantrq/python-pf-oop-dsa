"""
Conditional Structure: If else

These are used to control the flow of the code execution.

lets see basic example of how this works below
"""

num1, num2 = 5, 6

if num1 > num2:
    print('Num1 is greater')
    #   any thing written under if statement with indentation is part of the body of if statement
else:
    print('Num2 is greater')

"""
Above is a simple example of use of if and else.

unlike some other progamming languages, python does not use curly brackets for declaring body of if and else.
python uses indentation for this purpose. as can be seen in above example of if.

if can work alone without else as well.
"""

"""
in python, a short hand if is available similar to the ternary operators of c and cpp.

it can be used when code size needs to be reduced or kept simple. when the conditional requirement is simpler.

lets write short hand if of the above example.

num1, num2 = 5, 6

if num1 < num2:
    print('Num1 is greater')
    #   any thing written under if statement with indentation is part of the body of if statement
else:
    print('Num2 is greater')
"""

#   short hand if 

print('Num1 is greater') if num1 > num2 else print('Num2 is greater')


"""
What if you want multiple if statements for problems like writing code for grade assigning.
if marks between 90 and 100 assign A, if marks between 80 and 89 assign grade B and so on and so forth.

for purpose of using multiple if in parallel. Python provides 'elif'.

lets see below how it works.
"""

marks = int(input('Enter marks: '))

if marks >= 90:
    print('A')
elif marks >= 80:   #   you can write condition in from of elif the same way you write infront of if statements
    print('B')
elif marks >= 70:
    print('C')
elif marks >= 60:
    print('D')
else:
    print('F')


"""
Seems right. 

What if a student has 65 marks, that greater than 60 and 70 and 80 and 90. so the above code may work, 
but is not precise and covering all aspects.

for this purpose, we should cover both boundries in an if.

if marks >= 90 and aslo marks less than or equal to 100.

for this purpose, we use logical operators 'and' and 'or'.

lets edit above example to include the changes:
"""


if marks >= 90 and marks <= 100:
    print('A')
elif marks >= 80 and marks < 90:
    print('B')
elif marks >= 70 and marks < 80:
    print('C')
elif marks >= 60 and marks < 70:
    print('D')
else:
    print('F')