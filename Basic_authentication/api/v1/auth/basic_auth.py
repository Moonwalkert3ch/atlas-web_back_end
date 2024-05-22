#!/usr/bin/env python3
"""Module that creates a class that inherits form Auth"""
from api.v1.auth.auth import Auth
from base64 import b64decode
from typing import TypeVar
from models.user import User


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

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """method that returns the email and password of a user
        Parameter Args:
        decoded_base64_authorization_header: decoded values
        """
        if decoded_base64_authorization_header is None:
            return (None, None)

        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)

        if ':' not in decoded_base64_authorization_header:
            return (None, None)

        # Split string at the colon, set 1 to indicate where to stop
        email, password = decoded_base64_authorization_header.split(':', 1)

        # Return the user email and password
        return (email, password)

    def user_object_from_credentials(
            self,
            user_email: str,
            user_pwd: str) -> TypeVar('User'):
        """method that returns user email/password instance
        Parameter Args:
        user_email(str) - users email
        user_pwd(str) - users password
        return - user instance
        """
        if user_email is None or not isinstance(user_email, str):
            return None

        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        # look for the user by email
        try:
            user_search = User.search({'email': user_email})
        except Exception:
            return None

        for user in user_search:
            # check if password is correct
            if user.is_valid_password(user_pwd):
                return user

        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """overloads Auth and retrieves User instance for a request
        Parameter Args:
        request=None - retrieve request
        return - user instance
        """
        # get authorization header from request
        auth_header = self.authorization_header(request)
        if auth_header is None:
            return None

        base64_auth_header = self.extract_base64_authorization_header(
            auth_header)
        if base64_auth_header is None:
            return None

        decoded_auth_header = self.decode_base64_authorization_header(
            base64_auth_header)
        if decoded_auth_header is None:
            return None

        user_email, user_password = self.extract_user_credentials(
            decoded_auth_header)
        if user_email is None or user_password is None:
            return None

        return self.user_object_from_credentials(user_email, user_password)
