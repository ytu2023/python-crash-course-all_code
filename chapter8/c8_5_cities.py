# -*- coding: utf-8 -*-
"""
Created on Thu May 21 21:39:51 2020

@author: barbora
"""

# Write a function called describe_city() that accepts the name of a city and
# its country. The function should print a simple sentence. Give the 
# parameter for the country a default value. Call your function for three
# different cities, at least one of which is not in the default country.

# Define function
def describe_city(name, country='united kingdom'):
    """Function to print a message stating which country a city lies in."""
    print(f"\n{name.title()} is in {country.title()}.")
    
# Call function
describe_city('london')
describe_city(name='manchester')
describe_city(country='slovakia', name='nitra')
