# -*- coding: utf-8 -*-
"""
Created on Tue May 19 09:02:50 2020

@author: barbora
"""

# Write a program that polls users about their dream vacation. Write a prompt.
# Include a block of code that print the results of the poll.

# Create an empty dictionary
vacations = {}

# Set active flag to True
active_flag = True

# Create the loop to gather data
while active_flag:
    # Get user input
    name = input("Please tell us your name: ")
    place = input("If you could visit one place in the world, where would "
                  "you go? ")
    # Add data into dictionary
    vacations[name] = place
    # Check if more people wish to participate
    check = input("Do more people with to participate in the poll? Please "
                  "answer yes or no: ")
    if (check == 'no'):
        print("Thank you all for participating.")
        active_flag = False

# Print poll results
print("\n--- Poll Results ---")
for name, place in vacations.items():
    print(f"{name.title()} would like to go to {place.title()}.")