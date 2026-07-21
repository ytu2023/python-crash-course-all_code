# -*- coding: utf-8 -*-
"""
Created on Tue May  5 09:36:02 2020

@author: barbora
"""

# Make a list of the first 10 cubes using list comprehension, and use a for 
# loop to print each value.

# Using list comprehension
print(f"Using list comprehension:")
cubes2 = [value**3 for value in range(1,11)]
for cube in cubes2:
    print(cube)