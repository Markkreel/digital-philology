# Create a lambda function to add 15 to a given number
add_fifteen = lambda x: x + 15

# Create a lambda function to multiply two numbers
multiply = lambda x, y: x * y

# Test the lambda functions
number = 10
result_add = add_fifteen(number)
print(f"Result of adding 15 to {number}: {result_add}")

x = 5
y = 7
result_multiply = multiply(x, y)
print(f"Result of multiplying {x} and {y}: {result_multiply}")

# Sort a list of tuples using a lambda function
list_tuples = [(2, 4), (1, 3), (5, 1), (3, 2)]
sorted_tuples = sorted(list_tuples, key=lambda x: x[1])
print("Sorted list of tuples:", sorted_tuples)

# Filter even integers from a list using a lambda function
list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, list_numbers))
print("Filtered even numbers:", even_numbers)
