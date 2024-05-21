#!/usr/bin/env python3
"""Module thats creates a class to manage the API authentication"""


from flask import request
from typing import List, TypeVar


class Auth:
    """Class that manages the api authentication"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Method that returns false"""
        if path is None:
            return True

        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        # adds consistent slashes / eof name
        path_view = path.rstrip('/') + '/'

        for excluded_path in excluded_paths:
            if path_view == excluded_path:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """Public method returns none"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Public method that returns none"""
        return None
