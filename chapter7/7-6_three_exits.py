# -*- coding: utf-8 -*-
"""
Created on Mon May 18 23:41:50 2020

@author: barbora
"""

# Write different versions of 7-4 and 7-5 that do each of the following at 
# least once:
# - Use a conditional test in the while statement to stop the loop.
# - Use an active variable to control how long the loop runs.
# - Use a break statement to exit the loop when the user enter a 'quit' value.

# Starting with 7-4
# Retaining the same prompt for all three scenarios
prompt = "Please tell me one topping you would like to have on your pizza."
prompt += "\nEnter 'quit' to indicate that your selection is complete. "

# Using a conditional test
topping = ""
while (topping != 'quit'):
    topping = input(prompt)
    if (topping != 'quit'):
        print(f"We are adding {topping} to your pizza.")
        
# Using an active variable
flag = True
while flag:
    topping = input(prompt)
    if (topping == 'done'):
        flag = False
    else:
        print(f"We are adding {topping} to your pizza.")

# Using a break statement
while True:
    topping = input(prompt)
    if (topping == 'quit'):
        break
    print(f"We are adding {topping} to your pizza.")
    
    
# Moving onto 7-5
# Again retaining the same prompt for all scenarios
prompt = "Welcome to our cinema! Please tell us how old each member of your "
prompt += "group is, typing in 'done' when you're finished. "

# Using a conditional test
age = ""
while (age != 'done'):
    age = input(prompt)
    if (age.isnumeric() == True):
        age_no = int(age)
        if (age_no <= 3):
            print("\tYour ticket is free!")
        elif (age_no <= 12):
            print("\tYour ticket costs $10.")
        else:
            print("\tYour ticket costs $15.")

# Using an active variable
flag = True
while flag:
    age = input(prompt)
    if (age == 'done'):
        flag = False
    else:
        age = int(age)
        if (age <= 3):
            print("\tYour ticket is free!")
        elif (age <= 12):
            print("\tYour ticket costs $10.")
        else:
            print("\tYour ticket costs $15.")
    
# Using a break statement
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
    