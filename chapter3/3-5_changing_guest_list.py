# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 11:28:16 2020

@author: barbora
"""

# One of your guests from 3-4 can't make it:
# - Add a print() call stating the name of the guest who can't make it.
# - Modify your list, replacing the guest.
# - Print a second set of invitations.

guests = ['alan turing', 'duncan mackay', 'taylor swift']

cant_attend = guests[2]
print(f"Unfortunately {cant_attend.title()} cannot attend the dinner party.")

guests.remove('taylor swift')
guests.append('emma watson')

print(guests)

name0 = guests[0].title()
name1 = guests[1].title()
name2 = guests[2].title()

print(f"Dinner Party 2.0: {name0} please come to my dinner party!")
print(f"Dinner Party 2.0: {name1} please come to my dinner party!")
print(f"Dinner Party 2.0: {name2} please come to my dinner party!")
