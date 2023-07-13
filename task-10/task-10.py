'''
• Write a Python program to create a lambda function that adds 15 to a given number passed
in as an argument, also create a lambda function that multiplies argument x with argument y
and print the result.
• Write a Python program to sort a list of tuples using Lambda.
• Write a Python program to filter an even list of integers using Lambda.
'''

#Part I

# Lambda function to add 15 to a given number
add_15 = lambda num: num + 15

# Lambda function to multiply two numbers
multiply = lambda x, y: x * y

print("Result of adding 15 to 10:", add_15(10))
print("Result of multiplying 5 and 6:", multiply(5, 6))

# Part II

# List of tuples to be sorted using Lambda
tuple_list = [(3, 6), (1, 8), (2, 4), (5, 7)]

# Sorting the list of tuples using Lambda
sorted_list = sorted(tuple_list, key=lambda x: x[0])

print("Sorted list of tuples:", sorted_list)

# Part III

# List of integers to be filtered using Lambda
int_list = [2, 5, 8, 11, 14, 17]

# Filtering even numbers from the list using Lambda
filtered_list = list(filter(lambda x: x % 2 == 0, int_list))

print("Filtered list of even numbers:", filtered_list)
