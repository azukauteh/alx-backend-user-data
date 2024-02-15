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
        Requires authentication on every request.
        Returns True if authentication is required, False otherwise.
        """
        """ Return True if path is None or excluded_paths is None or empty"""
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True

        """ Remove trailing slashes from path and excluded_paths"""
        path = path.rstrip("/")
        excluded_paths = [p.rstrip("/") for p in excluded_paths]

        """ Check if path is in excluded_paths or a sub-path of any
        excluded path
        """
        for url in excluded_paths:
            if url.endswith("*"):
                """ Handle wildcard matching"""
                if path.startswith(url[:-1]):
                    return False
            else:
                """ Check for exact or sub-path match"""
                if path == url or path.startswith(url + "/"):
                    return False

        """ If no match  found, authentication is required"""
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

    uth_header = request.headers.get('Authorization', None)
    if auth_header is None:
        return None
        return auth_header

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
