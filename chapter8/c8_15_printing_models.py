# -*- coding: utf-8 -*-
"""
Created on Mon May 25 12:38:26 2020

@author: barbora
"""

# Separate printing_models.py from the book into printing_functions.py and
# printing_models.py. Write an import statement and modify the file as 
# necessary.

# Import statements
import c8_15_printing_functions as pfs

# Define input variables        
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Call functions
pfs.print_models(unprinted_designs, completed_models)
pfs.show_completed_models(completed_models)
