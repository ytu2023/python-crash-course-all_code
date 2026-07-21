# -*- coding: utf-8 -*-
"""
Created on Fri May  1 08:34:27 2020

@author: barbora
"""

# Indent placement
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()} that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
    
print("Thank you everyone, that was a great magic show.")

# Numerical lists using range() and list() functions
for value in range(1, 5):
    print(value)
    
for value in range(6):
    print(value)
    
numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print(f"Even numbers: {even_numbers}")

# List of square numbers
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)

print(f"List of squares: {squares}")

# More concise, omitting temporary variable
squares = []
for value in range(1,11):
    squares.append(value**2)

print(f"List of squares (more concise code): {squares}")

# Stats functions: min(), max() and sum()
digits = list(range(1,10))
digits.append(0)
print(f"Digits: {digits}")
min_val = min(digits)
max_val = max(digits)
sum_val = sum(digits)
print(f"Digits smallest value: {min_val}")
print(f"Digits largest value: {max_val}")
print(f"Digits sum: {sum_val}")

# List comprehension - build lists in one line
squares = [value**2 for value in range(1,11)]
print(f"List comprehension squares: {squares}")

# Slicing
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[:4])
print(players[2:])
print(players[-3:])
print(players[1:4:2])

# Looping through a slice
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

# Copying a list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favourite foods are:")
print(my_foods)
print("\nMy friend's favourite foods are:")
print(friend_foods)
my_foods.append('cannoli')
friend_foods.append('ice-cream')
print("\nMy edited favourite foods are:")
print(my_foods)
print("\nMy friend's edited favourite foods are:")
print(friend_foods)

# Equating lists retains link between them so it doesn't work
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods2 = my_foods
print(f"\nFriend's foods: {friend_foods2}")
print(f"My foods: {my_foods}")
my_foods.append('cannoli')
friend_foods2.append('ice-cream')
print("My edited foods:")
print(my_foods)
print("My friend's edited foods:")
print(friend_foods2)

# Tuples
dimensions = (200, 500)
print(dimensions[0])
print(dimensions[1])
#dimensions[0]= 250 # Cannot re-assign value since tuples are immutable

# For loops for tuples
for dimension in dimensions:
    print(dimension)

# Writing over a tuple
dims = (200, 500)
print("\nOriginal dimensions:")
for dim in dims:
    print(dim)
dims = (400, 100)
print("\nModified dimensions:")
for dim in dims:
    print(dim)
    
