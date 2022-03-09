Jsonism
=======
*A super-simple library for validating json against a schema.*

Install from pip
----------------

``pip install jsonism``

Why use Jsonism?
----------------

Jsonism aims to be the quickest way of validating JSON, with the simplest syntax. Check out examples below.

Example usage
-------------

**Basic flat objects**
::
    from jsonism.checker import validate
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
    validate(input, schema)


**Lists**
::
    from jsonism.checker import validate
    input = ["Bob", "Alice", "John"]
    schema = [str]
    validate(input, schema)

**Other stuff**
::
    from jsonism.checker import validate
    input = {"Usernames": [{"username": "Bob", "age": 23}, {"username": "Bill", "age": 98}]}
    schema = {"Usernames": [{"username": str, "age": int}]}
    validate(input, schema)

