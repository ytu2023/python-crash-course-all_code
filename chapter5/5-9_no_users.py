# -*- coding: utf-8 -*-
"""
Created on Sun May 10 22:29:24 2020

@author: barbora
"""

# Add an if test to 5-8 to make sure the list of users is not empty.
# - If the list is empty, print "We need to find some users!"
# - Remove all of the usernames from your list, and make sure the correct
# message is printed.

# List of usernames from 5-8
usernames = ['john1', 'adam2', 'beth3', 'rachel4', 'admin']

# Greetings with an added if loop
if usernames:
    for user in usernames:
        if user == 'admin':
            print(f"Hi {user}, would you like to see the status report?")
        else:
            print(f"Hi {user}, thank you for visiting the website!")
else:
    print("We need to find some users!")
    
# Remove usernames from list
for i in range(len(usernames)):
    usernames.pop(0)
    print(usernames)
print(usernames)

# Test code on an empty list
if usernames:
    for user in usernames:
        if user == 'admin':
            print(f"Hi {user}, would you like to see the status report?")
        else:
            print(f"Hi {user}, thank you for visiting the website!")
else:
    print("We need to find some users!")
