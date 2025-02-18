import numpy as np  # Importing the numpy library for numerical operations
import matplotlib.pyplot as plt  # Importing the matplotlib library for plotting graphs


# Creating an array of 100 linearly spaced values between -40 and 40
x = np.linspace(-40, 40, 100)

# Calculating the sine of each value in the array x
y = np.sin(x)

# Plotting the values of x and y
plt.plot(x, y)

# Displaying the plot
plt.show()

