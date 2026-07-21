# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 21:26:27 2020

@author: barbora

Write a function that accepts two parameters: a city name and a county name.
The function should return a single string of the form City, Country such as
Santiago, Chile. Store the function in a amodule called city_functions.py

Create a file called test_cities.py that tests the function you just wrote.
Write a method called test_city_country() to verify that calling your
function with values such as 'santiago' and 'chile' results in the 
correct string. Run test_cities.py and make sure test_city_country() passes.
"""

import unittest
from c11_1_city_functions import return_formatted_city_country

# Create a test class which inherits from unittest
class CityCountryTestCase(unittest.TestCase):
    """Tests for city_functions.py"""
    
    def test_city_country_format(self):
        """Does input such as 'Santiago, Chile' work?"""
        formatted = return_formatted_city_country('santiago', 'chile')
        self.assertEqual(formatted, 'Santiago, Chile')
        
# Run the tests
if __name__ == '__main__':
    unittest.main()
    