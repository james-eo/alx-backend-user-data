#!/usr/bin/env python3
"""
Auth module
"""
from flask import request
from typing import List, TypeVar
import re


class Auth:
    """ Auth class """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Check if a path requires authentication """
        if path is None or excluded_paths is None or not excluded_paths:
            return True
        path = path.rstrip('/') + '/'
        return not any(ex.rstrip('/') + '/' == path for ex in excluded_paths)

    def authorization_header(self, request=None) -> str:
        """ Get the Authorization header from a request """
        if request is None:
            return None
        return request.headers.get('Authorization', None)
    """
    def current_user(self, request=None) -> TypeVar('User'):
        """ Get the current user """
        return None
    """
