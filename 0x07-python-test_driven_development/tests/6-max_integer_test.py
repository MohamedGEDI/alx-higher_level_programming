"""Unittest for max_integer"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test max_integer"""
    def test_max(self):
        """with normal values"""
        self.assertEqual(max_integer([1, 2, 3]), 3)
    def test_max_floats(self):
        """with floats"""
        self.assertEqual(max_integer([1.21, 2.31, 3.12]), 3.12)
    def text_empty(self):
        """empty string"""
        self.assertEqual(max_integer([]), None) 
