# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 09:09:36 2020

@author: barbora
"""

# Methods to change case 
name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

# F-strings using f"{}" where f = format
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
greeting = f"Hello, {first_name.title()}!"
print(greeting)

# Whitespace stripping
item = " chair "
print(item.rstrip())
print(item.lstrip())
print(item.strip())

