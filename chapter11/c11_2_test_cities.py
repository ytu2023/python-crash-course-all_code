# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 21:36:49 2020

@author: barbora

Modify your function so it requires a third parameter, population. It should 
now return a single string of the form City, Country - population xxx, such as
Santiago, Chile - population 5000000. Run test_cities.py again. Make sure
test_city_country() fails this time.

Modify the function so the population parameter is optional. Run test_cities.py
again, and make sure test_city_country() passes again.

Write a second test called test_city_country_population() that verifies
you can call your function with the values 'santiago', 'chile', and
'population=5000000'. Run test_cities.py again, and make sure this new test 
passes.
"""

import unittest
from c11_2_city_functions import return_formatted_city_country

# Create a test class which inherits from unittest
class CityCountryTestCase(unittest.TestCase):
    """Tests for city_functions.py"""
    
    def test_city_country_format(self):
        """Does input such as 'Santiago, Chile' work?"""
        formatted = return_formatted_city_country('santiago', 'chile')
        self.assertEqual(formatted, 'Santiago, Chile')
        
    def test_city_country_population_format(self):
        """Does formatting work when population is included, e.g.
        'Santiago, Chile - population 5000000'?
        """
        formatted = return_formatted_city_country('santiago', 'chile', 5000000)
        self.assertEqual(formatted, 'Santiago, Chile - population 5000000')
        
# Run the tests
if __name__ == '__main__':
    unittest.main()
    