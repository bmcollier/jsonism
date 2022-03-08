Python JSON Checker
===================

*A simple alternative to JSONSchema for JSON validation in Python programs.*

Install from pip
----------------

```pip install jsonchecker```

Example usage
-------------

### Import the checker

```python
from jsonvalidator.checker import checkjson
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
checkjson(json, schema)
```

### Lists

```python
json = ["Bob", "Alice", "John"]
schema = [str]
checkjson(json, schema)
```

### Other stuff
```python
json = {"David": [{"Bob": 23, "Jane": True}]}
schema = {"David": [{"Bob": int, "Jane": bool}]}
checkjson(json, schema)
```

