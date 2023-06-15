colors = ["Red", "Green", "Blue"]
names = ["Alice", "Bob", "Charlie"]

# Sort both lists alphabetically
colors.sort()
names.sort()

# Combine both lists
combined_lists = colors + names

# Forget the last element of both lists and combine them
colors.pop()
names.pop()
combined_lists_forget_last = colors + names

# Print the results
print("Combined lists:")
print(combined_lists)
print("\nCombined lists (forgetting the last element):")
print(combined_lists_forget_last)
