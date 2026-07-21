# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 23:30:27 2020

@author: barbora

Modify remember_me.py in case the current user is not the person who last
user the program.

Before printing a welcome back message in greet_user(), ask the user if this is
the corrent username. If it's not, call get_new_username() to get the correct
username.
"""

# Starting with remember_me.py
import json

filename = 'c10_13_verify_user.json'

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def get_stored_username():
    """Get stored username if available."""
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username
    
# def greet_user():
#     """Greet the user by name."""
#     username = get_stored_username()
#     if username:
#         # Checking whether this is the correct username 
#         flag = input(f"Is {username} your username? y/n ")
#         if (flag == 'y'):
#             print(f"Welcome back, {username}!")
#         else:
#             username = get_new_username()
#             print(f"We'll remember you when you come back, {username}!")
#     else:
#         username = get_new_username()
#         print(f"We'll remember you when you come back, {username}!")
            
# greet_user()

# Clean up greet_user()
def check_username(username):
    """Check whether a username is accessible and 
    whether it is this user's username.
    """
    if username:
        flag = input(f"Is {username} your username? y/n ")
        if (flag == 'y'):
            print(f"Welcome back, {username}!")
            return "stored"
    
def greet_user_clean():
    """Greet the user by name - neater."""
    username = get_stored_username()
    if check_username(username) == "stored":
        return
    # If the check passes, we leave the function due to empty return statement
    # If the check fails, the following lines run hence else not needed
    username = get_new_username()
    print(f"We'll remember you when you come back, {username}!")
            
greet_user_clean()
