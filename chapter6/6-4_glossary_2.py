# -*- coding: utf-8 -*-
"""
Created on Wed May 13 20:39:56 2020

@author: barbora
"""

# Clean up the code from 6-3 using loops. When the code works, add five more
# terms to the glossary. Run the code again.

# Create glossary
glossary = {
    'dictionary': 'Collection of key-value pairs',
    'list': 'Collection of items in a particular order',
    'tuple': 'Immutable list',
    'f-string': 'Method of neatly formatting strings',
    'conditional test': 'Code that produces True or False answer',
    'set': 'Collection of items in which each item is unique',
    'string': 'Series of characters in quotation marks',
    'integer': 'Whole number without a decimal point',
    'float': 'Any non-integer number',
    'list comprehension': 'Method for creating lists in one line',
    }

# Print info using a for loop
for word, meaning in glossary.items():
    word = word.title()
    print(f"\n{word}:\n\t{meaning}.")
