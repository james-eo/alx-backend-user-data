#!/usr/bin/env python3
"""
Auth module
"""
from typing import List, TypeVar
from flask import request
import re


class Auth:
    """
    Auth class for handling authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        if not path or not excluded_paths:
            return True
        for excluded_path in excluded_paths:
            if excluded_path.endswith('*'):
                if re.match(f"^{excluded_path[:-1]}.*$", path):
                    return False
            elif path == excluded_path:
                return False
        return True

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determine if authentication is required for a given path
        """
        if path is None or excluded_paths is None or not excluded_paths:
            return True
        if path[-1] != '/':
            path += '/'
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        Get the Authorization header from the request
        """
        if request is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Get the current user (to be implemented)
        """
        return None
