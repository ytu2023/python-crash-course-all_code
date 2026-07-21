# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 19:22:25 2020

@author: barbora

Using 9_8 again, store the User class in one module, and store the Privileges
and Admin classes in a separate module. In a separate file, create an Admin
instance and call show_privileges() to show that everything is still working
correctly.

"""

# Import Admin class
from c9_12_multiple_modules_module_admin import Admin

# Create an instance and call methods
my_admin = Admin('barbora', 'c', 'barcern', 24, 'reading')
my_admin.describe_user()
my_admin.privileges_instance.show_privileges()
my_admin.privileges_instance.privileges = ['delete users', 'delete comments']
my_admin.privileges_instance.show_privileges()
