# -*- coding: utf-8 -*-
"""
Created on Sun May 17 10:27:55 2020

@author: barbora
"""

# Simple user input using input()
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

name = input("Please enter your name: ")
print(f"\nHello, {name}!")

prompt = "If you tell us who you are, we can personalise the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print(f"\nHello, {name}!")


# Simple user input using int()
age = input("How old are you? ")
age = int(age)
print(age >= 18)


# More complex example
height = input("How tall are you, in inches? ")
height = int(height)

if (height >= 48):
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")
    

# Using modulo operator
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if (number % 2 == 0):
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")


# Intro to while loops
print("\nIntro to while loops")
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
    

# Letting user choose when to stop
prompt = "\nTell me something, and I will repeat it back to you: \nEnter "
prompt += "'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    if (message != 'quit'):
        print(message)


# Using a flag
print("\nUsing a flag")
prompt = "\nTell me something, and I will repeat it back to you: \nEnter "
prompt += "'quit' to end the program. "

# Create flag
active = True
while active:
    message = input(prompt)
    if (message == 'quit'):
        active = False
    else:
        print(message)


# Using a break statement
print("\nUsing a break statement")
prompt = "\nPlease enter the name of a city you have visited."
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}.")


# Using continue in a loop
print("\nUsing continue in a loop")
current_number = 0
while (current_number < 10):
    current_number += 1
    if (current_number % 2 == 0):
        continue
    print(current_number)
    

# Moving items from one list to another
print("\nMoving items from one list to another")
# Start with user that need to be veridied, and an empty list to hold
# confirmed users
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verify each user until there are no more unconfirmed users
# Move each verified user into the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# Display all confirmed users
print("The following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
    

# Removing all instances of specific values from a list
print("\nRemoving all instances of specific values from a list")
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
    print(pets)
print(pets)


# Filling a dictionary with user input
print("\nFilling a dictionary with user input")
responses = {}

# Set a flag to indicate that polling is active
polling_active = True

while polling_active:
    # Prompt for the person's name and response
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    
    # Store the reponse in the dictionary
    responses[name] = response
    
    # Find out if anyone else is going to take the poll
    repeat = input("Would you like to let another person repond? (yes or no) ")
    if repeat == 'no':
        polling_active = False

# Polling complete, show the results
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")
