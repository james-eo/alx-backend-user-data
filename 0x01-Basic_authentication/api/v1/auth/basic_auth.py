#!/usr/bin/env python3
"""
BasicAuth module
"""
from api.v1.auth.auth import Auth
import base64
from models.user import User


class BasicAuth(Auth):
    """ Basic Auth class """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Extract and return the Base64 part of the Authorization header"""
        if authorization_header is None \
                or not isinstance(authorization_header, str) \
                or not authorization_header.startswith("Basic "):
            return None
        return authorization_header.split(" ")[1]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """ Decode Base64 part of the Authorization header """
        if base64_authorization_header is None \
                or not isinstance(base64_authorization_header, str):
            return None
        try:
            dec = base64.b64decode(base64_authorization_header).decode('utf-8')
            return dec
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """ Extract user credentials from decoded Base64 """
        if decoded_base64_authorization_header is None \
                or not isinstance(decoded_base64_authorization_header, str) \
                or ':' not in decoded_base64_authorization_header:
            return None, None
        usr_email, usr_pwd = decoded_base64_authorization_header.split(':', 1)
        return usr_email, usr_pwd

    def user_object_from_credentials(self,
                                     user_email: str, user_pwd: str) -> User:
        """ Get User instance based on email and password """
        if user_email is None or not isinstance(user_email, str) \
                or user_pwd is None or not isinstance(user_pwd, str):
            return None
        try:
            user = User.search({"email": user_email})
            if not user or not user.is_valid_password(user_pwd):
                return None
            return user
        except Exception:
            return None
