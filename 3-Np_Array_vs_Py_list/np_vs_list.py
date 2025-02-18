import sys  # Importing the sys library for system-specific parameters and functions
import numpy as np  # Importing the numpy library for numerical operations
import time  # Importing the time library to measure execution time

# Creating a range object with 100 elements
list1 = range(100)

# Creating a numpy array with a single element 100 (this seems to be an error, should be np.arange(100))
arr1 = np.array(100)

# Calculating and printing the memory size of the list
# sys.getsizeof(1) gives the size of an integer in bytes, multiplied by the length of the list
print(sys.getsizeof(1) * len(list1))

# Calculating and printing the memory size of the numpy array
# arr1.itemsize gives the size of one element in the array, multiplied by the number of elements in the array
print(arr1.itemsize * arr1.size)

# Creating two range objects with 1,000,000 elements each
x = range(1000000)
y = range(2000000, 3000000)

# Measuring the time taken to perform a list operation
start_time = time.time()
c = [(x, y) for x, y in zip(x, y)]  # Creating a list of tuples by zipping x and y
print("Time taken by list operation:", (time.time() - start_time) * 1000)  # Printing the time taken in milliseconds

# Creating two numpy arrays with 1,000,000 elements each
np1 = np.arange(1000000)
np2 = np.arange(2000000, 3000000)

# Measuring the time taken to perform a numpy operation
start_time = time.time()
np3 = np1 + np2  # Adding the two numpy arrays element-wise
print("Time taken by numpy operation:", (time.time() - start_time) * 1000)  # Printing the time taken in milliseconds