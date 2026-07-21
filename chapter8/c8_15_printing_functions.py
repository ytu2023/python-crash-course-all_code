# -*- coding: utf-8 -*-
"""
Created on Mon May 25 12:42:22 2020

@author: barbora
"""

# Module storing functions for c8-15_printing_models.py

def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}.")
        completed_models.append(current_design)
        
def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("The following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
