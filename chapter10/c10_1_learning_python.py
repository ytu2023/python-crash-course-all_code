# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 21:47:48 2020

@author: barbora

Open a blank file and write a few lines summarising what you've learned about
python so far. Start each line with the phase In python you can... . Save the
file as learning_python.txt in the same directory as exercises for this
chapter. Write a program that reads the file and prints what you wrote three
times. 
- Print the contents once by reading in the entire file, 
- once by looping over the file object, 
- and once by storing the lines in a list and then working with them outside 
the with block.
"""

# Create file_name variable
file_name = 'c10_1_learning_python.txt'

# Read the entire file
with open(file_name) as file_object:
    contents = file_object.read()
    
print(contents)

# Loop over the file object
with open(file_name) as file_object:
    for line in file_object:
        print(line)

# Store lines in a list
with open(file_name) as file_object:
    lines = file_object.readlines()
    
for line in lines:
    print(line)
