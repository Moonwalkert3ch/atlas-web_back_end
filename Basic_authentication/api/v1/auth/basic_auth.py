#!/usr/bin/env python3
"""Module that creates a class that inherits form Auth"""
from api.v1.auth.auth import Auth
from base64 import b64decode


class BasicAuth(Auth):
    """empty class for now"""

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """Decodes Baase64 Auth header
        Parameter Args:
        authorization_header (str): Authorization header string
        Returns:
        str: Base64 encoded string part, or None
        """
        if authorization_header is None:
            return None

        if not isinstance(authorization_header, str):
            return None

        if not authorization_header.startswith("Basic "):
            return None

        encoded = authorization_header.split(' ', 1)[1]

        return encoded
