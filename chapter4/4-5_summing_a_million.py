# -*- coding: utf-8 -*-
"""
Created on Tue May  5 09:24:34 2020

@author: barbora
"""

# Make a list of the numbers from 1 to 1 000 000, and then use min() and max()
# to make sure list starts at 1 and ends at 1 000 000. Also, use sum()
# to see how quickly Python can add a million numbers.

one_mill = list(range(1,1000001))
min_val = min(one_mill)
max_val = max(one_mill)
sum_val = sum(one_mill)
print(f"Min value: {min_val}")
print(f"Max value: {max_val}")
print(f"Sum: {sum_val}")
