# -*- coding: utf-8 -*-
"""
Created on Sun May 24 17:11:24 2020

@author: barbora
"""

# Write a function that stores information about your car in a dictionary.
# The function should always receive a manufacturer and a model name. It
# should then accept an arbitrary number of keyword arguments. Call the 
# function with the required information and two other name-value pairs, such
# as a colour or an optional feature.
# Print the dictionary that's returned to make sure all the information was
# stored correctly.

# Function definition
def make_car(manufacturer, model_name, **kwargs):
    """Function to store information about a car."""
    kwargs['manufacturer'] = manufacturer
    kwargs['model_name'] = model_name
    return kwargs

# Function calls
this_car = make_car('subaru', 'outback', colour='blue', tow_package=True)
print(this_car)

# Alternatively, function definition
def make_car(manufacturer, model_name, **kwargs):
    """Function to store information about a car."""
    car = {
        'manufacturer': manufacturer,
        'model_name': model_name,
        }
    for key, value in kwargs.items():
        car[key] = value
    return car
this_car = make_car('renault', 'clio', colour='silver', year=2003)
print(this_car)
