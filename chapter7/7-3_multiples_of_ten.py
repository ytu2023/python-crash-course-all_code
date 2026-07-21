# -*- coding: utf-8 -*-
"""
Created on Sun May 17 11:01:27 2020

@author: barbora
"""

# Ask the user for a number, and then report whether the number is a multiple
# of 10 or not.

# User input
number = input("Please tell me your number, and I'll tell you whether it is "
               "a multiple of 10 or not: ")
number = int(number)

# Print a message
if (number % 10 == 0):
    print(f"Your number {number} is a multiple of 10.")
else:
    print(f"Your number {number} isn't a multiple of 10.")
