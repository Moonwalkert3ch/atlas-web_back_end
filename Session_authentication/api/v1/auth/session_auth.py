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
