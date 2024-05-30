#!/usr/bin/env python3
"""Creates a unit test for utils.access_nested_map"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock
from typing import Dict


# the test case
class TestAccessNestedMap(unittest.TestCase):
    """creates class that inherits from testcase"""

    # the parameterized text
    @parameterized.expand([
        ({"a": 1}, ("a"), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, key_path, expected):
        """tests that the method returns that it works"""
        result = access_nested_map(nested_map, key_path)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b")
    ])
    def test_access_nested_map_exception(self, nested_map, key_path, error):
        """uses error handker to test input"""
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, key_path)
            self.assertEqual(error, cm.exception)


class TestGetJson(unittest.TestCase):
    """tests the utils json method functionality"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """method that mocks and patches"""
        with patch('requests.get') as mock_get:
            # creates a mock response object and return payload
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response

            # then call the json function with url
            response = get_json(test_url)

            # assert request.get only called once
            mock_get.assert_called_once_with(test_url)

            # assertion for if get_json is equal to payload
            self.assertEqual(response, test_payload)

class TestMemoize(unittest.TestCase):
    """implements a test_memoize method"""
    def test_memoize(self):
        """calls a_properties value"""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a-method', return_value=42) as mm:
            test_instance = TestClass()

            callOne = test_instance.a_property
            callTwo = test_instance.a_property

            self.assertEqual(callOne, 42)
            self.assertEqual(callTwo, 42)
            mm.assert_called_once()
