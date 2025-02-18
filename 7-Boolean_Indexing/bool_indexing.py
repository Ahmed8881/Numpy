import numpy as np  # Importing the numpy library for numerical operations

# Creating a 2D numpy array with random integers between 1 and 99, reshaped into a 4x5 matrix
arr = np.random.randint(1, 100, 20).reshape(4, 5)
print("Original array:\n", arr)

# Creating a boolean mask where elements are greater than 50
print("Boolean mask where elements > 50:\n", arr > 50)

# Using the boolean mask to filter elements greater than 50
print("Elements greater than 50:", arr[arr > 50])

# Using a combined boolean mask to filter elements greater than 50 and even
print(arr[(arr > 50) & (arr % 2 == 0)])