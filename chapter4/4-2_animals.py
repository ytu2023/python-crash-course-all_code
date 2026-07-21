# -*- coding: utf-8 -*-
"""
Created on Mon May  4 08:38:59 2020

@author: barbora
"""

# Think of at least three different animals with a common characteristic.
# Store the names in a list, then use a for loop to print the names.
# - Modidy your for loop to print a statement about each animal.
# - Add a line stating what they have in common.

# Birds list
birds = ['goldcrest', 'blue tit', 'yellowhammer']
for bird in birds:
    print(f"{bird.title()} is a type of bird which lives in the UK.")
    
print("You can see these three birds in your garden if you are lucky and live " 
      "in the UK!")
