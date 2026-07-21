# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 08:53:56 2020

@author: barbora

Write a while loop that prompts users for their name. When they enter their 
name, print a greeting to the screen and add a line recording their visit in 
a file called guest_book.txt. Make sure each entry appears on a new line
in the file.
"""

# Create a while loop to ask for guests' names
flag = True
filename = 'c10_4_guest_book.txt'

while flag:
    introduction = "Please tell us your name. If all guests have signed in, "
    introduction += "please type 'stop'. Type your name here: "
    guest = input(introduction)
    # Condition for exiting while loop
    if (guest == 'stop'):
        break
    greeting = f"Hello {guest}, welcome to our hotel!"
    greeting += "We will now add you to the guest book."
    print(greeting)
    # Write into a file
    with open(filename, 'a') as f:
        f.write(guest)
        f.write("\n")
        