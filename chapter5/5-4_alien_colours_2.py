# -*- coding: utf-8 -*-
"""
Created on Sun May 10 20:49:54 2020

@author: barbora
"""

# Choose a colour for an alien as you did in 5-3, and write an if-else chain.
# - If the alien's colour is green, print a statement that the player just
# earned 5 points for shooting the alien.
# - If the alien's colour isn't green, print a statement that the player just
# earned 10 points.
# - Write one version of this program that runs the if block and another that
# runs the else block.

# Running the if block
alien_colour = 'green'
if alien_colour == 'green':
    print("Congratulations, you just earned 5 points!")
else:
    print("Congratulations, you just earned 10 points!")
    
# Running the else block
alien_colour = 'yellow'
if alien_colour == 'green':
    print("Congratulations, you just earned 5 points!")
else:
    print("Congratulations, you just earned 10 points!")
