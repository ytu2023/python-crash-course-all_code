# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 15:13:56 2020

@author: barbora

Download a text from Project Gutenberg. Use the count() method to find out
how many times a word or phrase appears in a string. Using lower() will catch
all appearances of the word/phrase, regardless of formatting. 

Write a program that read the files from Project Gutenberg and determines how
many times the word 'the' appears in each text. This will be an approximation
since it will include words such as 'then' and 'there'. Try counting 'the '
and see how much lower your counter is.
"""

# List of files
filenames = ['c10_examples_alice.txt', 'c10_examples_metamorphosis.txt',
             'c10_examples_drjekyll.txt']

# For loop to analyse each text
for file in filenames:
    try:
        with open(file, 'r') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"\nFile {file} is not available")
    except UnicodeDecodeError:
        print(f"\nFile {file} cannot be read due to encoding mismatch")
    else:
        print(f"\nAnalysing {file}:")
        the = contents.lower().count('the')
        the_space = contents.lower().count('the ')
        print(f"Number of occurerences of 'the': {the}")
        print(f"Number of occurences of 'the ': {the_space}")
        