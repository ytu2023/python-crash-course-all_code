# -*- coding: utf-8 -*-
"""
Created on Wed May 13 21:01:03 2020

@author: barbora
"""

# Use the code in favourite_languages.py (in book).
# - Make a list of people who should take the favourite languages poll. 
# Include some names that are already in the dictionary and some that are not.
# - Loop through the list of people who should take the poll. If they have 
# already taken the poll, print a message thanking them for responding. If 
# they have not yet taken the poll, print a message inviting them to take it.

# Code from favourite_languages.py
favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
for person, language in favourite_languages.items():
    print(f"{person.title()}'s favourite language is {language.title()}.")

print("\n")

# Create a list of people
people = ['jen', 'adam', 'tom', 'sarah', 'phil', 'mary', 'dom']

# Loop through the list of people and print a relevant message
for person in people:
    if person in favourite_languages.keys():
        print(f"Hi {person.title()}, thank you for completing the poll!")
    else:
        print(f"Hi {person.title()}, please complete our poll!")
