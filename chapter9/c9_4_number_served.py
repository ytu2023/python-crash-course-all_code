# -*- coding: utf-8 -*-
"""
Created on Sun May 31 22:40:21 2020

@author: barbora

Start with 9_1. 
- Add an attribute called number_served with a default value of
0. Create an instance called restaurant from this class. Print the number of
customers the restaurant has served, and then change this value and print it
again.
- Add a method called set_number_served() that lets you set the number of 
customers that have been served. Call this method with a new number and print
the value again.
- Add a method called increment_number_served() that lets you increment the
number of customers who've been served. Call this method with any number
you like that could represent how many customers were in, say, a day of
business.

"""

# Start with 9_1
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

# Create an instance
restaurant = Restaurant('don giovanni', 'italian')

# Print number of customers served, then change and print again
print(restaurant.number_served)
restaurant.number_served = 2
print(restaurant.number_served)

# Set number of customers by calling set_number_served()
restaurant.set_number_served(5)
print(restaurant.number_served)

# Increment number of customers by calling increment_number_served()
restaurant.increment_number_served(10)
print(restaurant.number_served)
