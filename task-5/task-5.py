import random

redundant_list = [random.randint(0, 9) for _ in range(1000)]

unique_set = set(redundant_list)

# Print the results
print(f"Original list: {redundant_list}")
print(f"Unique set: {unique_set}")

# Will only ouput a number once in the unique set