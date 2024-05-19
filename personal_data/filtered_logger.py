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

    def filter_datum(self, message: str) -> str:
        """
        Writes a function that returns the log message obfuscated
        Param Arguments:
        fields(list(str)): a list of strings representing all fields to obfuscate
        Return(str): Values for fields in fields should be filtered..
        """
        for field in self.fields:
            # create the regex pattern for the field
            field_pattern = f"{re.escape(field)}=[^;]*"
            # then i substitute the field with the redaction
            message = re.sub(field_pattern, f"{field}={self.REDACTION}", message)
        return message

    def format(self, record: logging.LogRecord) -> str:
        record.msg = self.filter_datum(record.msg)
        return super().format(record)
