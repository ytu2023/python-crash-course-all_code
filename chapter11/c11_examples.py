# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 22:54:34 2020

@author: barbora
"""

import unittest


# Use function in c11_examples_name_function
from c11_examples_name_function import get_formatted_name

# print("Enter 'q' at any time to quit.")
# while True:
#     first = input("\nPlease give me a first name: ")
#     if first == 'q':
#         break
#     last = input("Please give me a last name: ")
#     if last == 'q':
#         break
#     # Print formatted name
#     formatted_name = get_formatted_name(first, last)
#     print(f"\tNeatly formatted name: {formatted_name}.")


# Test case
# from c11_examples_name_function import get_formatted_name

# class NamesTestCase(unittest.TestCase):
#     """Tests for 'name_function.py'."""
    
#     def test_first_last_name(self):
#         """Do names like 'Janis Joplin' work?"""
#         formatted_name = get_formatted_name('janis', 'joplin')
#         self.assertEqual(formatted_name, 'Janis Joplin')
        
#     def test_first_last_middle_name(self):
#         """Do names like 'Wolfgang Amadeus Mozart' work?"""
#         formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
#         self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')
        
# if __name__ == '__main__':
#     unittest.main()
    

# Testing classes
from c11_examples_survey import AnonymousSurvey

# # Check whether the survey class works
# # Define a question and make a survey
# question = "What language did you first learn to speak?"
# my_survey = AnonymousSurvey(question)
# # Show the question, and store responses to the question
# my_survey.show_question()
# print("Enter 'q' at any time to quit.\n")
# while True:
#     response = input("Language: ")
#     if response == 'q':
#         break
#     my_survey.store_response(response)
# # Show the survey results
# print("\nThank you to everyone who participated in the survey!")
# my_survey.show_results()

# # Write tests for the survey class
# class TestAnonymousSurvey(unittest.TestCase):
#     """Tests for the class AnonymousSurvey"""
    
#     def test_store_single_response(self):
#         """Test that a single response is stored properly."""
#         question = "What language did you first learn to speak?"
#         my_survey = AnonymousSurvey(question)
#         my_survey.store_response('English')
#         self.assertIn('English', my_survey.responses)
        
#     def test_store_three_responses(self):
#         """Test that athree individual responses are stored properly."""
#         question = "What language did you first learn to speak?"
#         my_survey = AnonymousSurvey(question)
#         responses = ['English', 'Spanish', 'Mandarin']
#         for response in responses:
#             my_survey.store_response(response)
#         for response in responses:
#             self.assertIn(response, my_survey.responses)
        
# # Run tests
# if __name__ == '__main__':
#     unittest.main()

# Write tests for the survey class with setUp() method
class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey"""
    
    def setUp(self):
        """
        Create a survey and a set of responses for use in all test methods.
        """
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']
    
    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)
        
    def test_store_three_responses(self):
        """Test that athree individual responses are stored properly."""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)
        
# Run tests
if __name__ == '__main__':
    unittest.main()
