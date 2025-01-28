#!/usr/bin/env python3
"""A module that returns the log message obfuscated:"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
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
