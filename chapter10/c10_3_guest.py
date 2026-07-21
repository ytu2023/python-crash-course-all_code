# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 08:49:39 2020

@author: barbora

Write a program that prompts the user for their name. When they respond,
write their name to a file called guest.txt.
"""

# Ask for user's name
guest = input("Please tell me your name: ")

print("Thank you, I will add you to the guest book.")

# Add guest to guest book
filename = 'c10_3_guest.txt'

with open(filename, 'w') as file_object:
    file_object.write(guest)
    file_object.write("\n")
