# -*- coding: utf-8 -*-
"""
Created on Sun May 31 22:59:10 2020

@author: barbora

Start with 9_3.
- Add an attribute called login_attempts.
- Write a method called increment_login_attempts() that increments the value
of login_attempts by 1. Write another method called reset_login_attempts()
that resets the value of login_attempts to 0.
- Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts to make sure it was 
incremented properly, and then call reset_login_attempts(). Print 
login_attempts again to make sure it was reset to 0.

"""

# Starting with 9_3
class User:
    """Class to describe a user."""
    
    def __init__(self, first_name, last_name, username, age, location):
        """Initialise attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.age = age
        self.location = location
        # Add attribute for login attempts
        self.login_attempts = 0
        
    def describe_user(self):
        """Method to print a summary about the user."""
        message = f"This user's full name is {self.first_name.title()} "
        message += f"{self.last_name.title()}. {self.first_name.title()} is "
        message += f"{self.age} years old, lives in "
        message += f"{self.location.title()} and uses {self.username} "
        message += f"as username."
        print(message)
        
    def greet_user(self):
        """Print a personalised greeting."""
        greeting = f"Hi {self.first_name.title()}, welcome back!\n"
        print(greeting)
    
    def increment_login_attempts(self):
        """
        Increment number of login attempts. 
        Positive values only allowed.
        """
        self.login_attempts += 1
            
    def reset_login_attempts(self):
        """Set number of login attempts to 0."""
        self.login_attempts = 0

# Create an instance
user_josh = User('josh', 'j', 'joshj', 26, 'reading')

# Simulate many login attempts
print(f"Before incrementing: {user_josh.login_attempts}")
user_josh.increment_login_attempts()
print(f"Increment 1: {user_josh.login_attempts}")
user_josh.increment_login_attempts()
print(f"Increment 2: {user_josh.login_attempts}")
user_josh.increment_login_attempts()
print(f"Increment 3: {user_josh.login_attempts}")
user_josh.increment_login_attempts()
print(f"Increment 4: {user_josh.login_attempts}")

# Reset login attempts
user_josh.reset_login_attempts()
print(f"After resetting: {user_josh.login_attempts}")
