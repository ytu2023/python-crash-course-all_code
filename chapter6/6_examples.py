# -*- coding: utf-8 -*-
"""
Created on Mon May 11 10:34:48 2020

@author: barbora
"""

# Simple dictionary
print("Simple dictionary example")
alien_0 = {'colour': 'green', 'points': 5}
print(alien_0['colour'])
print(alien_0['points'])
new_points = alien_0['points']
print(f"Congrats, you just earned {new_points} points!")


# Adding key-value pairs
print("\nAdding key-value pairs")
print(alien_0)
alien_0['x-position'] = 0
alien_0['y-position'] = 25
print(alien_0)


# Starting with an empty dictionary
print("\nEmpty dictionaries")
alien_0 = {}
alien_0['colour'] = 'green'
alien_0['points'] = 5
print(alien_0)


# Modifying values in a dictionary
print("\nModifying values")
alien_0 = {'colour': 'green'}
print(f"The alien is {alien_0['colour']}.")
alien_0['colour'] = 'yellow'
print(f"The alien is now {alien_0['colour']}.")


# Change alien's location
alien_0 = {'x-pos': 0, 'y-pos': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x-pos']}")

# Move the alien to the right
# Determine how far to move the alien based on its current speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien
    x_increment = 3

# The new position is the old position plus the increment
alien_0['x-pos'] = alien_0['x-pos'] + x_increment
print(f"New position: {alien_0['x-pos']}")


# Removing key-value pairs
print("\nRemoving key-value pairs")
alien_0 = {'colour': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)
del(alien_0['colour'])
print(alien_0)


# Similar objects
print("\nSimilar objects")
favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
print(favourite_languages)
language = favourite_languages['sarah'].title()
print(f"Sarah's favourite language is {language}.")


# Using get() to access values
print("\nUsing get()")
alien_0 = {'colour': 'green', 'speed': 'slow'}
#print(alien_0['points']) # Gives a key error

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

point_value = alien_0.get('points')
print(point_value)

alien_0 = {'colour': 'green', 'speed': 'slow', 'points': 5}
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)


# Looping through all key-value pairs
print("\nLooping through all key-value pairs")
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }
print(user_0['username'])

for key, value in user_0.items():
    print(f"Key: {key}")
    print(f"Value: {value}")

favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
for name, language in favourite_languages.items():
    print(f"{name.title()}'s favourite language is {language.title()}.")
    

# Looping through all keys
print("\nLooping through all keys")
favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name in favourite_languages.keys():
    print(f"{name.title()}")

for name in favourite_languages: #.keys() is the default method, so not needed
    print(f"{name.title()}")


# Only action for certain keys
print("\nCertain keys only")
favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
friends = ['phil', 'sarah']
for name in favourite_languages.keys():
    print(f"Hi {name.title()}.")
    if name in friends:
        language = favourite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

if 'erin' not in favourite_languages.keys():
    print("Erin, please take our poll!")
    

# Looping through keys in a particular order
print("\nLooping through keys in a particular order")
favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name in sorted(favourite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
    
for name in sorted(favourite_languages.keys(), reverse=True):
    print(f"{name.title()}, thank you for taking the poll.")


# Looping through all values
print("\nLooping through all values")
favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
print("The following languages have been mentioned:")
for language in favourite_languages.values():
    print(language.title())


# Using set() to give a unique collection of values
print("The following languages have been mentioned:")
for language in set(favourite_languages.values()):
    print(language.title())
    

# Create a test set
print("\nCreating a set")
languages = {'python', 'c', 'ruby', 'python'}
print(languages)


# A list of dictionaries
print("\nA list of dictionaries")
alien_0 = {'colour': 'green', 'points': 5}
alien_1 = {'colour': 'yellow', 'points': 10}
alien_2 = {'colour': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)


# More complex example
# Make an empty list for storing aliens
print("\n")
aliens = []

# Make 30 green aliens
for alien_number in range(30):
    new_alien = {'colour': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
    
# Show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
    
# Alternatively
for i in range(5):
    print(aliens[i])

# Show how many aliens have been created
print("...")
print(f"Total number of aliens: {len(aliens)}")

# Edit some of the aliens
for alien in aliens[:3]:
    if alien['colour'] == 'green':
        alien['colour'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['colour'] == 'yellow':
        alien['colour'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
        
# Show the first 5 aliens
for alien in aliens[:5]:
    print(alien)


# A list in a dictionary
print("\nA list in a dictionary")
# Store information about a pizza being ordered
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }

# Summarise order
print(f"You ordered a {pizza['crust']}-crust pizza with the following "
      "toppings:")
for topping in pizza['toppings']:
    print(f"\t{topping}")
    
# Another example
favourite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }

# Print each person's favourite languages
for name, languages in favourite_languages.items():
    print(f"\n{name.title()}'s favourite languages are:")
    for language in languages:
        print(f"\t{language.title()}")

# Alternatively - messier method
for person in favourite_languages.keys():
    print(f"{person.title()}'s favourite languages are:")
    for language in favourite_languages[person]:
        print(f"\t{language.title()}")
    print("")

# Refined to check if one or multiple favourite languages
for name, languages in favourite_languages.items():
    if (len(languages) == 1):
        print(f"\n{name.title()}'s favourite language is:")
    else:
        print(f"\n{name.title()}'s favourite languages are:")
    for language in languages:
        print(f"\t{language.title()}")


# A dictionary in a dictionary
print("\nA dictionary in a dictionary")
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
    }
for username, info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{info['first'].title()} {info['last'].title()}"
    location = f"{info['location'].title()}"
    print(f"\tFull name: {full_name}")
    print(f"\tLocation: {location}")
