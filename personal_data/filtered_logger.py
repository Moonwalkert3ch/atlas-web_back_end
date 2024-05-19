#!/usr/bin/env python3
"""Write a function called filter_datum that
returns the log message obfuscated"""

import re
from typing import List
import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields=None):
        super().__init__(self.FORMAT)
        if fields is None:
            self.fields = []
        else:
            self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        NotImplementedError

    def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
        """
        Writes a function that returns the log message obfuscated
        Param Arguments:
        fields(list(str)): a list of strings representing all fields to obfuscate
        redaction: a string representing by what the field will be obfuscated
        message(str): a string representing the log line
        separator(str): a string representing by which character is
        separating all fields in the log line
        Return: a regex to replace occurrences of certain field values.
        """
        for field in fields:
            # create the regex pattern for the field
            field_pattern = f"{re.escape(field)}=[^{re.escape(separator)}]*"
            # then i substitute the field with the redaction
            message = re.sub(field_pattern, f"{field}={redaction}", message)
        return message
