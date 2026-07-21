# -*- coding: utf-8 -*-
"""
Created on Mon May 18 23:27:49 2020

@author: barbora
"""

# Write a loop that prompts the user to enter a series of pizza toppings
# until they enter a 'quit' value. As they enter each topping, print a 
# message saying you'll add that topping to their pizza.

# Create a prompt
prompt = "Please tell me one topping you would like to have on your pizza."
prompt += "\nEnter 'done' to indicate that your selection is complete. "

# Create a flag
flag = True

# Create the loop
while flag:
    topping = input(prompt)
    if (topping == 'done'):
        flag = False
    else:
        print(f"We are adding {topping} to your pizza.")
