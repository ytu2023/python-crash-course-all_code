# -*- coding: utf-8 -*-
"""
Created on Sat May 23 12:27:11 2020

@author: barbora
"""

# Start with 8-10. Call the function send_messages() with a copy of the list
# of messages. After calling the function, print both your lists to show that
# the original list has retained its messages.

# Function to move messages to send_messages list from 8-10
def send_messages(list_messages):
    """Function to move each message to a sent_messages list."""
    # Loop through messages to move them into sent_messages list
    print("\nSending messages:")
    while list_messages:
        current_message = list_messages.pop(0)
        print("------------------------------------")
        print(current_message)
        print("------------------------------------")
        sent_messages.append(current_message)
        
# Function to neatly print lists from 8-10
def print_list(input_list):
    """Function to print values in a list in a formatted manner."""
    if input_list:
        print("This list contains the following values:")
        for value in input_list:
            print(value)
    else:
        print("This list is empty.")
  
# Initialise lists, call send_messages() and print lists      
messages = ['Hello', 'Hi', 'How are you?', 'Good thanks!', 'BYE']
sent_messages = []
send_messages(messages[:])
print("\nOriginal messages list:")
print_list(messages)
print("\nSent messages list:")
print_list(sent_messages)
