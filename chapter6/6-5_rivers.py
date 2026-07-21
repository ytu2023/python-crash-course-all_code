# -*- coding: utf-8 -*-
"""
Created on Wed May 13 20:48:21 2020

@author: barbora
"""

# Make a dictionary containing three major rivers and the country each river
# runs through, e.g. 'nile': 'egypt'.
# - Use a loop to print a sentence about each river, e.g. Nile runs through 
# Egypt.
# - Use a loop to print the name of each river included in the dictionary.
# - Use a loop to print the name of each country included in the dictionary.

# Create dictionary
rivers = {
    'nile': 'egypt',
    'vah': 'slovakia',
    'yellow river': 'china',
    'mississippi': 'usa',
    'thames': 'uk'
    }

# Print a sentence about each river
for river, country in rivers.items():
    f_river = river.title()
    if ((country == 'uk') or (country == 'usa')):
        f_country = country.upper()
    else:
        f_country = country.title()
    print(f"The {f_river} runs through {f_country}.")
    
# Print the name of each river
print("\nThe following rivers are included in the dictionary:")
for river in rivers.keys():
    print(f"- {river.title()}")
    
# Print the name of each country
print("\nIn alphabetical order, the following countries are included in the "
      "dictionary:")
for country in sorted(rivers.values()):
    if ((country == 'uk') or (country == 'usa')):
        print(country.upper())
    else:
        print(country.title())
        