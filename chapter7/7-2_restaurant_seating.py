# -*- coding: utf-8 -*-
"""
Created on Sun May 17 10:57:48 2020

@author: barbora
"""

# Write a program that asks the user how many people are in their dinner group.
# If the answer is more than 8, print a message saying they'll have to wait
# for a table. Otherwise, report that their table is ready.

# User input
guests = input("How many people are there in your dinner group? ")
guests = int(guests)

# Print a message
if (guests > 8):
    print("Due to the size of your group, you will have to wait for a table.")
else:
    print("Your table is ready, please follow me.")
