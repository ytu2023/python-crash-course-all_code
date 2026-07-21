# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 11:07:00 2020

@author: barbora
"""

# Use a variable to represent a person's name, and include some whitespace 
# characters at the beginning and end of the name. Make sure you use each
# character combination. Print the name using the stripping functions.

name = "\tada \tlovelace \n\t\t\tmathematician and computer scientist    "
print("No change: " + '\n' + name)
print("lstrip(): \n" + name.lstrip())
print("rstrip(): \n" + name.rstrip())
print("strip: \n" + name.strip())
