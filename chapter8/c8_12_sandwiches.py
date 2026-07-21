# -*- coding: utf-8 -*-
"""
Created on Sun May 24 16:58:31 2020

@author: barbora

"""

# Write a function that accepts a list of items a person wants on a sandwich.
# The function should have one parameter that collects as many items as
# the function call provides, and it should print a summary of the order.
# Call the function three times, using a different number of arguments
# each time.

# Function definition
def order_sandwich(*fillings):
    """Function to display fillings ordered for the customer's sandwich."""
    print("\nYou have ordered the following fillings for your sandwich:")
    for filling in fillings:
        print(f"- {filling}")

# Function calls
order_sandwich('cheese')
order_sandwich('tuna', 'mayo', 'sweetcorn')
order_sandwich('tomato', 'mozarella', 'pesto', 'pine nuts')
