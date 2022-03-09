import unittest

from jsonism.checker import validate


class TestCheck(unittest.TestCase):

    def test_basic_dictionary(self):
        schema = {
            "Bob": str,
            "Lucy": int,
            "Bert": bool
        }
        input = {
            "Bob": "Is Bob",
            "Lucy": 13,
            "Bert": True
        }
        self.assertTrue(validate(input, schema))

    def test_unsupported_type(self):
        schema = "JUST A STRING"
        input = {
            "Bob": "Is Bob",
        }
        with self.assertRaises(NotImplementedError):
            validate(input, schema)

    def test_nested_dictionaries(self):
        schema = {
            "Bob": str,
            "Lucy": int,
            "Bert": {
                "age": int,
                "size": str
            }
        }
        input = {
            "Bob": "Is Bob",
            "Lucy": 13,
            "Bert": {
                "age": 13,
                "size": "Medium"
            }
        }
        self.assertTrue(validate(input, schema))

    def test_nested_dictionaries_with_fault(self):
        schema = {
            "Bob": str,
            "Lucy": int,
            "Bert": {
                "age": int,
                "size": str
            }
        }
        input = {
            "Bob": "Is Bob",
            "Lucy": 13,
            "Bert": {
                "age": "12",
                "size": "Medium"
            }
        }
        self.assertFalse(validate(input, schema))

    def test_lists(self):
        input = ["Bob", "Alice", "John"]
        schema = [str]
        self.assertTrue(validate(input, schema))

    def test_empty_list(self):
        input = []
        schema = [str]
        self.assertFalse(validate(input, schema))

    def test_empty_list_allowed(self):
        input = []
        schema = [str]
        self.assertTrue(validate(input, schema, allow_empty_lists=True))

    def test_lists_invalid_value(self):
        input = ["Bob", "Alice", 12]
        schema = [str]
        self.assertFalse(validate(input, schema))

    def test_nested_lists(self):
        input = {
            "item": ["Bob", "Bob", "Bob"]
        }
        schema = {
            "item": [str]
        }
        self.assertTrue(validate(input, schema))

    def test_nested_lists_invalid_value(self):
        input = {
            "item": ["Bob", "Frank", True]
        }
        schema = {
            "item": [str]
        }
        self.assertFalse(validate(input, schema))

    def test_multiple_nesting(self):
        input = {"David": [{"Bob": 23, "Jane": True}]}
        schema = {"David": [{"Bob": int, "Jane": bool}]}
        self.assertTrue(validate(input, schema))

    def test_multiple_nesting_multiple_repeats(self):
        input = {"Usernames": [{"username": "Bob", "age": 23}, {"username": "Bill", "age": 98}]}
        schema = {"Usernames": [{"username": str, "age": int}]}
        self.assertTrue(validate(input, schema))

    def test_multiple_nesting_multiple_repeats_with_fault(self):
        input = {"David": [{"Bob": 23, "Jane": True}, {"Bob": 19, "Jane": 23}]}
        schema = {"David": [{"Bob": int, "Jane": bool}]}
        self.assertFalse(validate(input, schema))

    def test_string(self):
        input = "David"
        schema = str
        self.assertTrue(validate(input, schema))

    def test_int(self):
        input = 14
        schema = int
        self.assertTrue(validate(input, schema))

    def test_float(self):
        input = 14.3
        schema = float
        self.assertTrue(validate(input, schema))

    def test_missing_element(self):
        schema = {
            "Bob": str,
            "Lucy": int,
            "Bert": bool
        }
        input = {
            "Bob": "Is Bob",
            "Lucy": 13,
        }
        self.assertFalse(validate(input, schema))

    def test_extra_element(self):
        schema = {
            "Bob": str,
            "Lucy": int,
            "Bert": bool
        }
        input = {
            "Bob": "Is Bob",
            "Lucy": 13,
            "Bert": True,
            "Colin": 21
        }
        self.assertTrue(validate(input, schema))

    def test_longer_json(self):
        _testobject = {
            "family": {
                "available": True,
                "state": "passed",
                "members": [
                    {
                        "state": "ready",
                        "status": "alive",
                        "id": 1,
                        "permission": True,
                        "colour": "None",
                        "uuid": "221edec0-e5b8-4a34-8eb6-87f97dab04b6",
                        "year": 1990,
                        "attributes": [
                            {
                                "name": "rex",
                                "value": "no",
                            },
                            {
                                "name": "banded",
                                "value": "no"
                            }
                        ],
                        "sex": "MALE"
                    }
                ]
            }
        }
        _testschema = {
            "family": {
                "available": bool,
                "state": str,
                "members": [
                    {
                        "state": str,
                        "status": str,
                        "id": int,
                        "permission": bool,
                        "colour": str,
                        "uuid": str,
                        "year": int,
                        "attributes": [
                            {
                                "name": str,
                                "value": str,
                            }
                        ],
                        "sex": str
                    }
                ]
            }
        }
        self.assertTrue(validate(_testobject, _testschema))

    def test_repeated_dict_list(self):
        _testobject = {
            "family": {
                "members": [
                    {
                        "attributes": [
                            {
                                "name": "rex",
                                "value": "no",
                            }
                        ],
                        "sex": "MALE"
                    }
                ]
            }
        }
        _testschema = {
            "family": {
                "members": [
                    {
                        "attributes": [
                            {
                                "name": str,
                                "value": str,
                            }
                        ],
                        "sex": str
                    }
                ]
            }
        }
        self.assertTrue(validate(_testobject, _testschema))

    def test_missing_element(self):
        schema = {
            "Bob": str,
            "Lucy": int,
            "Bert": bool
        }
        input = {
            "Bob": "Is Bob",
            "Lucy": 13,
        }
        self.assertFalse(validate(input, schema))

if __name__ == '__main__':
    unittest.main()
