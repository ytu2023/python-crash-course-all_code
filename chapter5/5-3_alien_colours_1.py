# -*- coding: utf-8 -*-
"""
Created on Sun May 10 20:44:13 2020

@author: barbora
"""

# Imagine an alien was just shot down in a game. Create a variable called
# alien_colour and assign it a value of green, yellow or red.
# - Write an if statement to test whether the alien's colour is green. If it 
# is, print a message that the player just earned 5 points.
# - Write one version of this program that passes the if test and another 
# that fails.

# Create variable
alien_colour = 'green'

# if statement
if alien_colour == 'green':
    print("Congratulations, you just earned 5 points!")
else:
    print("Sorry, wrong colour")

# Repeat for failure    
alien_colour = 'yellow'
if alien_colour == 'green':
    print("Congratulations, you just earned 5 points!")
else:
    print("Sorry, wrong colour.")