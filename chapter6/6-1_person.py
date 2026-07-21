# -*- coding: utf-8 -*-
"""
Created on Mon May 11 11:44:03 2020

@author: barbora
"""

# Use a dictionary to store information about a person you know. Share their
# first name, last name, age, and the city in which they live. You should
# have keys such as first_name, etc. Print each piece of information.

# Create dictionary
personal_info = {
    'first_name': 'josh',
    'last_name': 'j',
    'age': 26,
    'city': 'reading',
    }

# Print info
first_name = personal_info['first_name'].title()
last_name = personal_info['last_name'].title()
age = personal_info['age']
city = personal_info['city'].title()

print(f"The person's name is {first_name} {last_name}. He is {age} years old "
      f"and lives in {city}.")
