#!/usr/bin/env python3
"""Modulde for hash_password"""
import bcrypt
from bcrypt import checkpw
from db import DB
import uuid
from user import User
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError


def _hash_password(password: str) -> bytes:
    """Hash a password using bcrypt

    Args:
        password: the password to hash

    Return:
        bytes: The salted hash of the password
    """
    pwd_bytes = password.encode('utf-8')

    hashed_pwd = bcrypt.hashpw(pwd_bytes, bcrypt.gensalt())
    return hashed_pwd


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """Initialises the Auth class instance"""
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a new user object"""
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = _hash_password(password)
            registered_user = self._db.add_user(email, hashed_password)
            return registered_user

    def valid_login(self, email: str, password: str) -> bool:
        """Checks for valid login credentails"""
        try:
            user = self._db.find_user_by(email=email)
            encoded_pwd = password.encode('utf-8')
            return checkpw(encoded_pwd, user.hashed_password)
        except NoResultFound:
            return False

    def _generate_uuid(self) -> str:
        """Generates uuid from the uuid module"""
        return str(uuid.uuid4())

    def create_session(self, email: str) -> str:
        """Creates a session for a user"""
        try:
            user = self._db.find_user_by(email=email)
            session_id = self._generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None
