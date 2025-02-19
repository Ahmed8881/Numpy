import numpy as np  # Importing the numpy library for numerical operations

# Generate a single random integer between 1 and 11 (inclusive)
print(np.random.randint(1, 12))  # Output: A single random integer between 1 and 11

# Set the seed for reproducibility
np.random.seed(100)

# Generate a single random float between 0 and 1
print(np.random.random())  # Output: A single random float between 0 and 1

# Generate an array of 1 random float between 0 and 1
print(np.random.random(1))  # Output: An array with a single random float between 0 and 1

# Generate an array of 5 random floats between 1 and 12
print(np.random.uniform(1, 12, 5))  # Output: An array of 5 random floats between 1 and 12

# Generate an array of 5 random integers between 1 and 12
print(np.random.randint(1, 12, 5))  # Output: An array of 5 random integers between 1 and 12

# Create an array of 5 random integers between 1 and 12
arr1 = np.random.randint(1, 12, 5)
print(arr1)  # Output: The generated array

# Find the maximum value in the array
print(arr1.max())  # Output: The maximum value in the array

# Find the minimum value in the array
print(arr1.min())  # Output: The minimum value in the array

# Find the index of the maximum value in the array
print(arr1.argmax())  # Output: The index of the maximum value in the array

# Find the index of the maximum value in the array using np.argmax
print(np.argmax(arr1))  # Output: The index of the maximum value in the array

# Find the index of the minimum value in the array
print(arr1.argmin())  # Output: The index of the minimum value in the array

# Access the maximum value in the array using its index
print(arr1[arr1.argmax()])  # Output: The maximum value in the array

# Create a new array with elements [1, 2, 3, 4, 5]
arr1 = np.array([1, 2, 3, 4, 5])

# Replace even elements in the array with -1
arr1[arr1 % 2 == 0] = -1
print(arr1)  # Output: [ 1 -1  3 -1  5]

# Create a new array with elements [1, 2, 3, 6, 7]
arr1 = np.array([1, 2, 3, 6, 7])

# Use np.where to replace odd elements with -1
print(np.where(arr1 % 2 != 0, -1, arr1))  # Output: [-1  2 -1  6 -1]

# Store the result of np.where in a variable
out = np.where(arr1 % 2 != 0, -1, arr1)
print(out)  # Output: [-1  2 -1  6 -1]

# Create an array of 5 random integers between 64 and 100
arr1 = np.random.randint(64, 100, 5)

# Sort the array
arr = np.sort(arr1)
print(arr)  # Output: The sorted array

# Find the 25th percentile of the array
print(np.percentile(arr, 25))  # Output: The 25th percentile of the array