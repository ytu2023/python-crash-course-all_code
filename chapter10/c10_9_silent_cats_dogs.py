# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 15:07:52 2020

@author: barbora

Modify except block from 10_8 to fail silently if either file is missing.
"""

# Read cats and dogs files
#filenames = ['c10_8_cats.txt', 'c10_8_dogs.txt']
# Test failure
filenames = ['c10_8_cats.txt', 'c10_8_dog.txt']

for file in filenames:
    try:
        print(f"\nReading file {file}:")
        with open(file, 'r') as f:
            contents = f.read()   
    except FileNotFoundError:
        pass
    else:
        print(contents)
