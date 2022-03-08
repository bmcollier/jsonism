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
        json = ["Bob", 14, True]
        schema = [str, int, bool]
        self.assertTrue(checkjson(json, schema))

    def test_lists_invalid_value(self):
        json = ["Bob", "John", True]
        schema = [str, int, bool]
        self.assertFalse(checkjson(json, schema))

    def test_nested_lists(self):
        json = {
            "item": ["Bob", 14, True]
        }
        schema = {
            "item": [str, int, bool]
        }
        self.assertTrue(checkjson(json, schema))

    def test_nested_lists_invalid_value(self):
        json = {
            "item": ["Bob", "Frank", True]
        }
        schema = {
            "item": [str, int, bool]
        }
        self.assertFalse(checkjson(json, schema))

    def test_tuple(self):
        pass

    def test_nested_tuple(self):
        pass

    def test_string(self):
        pass

    def test_nested_string(self):
        pass

    def test_int(self):
        pass

    def test_nested_int(self):
        pass

    def test_float(self):
        pass

    def test_nested_float(self):
        pass

    def test_boolean(self):
        pass

    def test_nested_boolean(self):
        pass

    def test_none(self):
        pass

    def test_nested_none(self):
        pass


        dict
        list
        tuple
        string
        int
        float
        True
        False
        None


if __name__ == '__main__':
    unittest.main()
