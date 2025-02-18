# Importing the NumPy library for numerical operations
import numpy as np

# Creating a 2D NumPy array (Matrix) with shape (2, 3)
arr1 = np.array([[1, 2, 3], [4, 5, 6]])

# Creating a 3D NumPy array with shape (2, 2, 2)
# This represents a 2-layer structure, each containing a 2x2 matrix
arr2 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# Printing the shape of the arrays
# Shape represents the dimensions of the array (rows, columns)
print('Shape of arr1:', arr1.shape)  # Output: (2, 3) -> 2 rows, 3 columns
print('Shape of arr2:', arr2.shape)  # Output: (2, 2, 2) -> 2 blocks of 2x2 matrices

# Printing the number of dimensions (ndim)
# ndim tells us how many axes (dimensions) an array has
print('Dimensions of arr1:', arr1.ndim)  # Output: 2D (2-dimensional array)
print('Dimensions of arr2:', arr2.ndim)  # Output: 3D (3-dimensional array)

# Printing the total number of elements in each array
# size gives the total count of elements in the array
print('Total elements in arr1:', arr1.size)  # Output: 6 (2x3 = 6)
print('Total elements in arr2:', arr2.size)  # Output: 8 (2x2x2 = 8)

# Printing the size of each element in bytes
# itemsize returns the size of one array element in bytes
print('Size of each element in arr1 (bytes):', arr1.itemsize)  # Typically 4 or 8 bytes depending on dtype
print('Size of each element in arr2 (bytes):', arr2.itemsize)  # Same as above

# Printing the data type of elements in the arrays
# dtype shows the type of elements stored in the array (int32, int64, float, etc.)
print('Data type of arr1 elements:', arr1.dtype)  # Output: int32 or int64 depending on the system
print('Data type of arr2 elements:', arr2.dtype)  # Output: int32 or int64

# Converting arr2 to float type (astype creates a new array with a different data type)
arr2_float = arr2.astype('float')

# Printing arr2 after conversion (original arr2 is unchanged because astype returns a new array)
print('arr2 after converting to float:\n', arr2_float)
#Key Differences with Similar Constructs:
#np.array([...]) vs. np.zeros(shape) or np.ones(shape)

#np.array([...]) manually defines array values.
#np.zeros((2,3)) creates a 2x3 array filled with zeros.
#np.ones((2,3)) creates a 2x3 array filled with ones.
#.astype(dtype) vs. arr.dtype
#
#.astype(dtype) converts an array into a new data type without modifying the original array.
#arr.dtype just tells the current data type without changing anything.
#.shape vs. .size
#
#.shape tells the dimensions of the array.
#.size tells the total number of elements in the array.
#2D (ndim = 2) vs. 3D (ndim = 3)
#
#arr1 is a matrix (2D).
#arr2 is a 3D array, which is like a collection of multiple 2D matrices.