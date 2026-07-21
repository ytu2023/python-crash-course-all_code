# -*- coding: utf-8 -*-
"""
Created on Sun May 17 00:23:03 2020

@author: barbora
"""

# Modify 6-2 so each person can have more than one favourite number. Then 
# print each person's name along with their favourite numbers.

# Edit dictionary from 6-2
fave_numbers = {
    'john': [25, 68, 12],
    'adam': [3, 783.2, -4431, 1],
    'mary': [8098, 55],
    'tom': [43, -80, 415.32, 6794],
    'alice': [907, 9],
    }

for person, numbers in fave_numbers.items():
    print(f"{person.title()}'s favourite numbers are:")
    for number in numbers:
        print(f"\t{number}")
        