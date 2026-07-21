# -*- coding: utf-8 -*-
"""
Created on Sun May 10 22:25:48 2020

@author: barbora
"""

# Make a list of five or more usernames, including the name 'admin'. Imagine
# you are writing code that will print a greeting to each user after they log 
# into a website. Loop through the list, and print a greeting to each user:
# - if the username is 'admin', print a special greeting
# - otherwise, print a generic greeting.

# Create list of usernames
usernames = ['john1', 'adam2', 'beth3', 'rachel4', 'admin']

# Greetings
for user in usernames:
    if user == 'admin':
        print(f"Hi {user}, would you like to see the status report?")
    else:
        print(f"Hi {user}, thank you for visiting the website!")
