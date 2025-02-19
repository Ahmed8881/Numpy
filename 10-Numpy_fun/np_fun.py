import numpy as np
print(np.random.randint(1,12))  # Generate an array of 10 random integers between 1 and 100
np.random.seed(100)  # Set the seed for reproducibility
print(np.random.random())
print(np.random.random(1))  # Generate an array of 5 random floats between 0 and 1
print(np.random.uniform(1, 12, 5))  # Generate an array of 5 random numbers between 1 and 12
print(np.random.randint(1, 12, 5))  # Generate an array of 5 random integers between 1 and 12

arr1=np.random.randint(1, 12, 5)
print(arr1)
print(arr1.max())  # Find the maximum value in the array
print(arr1.min())  # Find the minimum value in the array
print(arr1.argmax())  # Find the index of the maximum value
print(np.argmax(arr1))  # Find the index of the maximum value
print(arr1.argmin())  # Find the index of the minimum value
print(arr1[arr1.argmax()])
arr1=np.array([1, 2, 3, 4, 5])
arr1[arr1 % 2 == 0] = -1
print(arr1)
arr1=np.array([1, 2, 3, 6, 7])
print(np.where(arr1%2!=0, -1, arr1))
out=np.where(arr1%2!=0, -1, arr1)
print(out)
arr1=np.random.randint(64, 100, 5)
arr=np.sort(arr1)
print(arr)
print(np.percentile(arr, 25))  # Find the 25th percentile of the array