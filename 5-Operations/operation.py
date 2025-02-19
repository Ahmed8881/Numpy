import numpy as np  # Importing the numpy library for numerical operations

# Creating a 1D numpy array with elements from 1 to 10
arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("Original arr1:", arr1)

# Creating another 1D numpy array with elements from 11 to 20
arr2 = np.array([11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
print("Original arr2:", arr2)

# Performing element-wise subtraction between arr2 and arr1
print("Element-wise Subtraction (arr2 - arr1):", arr2 - arr1)  # Expected output: [10 10 10 10 10 10 10 10 10 10]

# Multiplying each element in arr1 by 2
arr1 = arr1 * 2
print("arr1 after multiplying each element by 2:", arr1)  # Expected output: [ 2  4  6  8 10 12 14 16 18 20]

# Performing element-wise comparison to check which elements in arr1 are greater than 5
print("Boolean mask where arr1 elements > 5:", arr1 > 5)  # Expected output: [False False  True  True  True  True  True  True  True  True]

# Creating a 2D array of shape (2,3) with elements from 0 to 5
arr1 = np.arange(6).reshape(2, 3)
print("New arr1 (2x3 matrix):\n", arr1)

# Creating another 2D array of shape (2,3) with elements from 6 to 11
arr2 = np.arange(6, 12).reshape(2, 3)
print("New arr2 (2x3 matrix):\n", arr2)

# Performing matrix multiplication (dot product) between arr1 and arr2.T (Transpose of arr2)
print("Dot product of arr1 and arr2.T:\n", arr1.dot(arr2.T))  # Expected output: [[ 23  32],[ 86 122]]

# Reshaping arr2 into a (3,2) matrix to perform another dot product with arr1
arr2 = np.arange(6).reshape(3, 2)
print("New arr2 reshaped to (3x2):\n", arr2)

# Performing matrix multiplication between arr1 (2x3) and arr2 (3x2)
print("Dot product of arr1 and reshaped arr2:\n", arr1.dot(arr2))  # Expected output: [[10 13],[28 40]]
arr1=np.array([[0,1,2],[3,4,5]])
# Finding maximum values in arr1
print("Maximum value in arr1:", arr1.max())  # Expected output: 5
print("Maximum values along columns (axis=0):", arr1.max(axis=0))  # Expected output: [3 4 5]
print("Maximum values along rows (axis=1):", arr1.max(axis=1))  # Expected output: [2 5]

# Finding minimum values in arr1
print("Minimum value in arr1:", arr1.min())  # Expected output: 0
print("Minimum values along columns (axis=0):", arr1.min(axis=0))
print("Minimum values along rows (axis=1):", arr1.min(axis=1))

# Finding sum of all elements in arr1
print("Sum of all elements in arr1:", arr1.sum())  # Expected output: 15
print("Sum along columns (axis=0):", arr1.sum(axis=0))  # Expected output: [3 5 7]
print("Sum along rows (axis=1):", arr1.sum(axis=1))  # Expected output: [ 3 12]

# Finding mean (average) values in arr1
print("Mean of all elements in arr1:", arr1.mean())  # Expected output: 2.5
print("Mean along columns (axis=0):", arr1.mean(axis=0))  # Expected output: [1.5 2.5 3.5]
print("Mean along rows (axis=1):", arr1.mean(axis=1))  # Expected output: [1. 4.]

# Finding standard deviation (measure of dispersion) in arr1
print("Standard deviation of all elements in arr1:", arr1.std())  # Expected output: 1.707825127659933
print("Standard deviation along columns (axis=0):", arr1.std(axis=0))  # Expected output: [1.5 1.5 1.5]
print("Standard deviation along rows (axis=1):", arr1.std(axis=1))  # Expected output: [0.81649658 0.81649658]

# Applying trigonometric function (sin) on arr1
print("Sine values of arr1:\n", np.sin(arr1))

# Finding the median value of arr1
print("Median of arr1:", np.median(arr1))

# Applying exponential function (e^x) on arr1
print("Exponential values of arr1:\n", np.exp(arr1))

# Applying natural logarithm (ln) on arr1
print("Natural Log (ln) values of arr1:\n", np.log(arr1))

# Applying base-10 logarithm (log10) on arr1
print("Base-10 Log values of arr1:\n", np.log10(arr1))

# Applying base-2 logarithm (log2) on arr1
print("Base-2 Log values of arr1:\n", np.log2(arr1))

# Finding square root of each element in arr1
print("Square root of arr1:\n", np.sqrt(arr1))

# Raising each element in arr1 to the power of 2
print("arr1 squared:\n", np.power(arr1, 2))

# Raising each element in arr1 to the power of 3
print("arr1 cubed:\n", np.power(arr1, 3))
