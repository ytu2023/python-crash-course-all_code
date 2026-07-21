# -*- coding: utf-8 -*-
"""
Created on Wed May 27 22:07:59 2020

@author: barbora

Make a class called Restaurant. The __init__() method should store two 
attributes: restaurant_name and cuisine_type. 
- Make a method called decribe_restaurant() that prints these two pieces of 
information.
- Make a method called open_restaurant() that prints a message indicating
that the restaurant is open.
- Make an instance called restaurant from your class. Print the two attributes
individually, then call both methods.

"""

# Create the Restaurant class
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
        
# Create an instance
restaurant = Restaurant('Don Giovanni', 'Italian')

# Print attributes individually and call both methods
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
