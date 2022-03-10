import logging


class String:
    """ Schema class for strings. Takes the place of a bare `str` when adding
    value validation. """

    type = str

    def __init__(self, len=None, max_len=None, min_len=None, options=None, mandatory=True):
        """ Create a new String object to validate strings in JSON schemas.

        :param len: Optional string length checker for a specific set length
        :param max_len: Optional max string length
        :param min_len: Optional min string length
        :param options: Optional list of valid values
        :param mandatory: Is the field mandatory? Defaults to `True`. Not yet implemented.
        """
        self.len = len
        self.max_len = max_len
        self.min_len = min_len
        self.options = options
        self.mandatory = mandatory

    def validate(self, input):
        """ Validate a string field

        :param input: The input to validate
        :return: True or False indicating validity
        """
        if type(input) != self.type:
            logging.info(f"Expected {str(self.type)}, got {str(type(input))}")
            return False
        if self.len:
            if len(input) != self.len:
                logging.info(f"Value '{input}' is not specified length of {self.len} for this field.")
                return False
        if self.max_len:
            if len(input) > self.max_len:
                logging.info(f"Length of value '{input}' exceeds maximum of {self.max_len} for this field.")
                return False
        if self.min_len:
            if len(input) < self.min_len:
                logging.info(f"Length of value '{input}' is shorter than minimum of {self.max_len} for this field.")
                return False
        if self.options:
            if input not in self.options:
                logging.info(f"'{input}' is not a permitted value. Expecting one of {str(self.options)}.")
                return False
        return True


class Integer:
    """ Schema class for integers. Takes the place of a bare `int` when adding
    value validation."""

    type = int

    def __init__(self, max=None, min=None, mandatory=True):
        """ Create a new Integer object to validate integers in JSON schemas.

        :param max: Optional maximum integer value
        :param min: Optional minimum integer value
        :param mandatory: Is the field mandatory? Defaults to `True`. Not yet implemented.
        """
        self.max = max
        self.min = min
        self.mandatory = mandatory

    def validate(self, input):
        """ Validate an integer field.

        :param input: The field to validate
        :return: True or False indicating validity
        """
        if type(input) != self.type:
            logging.info(f"Expected {str(self.type)}, got {str(type(input))}")
            return False
        if self.max:
            if input > self.max:
                logging.info(f"Value {input} exceeds maximum of {self.max} for this field.")
                return False
        if self.min:
            if input < self.min:
                logging.info(f"Value {input} is less than minimum of {self.min} for this field.")
                return False
        return True


class Float:
    """ Schema class for floats. Takes the place of a bare `float` when adding
    value validation."""

    type = float

    def __init__(self, max=None, min=None, mandatory=True):
        """ Create a new Float object to validate floats in JSON schemas.

        :param max: Optional maximum float value
        :param min: Optional minimum float value
        :param mandatory: Is the field mandatory? Defaults to `True`. Not yet implemented.
        """
        self.max = max
        self.min = min
        self.mandatory = mandatory

    def validate(self, input):
        """ Validate a floating-point field

        :param input: The field to validate
        :return: True or False indicating validity
        """
        if type(input) != self.type:
            logging.info(f"Expected {str(self.type)}, got {str(type(input))}")
            return False
        if self.max:
            if input > self.max:
                logging.info(f"Value {input} exceeds maximum of {self.max} for this field.")
                return False
        if self.min:
            if input < self.min:
                logging.info(f"Value {input} is less than minimum of {self.min} for this field.")
                return False
        return True


class Boolean:
    """ Schema class for booleans. Takes the place of a bare `bool` when adding
    value validation. """

    type = bool

    def __init__(self, allowed=None, mandatory=True):
        """ Create a new Boolean object to validate booleans in JSON schemas.

        :param allowed: Optional switch to only allow `true` or `false`.
        :param mandatory: Is the field mandatory? Defaults to `True`. Not yet implemented.
        """
        self.allowed = allowed
        self.mandatory = mandatory

    def validate(self, input):
        """ Validate a boolean field

        :param input: The field to validate
        :return: True or False indicating validity
        """
        if type(input) != self.type:
            logging.info(f"Expected {str(self.type)}, got {str(type(input))}")
            return False
        if self.allowed:
            if input != self.allowed:
                logging.info(f"Expecting value {self.allowed} but got {input}.")
                return False
        return True

