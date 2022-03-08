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
json = {
    "Bob": "Is Bob",
    "Lucy": 13,
    "Bert": True
}
validate(json, schema)
```

### Lists

```python
json = ["Bob", "Alice", "John"]
schema = [str]
validate(json, schema)
```

### Other stuff
```python
json = {"David": [{"Bob": 23, "Jane": True}]}
schema = {"David": [{"Bob": int, "Jane": bool}]}
validate(json, schema)
```

