# -*- coding: utf-8 -*-
"""
Created on Mon May 25 12:52:52 2020

@author: barbora
"""

# Using a previously used function, store it in a module, and import the
# function using each import option.

# Using c8_14_cars

# Import full module
import c8_16_imports_functions
this_car = c8_16_imports_functions.make_car('renault',
                                            'clio', year=2005, colour='silver')
print("\nFull module")
print(this_car)

# Import specific function
from c8_16_imports_functions import make_car
this_car = make_car('renault', 'clio', year=2005, colour='silver')
print("\nSpecific function")
print(this_car)

# Import specific function with alias
from c8_16_imports_functions import make_car as mc
this_car = mc('renault', 'clio', year=2005, colour='silver')
print("\nSpecific function with alias")
print(this_car)

# Import full module with alias
import c8_16_imports_functions as ic
this_car = ic.make_car('renault', 'clio', year=2005, colour='silver')
print("\nFull module with alias")
print(this_car)

# Import all functions
from c8_16_imports_functions import *
this_car = make_car('renault', 'clio', year=2005, colour='silver')
print("\nAll functions")
print(this_car)
