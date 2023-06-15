import pandas as pd

# Read the banklist.csv file into a dataframe called banks
file_path = "/home/mark/Documents/digital-philology/task-15/banklist.csv"
banks = pd.read_csv(file_path)

# Show the head of the dataframe
print("Head of the dataframe:")
print(banks.head())

# Get the column names
column_names = banks.columns
print("\nColumn names:")
print(column_names)

# Count the number of unique States (ST)
num_states = banks['ST'].nunique()
print("\nNumber of unique States (ST):", num_states)

# Get a list or array of all the states in the dataset
states_list = banks['ST'].unique()
print("\nList of all states:")
print(states_list)

# Get the top 5 states with the most failed banks
top_5_states = banks['ST'].value_counts().head(5)
print("\nTop 5 states with the most failed banks:")
print(top_5_states)

# Find the most common city in California for a bank to fail in
california_cities = banks[banks['ST'] == 'CA']['City']
most_common_city = california_cities.value_counts().idxmax()
print("\nMost common city in California for a bank to fail in:", most_common_city)

# Count the number of bank names that start with the letter 's'
num_banks_start_with_s = banks[banks['Bank Name'].str.startswith('S')]['Bank Name'].count()
print("\nNumber of bank names that start with the letter 's':", num_banks_start_with_s)

# Count the number of bank names that consist of just two words
num_banks_two_words = banks[banks['Bank Name'].str.count(' ') == 1]['Bank Name'].count()
print("\nNumber of bank names that consist of just two words:", num_banks_two_words)
