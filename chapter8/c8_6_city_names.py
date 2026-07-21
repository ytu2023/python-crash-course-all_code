# -*- coding: utf-8 -*-
"""
Created on Fri May 22 13:18:35 2020

@author: barbora
"""

# Write a function called city_country() that takes in the name of a city and
# its country. The function should return a formatted string.
# Call your function with at least three city-country pairs, and print the 
# values that are returned.

# Function definition
def city_country(city, country):
    """Display city and country in a formatted style."""
    message = f"------------------------------------------------------------"
    message += f"\n{city.title()}, {country.title()}\n"
    message += f"------------------------------------------------------------"
    return message

# Call function
pair = city_country('nitra', 'slovakia')
print(pair)
pair = city_country('manchester', 'united kingdom')
print(pair)
pair = city_country('hamburg', 'germany')
print(pair)
