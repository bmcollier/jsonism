Python JSON Checker
===================

*A simple alternative to JSONSchema for JSON validation in Python programs.*

Install from pip
----------------

```pip install jsonism```

Example usage
-------------

### Import the checker

```python
from jsonism.checker import validate
```

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

