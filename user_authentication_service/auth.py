#!/usr/bin/env python3
"""Defines a method that takes in a password string
args and returns bytes
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """method takes in arg and returns bytes
    Parameter Args:
    password(str) - input password
    Returns - salted hash bash
    """
    salt = bcrypt.gensalt()
    # hash password with the generated salt just made
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password
