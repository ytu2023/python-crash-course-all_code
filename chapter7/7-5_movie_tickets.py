# -*- coding: utf-8 -*-
"""
Created on Mon May 18 23:33:45 2020

@author: barbora
"""

# A cinema charges different ticket prices depending on a person's age. If a
# person is under the age of 3, the ticket is free. If they are between 3 and
# 12, the ticket is $10. If they are over age 12, the ticket is $15. Write 
# a loop in which you ask users their age, and then tell them the cost of
# their movie ticket.

# Create prompt
prompt = "Welcome to our cinema! Please tell us how old each member of your "
prompt += "group is, typing in 'done' when you're finished. "

# Loop and print ticket price
while True:
    age = input(prompt)
    if (age == 'done'):
        break
    age = int(age)
    if (age <= 3):
        print("\tYour ticket is free!")
    elif (age <= 12):
        print("\tYour ticket costs $10.")
    else:
        print("\tYour ticket costs $15.")
