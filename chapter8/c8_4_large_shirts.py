# -*- coding: utf-8 -*-
"""
Created on Thu May 21 21:35:23 2020

@author: barbora
"""

# Modify 8-3 so that shirts are large by default with a message that reads
# "I love Python". Make a large shirt and a medium shirt with the default
# message, and a shirt of any size with a different message.

# Starting with 8-3 to set size to large by default with a preset message
def make_shirt(text='I love Python', size='L'):
    """Function to display information about a shirt to be made."""
    message = f"\nYou have ordered a size {size} shirt with the following text: "
    message += f"\"{text}\". Thank you for your order!"
    print(message)

# Call the function
make_shirt()
make_shirt(size='M')
make_shirt(text="I <3 alpacas!")
make_shirt(size='XS', text='I <3 alpacas!')
