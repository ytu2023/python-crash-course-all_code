# -*- coding: utf-8 -*-
"""
Created on Sun May 24 17:07:41 2020

@author: barbora
"""

# Start with user_profily.py from the book. Build a profile of yourself by
# calling build_profile(), using your first and last names and three other
# key-value pairs that describe you.

# Function from book
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

my_profile = build_profile('barbora', 'cernakova', age=24, 
                           favourite_animal='alpaca', location='reading',
                           hobby='knitting')
print(my_profile)
