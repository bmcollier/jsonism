Jsonism - The Simple Python JSON Checker and Schema Validator
=============================================================

*A super-simple library for validating JSON against a schema.*

Technical is documentation at https://jsonism.readthedocs.io

Why use Jsonism?
----------------
Jsonism is a great alternative to *jsonschema* when you just want to do some simple validation of JSON without your code getting horrendously complicated. 

It's quick to set up a basic schema checker.

Getting Started
---------------

###Install from pip

```pip install jsonism```

### Import the checker

```python
from jsonism.checker import validate
```

The `validate` function returns `True` if the input you give it matches the schema that you provide.

### Basic flat objects

```python
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
```

### Lists

```python
input = ["Bob", "Alice", "John"]
schema = [str]
validate(input, schema)
```

### Other stuff
```python
input = {"Usernames": [{"username": "Bob", "age": 23}, {"username": "Bill", "age": 98}]}
schema = {"Usernames": [{"username": str, "age": int}]}
validate(input, schema)
```

Obviously for more complex json, you can `json.loads` the input.

### Permissive validation

Jsonism is *permissive* when it comes to extra elements. As long as the elements listed in the schema are provided, `validate` will return `True`. If additional elements are added to the input, `validate` will still return `True`.

```python
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
validate(input, schema)  # Will return True
```

##Value validation

This is absolutely optional, in order to keep things as simple as possible and enable the use of the in-built types `int`, `str`, `bool`, and `float` wherever possible. But we do also support the use of value validation as follows:

```python
from jsonism.checker import validate
from jsonism.types import String, Integer, Boolean, Float

schema = {
    "Bob": String(len=6),
    "Lucy": Integer(max=96),
    "Bert": Boolean(allowed=True),
    "Chris": Float(min=12.34)
}
input = {
    "Bob": "Is Bob",
    "Lucy": 30,
    "Bert": True,
    "Chris": 34.2
}
validate(input, schema)  # Will return True
```

### Lists of valid values

```python
from jsonism.checker import validate
from jsonism.types import String, Integer, Boolean, Float

schema = {
    "Bob": String(options=["Is Bob", "Not Bob"]),
    "Lucy": Integer(max=22),
    "Bert": Boolean(allowed=True)
}
input = {
    "Bob": "Was Bob",
    "Lucy": 22,
    "Bert": True
}
validate(input, schema)  # Will return False
```

But it doesn't have feature *x*!
--------------------------------

Well, I did say it was simple. It will always support the very simple initialisation shown above. We also now support value validation. If you have a burning desire to add a feature, please either post an issue or make a pull request at https://github.com/bmcollier/jsonism.