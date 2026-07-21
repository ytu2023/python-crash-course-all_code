# -*- coding: utf-8 -*-
"""
Created on Thu May 21 08:27:50 2020

@author: barbora
"""

# Import statements
#import c8_examples_module_pizza
#from c8_examples_module_pizza import make_pizza


# Simple function
def greet_user():
    """Display a simple greeting."""
    print("Hello!")
    
greet_user()


# Passing information to a function
def greet_user(username):
    """"Display a simple greeting."""
    print(f"Hello, {username.title()}.")
    
greet_user('jesse')
greet_user('sarah')
#name = input("Please tell me your username and I will say hello to you: ")
#greet_user(name)


# Positional arguments
print("\nPositional arguments")
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
    
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
describe_pet('harry', 'hamster')


# Keyword arguments
print("\nKeyword arguments")
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')


# Default values and equivalent function calls
print("\nDefault values and equivalent function calls")
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# A dog named Willie
describe_pet('willie')
describe_pet(pet_name='willie')

# A hamster named Harry
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')


# Returning a simple value
print("\nUsing return statement")
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)


# Making an argument optional
print("\nMaking an argument optional")
def get_formatted_name(first_name, middle_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

# With middle name optional
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)


# Returning a dictionary
print("\nReturning a dictionary")
def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

# Extended to include age
print("\nReturning a dictionary")
def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', 27)
print(musician)
musician = build_person('jimi', 'hendrix')
print(musician)


# Functions with while loops - break statement
print("\nFunctions with while loops")
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# Using a break statement
while True:
    print("\nPlease tell me your name.")
    print("(enter 'q' at any time to quit')")
    f_name = input("First name: ")
    if (f_name == 'q'):
        break
    l_name = input("Last name: ")
    if (l_name == 'q'):
        break
    # Call get_formatted_name
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
    

# Passing a list
print("\nPassing a list")
def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)


# Modifying a list outside of a function
print("\nModifying a list outside of a function")
# Start with some design that need to be printed
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simulate printing each design, until none are left
# Move each design to completed_models after printing
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}.")
    completed_models.append(current_design)

# Display all completed designs
print("The following models have been printed:")
for completed_model in completed_models:
    print(completed_model)
    

# Modifying a list using functions
print("\nModifying a list using functions")
def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}.")
        completed_models.append(current_design)
        
def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("The following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
        
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)


# Preventing a function from modifying a list
print("\nPreventing a function from modifying a list")
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Feed a copy of list into function using list[:]
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
print(unprinted_designs)


# Passing an arbitrary number of arguments, using an empty tuple
print("\nPassing an arbitrary number of arguments")
def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)
    
make_pizza('pepperoni')
make_pizza('mushrooms', 'extra cheese', 'sweetcorn')

# Example above extended
def make_pizza(*toppings):
    """Summarise the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'extra cheese', 'sweetcorn')


# Mixing positional and arbitrary arguments
print("\nMixing positional and arbitrary arguments")
def make_pizza(size, *toppings):
    """Summarise the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'extra cheese', 'sweetcorn')


# Using arbitrary keyword arguments
print("\nArbitrary keyword arguments")
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein', location='princeton',
                             field='physics')
print(user_profile)

# Importing modules - statements should be at top of file
print("\nImporting modules")
# Import full module
import c8_examples_module_pizza
c8_examples_module_pizza.make_pizza_module(16, 'pepperoni')
c8_examples_module_pizza.make_pizza_module(12, 'sweetcorn', 'mushrooms',
                                            'extra cheese')

# Import specific function
from c8_examples_module_pizza import make_pizza_module
make_pizza_module(16, 'pepperoni')
make_pizza_module(12, 'sweetcorn', 'mushrooms', 'extra cheese')

# Import specific function with alias
from c8_examples_module_pizza import make_pizza_module as mp
mp(16, 'pepperoni')
mp(12, 'sweetcorn', 'mushrooms', 'extra cheese')

# Import full module with alias
import c8_examples_module_pizza as p
p.make_pizza_module(16, 'pepperoni')
p.make_pizza_module(12, 'sweetcorn', 'mushrooms', 'extra cheese')

# Import all functions - not recommended, can overwrite existing functions
from c8_examples_module_pizza import *
make_pizza_module(16, 'pepperoni')
make_pizza_module(12, 'sweetcorn', 'mushrooms', 'extra cheese')
