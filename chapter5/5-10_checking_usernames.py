# -*- coding: utf-8 -*-
"""
Created on Sun May 10 22:36:04 2020

@author: barbora
"""

# Do the following to create a program that simulates how websites ensure
# that everyone has a unique username.
# - Make a list of five or more usernames called current_users.
# - Make another list of five or more usernames called new_users. Make sure
# one or two of the new usernames are also in the current_users list.
# - Loop through the new_users list to see if each new username has already
# been used. If it has, print a message that the person will need to enter a 
# new username. If a username has not been used, print a message saying that
# the username is available.
# - Make sure your comparison is case insensitive.

# Make lists of current and new users
current_users = ['JOHN1', 'adam2', 'beth3', 'rachel4', 'Admin']
new_users = ['tom5', 'John1', 'zac6', 'DOM7', 'ADMIN']

# Convert current_users to lower case
lower_current_users = []
for user in current_users:
    lower_current_users.append(user.lower())
print(lower_current_users)

# Alternatively, use a list comprehension to achieve this
#lower_current_users = [user.lower() for user in current_users]

# Loop to check if username is available
for new_user in new_users:
    if new_user.lower() in lower_current_users:
        print(f"Unfortunately {new_user.lower()} is already in use. Please "
              "choose a new username.")
    else:
        print(f"Good news, {new_user.lower()} is available!")
