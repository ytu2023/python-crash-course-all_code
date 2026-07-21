# -*- coding: utf-8 -*-
"""
Created on Wed May 27 22:22:17 2020

@author: barbora

Make a class called User. 
- Create two attributes called first_name and last_name, and then create 
several other attributes that are typically stored in a user profile.
- Make a method called describe_user() that prints a summary.
- Make a method called greet_user() that prints a personalised greeting.
- Create several instances representing different users. Call both methods
for each user.

"""

# Create class User
class User:
    """Class to describe a user."""
    
    def __init__(self, first_name, last_name, username, age, location):
        """Initialise attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.age = age
        self.location = location
        
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
        
# Create instances and call both methods
josh = User('josh', 'j', 'josh_j', 26, 'reading')
valentina = User('valentina', 'i', 'valentina_i', 33, 'west ealing')
becky = User('becky', 'm', 'becky_m', 23, 'stockholm')
john = User('john', 's', 'john_s', 22, 'madison')

josh.describe_user()
josh.greet_user()
valentina.describe_user()
valentina.greet_user()
becky.describe_user()
becky.greet_user()
john.describe_user()
john.greet_user()
