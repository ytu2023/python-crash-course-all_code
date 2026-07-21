# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 11:35:54 2020

@author: barbora
"""

# Invite three more guests to dinner:
# - Start with 3-5, add a print() call to tell people you found a bigger table.
# - Use insert() to add one guest at the beginning of the list.
# - Use insert() to add one guest at the middle of the list.
# - Use insert() to add one guests at the end of the list.
# - Print a new set of invitations.

guests = ['alan turing', 'duncan mackay', 'taylor swift']

print(f"Good news everyone, I found a bigger table!")

# Add in new guests
guests.insert(0, 'ada lovelace')
guests.insert(2, "d'arcy wentworth thompson")
guests.insert(5, 'joe exotic')

# Print new invitations
name = guests[0].title()
message = f"{name} please come to my bigger and better dinner party!"
print(message)
name = guests[1].title()
message = f"{name} please come to my bigger and better dinner party!"
print(message)
name = guests[2].title()
message = f"{name} please come to my bigger and better dinner party!"
print(message)
name = guests[3].title()
message = f"{name} please come to my bigger and better dinner party!"
print(message)
name = guests[4].title()
message = f"{name} please come to my bigger and better dinner party!"
print(message)
name = guests[5].title()
message = f"{name} please come to my bigger and better dinner party!"
print(message)