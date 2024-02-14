#!/usr/bin/env python3
"""
This module defines the Auth class which provides a template for implementing
authentication systems in the application.
"""
from flask import request

from typing import (
    List,
    TypeVar
)


class Auth:
    """
    Provides methods for API authentication.
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if authentication is required for the given path.

        Args:
            path (str): The request path.
            excluded_paths (List[str]): A list of paths excluded from
                                        authentication.

        Returns:
            bool: True if authentication is required, False otherwise.
        """
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True

        for url in excluded_paths:
            if url.endswith('*'):
                if url[:-1] in path:
                    return False
            else:
                if path in url or path + '/' in url:
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        Extracts the authorization header from the request.

        Args:
            request: The Flask request object.

        Returns:
            str: The value of the 'Authorization' header, or None
                                   if not present.
        """
        auth = request.headers.get('Authorization', None)

        if request is None or auth is None:
            return None
        return auth

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieves the current authenticated user.

        Args:
            request: The Flask request object.

        Returns:
            TypeVar('User'): The current authenticated user, or None if not
                             authenticated.
        """
        return None
