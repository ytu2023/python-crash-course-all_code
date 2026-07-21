# -*- coding: utf-8 -*-
"""
Created on Sat May 16 23:56:25 2020

@author: barbora
"""

# Start with 6-1. Make two new dictionaries representing different people, 
# and store all three dictionaries in a list called people. Loop through your 
# list of people. As you loop through the list, print everything you know
# about each person.

# Make an empty list
people = []

# From 6-1
josh_j = {
    'first_name': 'josh',
    'last_name': 'j',
    'age': 26,
    'city': 'reading',
    }

# Make two new dictionaries
becky_m = {
    'first_name': 'becky',
    'last_name': 'm',
    'age': 23,
    'city': 'stockholm',
    }

valentina_i = {
    'first_name': 'valentina',
    'last_name': 'i',
    'age': 33,
    'city': 'london',
    }

# Combine into a list
people = [josh_j, becky_m, valentina_i]

# Print personal info
for person in people:
    name = f"{person['first_name'].title()} {person['last_name'].title()}"
    age = person['age']
    city = f"{person['city'].title()}"
    print(f"{name} is {age} years old and lives in {city}.")

# Alternatively, use .append() to add each person into the list