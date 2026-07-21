# -*- coding: utf-8 -*-
"""
Created on Sun May 17 00:44:19 2020

@author: barbora
"""

# Use one of the example programs from this chapter, and extend it by adding 
# new keys and values, changing the contect of the program or improving the 
# formatting of the output.

# Extending pizza example to keep track of orders

pizza_orders = {
    'john': {
        'crust': 'stuffed',
        'sauce': 'tomato',
        'toppings': ['pepperoni'],
        },
    'craig': {
        'crust': 'thick',
        'sauce': 'white',
        'toppings': ['mushrooms', 'extra cheese', 'jalapenos'],
        },
    'beth': {
        'crust': 'thin',
        'sauce': 'tomato',
        'toppings': ['ham', 'chorizo'],
        },
    }

# Loop and print
for person, order in pizza_orders.items():
    print(f"{person.title()} ordered the following pizza this evening:")
    for key, value in order.items():
        if (key == 'toppings'):
            i = 1
            for topping in value:
                print(f"\tTopping {i}: {topping}")
                i = i + 1
        else:
            print(f"\t{key.title()}: {value}")