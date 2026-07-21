# -*- coding: utf-8 -*-
"""
Created on Mon May 25 12:54:53 2020

@author: barbora
"""

# Functions for c8_16_imports

# Function from c8_14_cars
def make_car(manufacturer, model_name, **kwargs):
    """Function to store information about a car."""
    kwargs['manufacturer'] = manufacturer
    kwargs['model_name'] = model_name
    return kwargs
