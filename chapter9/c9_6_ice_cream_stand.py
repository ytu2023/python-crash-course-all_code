# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 21:38:52 2020

@author: barbora

An ice cream stand is a specific kind of restaurant. Write a class called
IceCreamStand that inherits from the Restaurant class in 9_4.
- Add an attribute called flavours that stores a list of ice cream flavours.
- Write a method that displays these flavours.
- Create an instance of IceCreamStand and call this method.

"""

# Starting with Restaurant class from 9_4
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
        
# Creating IceCreamStand child class
class IceCreamStand(Restaurant):
    """Child class based on Restaurant class to model an ice cream stand."""
    
    def __init__(self, restaurant_name, cuisine_type, *flavours):
        """Initialise attributes from parent class and others."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = flavours
    
    # Alternatively    
#    def __init__(self, restaurant_name, cuisine_type='ice cream'):
#        """Initialise attributes from parent class and others."""
#        super().__init__(restaurant_name, cuisine_type)
#        self.flavours = []
        
    def display_flavours(self):
        """Display ice cream flavours."""
        print(f"We have the following flavours:")
        for flavour in self.flavours:
            print(f"- {flavour}")
        
# Create instance and call display_flavours() method
my_stand = IceCreamStand('ice cream #1', 'ice cream', 'vanilla',
                         'strawberry', 'chocolate', 
                         'rhubarb', 'blueberry')
my_stand.describe_restaurant()
my_stand.display_flavours()
