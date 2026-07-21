# -*- coding: utf-8 -*-
"""
Created on Tue May 19 08:57:16 2020

@author: barbora
"""

# Using 7-8, make sure the sandwich 'pastrami' appears in the list at least
# three times. Add code near the beginning of your program to print a 
# message saying the deli has run out of pastrami, and then use your while 
# loop to remove all occurrences of 'pastrami' from sandwich_orders. Make
# sure no pastrami sandwiches end up in finished_sandwiches.

# Create sandwich_orders list abd finished_sandwiches list
sandwich_orders = ['tuna', 'pastrami', 'blt', 'ploughman\'s', 'pastrami',
                   'smoked salmon', 'pastrami', 'ham & cheese', 'pastrami']
finished_sandwiches = []

# Loop through the sandwiches and print messages
print("Bad news, we have run out of pastrami!")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    if (current_sandwich == 'pastrami'):
        continue
    print(f"Your {current_sandwich} sandwich is being made.")
    finished_sandwiches.append(current_sandwich)
    
# Print all sandwiches
for sandwich in finished_sandwiches:
    print(f"We have made your {sandwich} sandwich.")
    
# Alternatively
#while 'pastrami' in sandwich_orders:
#    sandwich_orders.remove('pastrami')
