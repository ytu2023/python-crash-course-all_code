# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 14:47:51 2020

@author: barbora

Make two files, cats.txt and dogs.txt. Store at least three names of cats and 
three names of dogs in the files. Write a program that tries to read these
files and print the contents of the files to the screen. Wrap your code in a
try-except block to catch the FileNotFound error, and print a friendly message
if a file is missing. Make sure the code works properly.
"""

# Read cats and dogs files
filename_cats = 'c10_8_cats.txt'
# Available file
filename_dogs = 'c10_8_dogs.txt'
# File for testing failure
#filename_dogs = 'c10_8_dog.txt'

try:
    with open(filename_cats, 'r') as f:
        contents_cats = f.read()   
    with open(filename_dogs, 'r') as f:
        contents_dogs = f.read()
except FileNotFoundError:
    print("Please ensure that both files are available in the agreed folder")
else:
    print(f"\nCats: \n{contents_cats}")
    print(f"\nDogs: \n{contents_dogs}")
