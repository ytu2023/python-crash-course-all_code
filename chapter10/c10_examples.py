# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 08:43:58 2020

@author: barbora
"""

# Reading an entire file
print("\nReading an entire file")
with open('c10_examples_pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)
print(contents.rstrip())


# Using relative file paths
print("\nRelative file paths")
with open('text_files/c10_examples_pi_digits.txt') as file_object:
    cotents = file_object.read()
print(contents)


# Using absolute file paths
print("\nAbsolute file paths")
file_path = '/users/barbora/Documents/c10_examples_pi_digits.txt'
with open(file_path) as file_object:
    contents = file_object.read()
print(contents)


# Reading line by line
print("\nReading line by line")
file_name = 'c10_examples_pi_digits.txt'
with open(file_name) as file_object:
    for line in file_object:
        print(line)
with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip())
        

# Making a list of lines
print("\nMaking a list of lines")
file_name = 'c10_examples_pi_digits.txt'
with open(file_name) as file_object:
    lines = file_object.readlines()
    
for line in lines:
    print(line.rstrip())


# Working with a file's contents
print("\nWorking with a file's contents")
file_name = 'c10_examples_pi_digits.txt'
with open(file_name) as file_object:
    lines = file_object.readlines()
 
# Remove whitespace on right side of string only
pi_string = ''
for line in lines:
    pi_string += line.rstrip()
    
print(pi_string)
print(len(pi_string))

# Remove whitespace on both sides of string - doesn't make a difference
# in spyder
pi_string = ''
for line in lines:
    pi_string += line.strip()
    
print(pi_string)
print(len(pi_string))


# Extended example - using one million digits of pi
print("\nWorking with a file's contents")
file_name = 'c10_examples_pi_million_digits.txt'
with open(file_name) as file_object:
    lines = file_object.readlines()
 
pi_string = ''
for line in lines:
    pi_string += line.strip()
    
print(f"{pi_string[:52]}")
print(len(pi_string))


# Check if birthday in the first one million digits of pi
print("\nWorking with a file's contents")
file_name = 'c10_examples_pi_million_digits.txt'
with open(file_name) as file_object:
    lines = file_object.readlines()
 
pi_string = ''
for line in lines:
    pi_string += line.strip()
    
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")


# Writing to files
# Writing to an empty file
print("\nWriting to an empty file")
filename = 'c10_examples_programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.")

# Writing multiple lines
# Note that write() doesn't add newlines
filename = 'c10_examples_programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")
    file_object.write("Python is fun!\n")


# Appending to a file
print("\nAppending to a file")
filename = 'c10_examples_programming.txt'

with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.")
    

# Exceptions
# ZeroDivisionError exception
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")


# Using exceptions to prevent crashes
# Division calculator
# ZeroDivisionError
print("\nZeroDivisionError")
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if (first_number == 'q'):
        break
    second_number = input("\nSecond number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)
        
# FileNotFoundError
print("\nFileNotFoundError")
filename = 'alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")


# Using .split() method
title = 'Alice in Wonderland'
print(title.split())


# Count number of words in Alice in Wonderland
filename = 'c10_examples_alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
else:
    # Count the approximate number of words in the file
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")


# Create a function to count words in a file
def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

filename = 'c10_examples_alice.txt'
count_words(filename)

filenames = ['c10_examples_alice.txt', 'c10_examples_metamorphosis.txt',
             'c10_examples_littlewomen.txt','c10_examples_drjekyll.txt']
for file in filenames:
    count_words(file)


# Failing silently
print("\nFailing silently")
def count_words_silent_fail(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

filenames = ['c10_examples_alice.txt', 'c10_examples_metamorphosis.txt',
             'c10_examples_littlewomen.txt','c10_examples_drjekyll.txt']
for file in filenames:
    count_words_silent_fail(file)
    

# Storing data using JSON
print("\nUsing JSON")
import json

numbers = [2, 3, 5, 7, 11, 13]

filename_numbers = 'c10_examples_numbers.json'
with open(filename_numbers, 'w') as f:
    json.dump(numbers, f)


# Loading data using JSON
import json

filename_numbers = 'c10_examples_numbers.json'
with open(filename_numbers, 'r') as f:
    numbers_loaded = json.load(f)
    
print(numbers_loaded)


# Storing and loading users' data
print("\Storing and loading users' data")
import json

username = input("What is your name? ")

filename = 'c10_examples_username.json'
with open(filename, 'w') as f:
    json.dump(username, f)
    print(f"We'll remember you when you come back, {username}!")
    
with open(filename) as f:
    username_loaded = json.load(f)
    print(f"Welcome back, {username_loaded}!")
    
# Combine with a try-except block and make neater
# Load the username, if it has been stored previously
# Otherwise, prompt for the username and store it
import json    

filename = "c10_examples_username.json"
try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"We'll remember you when you come back, {username}!")
else:
    print(f"Welcome back, {username}!")

# Refactoring the above
print("\nRefactoring")
import json

def greet_user():
    """Greet the user by name."""
    filename = 'c10_examples_username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        username = input("What is your name? ")
        with open(filename, 'w') as f:
            json.dump(username, f)
            print(f"We'll remember you when you come back, {username}!")
    else:
        print(f"Welcome back, {username}!")
        
greet_user()

# Refactor further
import json

def get_stored_username():
    """Get stored username if available."""
    filename = 'c10_examples_username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username
    
def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = input("What is your name? ")
        filename = 'c10_examples_username.json'
        with open(filename, 'w') as f:
            json.dump(username, f)
            print(f"We'll remember you when you come back, {username}!")
            
greet_user()

# Refactor even further
import json

def get_stored_username():
    """Get stored username if available."""
    filename = 'c10_examples_username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username
    
def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'c10_examples_username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username
    
def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")
            
greet_user()
