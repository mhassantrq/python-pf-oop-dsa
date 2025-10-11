import random


#   generate random number between 0 and 1. any float number.
var_num = random.random()
print(f'random float number between 0 and 1: {var_num}')


#   generate random number between two numbers
var_num = random.randint(1, 9)
print(f'random int number between 1 and 9: {var_num}')


#   generate random float number between two float numbers
var_num = random.uniform(1.5, 9.5)
print(f'random float number between 1.5 and 9.5: {var_num}')


#   get random choice from given list, tuple, string etc.
var_ch = random.choice('python')
print(f'random choice from given string: {var_ch}')

