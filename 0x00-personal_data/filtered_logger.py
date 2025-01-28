#!/usr/bin/env python3

import re


def filter_datum(fields, redaction, message, separator):
    """
    Returns an obfuscated log message
    Args:
        fields: list of strings representing fields to obfuscate
        redaction: string to replace field values with
        message: string representing the log line
        separator: string representing the field separator
    Returns:
        Obfuscated log message
    """
    pattern = f'({"|".join(fields)})=[^{separator}]*'
    return re.sub(pattern, f'\\1={redaction}', message)
