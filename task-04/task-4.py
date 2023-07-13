'''
Create 2 lists with same length ID (int) and name (String):
• Combine both lists to a list of tuples
'''

# ID list
id_list = [1, 2, 3, 4, 5]

# Name list
name_list = ["Alice", "Bob", "Charlie", "David", "Eve"]

# Combining the lists into a list of tuples
combined_list = list(zip(id_list, name_list))

print(combined_list)
