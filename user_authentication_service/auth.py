#!/usr/bin/env python3
"""Defines a method that takes in a password string
args and returns bytes
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from db import DB
from bcrypt import gensalt, hashpw, checkpw
from uuid import UUID


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

    def valid_login(self, email: str, password: str) -> bool:
        """locates user by email and checks the password
        Parameter Args:
        email(str) - inputted email
        password(str) - inputted password
        Return - True or False if password is a match
        """
        try:
            user = self._db.find_user_by(email=email)
            return checkpw(password.encode('utf-8'), user.hashed_password)
        except NoResultFound:
            return False

    def generate_uuid() -> str:
        """string representation of a new uuid
        return - uuid string"""
        return str(UUID())
