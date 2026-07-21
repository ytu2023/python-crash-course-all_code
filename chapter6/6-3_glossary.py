# -*- coding: utf-8 -*-
"""
Created on Mon May 11 12:01:01 2020

@author: barbora
"""

# A python dictionary can be used to model an actual dictionary. Let's cal it
# glossary.
# - Think of five programming words you've learned. Store them as keys and 
# their meanings as values.
# - Print each word and its meaning as neatly formatted output.

# Create glossary
glossary = {
    'dictionary': 'Collection of key-value pairs',
    'list': 'Collection of items in a particular order',
    'tuple': 'Immutable list',
    'f-string': 'Method of neatly formatting strings',
    'conditional test': 'Code that produces True or False answer',
    }

# Print info
meaning = glossary['dictionary']
print(f"\nDictionary:\n\t{meaning}.")
meaning = glossary['list']
print(f"\nList:\n\t{meaning}.")
meaning = glossary['tuple']
print(f"\nTuple:\n\t{meaning}.")
meaning = glossary['f-string']
print(f"\nf-string:\n\t{meaning}.")
meaning = glossary['conditional test']
print(f"\nConditional test:\n\t{meaning}.")