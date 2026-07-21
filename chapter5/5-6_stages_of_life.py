# -*- coding: utf-8 -*-
"""
Created on Sun May 10 21:21:04 2020

@author: barbora
"""

# Write an if-elif-else chain that determines a person's stage of life. Set
# a value for the variable age, and then:
# - if the person is less that 2 years old, print > baby
# - if the person is at least 2 but less than 4, print > toddler
# - if the person is at least 4 but less than 13, print > kid
# - if the person is at least 13 but less than 20, print > teenager
# - if the person is at least 20 but less than 65, print > adult
# - if the person is at least 65, print > elder.

# Create the variable and if-elif-else chain
age = 2
if age < 2:
    stage = 'a baby'
elif age < 4:
    stage = 'a toddler'
elif age < 13:
    stage = 'a kid'
elif age < 20:
    stage = 'a teenager'
elif age < 65:
    stage = 'an adult'
else:
    stage = 'an elder'
    
message = f"This person is {stage}."
print(message)
