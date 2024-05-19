#!/usr/bin/env python3
"""Implement a hash_password function that expects
one string argument name password and returns a
salted, hashed password, which is a byte string."""

import bcrypt


def hash_password(password: str) -> bytes:
    """returns a salted hashed password"""
    secured_pw = password.encode()
    hashed_pw = bcrypt.hashpw(secured_pw, bcrypt.gensalt())

    return hashed_pw
