# -*- coding: utf-8 -*-
"""
Created on Sat May 23 12:07:42 2020

@author: barbora
"""

# Start with 8-9. Write a function called send_messages() that prints each
# text message and moves each message to a new list called sent_messages as
# it is printed. After calling the function, print both of your lists to 
# make sure the messages were moved correctly.

# Initiate sent_messages list
sent_messages = []

# Starting with 8-9 
def show_messages(list_messages):
    """Function to print each message in a list."""
    print("\nShowing messages:")
    for message in list_messages:
        print("------------------------------------")
        print(message)
        print("------------------------------------")

# Create function to move messages to send_messages list
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
        
# Create function to neatly print lists
def print_list(input_list):
    """Function to print values in a list in a formatted manner."""
    if input_list:
        print("This list contains the following values:")
        for value in input_list:
            print(value)
    else:
        print("This list is empty.")

# Create list and feed into function
messages = ['Hello', 'Hi', 'How are you?', 'Good thanks!', 'BYE']

print("\nOriginal messages list before sending:")
print_list(messages)

show_messages(messages)
send_messages(messages)

print("\nOriginal messages list after sending:")
print_list(messages)

print("\nSent messages list:")
print_list(sent_messages)
