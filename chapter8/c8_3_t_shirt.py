# -*- coding: utf-8 -*-
"""
Created on Thu May 21 21:26:36 2020

@author: barbora
"""

# Write a function called make_shirt() that accepts a size and the text of a
# message that should be printed on the shirt. The function should print a 
# sentence summarising the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt. Call
# the function a second time using keyword arguments.

# Function definition
def make_shirt(size, text):
    """Function to display information about a shirt to be made."""
    message = f"\nYou have ordered a size {size} shirt with the following text: "
    message += f"\"{text}\". Thank you for your order!"
    print(message)
    
# Call using positional arguments
make_shirt('S', 'Python is great!')
make_shirt('M', 'I <3 alpacas!')
    
# Call using keyword arguments
make_shirt(size='L', text='Maths is fun!')
make_shirt(text='Fudge is delicious!', size='S') 
