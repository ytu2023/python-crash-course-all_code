# -*- coding: utf-8 -*-
"""
Created on Wed May  6 09:04:32 2020

@author: barbora
"""

# Start with 4-1. Make a copy of the list of pizzas, and call it friend_pizzas.
# - Add a new pizza to the original list.
# - Add a different pizza to the list friend_pizzas.
# - Prove that the lists are separate. Print pizzas using for loops.

# Starting with 4-1
pizzas = ['veggie volcano', 'margherita', 'fiorentina']
for pizza in pizzas:
    print(f"I like {pizza} pizza.")
    
print("I like all pizza!")

# Create a copy of the list
friend_pizzas = pizzas[:]

# Add pizzas to lists and print the separate lists
pizzas.append('four cheese')
friend_pizzas.append('hawaiian')
print("\nMy favourite pizzas are:")
for pizza in pizzas:
    print(pizza)
print("\nMy friend's favourite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)