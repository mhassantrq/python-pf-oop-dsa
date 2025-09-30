"""
Similar to for loop, while loop is used to iterate and run the same piece of code multiple times.

while loop is run until a specific condition is not false.

as seen in previous lesson of for loop. many things are handled by for loop like incrementing.
however, in while loop, we have to take care of these ourselves.
"""

i = 0   #   initialize the start value of variable
while i<= 10:   #   condition of while stopping
    print(i)    
    i += 1      #   increment the variable controlling the loop
"""
i = 0 # initial value of i set to 0

while i<= 10: # loop runs while i is less than or equal to 10
    print(i)
    i += 1 # increment value of i with +1 in every iteration

the above loop will run until i reaches 10
i starts at value 0. with every iteration, i is incremented by +1. so loop will run total 11 times. for i=0, i=1 and until i=10.
"""

#   while loop can also be run based on a condition without increment of decrement

var = int(input('Enter number: '))
while var != -1 :
    var = int(input('Enter number: '))

"""
the above loop runs until -1 is entered.
this way, we are not sure how long the while loop may run.
it may run for 2 iterations or 20 or 200.
until the input -1 has been entered.
"""
