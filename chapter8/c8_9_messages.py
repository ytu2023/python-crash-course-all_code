# -*- coding: utf-8 -*-
"""
Created on Sat May 23 12:03:29 2020

@author: barbora
"""

# Make a list containing a series of short text messages. Pass the list to a 
# function called show_messages(), which prints each text message.

# Create function
def show_messages(list_messages):
    """Function to print each message in a list."""
    for message in list_messages:
        print(message)

# Create list and feed into function
messages = ['Hello', 'Hi', 'How are you?', 'Good thanks!', 'BYE']
show_messages(messages)
