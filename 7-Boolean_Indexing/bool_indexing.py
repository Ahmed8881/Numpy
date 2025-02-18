import numpy as np
arr=np.random.randint(1, 100, 20).reshape(4, 5)
print("Original array:\n", arr)
print("Boolean mask where elements > 50:\n", arr > 50)
print("Elements greater than 50:", arr[arr > 50])
print(arr[arr > 50 & (arr%2==0)])