import logging


def checkjson(input: any, schema: any):
    if type(schema) == dict:
        return validate_dict(input, schema)
    elif type(schema) == list:
        return validate_list(input, schema)
    else:
        raise NotImplementedError("Unknown type found in schema")


def validate_dict(input, schema):
    for key, value in schema.items():
        if type(value) in [dict, list]:
            if type(input.get(key)) == type(value):
                return checkjson(input.get(key), value)
            else:
                logging.warning(f"Schema field '{key}': Expected {str(dict)}, got {str(type(input.get(key)))}")
                return False
        elif input.get(key):
            if type(input.get(key)) != value:
                logging.warning(f"Schema field '{key}': Expected {str(value)}, got {str(type(input.get(key)))}")
                return False
        else:
            logging.warning(f"Schema field '{key}' not found")
            return False
    return True


def validate_list(input, schema):
    for i in range(len(schema)):
        if type(schema[i]) in [dict, list]:
            if isinstance(input[i], type(schema[i])):
                return checkjson(schema[i], input[i])
            else:
                logging.warning(f"Unexpected value found in list. "
                                f"Expected '{str(schema[i])}', got '{str(type(input[i]))}'")
                return False
        elif type(input[i]) != schema[i]:
            logging.warning(f"Unexpected value found in list. "
                            f"Expected '{str(schema[i])}', got '{str(type(input[i]))}'")
            return False
    return True