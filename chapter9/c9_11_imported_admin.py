# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 19:10:22 2020

@author: barbora

Start with 9_8. Store the classes User, Privileges and Admin in one module.
Create a separate file, make an Admin instance, and call show_privileges()
to show that everything is working correctly.

"""

# Import Admin class
from c9_11_imported_admin_module import Admin

# Make an Admin instance
my_admin = Admin('barbora', 'c', 'barcern', 24, 'reading')
my_admin.describe_user()
my_admin.privileges_instance.privileges = ['delete user', 'add comment']
my_admin.privileges_instance.show_privileges()
