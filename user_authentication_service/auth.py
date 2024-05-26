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
from uuid import uuid4


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

    def create_session(self, email: str) -> str:
        """
        finds the users email and generates a new uuid
        and stores it in the database as the users session_id
        Parameter Args:
        email(str) - email of the user
        Return -  session id
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None
        session_id = _generate_uuid()
        self._db.update_user(user.id, session_id=session_id)

        return session_id

    def get_user_from_session_id(self, session_id: str) -> User:
        """finds user and returns none it not found
        Parameter Args:
        session_id(str) - user session id
        return - corresponding user
        """
        if session_id is None:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """updates the users session id to none"""
        try:
            user = self._db.find_user_by(id=user_id)
            self._db.update_user(user_id, session_id=None)
        except NoResultFound:
            raise NoResultFound


def _generate_uuid() -> str:
    """
    string representation of a new uuid
    return - uuid string
    """
    return str(uuid4())
