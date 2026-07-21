# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 21:29:14 2020

@author: barbora

Store functions for 11-1.
"""

def return_formatted_city_country(city, country, population=''):
    """Return a string formatted as City, Country - population xxx
    when population data available. Otherwise return as City, Country.
    """
    if population:
        formatted = f"{city.title()}, {country.title()}"
        formatted += f" - population {population}"
    else:
        formatted = f"{city.title()}, {country.title()}"
    return formatted
