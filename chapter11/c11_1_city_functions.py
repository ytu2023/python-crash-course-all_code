# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 21:29:14 2020

@author: barbora

Store functions for 11-1.
"""

def return_formatted_city_country(city, country):
    """Return a string formatted as City, Country"""
    formatted = f"{city.title()}, {country.title()}"
    return formatted
