#!/usr/bin/env python3
"""Defines a logger with custom log formatter """
import os
import re


def filter_datum(fields, redaction, message, separator):
    """
    Filters the log message by obfuscating specified fields.
    """
    return re.sub(
        r'({})=(.*?){}'.format('|'.join(fields), separator),
        r'\1{}{}'.format(redaction, separator),
        message
    )
