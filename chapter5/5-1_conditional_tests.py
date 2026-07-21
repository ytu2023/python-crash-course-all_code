# -*- coding: utf-8 -*-
"""
Created on Sat May  9 11:07:41 2020

@author: barbora
"""

# Write a series of conditional tests. Print a statement describing each test 
# and your prediction for the results of each test. Create at least 10 tests.

fave_animals = ['alpaca', 'duck', 'flying squirrel', 'goldcrest']
print("Test 1: Is alpaca in fave_animals? I predict True.")
print('alpaca' in fave_animals)

print("Test 2: Is cockroach in fave_animals? I predict False.")
print('cockroach' in fave_animals)

print("Test 3: Is goose not in fave_animals? I predict True.")
print('goose' not in fave_animals)

print("Test 4: Is duck not if fave_animals? I predict False.")
print('duck' not in fave_animals)

print("Test 5: Are flying squirrel and goldcrest in fave_animals? I predict"
      " True.")
print(('flying squirrel' in fave_animals) and ('goldcrest' in fave_animals))

print("Test 6: Are flying squirrel and shark in fave_animals? I predict"
      " False.")
print(('flying squirrel' in fave_animals) and ('shark' in fave_animals))

print("Test 7: Are flying squirrel or shark in fave_animals? I predict"
      " True.")
print(('flying squirrel' in fave_animals) or ('shark' in fave_animals))

print("Test 8: Are mouse or shark in fave_animals? I predict False.")
print(('mouse' in fave_animals) or ('shark' in fave_animals))

plant = 'easter cactus'
print("Test 9: Is plant = 'easter cactus'? I predict True.")
print(plant == 'easter cactus')

print("Test 10: Is plant = 'kalanchoe'? I predict False.")
print(plant == 'kalanchoe')