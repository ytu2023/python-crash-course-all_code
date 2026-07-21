# -*- coding: utf-8 -*-
"""
Created on Tue May  5 09:32:18 2020

@author: barbora
"""

# Make a list of the first 10 cubes, and use a for loop to print each value.

# Using a for loop
print("Using a for loop:")
cubes = []
for value in range(1,11):
    cube = value**3
    cubes.append(cube)
    print(cube)
    