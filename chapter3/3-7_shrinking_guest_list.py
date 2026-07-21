# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 11:59:19 2020

@author: barbora
"""

# Dinner table won't arrive in time, so there is only place for two guests.
# - Start with 3-6, add a new line that prints a message saying that 
# only two people can come.
# - Use pop() to remove guests until only two remain. Print messages to all 
# uninvited people.
# - Print a message to each person left letting them know they're still invited.
# - Use del to remove the last two names from your list, so you have an empty 
# list. Print your list to make sure it's empty.

# 3-6
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

# Print message saying table won't arrive
print(f"Bad news everyone, the new table won't arrive in time, so there is only space for 2 guests. :(")

# Remove guests and print messages
uninvited = guests.pop(0).title()
print(f"Sorry {uninvited}, you are no longer invited to my dinner party.")
uninvited = guests.pop(0).title()
print(f"Sorry {uninvited}, you are no longer invited to my dinner party.")
uninvited = guests.pop(2).title()
print(f"Sorry {uninvited}, you are no longer invited to my dinner party.")
uninvited = guests.pop(2).title()
print(f"Sorry {uninvited}, you are no longer invited to my dinner party.")

# Print a message to each person still invited
invited = guests[0].title()
print(f"Good news {invited}, you're still invited to my dinner party!")
invited = guests[1].title()
print(f"Good news {invited}, you're still invited to my dinner party!")

# Clear the list for the next dinner party
del guests[0]
del guests[0]
print(guests)

