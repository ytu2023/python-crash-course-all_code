# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 14:50:11 2020

@author: barbora

Make a list or tuple containing a series of 10 numbers and five letters.
Randomly select four numbers or letters from the list and print a message
saying that any ticket matching these four numbers or letters wins a prize.

"""

# Import randint from random module
from random import randint

# Create a list containing 10 numbers and 5 letters.
raffle_available = [1, 5, 23, 6, 2, 7, 4, 9, 43, 54, 'e', 'g', 'c', 'd', 'm']

# Randomly choose 4 values and create a list of winning positions
length_list = len(raffle_available)
prize_positions = []
winners = []
while len(prize_positions) < 4:
    prize_position = randint(1, length_list)
    if prize_position not in prize_positions:
        print("We've got a winner! The ticket number is ")
        print(raffle_available[prize_position])
        prize_positions.append(prize_position)
        winners.append(raffle_available[prize_position])

print(prize_positions)
print(winners)
    
# Alternatively, this can be achieved using choice() from random module
