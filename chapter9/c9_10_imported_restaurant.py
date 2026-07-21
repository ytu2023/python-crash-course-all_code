# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 19:03:59 2020

@author: barbora

Using 9_6, store it in a module. Make a separate file that imports Restaurant.
Make a Restaurant instance, and call one of Restaurant's methods to show that
the import statement is working properly.

"""

# Import Restaurant class
from c9_10_imported_restaurant_module import Restaurant as R

# Create an instance and call a method
my_restaurant = R('quattro', 'italian')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
