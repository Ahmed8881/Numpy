import numpy as np  # Importing the numpy library

# Creating a 1D array with elements 1, 2, 3, 4, 5
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)  # Printing the 1D array

# Getting the type of the array
new = type(arr1)
print(new)  # Printing the type of the array, which should be <class 'numpy.ndarray'>

# Creating a 2D array with elements [[1, 2, 3], [4, 5, 6]]
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2)  # Printing the 2D array

# Creating a 1D array of zeros with 5 elements
ar3 = np.zeros(5)
print(ar3)  # Printing the array of zeros

# Creating a 2D array of zeros with shape (2, 3)
ar4 = np.zeros((2, 3))
print(ar4)  # Printing the 2D array of zeros

# Creating a 1D array of ones with 5 elements
ar5 = np.ones(5)
print(ar5)  # Printing the array of ones

# Creating a 2D array of ones with shape (2, 3)
ar6 = np.ones((2, 3))
print(ar6)  # Printing the 2D array of ones

# Creating a 3x3 identity matrix
arr6 = np.identity(3)
print(arr6)  # Printing the identity matrix

# Creating a 1D array with elements from 1 to 9 with a step of 2
arr7 = np.arange(1, 10, 2)
print(arr7)  # Printing the array

# Creating a 1D array with elements from 0 to 9
arr8 = np.arange(10)
print(arr8)  # Printing the array

# Creating a 1D array with 5 elements evenly spaced between 1 and 10
arr9 = np.linspace(1, 10, 5)
print(arr9)  # Printing the array

# Creating a 1D array with 5 elements evenly spaced between 1 and 10, excluding the endpoint
arr10 = np.linspace(1, 10, 5, endpoint=False)
print(arr10)  # Printing the array

# Creating a 1D array with 5 elements evenly spaced between 1 and 10, and returning the step size
arr11 = np.linspace(1, 10, 5, retstep=True)
print(arr11)  # Printing the array and the step size

# Creating a 1D array with 5 elements evenly spaced between 1 and 10, returning the step size, and specifying the data type as int
arr12 = np.linspace(1, 10, 5, retstep=True, dtype=int)
print(arr12)  # Printing the array and the step size

# Creating a copy of arr1
arr13 = arr1.copy()
print(arr13)  # Printing the copied array