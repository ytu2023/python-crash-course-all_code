# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 15:08:23 2020

@author: barbora

Use a loop to see how hard it might be to win the kind of lottery modelled in
9_14. Make a list or tuple called my_ticket. Write a loop that keeps pulling 
numbers until your ticket wins. Print a message reporting how many times the 
loop had to run to give you a winning ticket.

"""

# Import choice from random module
from random import choice

# Create lists to hold my tickets and all tickets
raffle_available = [1, 5, 23, 6, 2, 7, 4, 9, 43, 54, 'e', 'g', 'c', 'd', 'm']
my_tickets = [23, 'm']

# Pull tickets until one of my tickets wins
flag = True
counter = 0
all_chosen = []
while flag:
    counter += 1
    chosen = choice(raffle_available)
    # Delete chosen value from list of all available values
    raffle_available.remove(chosen)
    all_chosen.append(chosen)
    if chosen in my_tickets:
        print("I have won!")
        print(f"It took me {counter} attempts.")
        flag = False
    
print(all_chosen)


# Alternatively, split the above into functions
raffle_available = [1, 5, 23, 6, 2, 7, 4, 9, 43, 54, 'e', 'g', 'c', 'd', 'm']
my_tickets = [23, 'm']
counter = 0

def pick_ticket(local_list):
    # Function to choose a random value from a list
    chosen = choice(local_list)
    return chosen

def counter(counter):
    # Function to count the number of attempts to pick a ticket
    counter += 1
    return counter
    
def check_ticket(my_ticket_list, ticket_list):
    # Function to check whether a value selected in pick_ticket() matches
    # one of my tickets
    count = 0
    flag = True
    local_list = ticket_list
    # Loop until a matching ticket found
    while flag:
        # Call pick_ticket() to choose a ticket
        chosen = pick_ticket(local_list)
        # Call counter() to count attempts
        count = counter(count)
        # Check if chosen ticket is one of mine
        if chosen in my_ticket_list:
            print("I have won!")
            flag = False
        # Remove chosen value from list of available values
        local_list.remove(chosen)
    final_count = count
    print(f"The final count is {final_count}")
    
pick_ticket(raffle_available)
check_ticket(my_tickets, raffle_available)
