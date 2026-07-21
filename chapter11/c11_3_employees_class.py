# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 22:32:06 2020

@author: barbora

Store class for 11-3.
"""

class Employee:
    """
    Class to store an employee's first name, last name and salary.
    Include functionality to increase salary.
    """
    
    def __init__(self, first, last, salary):
        """Store first name, last name, and salary."""
        self.first = first.title()
        self.last = last.title()
        self.salary = salary
        
    def give_raise(self, increase=5000):
        """Increase salary by 5000 by default."""
        self.salary += increase
        