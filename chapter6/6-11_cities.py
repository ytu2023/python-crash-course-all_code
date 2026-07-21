# -*- coding: utf-8 -*-
"""
Created on Sun May 17 00:27:53 2020

@author: barbora
"""

# Make a dictionary called cities. Use the names of three cities as keys in 
# your dictionary. Create a dictionary of information about each city and 
# include the country that the city is in, its approximate population, and one
# fact about the city. Print all info.

# Create cities dictionary
cities = {
    'london': {
        'country': 'united kingdom',
        'population': 9000000,
        'fact': 'Big Ben is not actually called Big Ben, it is called The '
        'Clock Tower',
        },
    'bojnice': {
        'country': 'slovakia',
        'population': 5000,
        'fact': 'The castle was originally made out of wood',
        },
    'asuncion': {
        'country': 'paraguay',
        'population': 530000,
        'fact': 'Known as the “Mother of Cities,” is one of the oldest '
        'cities in South America',
        },
    }

# Print info
for city, city_info in cities.items():
    print(f"\nThis is what we know about {city.title()}:")
    for key, value in city_info.items():
        if (key == 'country'):
            print(f"\t{key.title()}: {value.title()}")
        else:
            print(f"\t{key.title()}: {value}")