# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 23:17:09 2021

@author: barbora

A number raised to the third power is a cube. Plot the first five cubic
numbers, and then plot the first 5000 cubic numbers.
"""

import matplotlib.pyplot as plt

# Starting with 5 cubes
# Generate x and y values
x_vals = range(1, 6)
y_vals = [x**3 for x in x_vals]

# Create the plot
plt.style.use('dark_background')
fig, ax = plt.subplots()
ax.scatter(x_vals, y_vals, s=50)
ax.set_title("First five cubes")
ax.set_xlabel("Values")
ax.set_ylabel("Values cubed")
ax.tick_params(axis='both', which='major', labelsize=10)

# Show plot
plt.show()


# Starting with 5000 cubes
# Generate x and y values
x_vals = range(1, 5001)
y_vals = [x**3 for x in x_vals]

# Create the plot
plt.style.use('bmh')
fig, ax = plt.subplots()
ax.scatter(x_vals, y_vals, s=15)
ax.set_title("First 5000 cubes")
ax.set_xlabel("Values")
ax.set_ylabel("Values cubed")
ax.tick_params(axis='both', which='major', labelsize=10)
ax.axis([0, 5000, 0, 5000**3])

# Show plot
plt.show()
