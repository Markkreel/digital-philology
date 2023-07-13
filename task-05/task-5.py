'''
Make a list of integers with redundant items using sampling (from random import randintn;
num1= randint(0,9)). Repeat 1000 times and build a list
• Create a set from the list.
'''

import random

# Generating a list of integers
num_list = [random.randint(0, 9) for i in range(1000)]

# Creating a set from the list
num_set = set(num_list)

print(num_set)

'''
Despite the algorithm generating 1000 instances of digits ranging from 0 to 9, 
when we pass the list as input to the set() function, 
it will only select unique values and organize them in a sorted manner.
'''
