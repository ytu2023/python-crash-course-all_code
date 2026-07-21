# -*- coding: utf-8 -*-
"""
Created on Sun May 10 22:47:56 2020

@author: barbora
"""

# Ordinal numbers indicate their position in alist, such as 1st and 2nd. Most
# ordinal numbers end in th, except 1, 2 and 3.
# - Store the numbers 1 through 9 in a list.
# - Loop through the list.
# - Use an if-elif-else chain inside the loop to print the proper ordinal
# ending for each number.

# Create the list
numbers = []
for i in range(1,10):
    numbers.append(i)
print(numbers)

# Alternatively
#numbers = list(range(1,10))

# Loops for ordinal endings
for i in numbers:
    if i == 1:
        print(f"{i}st")
    elif i == 2:
        print(f"{i}nd")
    elif i == 3:
        print(f"{i}rd")
    else:
        print(f"{i}th")
