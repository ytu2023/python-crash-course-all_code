# -*- coding: utf-8 -*-
"""
Created on Mon May 25 11:22:37 2020

@author: barbora
"""

# Module which contains make_pizza() function
def make_pizza_module(size, *toppings):
    """Summarise pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
