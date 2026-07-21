# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 19:25:05 2020

@author: barbora

Classes to describe an admin user and an admin user's privileges, from 9_8.

"""

# Import User class
from c9_12_multiple_modules_module_user import User

# Privileges class from 9_8, with added statement if no privileges available
class Privileges:
    """Class to describe a user's privileges."""
    
    def __init__(self, privileges=[]):
        """Initialise attributes."""
        self.privileges = privileges
        
    def show_privileges(self):
        """Print all privileges the admin user has."""
        if self.privileges:
            print("This admin user has the following privileges:")
            for item in self.privileges:
                print(f"- {item}")
        else:
            print("This admin user has no privileges.")
     
# Admin class from 9_8
class Admin(User):
    """Class to describe an admin user."""
    
    def __init__(self, first_name, last_name, username, age, location):
        """Initialise all attributes."""
        super().__init__(first_name, last_name, username, age, location)
        # Create an instance of Privileges class
        self.privileges_instance = Privileges()
