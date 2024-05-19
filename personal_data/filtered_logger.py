#!/usr/bin/env python3
"""Write a function called filter_datum that
returns the log message obfuscated"""

import re
from typing import List, Tuple
import logging

# Creates the tuple pii_fields at the root of module
PII_FIELDS: Tuple[str, str, str, str, str] = (
    'name', 'email', 'phone', 'ssn', 'password')


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
        message(str): a string representing the log line
        Return: a regex to replace occurrences of certain field values.
        """
        for field in self.fields:
            # create the regex pattern for the field
            field_pattern = f"{re.escape(field)}=[^;]*"
            # then i substitute the field with the redaction
            message = re.sub(
                field_pattern,
                f"{field}={self.REDACTION}",
                message)
        return message

    def format(self, record: logging.LogRecord) -> str:
        """filters the values in incoming log records using filter_datum"""
        recorded_message = self.filter_datum(record.msg)
        # set message back
        record.msg = recorded_message
        # call parent method class
        return super().format(record)


def get_logger() -> logging.Logger:
    """takes no args and returns a logging.Logger object"""
    # creates the logger
    logger = logging.getLogger('user_data')
    # set the logging level
    logger.setLevel(logging.INFO)
    # disallow logged messages to propogate to other users
    logger.propagate = False

    # creates the streamhandler
    stream_handler = logging.StreamHandler()
    # create stream handler format
    stream_handler.setFormatter(RedactingFormatter(PII_FIELDS))
    # adds handler to the log
    logger.addHandler(stream_handler)

    return logger
