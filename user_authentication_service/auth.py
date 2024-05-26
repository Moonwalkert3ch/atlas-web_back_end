#!/usr/bin/env python3
"""Defines a method that takes in a password string
args and returns bytes
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


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

from db import DB


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Registers and returns a new user if there is no email
        Parameter Args:
        email(str) - inputted email
        password(str) - inputted password
        Return - new user
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            hashed_password = _hash_password(password)
            user = self._db.add_user(email, hashed_password)

            return user

        else:
            raise ValueError(f'User <user email> already exists')
