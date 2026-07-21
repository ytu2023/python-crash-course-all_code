# -*- coding: utf-8 -*-
"""
Created on Wed May  6 08:59:11 2020

@author: barbora
"""

# Using one of the programs you wrote in this chapter, add several lines
# to the end of the program that do the following:
# - Print the message "The first three items in the list are:"
# - Print the message "Three items from the middle of the list are:"
# - Print the message "The last three items in the list are:"

# Using 4-9 creating the first 10 cubes using list comprehension example
print(f"Using list comprehension:")
cubes2 = [value**3 for value in range(1,11)]
print("The full list of the first 10 cubes:")
print(cubes2)

# First three items
print("The first three items in the list are:")
print(cubes2[0:2])

# Middle three items
print("Three items from the middle of the list are:")
print(cubes2[3:6])

# Last three items
print("The last three items in the list are:")
print(cubes2[-3:])
