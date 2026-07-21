# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 14:38:15 2020

@author: barbora

Make a class Die with one attribute called sides, which has a default value of
6. Write a method called roll_die() that prints a random number between 1 and
the number of sides the die has. Make a 6-sided die and roll it 10 times.
Make a 10-sided die and a 20-sided die. Roll each die 10 times.

"""

# Import randint from random module
from random import randint

# Create Die class
class Die:
    """Class to represent a die."""
    
    def __init__(self, sides=6):
        """Initialise attributes for a die."""
        self.sides = sides
        
    def roll_die(self):
        """
        Method to simulate rolling a die by printing a random number 
        between 1 and number of sides.
        """
        print("Rolling your die...")
        result = randint(1, self.sides)
        print(f"You have rolled {result}.")
        
# Make an instance of a 6-sided die and roll it 10 times
die6 = Die()
print(f"\nRolling a die with {die6.sides} sides:")
for i in range(1,11):
    print(f"\nRoll number {i}:")
    die6.roll_die()
    
# Make an instance of a 10-sided die and roll it 10 times
die10 = Die(10)
print(f"\nRolling a die with {die10.sides} sides:")
for i in range(1,11):
    print(f"\nRoll number {i}:")
    die10.roll_die()
    
# Make an instance of a 6-sided die and roll it 10 times
die20 = Die(20)
print(f"\nRolling a die with {die20.sides} sides:")
for i in range(1,11):
    print(f"\nRoll number {i}:")
    die20.roll_die()
