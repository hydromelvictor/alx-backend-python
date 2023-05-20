#!/usr/bin/env python3
"""
Create a TestAccessNestedMap class that inherits
from unittest.TestCase
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """
    unittest write
    inheritance to unittest.TestCase
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        test for access nested map
        parameter
        ==========
        nested_map : dict
        path : tuple
        expected : sequence

        exemple
        =========
        >>> #view access_nested_map method
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        exception for access_nested_map
        parameter
        ===========
        nested_map : dict
        path : tuple

        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    unittest write
    inheritance to unittest.TestCase
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, url, payload):
        """
        get_json method test
        parameter
        ===========
        url : str
        preload : dict
        """
        class Jsonified(Mock):
            """
            class inheritance at Mock
            """
            def json(self):
                """
                to_json
                """
                return payload
        
        with patch('requests.get') as stoper:
            stoper.return_value = Jsonified()
            self.assertEqual(get_json(url), payload)
        

class TestMemoize(unittest.TestCase):
    """
    inheritance unittest.TestCase
    """

    def test_memoize(self):
        """
        memoize method test
        """
        class TestClass:
            """
            test class in test_memoize method
            """

            def a_method(self):
                """return 42 always"""
                return 42

            @memoize
            def a_property(self):
                """call class method a_method"""
                return self.a_method()
        
        with patch.object(TestClass,'a_method') as patcher:
            testClass = TestClass()
            for i in range(2):
                with self.subTest(i):
                    testClass.a_property()
            patcher.assert_called_once()
