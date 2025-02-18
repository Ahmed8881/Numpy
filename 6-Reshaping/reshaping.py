#Reshaping arrrays
import numpy as np
#ravel fun converts higher dim array in one dim array
arr = np.array([[1, 2, 3], [4, 5, 6]])
print("Original array:\n", arr)
print("Flattened array:", arr.ravel())
#transpose fun converts rows into columns and columns into rows
print("Transposed array:\n", arr.transpose())
#hstack
arr1=np.arange(6).reshape(2,3)
arr2=np.arange(6,12).reshape(2,3)
print("Original arr1:\n", arr1)
print("Original arr2:\n", arr2)
print("Horizontal stacking:\n", np.hstack((arr1, arr2)))
#vstack
print("Vertical stacking:\n", np.vstack((arr1, arr2)))
#hsplit
arr3 = np.arange(24).reshape(4, 6)
print("Original array:\n", arr3)
print("Horizontal splitting:\n", np.hsplit(arr3, 2))