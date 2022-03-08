import unittest

from pyjsonchecker.checker import checkjson


class TestCheck(unittest.TestCase):

    def test_basic_dictionary(self):
        schema = {
            "Bob": str,
            "Lucy": int,
            "Bert": bool
        }
        json = {
            "Bob": "Is Bob",
            "Lucy": 13,
            "Bert": True
        }
        self.assertTrue(checkjson(json, schema))

    def test_unsupported_type(self):
        schema = "JUST A STRING"
        json = {
            "Bob": "Is Bob",
        }
        with self.assertRaises(NotImplementedError):
            checkjson(json, schema)

    def test_nested_dictionaries(self):
        schema = {
            "Bob": str,
            "Lucy": int,
            "Bert": {
                "age": int,
                "size": str
            }
        }
        json = {
            "Bob": "Is Bob",
            "Lucy": 13,
            "Bert": {
                "age": 13,
                "size": "Medium"
            }
        }
        self.assertTrue(checkjson(json, schema))

    def test_nested_dictionaries_with_fault(self):
        schema = {
            "Bob": str,
            "Lucy": int,
            "Bert": {
                "age": int,
                "size": str
            }
        }
        json = {
            "Bob": "Is Bob",
            "Lucy": 13,
            "Bert": {
                "age": "12",
                "size": "Medium"
            }
        }
        self.assertFalse(checkjson(json, schema))

    def test_lists(self):
        json = ["Bob", "Alice", "John"]
        schema = [str]
        self.assertTrue(checkjson(json, schema))

    def test_lists_invalid_value(self):
        json = ["Bob", "Alice", 12]
        schema = [str]
        self.assertFalse(checkjson(json, schema))

    def test_nested_lists(self):
        json = {
            "item": ["Bob", "Bob", "Bob"]
        }
        schema = {
            "item": [str]
        }
        self.assertTrue(checkjson(json, schema))

    def test_nested_lists_invalid_value(self):
        json = {
            "item": ["Bob", "Frank", True]
        }
        schema = {
            "item": [str]
        }
        self.assertFalse(checkjson(json, schema))

    def test_multiple_nesting(self):
        json = {"David": [{"Bob": 23, "Jane": True}]}
        schema = {"David": [{"Bob": int, "Jane": bool}]}
        self.assertTrue(checkjson(json, schema))

    def test_string(self):
        json = "David"
        schema = str
        self.assertTrue(checkjson(json, schema))

    def test_int(self):
        json = 14
        schema = int
        self.assertTrue(checkjson(json, schema))

    def test_float(self):
        json = 14.3
        schema = float
        self.assertTrue(checkjson(json, schema))


if __name__ == '__main__':
    unittest.main()
