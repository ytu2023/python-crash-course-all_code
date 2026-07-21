# -*- coding: utf-8 -*-
"""
Created on Wed May  6 09:10:41 2020

@author: barbora
"""

# Choose a version of foods.py from the book and print using for loops.

# Using foods.py from the book
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice-cream')

# Print foods using for loops
print("My favourite foods are:")
for food in my_foods:
    print(food.title())
    
print("\nMy friend's favourite foods are:")
for food in friend_foods:
    print(food.title())
