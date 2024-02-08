#!/usr/bin/env python3
"""Defines a logger with custom log formatter """
import os
import re
import logging


def filter_datum(fields, redaction, message, separator):
    """
    Filters the log message by obfuscating specified fields.
    """
    return re.sub(
        r'({})=(.*?){}'.format('|'.join(fields), separator),
        r'\1{}{}'.format(redaction, separator),
        message
    )


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields):
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        record.msg = filter_datum(self.fields, self.REDACTION, record.msg,
                                  self.SEPARATOR)
        return super().format(record)
