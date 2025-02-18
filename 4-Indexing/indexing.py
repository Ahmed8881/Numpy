import numpy as np  # Importing the numpy library for numerical operations

# Creating a 1D numpy array with elements from 1 to 10
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Creating a 2D numpy array with elements from 0 to 23, reshaped into a 6x4 matrix
arr1 = np.arange(24).reshape(6, 4)
print(arr1)  # Printing the 2D array

# Accessing the 4th element (index 3) of the 1D array
print(arr[3])  # Output: 4

# Slicing the 1D array to get elements from index 2 to 2 (inclusive)
print(arr[2:3])  # Output: [3]

# Slicing the 2D array to get a subarray from rows 1 to 2 (inclusive) and columns 1 to 2 (inclusive)
print(arr1[1:3, 1:3])  # Output: [[5 6]
                       #          [9 10]]

# Accessing all rows and the 3rd column (index 2) of the 2D array
print(arr1[:, 2])  # Output: [2 6 10 14 18 22]