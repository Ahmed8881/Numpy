import numpy as np
# Broadcasting allows numpy to perform element-wise operations on arrays of different shapes.
# For example, if you have an array of shape (3, 1) and another array of shape (1, 4),
# numpy will broadcast them to a common shape (3, 4) to perform element-wise operations.

# Example 1: Adding a scalar to an array
array = np.array([1, 2, 3])
scalar = 2
result = array + scalar
print("Adding scalar to array:", result)  # Output: [3 4 5]

# Example 2: Adding two arrays of different shapes
array1 = np.array([[1], [2], [3]])
array2 = np.array([4, 5, 6])
result = array1 + array2
print("Adding arrays of different shapes:\n", result)
# Output:
# [[5 6 7]
#  [6 7 8]
#  [7 8 9]]

# Example 3: Multiplying arrays of different shapes
array3 = np.array([[1, 2, 3], [4, 5, 6]])
array4 = np.array([1, 2, 3])
result = array3 * array4
print("Multiplying arrays of different shapes:\n", result)
# Output:
# [[ 1  4  9]
#  [ 4 10 18]]