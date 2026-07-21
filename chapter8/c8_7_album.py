# -*- coding: utf-8 -*-
"""
Created on Fri May 22 20:45:54 2020

@author: barbora
"""

# Write a function called make_album() that builds a dictionary describing a 
# music album. The function should take in an artist name and an album title,
# and it should return a dictionary containing these two pieces of information.
# Use the function to make three dictionaries representing different albums.
# Print each return value to show that the dictionaries are storing the album
# information correctly.
# Use None to add an optional parameter to make_album() that allow you to
# store the number of songs on an album. If the calling line includes a value
# for the number of songs, add that value to the album's dictionary. Make
# at least one new function call that includes the number of songs on an 
# album.

# Create function
def make_album(artist, title):
    """Function to make a dictionary containing information about an album."""
    album = {}
#    print("\nPlease give us information about an album.")
#    artist = input("Please name the artist: ")
#    title = input("Please name the title of the album: ")
    album['artist'] = artist
    album['title'] = title
    # Alternatively
#    album = {
#        'artist': artist,
#        'title': title,
#        }
    return album

# Call the function and print the returned dictionary
this_album = make_album('the killers', 'hot fuss')
print(this_album)
print(isinstance(this_album, dict))
for key, value in this_album.items():
    if (key == 'artist'):
        print(f"The {key}'s name is {value.title()}.")
    elif (key == 'title'):
        print(f"The album's {key} is {value.title()}.")
print("\n")
    
this_album = make_album('calvin harris', 'i created disco')
print(this_album)
for key, value in this_album.items():
    if (key == 'artist'):
        print(f"The {key}'s name is {value.title()}.")
    elif (key == 'title'):
        print(f"The album's {key} is {value.title()}.")
print("\n")
        
        
# Extend make_album() to include number of songs
def make_album(artist, title, songs=None):
    """Function to make a dictionary containing information about an album."""
    album = {}
    album['artist'] = artist
    album['title'] = title
    if songs:
        album['songs'] = songs
    return album

# Call the function and print the returned dictionary
this_album = make_album('the killers', 'hot fuss')
print(this_album)
print(isinstance(this_album, dict))
for key, value in this_album.items():
    if (key == 'artist'):
        print(f"The {key}'s name is {value.title()}.")
    elif (key == 'title'):
        print(f"The album's {key} is {value.title()}.")
    elif (key == 'songs'):
        print(f"The album has {value} {key}.")
print("\n")
    
this_album = make_album('calvin harris', 'i created disco', 12)
print(this_album)
for key, value in this_album.items():
    if (key == 'artist'):
        print(f"The {key}'s name is {value.title()}.")
    elif (key == 'title'):
        print(f"The album's {key} is {value.title()}.")
    elif (key == 'songs'):
        print(f"The album has {value} {key}.")
print("\n")
