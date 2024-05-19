#!/usr/bin/env python3
"""Write a function called filter_datum that
returns the log message obfuscated"""

import re
from typing import List, Tuple
import logging
import os
import mysql.connector
from mysql.connector.connection import MySQLConnection


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


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    Description: connects to a secure holberton database
    to read a users table. The database is protected by a
    username and password that are set as environment
    variables on the server named PERSONAL_DATA_DB_USERNAME
    (set the default as “root”), PERSONAL_DATA_DB_PASSWORD
    (set the default as an empty string) and
    PERSONAL_DATA_DB_HOST (set the default as “localhost”).
    The database name is stored in PERSONAL_DATA_DB_NAME.
    Implement a get_db function that returns a connector
    to the database
    (mysql.connector.connection.MySQLConnection object).
    """
    # retreive variable environment
    username: str = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    password: str = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    host: str = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    database: str = os.getenv('PERSONAL_DATA_DB_NAME')

    # connect to the database
    connection: MySQLConnection = mysql.connector.connect(
        user=username,
        password=password,
        host=host,
        database=database
    )

    return connection


def main() -> None:
    """Description: Obtains a db connection and display all rows"""
    db = get_db()
    logger = get_logger()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    rows = cursor.fetchall()

    # For each row, a log message is constructed
    for row in rows:
        message_log = (
            f"name={row['name']}; email={row['email']}; phone={row['phone']}; "
            f"ssn={row['ssn']}; password={row['password']}; ip={row['ip']}; "
            f"last_login={row['last_login']}; user_agent={row['user_agent']};"
        )
        logger.info(message_log)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
