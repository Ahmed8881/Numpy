import numpy as np
print(np.random.randint(1,12))  # Generate an array of 10 random integers between 1 and 100
np.random.seed(100)  # Set the seed for reproducibility
print(np.random.random())
print(np.random.random(1))  # Generate an array of 5 random floats between 0 and 1
print(np.random.uniform(1, 12, 5))  # Generate an array of 5 random numbers between 1 and 12
print(np.random.randint(1, 12, 5))  # Generate an array of 5 random integers between 1 and 12