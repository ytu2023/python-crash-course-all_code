# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 14:38:52 2020

@author: barbora

Wrap your code from 10_6 in a while loop so the user can continue entering
numbers even if they make a mistake and enter text instead of number.
"""

# Create a while loop to allow for users to input the two values
# Check for ValueError as soon as possible within code
flag = True
while flag:
    message1 = "Please input the first value to add. To quit, type 'q': "
    message2 = "Please input the second value to add. To quit, type 'q': "
    try:
        value1 = input(message1)
        if (value1 == 'q'):
            print("Ending program")
            break
        value2 = input(message2)
        if (value2 == 'q'):
            print("Ending program")
            break
        # Convert to integer and check for a ValueError
        int1 = int(value1)
        int2 = int(value2)
    except ValueError:
        print("Please input two integer values")
    else:
        result = int1 + int2
        print(f"Final result: {result}")
