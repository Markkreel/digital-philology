numbers = [1, 2, 3, 4, 5]

# Use list comprehension to create a list of numbers plus one
numbers_plus_one = [num + 1 for num in numbers]
print("Numbers plus one:", numbers_plus_one)

fruits = ["apple", "banana", "cherry", "date"]

# Create a list of uppercase strings from the fruits list
uppercase_fruits = [fruit.upper() for fruit in fruits]
print("Uppercase fruits:", uppercase_fruits)

# Create a list of fruits with exactly 5 characters
fruits_with_5_chars = [fruit for fruit in fruits if len(fruit) == 5]
print("Fruits with exactly 5 characters:", fruits_with_5_chars)
