# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 23:34:25 2021

@author: barbora

Apply a colormap to the cubes plot.
"""

import matplotlib.pyplot as plt

# Generate x and y values
x_vals = range(1, 50001)
y_vals = [x**3 for x in x_vals]

# Create the plot
plt.style.use('bmh')
fig, ax = plt.subplots()

# Include colormap here
# Further options can be seen here: 
# https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html 
ax.scatter(x_vals, y_vals, c=y_vals, cmap=plt.cm.cool, s=15)
ax.set_title("First 5000 cubes")
ax.set_xlabel("Values")
ax.set_ylabel("Values cubed")
ax.tick_params(axis='both', which='major', labelsize=10)
ax.axis([0, 50000, 0, 50000**3])

# Show plot
plt.show()
