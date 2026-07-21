# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 22:11:05 2020

@author: barbora

Write a separate Privileges class. The class should have one attribute,
privileges, that stores a list of strings as described in 9_7. 
- Move the show_privileges() method to this class.
- Make a Privileges instance as an attribute in the Admin class.
- Create a new instance of Admin and use your method to show its privileges.

"""

# Starting with 9_5
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
   
# Write Privileges class
class Privileges:
    """Class to describe a user's privileges."""
    
    def __init__(self, privileges=[]):
        """Initialise attributes."""
        self.privileges = privileges
        
    def show_privileges(self):
        """Print all privileges the admin user has."""
        print("This admin user has the following privileges:")
        for item in self.privileges:
            print(f"- {item}")
     
# Write Admin class
class Admin(User):
    """Class to describe an admin user."""
    
    def __init__(self, first_name, last_name, username, age, location):
        """Initialise all attributes."""
        super().__init__(first_name, last_name, username, age, location)
        # Create an instance of Privileges class
        self.privileges_instance = Privileges()
                    
# Create instance
my_admin = Admin('admin', 'a', 'admin.a', 24, 'london')
my_admin.privileges_instance.privileges = ['can add post', 'can delete post',
                                           'can create user',
                                           'can ban user',
                                           'can reset password']
my_admin.describe_user()
my_admin.greet_user()
my_admin.privileges_instance.show_privileges()
