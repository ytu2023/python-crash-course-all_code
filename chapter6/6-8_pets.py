# -*- coding: utf-8 -*-
"""
Created on Sun May 17 00:06:18 2020

@author: barbora
"""

# Make several dictionaries, where each dictionary represents a different pet.
# In each dictionary, include the kind of animal and the owner's name.
# Store these dictionaries in a list called pets. Next, loop through your
# list and print info.

# Create an empty list to hold pets
pets = []

# Create dictionaries and add to the list
pet = {
       'name': 'winnie',
       'animal': 'a golden labrador',
       'owner': 'j family',
       'age': 1,
       }
pets.append(pet)

pet = {
       'name': 'toby',
       'animal': 'a main coon',
       'owner': 'emma',
       'age': 5,
       }
pets.append(pet)

pet = {
       'name': 'slovaka',
       'animal': 'an alpaca',
       'owner': 'barbora',
       'age': 3,
       }
pets.append(pet)

for pet in pets:
    print(f"{pet['name'].title()} is {pet['animal']} aged {pet['age']} "
          f"owned by {pet['owner'].title()}.")
