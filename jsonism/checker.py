import logging


def validate(input: any, schema: any):
    """ Validate a top-level element. JSON supports lists, dicts and raw
    elements at the top level.

    :param input: JSON to be validated, as Python list, dict or base type
    :param schema: JSON schema, as Python list, dict or base type
    :return: True or False
    """
    if schema in [int, str, bool, float]:
        return _validate_generic(input, schema)
    if type(schema) == dict:
        return _validate_dict(input, schema)
    elif type(schema) == list:
        return _validate_list(input, schema)
    else:
        raise NotImplementedError("Unknown type found in schema")


def _validate_generic(input, schema):
    """ Validate a base type.

    :param input: A base value to be validated
    :param schema: A base type to validate the input against
    :return: True or False
    """
    if type(input) != schema:
        return False
    else:
        return True


def _validate_dict(input, schema):
    """ Validate a dictionary.

    :param input: The dictionary to be validated
    :param schema: The schema against which to validate, as a dictionary
    :return: True or False
    """
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
    """ Validate a list.

    :param input: The list to be validated
    :param schema: The schema against which to validate, as a list
    :return: True or False
    """
    list_item_type = schema[0]
    for item in input:
        if not validate(item, list_item_type):
            return False
    return True
