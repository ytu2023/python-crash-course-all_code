# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 12:27:25 2020

@author: barbora

One common problem when prompting for numerical input occurs when people 
provide text instead of numbers. When you try to convert the input to an int,
you'll get a ValueError. Write a program that prompts for two numbers. 
Add them together and print the result. Catch the ValueError if either input
value is not a number, and print a friendly error message. Test your program
by entering two numbers and then by entering some text instead of a number.
"""

# Option 1 - while loop
# Create a while loop to allow for users to input the two values
flag = True
while flag:
    message1 = "Please input the first value to add. To quit, type 'q': "
    message2 = "Please input the second value to add. To quit, type 'q': "
    value1 = input(message1)
    # Exit conditions
    if (value1 == 'q'):
        print("Ending program")
        break
    value2 = input(message2)
    if (value2 == 'q'):
        print("Ending program")
        break
    # Convert to integer and check for a ValueError
    try:
        int1 = int(value1)
        int2 = int(value2)
    except ValueError:
        print("Please input two integer values")
    else:
        result = int1 + int2
        print(f"Final result: {result}")
        

# Option 2 - while loop and function      
# Create a function to add two values
def addition(value1, value2):
    """Function to add two integer values, with a ValueError check."""
    try:
        int1 = int(value1)
        int2 = int(value2)
    except ValueError:
        return("Please input two integer values")
    else:
        result = int1 + int2
        return(f"Final result: {result}")
        
print(addition(2,3))

# While loop to obtain user input
flag = True
while flag:
    message1 = "Please input the first value to add. To quit, type 'q': "
    message2 = "Please input the second value to add. To quit, type 'q': "
    value1 = input(message1)
    # Exit conditions
    if (value1 == 'q'):
        print("Ending program")
        break
    value2 = input(message2)
    if (value2 == 'q'):
        print("Ending program")
        break
    # Call function
    print(addition(value1, value2))
