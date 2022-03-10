import unittest
import logging

from jsonism.checker import validate
from jsonism.types import String, Integer, Boolean, Float

logging.basicConfig(level=logging.DEBUG)

class TestCheck(unittest.TestCase):

    def test_value_validation(self):
        schema = {
            "Bob": String(len=6),
            "Lucy": Integer(max=13),
            "Bert": Boolean(allowed=True),
            "Chris": Float(min=12.34)
        }
        input = {
            "Bob": "Is Bob",
            "Lucy": 13,
            "Bert": True,
            "Chris": 34.2
        }
        self.assertTrue(validate(input, schema))

    def test_value_validation_string_list(self):
        schema = {
            "Bob": String(options=["Is Bob", "Not Bob"]),
            "Lucy": Integer(max=13),
            "Bert": Boolean(allowed=True)
        }
        input = {
            "Bob": "Is Bob",
            "Lucy": 13,
            "Bert": True
        }
        self.assertTrue(validate(input, schema))

    def test_value_validation_string_list_bad(self):
        schema = {
            "Bob": String(options=["Is Bob", "Not Bob"]),
            "Lucy": Integer(max=13),
            "Bert": Boolean(allowed=True)
        }
        input = {
            "Bob": "Was Bob",
            "Lucy": 13,
            "Bert": True
        }
        self.assertFalse(validate(input, schema))

    def test_value_validation_wrong_str_len(self):
        schema = {
            "Bob": String(len=6),
            "Lucy": Integer(max=13),
            "Bert": Boolean(allowed=True)
        }
        input = {
            "Bob": "Is Bob and someone else",
            "Lucy": 13,
            "Bert": True
        }
        self.assertFalse(validate(input, schema))

    def test_value_validation_wrong_max_int(self):
        schema = {
            "Bob": String(len=6),
            "Lucy": Integer(max=13),
            "Bert": Boolean(allowed=True)
        }
        input = {
            "Bob": "Is Bob",
            "Lucy": 15,
            "Bert": True
        }
        self.assertFalse(validate(input, schema))

    def test_value_validation_wrong_bool(self):
        schema = {
            "Bob": String(len=6),
            "Lucy": Integer(max=13),
            "Bert": Boolean(allowed=True)
        }
        input = {
            "Bob": "Is Bob",
            "Lucy": 13,
            "Bert": False
        }
        self.assertFalse(validate(input, schema))


if __name__ == '__main__':
    unittest.main()