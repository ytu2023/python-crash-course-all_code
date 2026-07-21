# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 22:28:12 2020

@author: barbora

Write a class called Employee. The __init__() method should take in a first 
name, a last name, and an annual salary, and store each of these as 
attributes. Write a method called give_raise() that adds $5000 to the
annual salary by default but also accepts a different raise amount.

Write a test case for Employee. Write two test methods, 
test_give_default_raise() and test_give_custom_raise(). Use the setUp()
method so you don't have to create a new employee instance in each test
method. Run your test case, and make sure both tests pass.
"""

import unittest
from c11_3_employees_class import Employee

# Write test case for the Employee class
class TestEmployeeClass(unittest.TestCase):
    """Tests for the class Employee."""
    
    def setUp(self):
        """Create an employee instance."""
        self.my_employee = Employee('joe', 'bloggs', 20000)
        self.custom_raise = 10000
        
    def test_give_default_raise(self):
        """Test that the default raise adds 5000 to the salary."""
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.salary, 25000)
        
    def test_give_custom_raise(self):
        """Test that a custom raise of 10000 adds 10000 to the salary."""
        self.my_employee.give_raise(self.custom_raise)
        self.assertEqual(self.my_employee.salary, 30000)
        
# Run test case
if __name__ == '__main__':
    unittest.main()
    