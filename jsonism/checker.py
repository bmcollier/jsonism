import logging


def validate(input: any, schema: any, allow_empty_lists=False, parent=None):
    """ Validate a top-level element. JSON supports lists, dicts and raw
    elements at the top level.

    :param input: JSON to be validated, as Python list, dict or base type
    :param schema: JSON schema, as Python list, dict or base type
    :return: True or False
    """
    if schema in [int, str, bool, float]:
        return _validate_generic(input, schema, parent=parent)
    if type(schema) == dict:
        return _validate_dict(input, schema, allow_empty_lists=allow_empty_lists, parent=parent)
    elif type(schema) == list:
        return _validate_list(input, schema, allow_empty_lists=allow_empty_lists, parent=parent)
    else:
        raise NotImplementedError("Unknown type found in schema")


def _validate_generic(input, schema, parent=None):
    """ Validate a base type.

    :param input: A base value to be validated
    :param schema: A base type to validate the input against
    :return: True or False
    """
    if type(input) != schema:
        if parent:
            logging.info(f"Fault in {parent}")
        return False
    else:
        return True


def _validate_dict(input, schema, allow_empty_lists, parent=None):
    """ Validate a dictionary.

    :param input: The dictionary to be validated
    :param schema: The schema against which to validate, as a dictionary
    :return: True or False
    """
    for key, value in schema.items():
        if type(value) in [dict, list]:
            if type(input.get(key)) == type(value):
                if not validate(input.get(key), value, allow_empty_lists=allow_empty_lists, parent=key):
                    return False
            else:
                if parent:
                    logging.info(f"In {parent}:")
                logging.warning(f"Schema field '{key}': Expected {str(dict)}, got {str(type(input.get(key)))}")
                return False
        elif key in input:
            if type(input.get(key)) != value:
                if parent:
                    logging.info(f"In {parent}:")
                logging.warning(f"Schema field '{key}': Expected {str(value)}, got {str(type(input.get(key)))}")
                return False
        else:
            if parent:
                logging.info(f"In {parent}")
            logging.warning(f"Schema field '{key}' not found in input.")
            return False
    return True


def _validate_list(input, schema, allow_empty_lists, parent=None):
    """ Validate a list.

    :param input: The list to be validated
    :param schema: The schema against which to validate, as a list
    :return: True or False
    """
    if len(input) == 0:
        if parent:
            logging.info(f"In {parent}:")
        logging.info(f"Warning! Empty list encountered. 'allow_empty_lists' is currently set to {allow_empty_lists}")
        return allow_empty_lists
    list_item_type = schema[0]
    for item in input:
        if not validate(item, list_item_type, allow_empty_lists=allow_empty_lists):
            if parent:
                logging.info(f"In {parent}")
            return False
    return True
