import logging


def validate(input: any, schema: any):
    if schema in [int, str, bool, float]:
        return _validate_generic(input, schema)
    if type(schema) == dict:
        return _validate_dict(input, schema)
    elif type(schema) == list:
        return _validate_list(input, schema)
    else:
        raise NotImplementedError("Unknown type found in schema")


def _validate_generic(input, schema):
    if type(input) != schema:
        return False
    else:
        return True


def _validate_dict(input, schema):
    for key, value in schema.items():
        if type(value) in [dict, list]:
            if type(input.get(key)) == type(value):
                return validate(input.get(key), value)
            else:
                logging.warning(f"Schema field '{key}': Expected {str(dict)}, got {str(type(input.get(key)))}")
                return False
        elif key in input:
            if type(input.get(key)) != value:
                logging.warning(f"Schema field '{key}': Expected {str(value)}, got {str(type(input.get(key)))}")
                return False
        else:
            logging.warning(f"Schema field '{key}' not found in input.")
            return False
    return True


def _validate_list(input, schema):
    list_item_type = schema[0]
    for item in input:
        if not validate(item, list_item_type):
            return False
    return True
