#!/usr/bin/env python3
"""
User model definition using SQLAlchemy.
This module defines the `User` class for mapping to the `users`
table in the database.
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class User(Base):
    """
    User class represents the `users` table in the database.

    Attributes:
        id (int): The user's unique identifier.
        email (str): The user's email address.
        hashed_password (str): The hashed password of the user.
        session_id (str, optional): The user's session identifier.
        reset_token (str, optional): The token used to reset
        the user's password.
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
