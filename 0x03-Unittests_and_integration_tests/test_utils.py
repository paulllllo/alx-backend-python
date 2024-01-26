#!/usr/bin/env python3
"""Test utils module"""
import unittest
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from unittest.mock import patch


class TestAccessNestedMap(unittest.TestCase):
    """Test class for access_nested_map function"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map function defined in utils.py"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test exception raised in access_nested_map function"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Test class for get_json function"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests')
    def test_get_json(self, test_url, test_payload, mock_req):
        """test get_json function for correct ouput"""
        mock_req.get.return_value.json.return_value = test_payload
        self.assertEqual(get_json(test_url), test_payload)


class TestMemoize(unittest.TestCase):
    """Test class for the memoize function"""
    def test_memoize(self):
        """check if a_method is memoized"""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        test_instance = TestClass()
        with patch.object(
                TestClass, 'a_method', return_value=42) as mock_a_method:
            res = test_instance.a_property
            res2 = test_instance.a_property
            mock_a_method.assert_called_once()
            self.assertEqual(res, 42)
            self.assertEqual(res2, 42)
