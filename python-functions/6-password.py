#!/usr/bin/env python3
import re

def validate_password(password):
    # Check if the password is at least 8 characters long
    if len(password) < 8:
        return False

    # Check if the password contains at least one uppercase letter
    if not re.search(r"[A-Z]", password):
        return False

    # Check if the password contains at least one lowercase letter
    if not re.search(r"[a-z]", password):
        return False

    # Check if the password contains at least one digit
    if not re.search(r"\d", password):
        return False

    # Check if the password contains any spaces
    if " " in password:
        return False

    # If all checks passed, return True
    return True

# Test cases
print(validate_password("Password123"))  # True
print(validate_password("abc123"))  # False (no uppercase letter)
print(validate_password("Password 123"))  # False (contains spaces)
print(validate_password("password123"))  # False (no uppercase letter)
