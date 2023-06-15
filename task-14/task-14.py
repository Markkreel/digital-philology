import numpy as np

# Create a null vector of size 10
null_vector = np.zeros(10)
print("Null vector of size 10:", null_vector)

# Create a null vector of size 10 with the fifth value as 1
null_vector_fifth_one = np.zeros(10)
null_vector_fifth_one[4] = 1
print("Null vector of size 10 with fifth value as 1:", null_vector_fifth_one)

# Create a vector with values ranging from 10 to 49
vector_range = np.arange(10, 50)
print("Vector with values ranging from 10 to 49:", vector_range)

# Reverse a vector
reversed_vector = vector_range[::-1]
print("Reversed vector:", reversed_vector)

# Create a 3x3 matrix with values ranging from 0 to 8
matrix_3x3 = np.arange(9).reshape((3, 3))
print("3x3 matrix with values ranging from 0 to 8:")
print(matrix_3x3)

# Find indices of non-zero elements from [1, 2, 0, 0, 4, 0]
nonzero_indices = np.nonzero([1, 2, 0, 0, 4, 0])
print("Indices of non-zero elements:", nonzero_indices)

# Create a 3x3 identity matrix
identity_matrix = np.eye(3)
print("3x3 identity matrix:")
print(identity_matrix)

# Create a 3x3x3 array with random values
random_array = np.random.random((3, 3, 3))
print("3x3x3 array with random values:")
print(random_array)

# Create a 10x10 array with random values and find the minimum and maximum values
random_10x10_array = np.random.random((10, 10))
min_value = np.min(random_10x10_array)
max_value = np.max(random_10x10_array)
print("10x10 array with random values:")
print(random_10x10_array)
print("Minimum value:", min_value)
print("Maximum value:", max_value)

# Create a random vector of size 30 and find the mean value
random_vector = np.random.random(30)
mean_value = np.mean(random_vector)
print("Random vector of size 30:")
print(random_vector)
print("Mean value:", mean_value)

# Create a 2D array with 1 on the border and 0 inside
border_array = np.ones((5, 5))
border_array[1:-1, 1:-1] = 0
print("2D array with 1 on the border and 0 inside:")
print(border_array)

# Add a border (filled with 0's) around an existing array
existing_array = np.ones((3, 3))
array_with_border = np.pad(existing_array, pad_width=1, mode='constant', constant_values=0)
print("Existing array with added border:")
print(array_with_border)
