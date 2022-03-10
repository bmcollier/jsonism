import logging


class String:

    type = str

    def __init__(self, len=None, max_len=None, min_len=None, options=None, mandatory=True):
        self.len = len
        self.max_len = max_len
        self.min_len = min_len
        self.options = options
        self.mandatory = mandatory

    def validate(self, input):
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

    type = int

    def __init__(self, max=None, min=None, mandatory=True):
        self.max = max
        self.min = min
        self.mandatory = mandatory

    def validate(self, input):
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

    type = float

    def __init__(self, max=None, min=None, mandatory=True):
        self.max = max
        self.min = min
        self.mandatory = mandatory

    def validate(self, input):
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

    type = bool

    def __init__(self, value=None, mandatory=True):
        self.value = value
        self.mandatory = mandatory

    def validate(self, input):
        if type(input) != self.type:
            logging.info(f"Expected {str(self.type)}, got {str(type(input))}")
            return False
        if self.value:
            if input != self.value:
                logging.info(f"Expecting value {self.value} but got {input}.")
                return False
        return True

