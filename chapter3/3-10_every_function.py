# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 13:45:04 2020

@author: barbora
"""

# Think of something you could store in a list. Write a program that creates a 
# list comtaining these items and then uses each function introduced in this
# chapter at least once.

# Define orginal list
icecreams = ['magnum raspberry', 'cornetto', 'feast', 'twister']
print("Original list:")
print(icecreams)

# Add elements
print("\nUse insertion:")
icecreams[0] = 'magnum classic'
print(icecreams)
print("Use append() method:")
icecreams.append('magnum raspberry')
print(icecreams)
print("Use insert() method:")
icecreams.insert(0, 'viennetta')
print(icecreams)

# Remove elements
print("\nUse del function (by index):")
del(icecreams[5])
print(icecreams)
print("Use pop() method (by index):")
popped_icecream = icecreams.pop(0)
print(icecreams)
print(popped_icecream)
print("Use remove() method (by value):")
to_remove = 'twister'
icecreams.remove(to_remove)
print(icecreams)

# Organise
print("\nUse sorted() function:")
print(sorted(icecreams))
print(sorted(icecreams, reverse=True))
print("Use reverse() method twice:")
icecreams.reverse()
print(icecreams)
icecreams.reverse()
print(icecreams)
print("Use sort() method twice:")
icecreams.sort()
print(icecreams)
icecreams.sort(reverse=True)
print(icecreams)

# Find length
length = len(icecreams)
print(f"We ended up with {length} ice creams!")








