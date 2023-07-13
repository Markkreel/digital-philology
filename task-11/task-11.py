'''
• Use a list comprehension to create a list of the numbers plus one.
• Creates a list of all of the list of strings in fruits and uppercases every string
• Make a list that contains each fruit with exactly 5 characters
```
fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]
#????
```
'''

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

# List comprehension to create a list of numbers plus one
numbers_plus_one = [num + 1 for num in numbers]
print("Numbers plus one:", numbers_plus_one)

# List comprehension to create a list of uppercased strings
uppercased_fruits = [fruit.upper() for fruit in fruits]
print("Uppercased fruits:", uppercased_fruits)

# List comprehension to create a list of fruits with exactly 5 characters
fruits_with_5_characters = [fruit for fruit in fruits if len(fruit) == 5]
print("Fruits with exactly 5 characters:", fruits_with_5_characters)
