# -*- coding: utf-8 -*-
"""
Created on Fri May  8 16:24:58 2020

@author: barbora
"""

# A buffet-style restaurant offers only five basic foods. Think of five 
# simple foods, and store them in a tuple.
# - Use a for loop to print each food the restaurant offers.
# - Try to modify one of the items, and make sure that Python rejects the
# - change.
# - The restaurant changes its menu, replacing two of the items with 
# different foods. Add a line that rewrites the tuple, and then use a for loop
# to print each of the items on the revised menu.

# Create a tuple
foods = ('poached eggs on toast', 'veggie burger', 'brownie with ice cream', 
         'pancakes', 'tomato soup')

# For loop
print("The buffet offers the following five dishes:")
for food in foods:
    print(food.title())

# Try to modify an item
#foods[0] = 'scrambled eggs on toast'
# TypeError given

# Replace two items and print each dish again
foods = ('scrambled eggs on toast', 'halloumi burger', 'brownie with ice cream', 
         'pancakes', 'tomato soup')
print("\nThe buffet's new menu offers the following five dishes:")
for food in foods:
    print(food.title())