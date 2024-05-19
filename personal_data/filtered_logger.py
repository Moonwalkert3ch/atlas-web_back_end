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

    def __init__(self, fields: List[str]):
        """Initializes class method"""
        super().__init__(self.FORMAT)
        if fields is None:
            self.fields = []
        else:
            self.fields = fields

    def filter_datum(self, message: str) -> str:
        """
        Writes a function that returns the log message obfuscated
        Param Arguments:
        fields(list(str)): a list of strings representing all fields
        to obfuscate
        redaction: a string representing by what the field will be
        obfuscated
        message(str): a string representing the log line
        separator(str): a string representing by which character is
        separating all fields in the log line
        Return: a regex to replace occurrences of certain field values.
        """
        for field in self.fields:
            # create the regex pattern for the field
            field_pattern = f"{re.escape(field)}=[^;]*"
            # then i substitute the field with the redaction
            message = re.sub(field_pattern, f"{field}={
                             self.REDACTION}", message)
        return message

    def format(self, record: logging.LogRecord) -> str:
        """filters the values in incoming log records using filter_datum"""
        recorded_message = self.filter_datum(record.msg)
        # set message back
        record.msg = recorded_message
        # call parent method class
        return super().format(record)
