# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 17:02:40 2020

@author: barbora

Write a while loop that asks people why they like programming. Each time
someone enters a reason, add their reason to a file that stores all the 
responses.
"""

# Set a filename and a flag for the while loop
filename = 'c10_5_programming_reasons.txt'
flag = True

# Create a while loop to ask why people like programming
while flag:
    message = "Please tell us why you like programming. Once you're done, "
    message += "type 'stop'. "
    reason = input(message)
    # Condition for exiting the loop
    if reason == 'stop':
        break
    # Write reasons into a file, choosing append method
    with open(filename, 'a') as f:
        f.write(reason)
        f.write("\n")    
