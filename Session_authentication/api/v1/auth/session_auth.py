#!/usr/bin/env python3
"""A module that inherits form Auth"""

from api.v1.auth.auth import Auth
import base64
import uuid
from typing import List
from models.user import User


class SessionAuth(Auth):
    """session auth manages session ids"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates a session id for the user id.
        Parameter Args:
        user_id - id of session user
        Returns(str) -  session id if valid
        """
        if user_id is None or not isinstance(user_id, str):
            return

        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Creates a session id for the user id.
        Parameter Args:
        session_id - id of session
        Returns(str) -  session id if user valid
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """Returns a user instance based on a cookie value"""
        session_cookie = self.session_cookie(request)
        session_id = self.user_id_for_session_id(session_cookie)
        return User.get(session_id)

    def destroy_session(self, request=None):
        """deletes the user session"""
        if not request:
            return False
        session_cookies = self.session_cookie(request)

        if not session_cookies:
            return False

        user_id = self.user_id_for_session_id(session_cookies)
        if not user_id:
            return False
        self.user_id_by_session_id.pop(session_cookies)
        return True
