import numpy as np

# Create a 3x3 array of random integers between 1 and 10
random_matrix = np.random.randint(1, 11, size=(3, 3))
print("Random 3x3 Matrix:\n", random_matrix)

# Find the sum of all elements in the matrix
matrix_sum = np.sum(random_matrix)
print(f"\nSum of all elements: {matrix_sum}")

# Find the mean of the matrix
matrix_mean = np.mean(random_matrix)
print(f"\nMean of the matrix: {matrix_mean:2.2f}")

# Transpose the matrix
transposed_matrix = np.transpose(random_matrix)
print("\nTransposed Matrix:\n", transposed_matrix)