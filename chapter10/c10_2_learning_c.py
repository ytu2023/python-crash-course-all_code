# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 22:04:03 2020

@author: barbora

You can use the replace() method to replace any word in a string with a 
different word. Read in each line from learning_python.txt and replace
the word python with the name of another language, such as C. Print each
modified line to the screen.
"""

# Read in the lines in the file
file_name = 'c10_1_learning_python.txt'
with open(file_name) as f:
    lines = f.readlines()
    
# Replace python with C and print
for line in lines:
    print(line.replace('python', 'C').strip())
