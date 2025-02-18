import numpy as np  # Importing the numpy library for numerical operations

# Creating a 2D numpy array with elements from 0 to 23, reshaped into a 6x4 matrix
arr12 = np.arange(24).reshape(6, 4)

# Iterating over each row in the 2D array
for i in arr12:
    print(i)  # Printing the entire row

    # Printing the row again (this seems redundant, but it prints the row again)
    print(i)