import re

def validate_input(input_string, pattern):
    """Validate input using regular expressions."""
    if not re.match(pattern, input_string):
        raise ValueError(f"Input '{input_string}' does not match the expected pattern.")
