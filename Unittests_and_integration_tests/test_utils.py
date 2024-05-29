#!/usr/bin/env python3
"""Creates a unit test for utils.access_nested_map"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


# the test case
def TestAccessNestedMap(unittest.TestCase):
    """creates class that inherits from testcase"""

    """the parameterized text"""
    @parameterized.expand([
        ({"a": 1}, ("a"), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, map, path, expected):
        """tests that the method returns that it works"""
        result = access_nested_map(map, path)
        self.assertEqual(result, expected)
