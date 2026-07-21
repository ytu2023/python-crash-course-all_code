# -*- coding: utf-8 -*-
"""
Created on Wed May 27 22:18:12 2020

@author: barbora

Start with 9_1. Create three different instances from the class.
Call describe_restaurant() for each instance.

"""

# Restaurant class from 9_1
class Restaurant:
    """A class to describe a restaurant."""
    
    def __init__(self, restaurant_name, cuisine_type):
        """Initialise name and cuisine type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        """Print a statement to describe the restaurant."""
        print(f"The restaurant's name is {self.restaurant_name} and it "
              f"serves {self.cuisine_type} cuisine.")
        
    def open_restaurant(self):
        """Print a statement to indicate that the restaurant is open."""
        print("Welcome, we are open!")
        
# Create three instances
italian = Restaurant('Don Giovanni', 'Italian')
fishchips = Restaurant('Wings', 'British')
indian = Restaurant('Caversham Tandoori', 'Indian')
        
# Call describe_restaurant()
italian.describe_restaurant()
fishchips.describe_restaurant()
indian.describe_restaurant()
