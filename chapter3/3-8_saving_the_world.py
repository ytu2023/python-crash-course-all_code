# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 13:31:22 2020

@author: barbora
"""

# Think of at least five places in the world you'd like to visit.
# - Store the locations in a list, not in alphabetical order.
# - Print list in original order.
# - Use sorted() to print in alphabetical order.
# - Show original list remains unchanged.
# - User sorted() to print in reverse alphabetical order.
# - Show original list remains unchanged.
# - Use reverse() to change the order of the list and print.
# - Use reverse() to change the order of the list again and print.
# - Use sort() to change the list into alphabetical order and print.
# - Use sort() to change the list into reverse alphabetical order and print.

# Create the list and print
places = ['demandice', 'peru', 'iceland', 'thailand', 'norway']
print(places)

# Use sorted() function
print("\nUsing sorted() function into alphabetical order and showing original list:")
print(sorted(places))
print(places)
print("Using sorted() function into reverse alphabetical order and showing original list:")
print(sorted(places, reverse=True))
print(places)

# Use reverse() method
print("\nUsing reverse() method into reverse order:")
places.reverse()
print(places)
print("And using reverse() method again:")
places.reverse()
print(places)

# Use sort() method
print("\nUsing sort() method into alphabetical order:")
places.sort()
print(places)
print("Using sort() method into reverse alphabetical order:")
places.sort(reverse=True)
print(places)


