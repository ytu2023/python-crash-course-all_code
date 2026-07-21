# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 23:20:10 2020

@author: barbora

Combine the two programs from 10-11 into one file. If the number is already
stored, report the favourite number to the user. If not, prompt for the 
user's favourite number and store it in a file. Run the program twice to see
if it works.
"""

# Starting with 10-11
import json

# Function to prompt for user's favourite number
def user_fav_number():
    """Check whether the user's favourite number is already stored. 
    If it isn't, get the user's favourite number and store it in a json file.
    Print an appropriate message.
    """
    filename = 'c10_12_number.json'
    # Check whether the number is already stored    
    try:
        with open(filename, 'r') as f:
            number = json.load(f)
    # Prompt for a number if file not found
    except FileNotFoundError:
        number = int(input("What is your favourite number? "))
        with open(filename, 'w') as f:
            json.dump(number, f)
        print(f"Your favourite number is {number}, I'll remember that!")
    else:
        print(f"I know your favourite number! It's {number}")
  
user_fav_number()
    