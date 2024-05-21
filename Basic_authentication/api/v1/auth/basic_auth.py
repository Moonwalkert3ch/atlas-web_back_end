#!/usr/bin/env python3
"""Module that creates a class that inherits form Auth"""
from api.v1.auth.auth import Auth
from base64 import b64decode


class BasicAuth(Auth):
    """empty class for now"""

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """returns Baase64 Auth header
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

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """method that decodes the base64 string
        Parameter Args:
        base64_authorization_header: base64 part of the authorization
        header for a basic authentication
        Returns:
        str: Base64 encoded string part, or None
        """
        if base64_authorization_header is None:
            return None

        if not isinstance(base64_authorization_header, str):
            return None

        try:
            encoded = base64_authorization_header.encode('utf-8')
            decoded64 = b64decode(encoded)
            decoded = decoded64.decode('utf-8')
        except BaseException:
            return None

        return decoded
