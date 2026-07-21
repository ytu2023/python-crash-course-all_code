# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 23:00:09 2020

@author: barbora
"""

# Create an example function
# Version 1
# def get_formatted_name(first, last):
# Failing version 1
#def get_formatted_name(first, middle, last):
# Corrected version
def get_formatted_name(first, last, middle=''):
    """Generate a neatly formatted full name."""
    # Version 1
    # full_name = f"{first} {last}"
    # Failing version 1
    full_name = f"{first} {middle} {last}"
    # Corrected
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()
