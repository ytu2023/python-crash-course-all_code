# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 23:08:51 2020

@author: barbora

Write a program that prompts for the user's favourite number. Use json.dump()
to store this number in a file. Write a separate program that reads in this 
value and prints the message "I know your favourite number! It's ..."
"""

import json

# Function to prompt for user's favourite number
def get_fav_number():
    """Get a user's favourite number and store it in a json file."""
    number = int(input("What is your favourite number? "))
    filename = 'c10_11_number.json'
    with open(filename, 'w') as f:
        json.dump(number, f)
    return number

get_fav_number()

# Function to read value from json file and print a message
def print_fav_number():
    """Read a user's favourite number and print it."""
    filename = 'c10_11_number.json'
    with open(filename, 'r') as f:
        number_loaded = json.load(f)
    print(f"I know your favourite number! It's {number_loaded}")
    
print_fav_number()
