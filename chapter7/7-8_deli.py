# -*- coding: utf-8 -*-
"""
Created on Tue May 19 08:49:35 2020

@author: barbora
"""

# Make a list called sandwich_orders and fill it with the names of various 
# sandwiches. Then make an empty list called finished_sandwiches. Loop through
# the list of sandwich orders and print a message for each order. As each
# sandwich is made, move it to the list of finished sandwiches. After all the
# sandwiches have been made, print a message listing each sandwich that was
# made.

# Create sandwich_orders list abd finished_sandwiches list
sandwich_orders = ['tuna', 'blt', 'ploughman\'s', 'smoked salmon',
                   'ham & cheese']
finished_sandwiches = []

# Loop through the sandwiches and print messages
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"Your {current_sandwich} sandwich is being made.")
    finished_sandwiches.append(current_sandwich)
    
# Print all sandwiches
for sandwich in finished_sandwiches:
    print(f"We have made your {sandwich} sandwich.")
