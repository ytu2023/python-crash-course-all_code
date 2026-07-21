# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 20:09:36 2021

@author: barbora
"""

import matplotlib.pyplot as plt

# First matplotlib plot
squares = [1, 4, 9, 16, 25]
fig, ax = plt.subplots()
ax.plot(squares)
plt.show()


# View available styles
#plt.style.available


# Plot improved, x values included
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

# Add in a style value
plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# Set chart title and label axes
ax.set_title("Square Numbers", fontsize=34)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels
ax.tick_params(axis='both', labelsize=14)

# Show plot
plt.show()


# Plotting a scatter graph
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(2, 4, s=200)

# Set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()


# Plotting a scatter graph with a series of points
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=100)

# Set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()


# Collecting data automatically and playing with colours
x_values = range(1, 1001)
y_values = [x**2 for x in x_values] # list comprehension
plt.style.use('seaborn')
fig, ax = plt.subplots()
#ax.scatter(x_values, y_values, s=10)
#ax.scatter(x_values, y_values, c='red', s=10)
ax.scatter(x_values, y_values, c=(0, 0.8, 0), s=10)

# Set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels
ax.tick_params(axis='both', which='major', labelsize=14)

# Set the range for each axis
ax.axis([0, 1100, 0, 1100000])

plt.show()


# Colormaps = series of colours in a gradient
x_values = range(1, 1001)
y_values = [x**2 for x in x_values] # list comprehension
plt.style.use('seaborn')
fig, ax = plt.subplots()

# Set colormap here
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# Set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels
ax.tick_params(axis='both', which='major', labelsize=14)

# Set the range for each axis
ax.axis([0, 1100, 0, 1100000])

plt.show()


# Saving plots
x_values = range(1, 1001)
y_values = [x**2 for x in x_values] # list comprehension
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# Set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels
ax.tick_params(axis='both', which='major', labelsize=14)

# Set the range for each axis
ax.axis([0, 1100, 0, 1100000])

# Save plot here
plt.savefig('squares_plot.png', bbox_inches='tight')


# Random walks
from random import choice

class RandomWalk:
    """A class to generate random walks."""
    
    def __init__(self, num_points=5000):
        """Initialise attributes of a walk."""
        self.num_points = num_points
        
        # All walks start at (0, 0)
        self.x_values = [0]
        self.y_values = [0]
        
    def fill_walk(self):
        """Calculate all the points in the walk."""        
        # Keep taking steps until the walk reaches the desired length
        while len(self.x_values) < self.num_points:
            # Decide which direction to go and how far to go
            x_dir = choice([1, -1])
            x_dist = choice([0, 1, 2, 3, 4])
            x_step = x_dir * x_dist
            y_dir = choice([1, -1])
            y_dist = choice([0, 1, 2, 3, 4])
            y_step = y_dir * y_dist
            # Reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue
            # Calculate the new position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            self.x_values.append(x)
            self.y_values.append(y)
            