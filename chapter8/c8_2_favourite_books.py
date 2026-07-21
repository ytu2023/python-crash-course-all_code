# -*- coding: utf-8 -*-
"""
Created on Thu May 21 08:46:21 2020

@author: barbora
"""

# Write a function called favourite_book() that accepts one parameter, title.
# The function should print a message. Call the function, making sure to 
# include a book title as an argument in the function call.

def favourite_book(title):
    """Function to print a message about favourite books."""
    print(f"One of my favourite books is {title.title()}.")

favourite_book("little prince")
favourite_book("the sense of an ending")
favourite_book("the girl on the train")    