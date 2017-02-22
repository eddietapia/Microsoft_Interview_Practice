"""
Author: Eddie Tapia
File name: unittests.py
Purpose: To test my function that converts a string to an integer
"""
import unittest
from stringtointconverter import string_to_int

class TestStringMethods(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(string_to_int(''), 'Invalid string passed in')

    def test_positive_string_passed_in(self):
        self.assertEqual(string_to_int('3693'), 3693)
        self.assertEqual(string_to_int('232'), 232)

    def test_negative_string_passed_in(self):
        self.assertTrue(string_to_int('-42'), 42)
        self.assertTrue(string_to_int('-322'), 322)

    def test_zeros_before_number(self):
        self.assertEqual(string_to_int('0002'), 2)
        self.assertEqual(string_to_int('010101'), 10101)

    def test_nonstring_input(self):
        self.assertEqual(string_to_int([3,4]), 'Invalid string passed in')
        self.assertEqual(string_to_int(32), 'Invalid string passed in')
        self.assertEqual(string_to_int(True), 'Invalid string passed in')

    def test_decimal_number(self):
        self.assertEqual(string_to_int('4.3'), 'Invalid string passed in')
        self.assertEqual(string_to_int('23.323.23'), 'Invalid string passed in')

if __name__ == '__main__':
    unittest.main()