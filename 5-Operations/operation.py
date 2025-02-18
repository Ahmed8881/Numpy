import numpy as np  # Importing the numpy library for numerical operations

# Creating a 1D numpy array with elements from 1 to 10
arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Creating another 1D numpy array with elements from 11 to 20
arr2 = np.array([11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

# Performing element-wise subtraction between arr2 and arr1
print(arr2 - arr1)  # Output: [10 10 10 10 10 10 10 10 10 10]

# Multiplying each element in arr1 by 2
arr1 = arr1 * 2
print(arr1)  # Output: [ 2  4  6  8 10 12 14 16 18 20]

# Performing element-wise comparison to check which elements in arr1 are greater than 5
print(arr1 > 5)  # Output: [False False  True  True  True  True  True  True  True  True]

arr1=np.arange(6).reshape(2,3)
arr2=np.arange(6,12).reshape(2,3)
print(arr1.dot(arr2.T))  # Output: [[ 23  32],[ 86 122]]
arr2=np.arange(6).reshape(3,2)
print(arr1.dot(arr2))  # Output: [[10 13],[28 40]]
print(arr1)
print(arr1.max())  # Output: 5
print(arr1.max(axis=0))  # Output: [3 4 5]
print(arr1.max(axis=1))  # Output: [2 5]
print(arr1.min())  # Output: 0
print(arr1.min(axis=1))
print(arr1.min(axis=0))
print(arr1.sum())  # Output: 15
print(arr1.sum(axis=0))  # Output: [3 5 7]
print(arr1.sum(axis=1))  # Output: [ 3 12]
print(arr1.mean())  # Output: 2.5
print(arr1.mean(axis=0))  # Output: [1.5 2.5 3.5]
print(arr1.mean(axis=1))  # Output: [1. 4.]
print(arr1.std())  # Output: 1.707825127659933
print(arr1.std(axis=0))  # Output: [1.5 1.5 1.5]
print(arr1.std(axis=1))  # Output: [0.81649658 0.81649658]
print(np.sin(arr1))
np.median(arr1)
print(np.exp(arr1))
print(np.log(arr1))
print(np.log10(arr1))
print(np.log2(arr1))
print(np.sqrt(arr1))
print(np.power(arr1,2))
print(np.power(arr1,3))