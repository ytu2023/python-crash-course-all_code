# -*- coding: utf-8 -*-
"""
Created on Fri May 22 21:18:10 2020

@author: barbora
"""

# Start with 8-7. Write a while loop that allows users to enter an album's
# artist and title. Once you have that information, call make_album() with the
# user's input and print the dictionary.

# From 8-7
def make_album(artist, title):
    """Function to make a dictionary containing information about an album."""
    album = {}
    album['artist'] = artist.title()
    album['title'] = title.title()
    return album

# User input
while True:
    # Tell user how to stop the program
    print("\nPlease give us information about an album.")
    print("Once you're done, type 'quit' to exit.")
    # User prompts and quitting conditions
    artist = input("Please name the artist: ")
    if (artist == 'quit'):
        break
    title = input("Please name the title of the album: ")
    if (title == 'quit'):
        break
    # Call make_album() and print the information
    album_info = make_album(artist, title)
    print(album_info)
    print("-------------------------------------------------------")
    