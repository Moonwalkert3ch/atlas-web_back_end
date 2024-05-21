#!/usr/bin/env python3
"""Module thats creates a class to manage the API authentication"""


from flask import request
from typing import List, TypeVar


class Auth:
    """Class that manages the api authentication"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Method that returns false"""
        return False

    def authorization_header(self, request=None) -> str:
        """Public method returns none"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Public method that returns none"""
        return None
