# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 19:06:31 2020

@author: barbora

Module to store class which describes a restaurant, from 9_6.

"""

# Starting with Restaurant class from 9_6
class Restaurant:
    """A class to describe a restaurant."""
    
    def __init__(self, restaurant_name, cuisine_type):
        """Initialise name and cuisine type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        # Adding in a number_served attribute
        self.number_served = 0
        
    def describe_restaurant(self):
        """Print a statement to describe the restaurant."""
        print(f"The restaurant's name is {self.restaurant_name} and it "
              f"serves {self.cuisine_type} cuisine.")
        
    def open_restaurant(self):
        """Print a statement to indicate that the restaurant is open."""
        print("Welcome, we are open!")
        
    def set_number_served(self, customers):
        """Set number of customers served."""
        self.number_served = customers
        
    def increment_number_served(self, increment_customers):
        """Increment number of customers seved."""
        self.number_served += increment_customers
