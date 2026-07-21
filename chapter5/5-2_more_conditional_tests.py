# -*- coding: utf-8 -*-
"""
Created on Sat May  9 11:34:21 2020

@author: barbora
"""

# Write more conditional tests, with at least one True and one False example
# for each of the following:
# - Equality and inequality with string
# - Using the lower() method
# - Numerical tests
# - Using and and or
# - Item in a list
# - Item not in a list

# Strings
item = 'chair'
print("Test 1: Is item == 'chair'? I predict True.")
print(item == 'chair')
print("Test 2: Is item != 'chair'? I predict False.")
print(item != 'chair')

# Using the lower() method
full_name = 'John Smith'
print("Test 3: Is full_name = 'john smith' not using lower()? I predict False.")
print(full_name == 'john smith')
print("Test 4: Is full_name = 'john smith' using lower()? I predict True.")
print(full_name.lower() == 'john smith')

# Numerical tests
john_height = 180
craig_height = 170
print("Test 5: Is John taller than 175cm? I predict True.")
print(john_height > 175)
print("Test 6: Is Craig taller than 175cm? I predict False.")
print(craig_height > 175)

# Using and and or
print("Test 7: Are both John and Craig taller than or equal to 170 cm? I "
      "predict True.")
print((john_height >= 170) and (craig_height >= 170))
print("Test 8: Are both John and Craig taller than or equal to 180 cm? I "
      "predict False.")
print((john_height >= 180) and (craig_height >= 180))
print("Test 9: Are John or Craig taller than 175 cm? I "
      "predict True.")
print((john_height > 175) or (craig_height > 175))
print("Test 10: Are John or Craig taller than 180 cm? I "
      "predict False.")
print((john_height > 180) and (craig_height > 180))

# Item in a list
plants = ['aloe vera', 'kalanchoe', 'easter cactus']
print("Test 11: Is aloe vera in the list? I predict True.")
print('aloe vera' in plants)
print("Test 12: Is orchid in the list? I predict False.")
print('orchid' in plants)

# Item not in a list
print("Test 13: Is rose not in the list? I predict True.")
print('rose' not in plants)
print("Test 14: Is kalanchoe not in the list? I predict False.")
print('kalanchoe' not in plants)