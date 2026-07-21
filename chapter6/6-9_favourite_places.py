# -*- coding: utf-8 -*-
"""
Created on Sun May 17 00:16:46 2020

@author: barbora
"""

# Make a dictionary called favourite_places. Think of three names to use as 
# keys in the dictionary, and store one to three favourite places for each
# person. Loop and print.

# Create the dictionary
favourite_places = {
    'barbora': ['demandice', 'st andrews', 'edinburgh'],
    'josh': ['devon', 'central london'],
    'becky': ['stockholm'],
    }

# Loop and print
for person, places in favourite_places.items():
    if (len(places) == 1):
        print(f"{person.title()}'s favourite place is:")
    else:
        print(f"{person.title()}'s favourite places are:")
    for place in places:
        print(f"\t{place.title()}")
        